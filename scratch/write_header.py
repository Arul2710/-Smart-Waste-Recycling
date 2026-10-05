"""Rewrite the <header> block of every public page from scratch/site_base.navbar()."""
import io, os, sys

BASE = r"C:\Users\arulp\OneDrive\Desktop\Local Waste"
sys.path.insert(0, os.path.join(BASE, "scratch"))
import site_base  # noqa: E402

PAGES = {
    "index.html": "index",
    "home2.html": "home2",
    "about.html": "About",
    "services.html": "Services",
    "rate-card.html": "Rate Card",
    "how-it-works.html": "How It Works",
    "blog.html": "Blog",
    "blog-details.html": "Blog",
    "contact.html": "Contact",
    "locations.html": "Locations",
    "terms.html": "Terms",
    "privacy-policy.html": "Privacy Policy",
    "404.html": "",
}

bad = 0
for name, active in PAGES.items():
    path = os.path.join(BASE, name)
    with io.open(path, "r", encoding="utf-8") as fh:
        html = fh.read()
    start = html.find('<header class="es-nav">')
    end = html.find("</header>", start)
    if start == -1 or end == -1:
        print("FAIL", name, "no header found")
        bad += 1
        continue
    new_header = site_base.navbar(active).rstrip("\n")
    html = html[:start] + new_header + html[end + len("</header>"):]
    with io.open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(html)
    print("rewrote", name)

print("\n%d failure(s)" % bad)
sys.exit(1 if bad else 0)
