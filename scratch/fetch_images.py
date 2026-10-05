"""
EcoScrap â€” image sourcing & processing helper.

Queries the Openverse API (public, no API key) for commercially licensed
photographs, scores every candidate against the theme keywords so only
genuinely on-topic images are kept, then downloads, crops and re-encodes them
into assets/images/ so the finished site never depends on a hot-linked URL.

Run:  python scratch/fetch_images.py
"""

import io
import json
import os
import re
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request

from PIL import Image, ImageOps

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(BASE_DIR, "assets", "images")
OUT_FILE = os.path.join(IMG_DIR, "manifest.json")

API = "https://api.openverse.org/v1/images/"
UA = "EcoScrapSiteBuilder/1.0 (front-end demo project)"
CTX = ssl.create_default_context()

TARGET_W, TARGET_H = 1600, 900
JPEG_QUALITY = 72

STOPWORDS = {
    "a", "an", "the", "of", "and", "in", "on", "at", "to", "for", "with",
    "old", "used", "new", "india", "city", "image", "photo", "picture",
}

# key -> (must-have keywords, ordered search queries)
THEMES = {
    "hero-pickup":   (["recycl", "truck", "collect", "waste"], ["recycling truck", "recycling vehicle", "waste collection truck", "scrap collection vehicle"]),
    "hero-recycle":  (["recycl", "plant", "conveyor", "sort", "facility"], ["recycling plant conveyor", "recycling facility sorting", "material recovery facility", "recycling centre"]),
    "paper":         (["cardboard", "paper", "newspaper", "carton"], ["newspaper stack", "cardboard boxes pile", "paper recycling stack", "waste paper pile"]),
    "metal":         (["metal", "scrap", "copper", "steel", "aluminium"], ["scrap metal pile", "copper scrap", "steel scrap yard", "aluminium cans"]),
    "plastic":       (["plastic", "bottle", "pet", "jug"], ["plastic bottles recycling", "pet bottle waste", "plastic bottle pile", "plastic jugs waste"]),
    "ewaste":        (["electronic", "circuit", "computer", "laptop", "e-waste"], ["electronic waste", "circuit boards", "old computers", "electronic components"]),
    "appliance":     (["appliance", "washing", "fridge", "refrigerator", "microwave", "discarded"], ["discarded washing machines", "old refrigerators", "broken microwaves", "appliance waste"]),
    "battery":       (["batter", "battery", "cells", "lithium"], ["old car batteries", "used battery cells", "battery waste", "dead batteries pile"]),
    "paper-hero":    (["paper", "bales", "recycl", "pulper"], ["waste paper bales", "paper recycling mill", "recycled paper", "paper mill"]),
    "scrapyard":     (["scrap", "yard", "junk", "metal"], ["junkyard scrap metal", "scrap metal yard", "salvage yard cars", "metal salvage"]),
    "collection":    (["truck", "collect", "waste", "garbage", "refuse"], ["garbage truck collection", "refuse collection vehicle", "waste lorry", "municipal garbage truck"]),
    "plant":         (["recycl", "facility", "plant", "machinery", "conveyor"], ["recycling facility", "waste processing plant", "recycling machinery", "sorting plant"]),
    "sustain-city":  (["solar", "wind", "green", "sustainab", "renewab"], ["solar panels renewable energy", "wind turbines green", "sustainable city", "solar farm"]),
    "support":       (["support", "team", "service", "help", "office"], ["customer service team", "help desk", "support agents office", "office team meeting"]),
    "delhi":         (["delhi"], ["new delhi", "delhi india", "delhi street", "delhi landmark"]),
    "mumbai":        (["mumbai", "bombay"], ["mumbai skyline", "mumbai india", "mumbai city", "bombay mumbai"]),
    "bangalore":     (["bangalore", "bengaluru"], ["bangalore city", "bengaluru city", "bangalore street", "bengaluru street"]),
    "pune":          (["pune"], ["pune city view", "pune cityscape", "pune india street", "pune buildings"]),
    "hyderabad":     (["hyderabad"], ["hyderabad city", "hyderabad charminar", "hyderabad buildings", "hyderabad street"]),
    "chennai":       (["chennai"], ["chennai city", "chennai marina", "chennai buildings", "chennai street"]),
    "green":         (["leaf", "leaves", "tree", "forest", "green", "plant", "nature"], ["green leaves", "forest sunlight", "green plant nature", "tree canopy green"]),
    "scale":         (["scale", "weigh", "weighing", "balance"], ["weighing scale", "industrial scale", "cargo weighing", "platform scale"]),
    "community":     (["volunteer", "cleanup", "clean", "community", "people", "collection"], ["volunteers cleanup", "community clean up", "beach cleanup volunteers", "community collection drive"]),
    "team":          (["worker", "team", "staff", "crew", "people"], ["recycling team", "waste management staff", "sorting line workers", "collection team"]),
    "household":     (["household", "kitchen", "home", "bin", "waste", "segregat"], ["household waste", "kitchen waste bin", "home waste segregation", "domestic waste"]),
    "office":        (["office", "building", "corporate", "tower", "business"], ["office building", "corporate office", "modern office tower", "business building"]),
    "laptop":        (["laptop", "computer", "notebook", "pc", "screen"], ["old laptop", "broken laptop", "computer parts", "obsolete computer"]),
    "boxes":         (["cardboard", "box", "boxes", "carton"], ["cardboard boxes recycling", "cardboard sheets", "carton boxes", "flattened cardboard"]),
    "solar":         (["solar", "wind", "renewab", "panel", "turbine"], ["solar panels", "wind turbines", "renewable energy solar", "solar panel array"]),
}

