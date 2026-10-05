"""
EcoScrap — shared page skeleton (head / navbar / footer / wrapper).

Every public page is assembled from the same stable layout so branding, the
responsive navbar, dark-mode + RTL controls and the footer stay identical.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ORIGIN = "https://docs.unsplash.com"  # placeholder — unused now that images are local

TAILWIND_CFG = (
    """
tailwind.config = {
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        primary: '#16A34A',
        primaryDark: '#14532D',
        primaryLight: '#86EFAC',
        lightBg: '#F0FDF4',
        darkBg: '#0B1220'
      },
      fontFamily: { sans: ['Poppins', 'sans-serif'] }
    }
  }
};""".strip()
)

NAV_LINKS = [
    # (label, href, icon)
    ("About", "about.html", "fa-circle-info"),
    ("Services", "services.html", "fa-truck-pickup"),
    ("Rate Card", "rate-card.html", "fa-tags"),
    ("How It Works", "how-it-works.html", "fa-list-check"),
    ("Blog", "blog.html", "fa-newspaper"),
]

# Contact is a plain navbar link; the contact page itself carries the
# phone / WhatsApp / email shortcuts.


def _is_active(active, label, href):
    return " is-active" if (active == label or active == file_base(href)) else ""


def _icon_cls(icon):
    # Font Awesome ships brand marks in a separate family.
    return "fa-brands fa-whatsapp" if icon == "fa-whatsapp" else "fa-solid %s" % icon


def _link_attrs(href):
    # Off-site links open in a new tab and drop the opener reference.
    return ' target="_blank" rel="noopener"' if href.startswith("http") else ""


def _theme_script():
    return '<script>try{if(localStorage.getItem("ecoscrap-theme")==="dark"||(!localStorage.getItem("ecoscrap-theme")&&window.matchMedia&&window.matchMedia("(prefers-color-scheme: dark)").matches)){document.documentElement.classList.add("dark");document.documentElement.style.colorScheme="dark"}else{document.documentElement.style.colorScheme="light"}if(localStorage.getItem("ecoscrap-dir")==="rtl"){document.documentElement.setAttribute("dir","rtl")}}catch(e){}</script>'


def head(title, description):
    return """<!DOCTYPE html>
<html lang="en" dir="ltr" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>%s</title>
    <meta name="description" content="%s">
    <meta property="og:title" content="%s">
    <meta property="og:description" content="%s">
    <meta property="og:type" content="website">
    <meta name="theme-color" content="#16A34A">
    %s
    <link rel="icon" href="assets/icons/recycle.svg" type="image/svg+xml">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>%s</script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="css/styles.css">
    <script src="js/theme.js" defer></script>
    <script src="js/rtl.js" defer></script>
    <script src="js/data.js" defer></script>
    <script src="js/main.js" defer></script>
    <script src="js/auth.js" defer></script>
