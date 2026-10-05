"""Compare scratch/site_base.navbar() against the navbar in each built page."""
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
    if not os.path.exists(path):
        print("MISSING", name)
        bad += 1
        continue
    with io.open(path, "r", encoding="utf-8") as fh:
        html = fh.read()
    start = html.find("<header class=\"es-nav\">")
    end = html.find("</header>", start)
    actual = html[start:end + len("</header>")]
    expected = site_base.navbar(active).rstrip("\n")
    if actual != expected:
        bad += 1
        print("MISMATCH", name)
        import difflib
        diff = list(difflib.unified_diff(
            expected.splitlines(), actual.splitlines(),
            "generator", "on-disk", lineterm="", n=0))
        for line in diff[:24]:
            print("   ", line)
    else:
        print("ok      ", name)

print("\n%d mismatch(es)" % bad)
sys.exit(1 if bad else 0)