# Titles that match these are almost never usable for a commercial hero/category
# shot, so they are filtered out before anything is downloaded.
AVOID_TITLE = re.compile(
    r"\b(cat|cats|dog|dogs|puppy|kitten|police|riot control|toll gate|school|"
    r"student|children|child|art in public|art installation|digital dna|"
    r"search-and-rescue|hacking|meme|comic|logo|map|stamp|coin|token|"
    r"discarded ideas|portrait|selfie|graffiti|wall art|seafront|painted|"
    r"regrade|1930|1910|1920|1940)\b",
    re.I,
)

# The anonymous Openverse quota is strict, so every call is paced and retried.
THROTTLE_SECONDS = 3.5
_last_call = [0.0]


def _pace():
    wait = THROTTLE_SECONDS - (time.time() - _last_call[0])
    if wait > 0:
        time.sleep(wait)
    _last_call[0] = time.time()


def http_json(url, attempts=6):
    delay = 10
    for _ in range(attempts):
        _pace()
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=60, context=CTX) as resp:
                _last_call[0] = time.time()
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            if exc.code not in (429, 500, 502, 503, 504):
                raise
            retry_after = (exc.headers or {}).get("Retry-After")
            wait = float(retry_after) if (retry_after or "").isdigit() else delay
            print("   . throttled (%s) â€” waiting %ss" % (exc.code, wait))
            time.sleep(min(wait, 90))
            delay = min(delay * 2, 90)
        except Exception:
            time.sleep(delay)
            delay = min(delay * 2, 90)
    raise RuntimeError("openverse unavailable after retries")


def fetch_bytes(url, attempts=3):
    for attempt in range(attempts):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=90, context=CTX) as resp:
                return resp.read()
        except Exception:
            if attempt == attempts - 1:
                return None
            time.sleep(4)
    return None


def bigger_flickr(url):
    """Flickr serves _c (800) / _b (1024) / _h (1600) renditions."""
    base = url.rsplit(".", 1)[0]
    for suffix in ("_h.jpg", "_b.jpg"):
        candidate = base + suffix
        data = fetch_bytes(candidate, attempts=1)
        if data and len(data) > 60000:
            return candidate, data
    return url, None