</head>
<body class="bg-lightBg dark:bg-darkBg text-gray-800 dark:text-gray-200 font-sans flex flex-col min-h-screen antialiased">
""" % (title, description, title, description, _theme_script(), TAILWIND_CFG)


def navbar(active=""):
    contact_active = _is_active(active, "Contact", "contact.html")
    links = "".join(
        '<a href="%s" class="es-nav__link%s">%s</a>' % (href, _is_active(active, label, href), label)
        for label, href, _ in NAV_LINKS
    )
    contact_link = '<a href="contact.html" class="es-nav__link%s">Contact</a>' % contact_active
    mobile_links = "".join(
        '<a href="%s" class="es-mobile__link%s"><i class="fa-solid %s"></i> %s</a>'
        % (href, _is_active(active, label, href), icon, label)
        for label, href, icon in NAV_LINKS
    )
    mobile_contact = (
        '<a href="contact.html" class="es-mobile__link%s"><i class="fa-solid fa-envelope"></i> Contact</a>'
        % contact_active
    )
    return """<header class="es-nav">
    <div class="container-es">
        <div class="es-nav__inner">
            <a href="index.html" class="es-logo" aria-label="EcoScrap home">
                <span class="es-logo__mark"><i class="fa-solid fa-recycle"></i></span>
                <span class="es-logo__text">
                    <span class="es-logo__name">EcoScrap</span>
                    <span class="es-logo__tag">Scrap · To · Cash</span>
                </span>
            </a>

            <nav class="es-nav__links" aria-label="Primary navigation">
                <div class="es-drop" data-dropdown>
                    <button type="button" class="es-nav__link" data-dropdown-trigger aria-haspopup="true" aria-expanded="false">
                        Home <i class="fa-solid fa-chevron-down"></i>
                    </button>
                    <div class="es-drop__menu" role="menu">
                        <a class="es-drop__item" href="index.html" role="menuitem"><i class="fa-solid fa-house"></i> Home 1 <span class="ms-auto text-xs text-gray-400 dark:text-gray-500">Classic</span></a>
                        <a class="es-drop__item" href="home2.html" role="menuitem"><i class="fa-solid fa-sprout"></i> Home 2 <span class="ms-auto text-xs text-gray-400 dark:text-gray-500">Fresh</span></a>
                    </div>
                </div>
                %(links)s%(contact_link)s
                <div class="es-drop" data-dropdown>
                    <button type="button" class="es-nav__link" data-dropdown-trigger aria-haspopup="true" aria-expanded="false">
                        <i class="fa-solid fa-gauge-high"></i> Dashboard <i class="fa-solid fa-chevron-down"></i>
                    </button>
                    <div class="es-drop__menu" role="menu">
                        <a class="es-drop__item" href="customer-dashboard.html" role="menuitem"><i class="fa-solid fa-user"></i> User</a>
                        <a class="es-drop__item" href="admin-dashboard.html" role="menuitem"><i class="fa-solid fa-user-shield"></i> Admin</a>
                    </div>
                </div>
            </nav>

            <div class="es-nav__actions">
                <button type="button" class="es-iconbtn es-iconbtn--pill" data-rtl-toggle aria-label="Toggle RTL layout" title="Toggle RTL layout">
                    <i class="fa-solid fa-language"></i><span data-rtl-label>RTL</span>
                </button>
                <button type="button" class="es-iconbtn" data-theme-toggle aria-label="Toggle dark mode" title="Toggle dark mode">
                    <i class="fa-solid fa-moon"></i><i class="fa-solid fa-sun hidden text-yellow-400"></i>
                </button>

                <!-- Guest actions: shown only when no EcoScrap session exists -->
    <div class="flex items-center gap-1.5" data-auth-guest>
    <a href="login.html" class="es-nav__link" title="Login">Login</a>
    <a href="signup.html" class="es-btn es-btn--primary es-btn--sm">Sign Up</a>
    </div>


                <!-- Account dropdown: shown only when logged in -->
                <div class="es-drop" data-dropdown data-auth-user hidden>
                    <button type="button" class="es-nav__link es-nav__link--btn" data-dropdown-trigger aria-haspopup="true" aria-expanded="false">
                        <span class="es-avatar" data-user-initials>GU</span>
                        <span class="hidden xl:inline max-w-[8rem] truncate" data-user-name>Account</span>
                        <i class="fa-solid fa-chevron-down"></i>
                    </button>
                    <div class="es-drop__menu es-drop__menu--end" role="menu">
                        <div class="px-3 py-2.5 border-b border-gray-100 dark:border-gray-700">
                            <p class="text-sm font-semibold text-gray-900 dark:text-white truncate" data-user-name>Account</p>
                            <p class="text-xs text-gray-400 dark:text-gray-500 truncate" data-user-email>you@example.com</p>
                        </div>
                        <a class="es-drop__item" href="customer-dashboard.html" role="menuitem"><i class="fa-solid fa-gauge-high"></i> My Dashboard</a>
                        <a class="es-drop__item" href="admin-dashboard.html" role="menuitem"><i class="fa-solid fa-user-shield"></i> Admin Console</a>
                        <a class="es-drop__item" href="rate-card.html" role="menuitem"><i class="fa-solid fa-tags"></i> Today's Rates</a>
                        <div class="es-drop__sep"></div>
                        <button type="button" class="es-drop__item !text-red-500 dark:!text-red-400" data-auth-logout role="menuitem"><i class="fa-solid fa-right-from-bracket"></i> Log out</button>
                    </div>
                </div>
            </div>

            <button type="button" id="es-burger" class="es-burger es-iconbtn" aria-label="Open main menu" aria-expanded="false">
                <i class="fa-solid fa-bars"></i>
            </button>
        </div>
    </div>

    <div id="es-mobile-nav" class="es-mobile bg-white dark:bg-gray-900 border-t border-gray-100 dark:border-gray-800">
        <div class="container-es py-5 space-y-1">
            <p class="es-mobile__label px-3 pb-1">Home</p>
            <div class="ps-1">
                <button type="button" class="es-mobile__link" data-mobile-sub="mobile-home" aria-expanded="false">
                    <i class="fa-solid fa-house"></i> Home <i class="fa-solid fa-chevron-down ms-auto text-xs"></i>
                </button>
                <div id="mobile-home" class="es-mobile__sub">
                    <a href="index.html" class="es-mobile__link%(home1_active)s"><i class="fa-solid fa-angles-right"></i> Home 1 — Classic</a>
                    <a href="home2.html" class="es-mobile__link%(home2_active)s"><i class="fa-solid fa-angles-right"></i> Home 2 — Fresh</a>
                </div>
            </div>
            <p class="es-mobile__label px-3 pt-3 pb-1">Menu</p>
            %(mobile_links)s%(mobile_contact)s
            <button type="button" class="es-mobile__link" data-mobile-sub="mobile-dashboard" aria-haspopup="true" aria-controls="mobile-dashboard" aria-expanded="false">
                <i class="fa-solid fa-gauge-high"></i> Dashboard <i class="fa-solid fa-chevron-down ms-auto text-xs"></i>
            </button>
            <div id="mobile-dashboard" class="es-mobile__sub">
                <a href="customer-dashboard.html" class="es-mobile__link"><i class="fa-solid fa-user"></i> User</a>
                <a href="admin-dashboard.html" class="es-mobile__link"><i class="fa-solid fa-user-shield"></i> Admin</a>
            </div>
            <div class="flex items-center gap-2 pt-4">
                <button type="button" class="es-btn es-btn--ghost es-btn--sm flex-1" data-rtl-toggle aria-label="Toggle RTL layout"><i class="fa-solid fa-language"></i> <span data-rtl-label>RTL</span></button>
                <button type="button" class="es-btn es-btn--ghost es-btn--sm flex-1" data-theme-toggle aria-label="Toggle dark mode"><i class="fa-solid fa-circle-half-stroke"></i> <span data-theme-label>Dark Mode</span></button>
            </div>
            <div class="flex gap-2 pt-4" data-auth-guest>
                <a href="login.html" class="es-btn es-btn--ghost es-btn--block">Login</a>
                <a href="signup.html" class="es-btn es-btn--primary es-btn--block">Sign Up</a>
            </div>
            <div class="pt-2 space-y-1" data-auth-user hidden>
                <p class="es-mobile__label px-3 pt-2">Account</p>
                <a href="customer-dashboard.html" class="es-mobile__link"><i class="fa-solid fa-gauge-high"></i> My Dashboard</a>
                <a href="admin-dashboard.html" class="es-mobile__link"><i class="fa-solid fa-user-shield"></i> Admin Console</a>
                <button type="button" class="es-mobile__link !text-red-500 dark:!text-red-400" data-auth-logout><i class="fa-solid fa-right-from-bracket"></i> Log out</button>
            </div>
        </div>
    </div>