def search(query, page_size=20):
    params = urllib.parse.urlencode({
        "q": query,
        "page_size": page_size,
        "license_type": "commercial",
        "mature": "false",
        "extension": "jpg",
    })
    try:
        return http_json(API + "?" + params).get("results", [])
    except Exception as exc:
        print("   ! search failed:", exc)
        return []


def blob(item):
    parts = [item.get("title") or "", item.get("description") or ""]
    tags = item.get("tags") or []
    if tags and isinstance(tags[0], dict):
        parts.extend(t.get("name") or "" for t in tags)
    return " ".join(parts).lower()


def relevance(item, keywords):
    """Title matches are the strongest signal, so they carry the most weight."""
    title = (item.get("title") or "").lower()
    text = blob(item)
    title_hits = sum(1 for kw in keywords if kw in title)
    body_hits = sum(1 for kw in keywords if kw in text)
    if title_hits == 0:
        return 0.0
    return title_hits * 2.0 + body_hits * 0.5


def usable(item):
    w, h = item.get("width") or 0, item.get("height") or 0
    if w < 900 or h < 500:
        return False
    return 1.15 <= (w / float(h)) <= 2.4


def process(raw_bytes):
    """Centre-crop to 16:9 and re-encode so every asset matches exactly."""
    img = Image.open(io.BytesIO(raw_bytes))
    img = ImageOps.exif_transpose(img).convert("RGB")
    img = ImageOps.fit(img, (TARGET_W, TARGET_H), method=Image.LANCZOS, centering=(0.5, 0.45))
    buf = io.BytesIO()
    img.save(buf, "JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)
    return buf.getvalue()


def pick(key, keywords, queries, manifest):
    seen = set()
    best = None
    for query in queries:
        print("  -> %-14s | %s" % (key, query))
        for item in search(query):
            if not usable(item):
                continue
            if AVOID_TITLE.search(item.get("title") or ""):
                continue
            url = item.get("url") or ""
            if not url or url in seen:
                continue
            seen.add(url)
            score = relevance(item, keywords)
            if score < 1.5:
                continue
            if best and score <= best["score"]:
                continue
            url, preloaded = (bigger_flickr(url) if "staticflickr.com" in url else (url, None))
            raw = preloaded or fetch_bytes(url)
            if not raw or len(raw) < 20000:
                continue
            try:
                jpeg = process(raw)
            except Exception as exc:
                print("     ! decode failed:", exc)
                continue
            best = {
                "score": round(score, 2),
                "file": "assets/images/%s.jpg" % key,
                "title": (item.get("title") or key).strip(),
                "creator": item.get("creator") or "",
                "license": (item.get("license") or "").upper(),
                "license_url": item.get("license_url") or "",
                "source": item.get("source") or "",
                "page": item.get("foreign_landing_url") or "",
                "original": item.get("url") or "",
            }
            with open(os.path.join(IMG_DIR, "%s.jpg" % key), "wb") as handle:
                handle.write(jpeg)
            manifest[key] = best
            print("     OK (score %.2f) %s" % (score, item.get("title")))
            break
        if best:
            break
    return best


def main():
    os.makedirs(IMG_DIR, exist_ok=True)
    manifest = {}
    if os.path.exists(OUT_FILE):
        try:
            with open(OUT_FILE, "r", encoding="utf-8") as handle:
                manifest = json.load(handle)
        except Exception:
            manifest = {}

    for key, (keywords, queries) in THEMES.items():
        target = os.path.join(IMG_DIR, "%s.jpg" % key)
        if key in manifest and os.path.exists(target):
            print("  == %-14s cached" % key)
            continue
        pick(key, keywords, queries, manifest)
        with open(OUT_FILE, "w", encoding="utf-8") as handle:
            json.dump(manifest, handle, indent=2, ensure_ascii=False)

    missing = [k for k in THEMES if k not in manifest]
    print("\nimages ready: %d / %d" % (len(THEMES) - len(missing), len(THEMES)))
    if missing:
        print("still missing:", ", ".join(missing))


if __name__ == "__main__":
    main()