</header>
""" % {
        "links": links,
        "contact_link": contact_link,
        "home1_active": " is-active" if active in ("", "index") and active != "home2" else "",
        "home2_active": " is-active" if active == "home2" else "",
        "mobile_links": mobile_links,
        "mobile_contact": mobile_contact,
    }


def file_base(href):
    return href.split("/")[-1].replace(".html", "")


def footer():
    return """<footer class="bg-primaryDark text-white pt-16 pb-8 mt-auto">
    <div class="container-es">
        <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-6 gap-10 mb-12">
            <div class="xl:col-span-2 max-w-md">
                <a href="index.html" class="flex items-center gap-2 mb-5">
                    <span class="es-logo__mark"><i class="fa-solid fa-recycle"></i></span>
                    <span class="text-2xl font-bold text-white">EcoScrap</span>
                </a>
                <p class="text-gray-300 mb-6 text-sm leading-relaxed">Your trusted local waste pickup and scrap dealer. Book a doorstep pickup, get transparent weighing and instant payment — while keeping waste out of landfill.</p>
                <div class="flex gap-3">
                    <a href="#" class="w-10 h-10 rounded-full bg-white/10 hover:bg-primary flex items-center justify-center transition" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i></a>
                    <a href="#" class="w-10 h-10 rounded-full bg-white/10 hover:bg-primary flex items-center justify-center transition" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a>
                    <a href="#" class="w-10 h-10 rounded-full bg-white/10 hover:bg-primary flex items-center justify-center transition" aria-label="X (Twitter)"><i class="fa-brands fa-x-twitter"></i></a>
                    <a href="#" class="w-10 h-10 rounded-full bg-white/10 hover:bg-primary flex items-center justify-center transition" aria-label="YouTube"><i class="fa-brands fa-youtube"></i></a>
                    <a href="#" class="w-10 h-10 rounded-full bg-white/10 hover:bg-primary flex items-center justify-center transition" aria-label="LinkedIn"><i class="fa-brands fa-linkedin-in"></i></a>
                </div>
            </div>
            <div>
                <h4 class="text-lg font-semibold mb-5">Quick Links</h4>
                <ul class="space-y-3 text-sm text-gray-300">
                    <li><a href="about.html" class="hover:text-white flex items-center gap-2 transition"><i class="fa-solid fa-angle-right text-primaryLight text-xs"></i>About Us</a></li>
                    <li><a href="services.html" class="hover:text-white flex items-center gap-2 transition"><i class="fa-solid fa-angle-right text-primaryLight text-xs"></i>Services</a></li>
                    <li><a href="rate-card.html" class="hover:text-white flex items-center gap-2 transition"><i class="fa-solid fa-angle-right text-primaryLight text-xs"></i>Scrap Rates</a></li>
                    <li><a href="how-it-works.html" class="hover:text-white flex items-center gap-2 transition"><i class="fa-solid fa-angle-right text-primaryLight text-xs"></i>How It Works</a></li>
                    <li><a href="blog.html" class="hover:text-white flex items-center gap-2 transition"><i class="fa-solid fa-angle-right text-primaryLight text-xs"></i>Blog</a></li>
                    <li><a href="contact.html" class="hover:text-white flex items-center gap-2 transition"><i class="fa-solid fa-angle-right text-primaryLight text-xs"></i>Contact Us</a></li>
                </ul>
            </div>
            <div>
                <h4 class="text-lg font-semibold mb-5">Scrap Categories</h4>
                <ul class="space-y-3 text-sm text-gray-300">
                    <li><a href="rate-card.html#paper" class="hover:text-white flex items-center gap-2 transition"><i class="fa-solid fa-angle-right text-primaryLight text-xs"></i>Paper &amp; Cardboard</a></li>
                    <li><a href="rate-card.html#metal" class="hover:text-white flex items-center gap-2 transition"><i class="fa-solid fa-angle-right text-primaryLight text-xs"></i>Metal &amp; Aluminum</a></li>
                    <li><a href="rate-card.html#plastic" class="hover:text-white flex items-center gap-2 transition"><i class="fa-solid fa-angle-right text-primaryLight text-xs"></i>Plastic &amp; Packaging</a></li>
                    <li><a href="rate-card.html#ewaste" class="hover:text-white flex items-center gap-2 transition"><i class="fa-solid fa-angle-right text-primaryLight text-xs"></i>E-Waste</a></li>
                    <li><a href="rate-card.html#appliance" class="hover:text-white flex items-center gap-2 transition"><i class="fa-solid fa-angle-right text-primaryLight text-xs"></i>Old Appliances</a></li>
                    <li><a href="rate-card.html#battery" class="hover:text-white flex items-center gap-2 transition"><i class="fa-solid fa-angle-right text-primaryLight text-xs"></i>Batteries</a></li>
                </ul>
            </div>
            <div>
                <h4 class="text-lg font-semibold mb-5">Service Locations</h4>
                <ul class="space-y-3 text-sm text-gray-300">
                    <li><a href="index.html#locations" class="hover:text-white flex items-center gap-2 transition"><i class="fa-solid fa-location-dot text-primaryLight text-xs"></i>Delhi NCR</a></li>
                    <li><a href="index.html#locations" class="hover:text-white flex items-center gap-2 transition"><i class="fa-solid fa-location-dot text-primaryLight text-xs"></i>Mumbai</a></li>
                    <li><a href="index.html#locations" class="hover:text-white flex items-center gap-2 transition"><i class="fa-solid fa-location-dot text-primaryLight text-xs"></i>Bangalore</a></li>
                    <li><a href="index.html#locations" class="hover:text-white flex items-center gap-2 transition"><i class="fa-solid fa-location-dot text-primaryLight text-xs"></i>Pune · Hyderabad · Chennai</a></li>
                </ul>
                <div class="mt-5 space-y-2 text-sm text-gray-300">
                    <p><i class="fa-solid fa-phone text-primaryLight me-2"></i>1800-266-5432</p>
                    <p><i class="fa-solid fa-envelope text-primaryLight me-2"></i>hello@ecoscrap.in</p>
                    <p><i class="fa-solid fa-clock text-primaryLight me-2"></i>Mon – Sun · 7 AM – 9 PM</p>
                </div>
            </div>
            <div>
                <h4 class="text-lg font-semibold mb-5">Newsletter</h4>
                <p class="text-gray-300 text-sm mb-4">Get rate updates, recycling tips and pickup offers. No spam.</p>
                <form id="newsletter-form" class="flex flex-col gap-3">
                    <input type="email" name="email" placeholder="Your email address" class="es-input !bg-white/10 !border-white/25 !text-white placeholder:!text-gray-300" aria-label="Email for newsletter">
                    <button type="submit" class="es-btn es-btn--primary es-btn--block">Subscribe</button>
                </form>
                <p class="text-xs text-gray-400 mt-3">Join 8,200+ households already recycling with us.</p>
            </div>
        </div>
        <div class="border-t border-white/20 pt-7 flex flex-col md:flex-row justify-between items-center gap-4 text-gray-400 text-sm">
            <p>&copy; 2026 EcoScrap. All rights reserved. Made for a cleaner India.</p>
            <div class="flex gap-5">
                <a href="privacy-policy.html" class="hover:text-white transition">Privacy Policy</a>
                <a href="terms.html" class="hover:text-white transition">Terms &amp; Conditions</a>
                <a href="#" class="hover:text-white transition">Refund Policy</a>
            </div>
        </div>
    </div>
</footer>
"""


CAROUSEL_JS = ""


def public_page(filename, title, description, main, active=""):
    # Note: theme.js / rtl.js / data.js / main.js are already injected by head()
    # (defer) — do NOT append them again here or event listeners double-bind.
    html = (
        head(title, description)
        + navbar(active)
        + '<main class="flex-grow">\n'
        + main
        + "\n</main>\n"
        + footer()
        + "</body>\n</html>\n"
    )
    out = os.path.join(BASE_DIR, filename)
    with open(out, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(html)
    print("wrote", filename, "(%d sections detected above)" % main.count("<section"))


def write_file(filename, html):
    out = os.path.join(BASE_DIR, filename)
    with open(out, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(html)
    print("wrote", filename)