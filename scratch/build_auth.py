"""
EcoScrap — authentication pages builder.

Generates split-screen login.html, signup.html and forgot-password.html.
These pages intentionally have no navbar/footer; they reuse the shared
stylesheet and the global theme/RTL scripts plus js/auth.js.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_base import BASE_DIR, TAILWIND_CFG, _theme_script  # noqa: E402

H = "assets/images/"

HEAD = """<!DOCTYPE html>
<html lang="en" dir="ltr" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <meta name="theme-color" content="#16A34A">
    {theme}
    <link rel="icon" href="assets/icons/recycle.svg" type="image/svg+xml">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>{cfg}</script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="css/styles.css">
    <script src="js/theme.js" defer></script>
    <script src="js/rtl.js" defer></script>
    <script src="js/main.js" defer></script>
    <script src="js/auth.js" defer></script>
</head>
<body data-no-backtop class="bg-white dark:bg-darkBg text-gray-800 dark:text-gray-200 font-sans min-h-screen antialiased">
"""

BRAND_HEAD = """<div class="flex items-center justify-between">
    <a href="index.html" class="es-logo" aria-label="EcoScrap home">
        <span class="es-logo__mark"><i class="fa-solid fa-recycle"></i></span>
        <span class="es-logo__text">
            <span class="es-logo__name">EcoScrap</span>
            <span class="es-logo__tag">Scrap · To · Cash</span>
        </span>
    </a>
    <div class="flex items-center gap-1">
        <button type="button" class="es-iconbtn" data-rtl-toggle aria-label="Toggle RTL layout" title="Toggle RTL layout"><i class="fa-solid fa-language"></i></button>
        <button type="button" class="es-iconbtn" data-theme-toggle aria-label="Toggle dark mode" title="Toggle dark mode"><i class="fa-solid fa-moon"></i><i class="fa-solid fa-sun hidden text-yellow-400"></i></button>
    </div>
</div>
"""


def brand_panel(img, heading, sub, points, stat_value, stat_label):
    bullets = "".join(
        '<li class="flex items-start gap-3"><span class="mt-0.5 inline-flex h-7 w-7 flex-none items-center justify-center rounded-full bg-white/15 text-primaryLight"><i class="fa-solid %s"></i></span><span class="text-sm text-gray-200">%s</span></li>' % (icon, text)
        for icon, text in points
    )
    return """<div class="hidden lg:flex lg:w-1/2 relative overflow-hidden">
    <div class="hero__media absolute inset-0" style="background-image:url('{img}')" role="img" aria-label="{alt}"></div>
    <div class="absolute inset-0 bg-primaryDark/90"></div>
    <div class="relative z-10 flex flex-col justify-center px-16 py-14 text-white w-full">
        <span class="es-eyebrow !bg-white/15 !text-primaryLight">EcoScrap · Scrap to Cash</span>
        <h2 class="mt-6 text-4xl xl:text-5xl font-extrabold leading-tight text-white">{heading}</h2>
        <p class="mt-5 text-lg text-gray-200 max-w-md">{sub}</p>
        <ul class="mt-9 space-y-4 max-w-md">{bullets}</ul>
        <div class="mt-10 flex items-center gap-4 rounded-2xl bg-white/10 border border-white/15 px-5 py-4 max-w-xs">
            <span class="text-3xl font-extrabold text-primaryLight">{stat_value}</span>
            <span class="text-sm text-gray-200">{stat_label}</span>
        </div>
    </div>
</div>
""".format(img=H + img, alt=heading, heading=heading, sub=sub, bullets=bullets, stat_value=stat_value, stat_label=stat_label)


def page(filename, title, desc, active_label, left_html, panel_html):
    html = (
        HEAD.format(title=title, desc=desc, theme=_theme_script(), cfg=TAILWIND_CFG)
        + '<div class="flex min-h-screen">\n'
        + '  <div class="w-full lg:w-1/2 flex flex-col px-6 sm:px-10 lg:px-16 py-8">\n'
        + "    " + BRAND_HEAD
        + '    <div class="flex-1 flex items-center justify-center py-10">\n'
        + '      <div class="w-full max-w-md">\n'
        + left_html
        + "\n      </div>\n    </div>\n"
        + '    <p class="text-center text-xs text-gray-400 dark:text-gray-500">© 2026 EcoScrap · Demo interface. No real account is created.</p>\n'
        + "  </div>\n"
        + panel_html
        + "</div>\n"
        + "</body>\n</html>\n"
    )
    out = os.path.join(BASE_DIR, filename)
    with open(out, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(html)
    print("wrote", filename, "(%d sections)" % left_html.count("<section"))


SOCIAL_ROW = """<div class="my-7 flex items-center before:flex-1 before:border-t before:border-gray-200 dark:before:border-gray-700 after:flex-1 after:border-t after:border-gray-200 dark:after:border-gray-700">
    <span class="px-4 text-xs uppercase tracking-wide text-gray-400">or continue with</span>
</div>
<div class="grid grid-cols-3 gap-3">
    <button type="button" data-social="Google" class="es-btn es-btn--ghost"><i class="fa-brands fa-google text-red-500"></i> Google</button>
    <button type="button" data-social="Facebook" class="es-btn es-btn--ghost"><i class="fa-brands fa-facebook-f text-blue-600"></i> Facebook</button>
    <button type="button" data-social="Apple" class="es-btn es-btn--ghost"><i class="fa-brands fa-apple"></i> Apple</button>
</div>
"""

DEMO_HINT = """<div class="mt-6 rounded-xl border border-primary/20 bg-primary/5 px-4 py-3 text-xs text-gray-600 dark:text-gray-300">
    <p class="font-semibold text-primary dark:text-primaryLight"><i class="fa-solid fa-circle-info me-1"></i>Demo login</p>
    <p class="mt-1">Any email + a 6+ character password works and takes you to your dashboard. Use the navbar <strong>Dashboard</strong> menu for instant access without signing in.</p>
</div>
"""


def login_left():
    return """<div>
    <span class="es-eyebrow">Welcome Back</span>
    <h1 class="mt-4 text-3xl font-extrabold text-gray-900 dark:text-white">Log in to EcoScrap</h1>
    <p class="mt-3 text-gray-500 dark:text-gray-400">Track pickups, view payouts and schedule your next doorstep collection.</p>
</div>

<form id="login-form" data-validate class="mt-8 space-y-5">
    <input type="hidden" id="login-role" name="role" value="customer">
    <div data-form-alert class="es-alert es-alert--error"></div>

    <div class="es-field">
        <label class="es-label" for="l-email">Email or phone</label>
        <input id="l-email" name="email" type="text" class="es-input" data-label="Email or phone" autocomplete="username" placeholder="you@example.com" required>
        <span class="es-error"><i class="fa-solid fa-circle-exclamation"></i></span>
    </div>

    <div class="es-field">
        <label class="es-label" for="l-password">Password</label>
        <div class="relative">
            <input id="l-password" name="password" type="password" class="es-input !pe-11" data-label="Password" autocomplete="current-password" placeholder="••••••••" required>
            <button type="button" class="absolute inset-y-0 end-3 flex items-center text-gray-400 hover:text-primary" data-pw-toggle="l-password" aria-label="Show password"><i class="fa-solid fa-eye"></i></button>
        </div>
        <span class="es-error"><i class="fa-solid fa-circle-exclamation"></i></span>
    </div>

    <div class="flex items-center justify-between">
        <label class="flex items-center gap-2 text-sm text-gray-600 dark:text-gray-300"><input type="checkbox" name="remember" class="rounded border-gray-300 text-primary focus:ring-primary"> Remember me</label>
        <a href="forgot-password.html" class="text-sm font-semibold text-primary hover:underline">Forgot password?</a>
    </div>

    <button type="submit" class="es-btn es-btn--primary es-btn--lg es-btn--block">Log In <i class="fa-solid fa-right-to-bracket"></i></button>
</form>

""" + SOCIAL_ROW + DEMO_HINT + """
<p class="mt-7 text-center text-sm text-gray-600 dark:text-gray-400">New to EcoScrap? <a href="signup.html" class="font-bold text-primary hover:underline">Create an account</a></p>
"""


def signup_left():
    return """<div>
    <span class="es-eyebrow">Get Started Free</span>
    <h1 class="mt-4 text-3xl font-extrabold text-gray-900 dark:text-white">Create your account</h1>
    <p class="mt-3 text-gray-500 dark:text-gray-400">It takes two minutes. Book a pickup and get paid the same visit.</p>
</div>

<form id="signup-form" data-validate class="mt-8 space-y-5">
    <div data-form-alert class="es-alert es-alert--error"></div>

    <div class="es-field">
        <label class="es-label" for="s-name">Full name</label>
        <input id="s-name" name="name" type="text" class="es-input" data-label="Full name" autocomplete="name" placeholder="e.g. Priya Sharma" required>
        <span class="es-error"><i class="fa-solid fa-circle-exclamation"></i></span>
    </div>

    <div class="grid sm:grid-cols-2 gap-4">
        <div class="es-field">
            <label class="es-label" for="s-phone">Phone number</label>
            <input id="s-phone" name="phone" type="tel" class="es-input" data-label="Phone number" autocomplete="tel" placeholder="+91 98xxx xxxxx" required>
            <span class="es-error"><i class="fa-solid fa-circle-exclamation"></i></span>
        </div>
        <div class="es-field">
            <label class="es-label" for="s-email">Mail ID</label>
            <input id="s-email" name="email" type="email" class="es-input" data-label="Mail ID" autocomplete="email" placeholder="you@example.com" required>
            <span class="es-error"><i class="fa-solid fa-circle-exclamation"></i></span>
        </div>
    </div>

    <div class="grid sm:grid-cols-2 gap-4">
        <div class="es-field">
            <label class="es-label" for="s-password">Password</label>
            <div class="relative">
                <input id="s-password" name="password" type="password" class="es-input !pe-11" data-label="Password" autocomplete="new-password" placeholder="6+ characters" required>
                <button type="button" class="absolute inset-y-0 end-3 flex items-center text-gray-400 hover:text-primary" data-pw-toggle="s-password" aria-label="Show password"><i class="fa-solid fa-eye"></i></button>
            </div>
            <span class="es-error"><i class="fa-solid fa-circle-exclamation"></i></span>
        </div>
        <div class="es-field">
            <label class="es-label" for="s-confirm">Confirm password</label>
            <input id="s-confirm" name="confirm" type="password" class="es-input" data-label="Confirm password" data-match="s-password" autocomplete="new-password" placeholder="Repeat password" required>
            <span class="es-error"><i class="fa-solid fa-circle-exclamation"></i></span>
        </div>
    </div>

    <label class="flex items-start gap-3 text-sm text-gray-600 dark:text-gray-300">
        <input type="checkbox" name="terms" data-label="Terms agreement" class="mt-1 rounded border-gray-300 text-primary focus:ring-primary" required>
        <span>I agree to the <a href="terms.html" class="font-semibold text-primary hover:underline">Terms</a> and <a href="privacy-policy.html" class="font-semibold text-primary hover:underline">Privacy Policy</a>.</span>
    </label>
    <span class="es-error"><i class="fa-solid fa-circle-exclamation"></i></span>

    <button type="submit" class="es-btn es-btn--primary es-btn--lg es-btn--block">Create Account <i class="fa-solid fa-arrow-right rtl-flip"></i></button>
</form>

""" + SOCIAL_ROW + """
<p class="mt-7 text-center text-sm text-gray-600 dark:text-gray-400">Already have an account? <a href="login.html" class="font-bold text-primary hover:underline">Log in</a></p>
"""


def forgot_left():
    return """<a href="login.html" class="inline-flex items-center gap-2 text-sm font-semibold text-primary hover:underline mb-8"><i class="fa-solid fa-arrow-left rtl-flip"></i> Back to login</a>
<div>
    <span class="es-eyebrow">Password Help</span>
    <h1 class="mt-4 text-3xl font-extrabold text-gray-900 dark:text-white">Forgot your password?</h1>
    <p class="mt-3 text-gray-500 dark:text-gray-400">Enter the email linked to your account and we'll send a reset link. Demo only — nothing is actually emailed.</p>
</div>

<form id="forgot-form" data-validate class="mt-8 space-y-5">
    <div data-form-alert class="es-alert es-alert--error"></div>
    <div class="es-field">
        <label class="es-label" for="f-email">Email address</label>
        <input id="f-email" name="email" type="email" class="es-input" data-label="Email address" autocomplete="email" placeholder="you@example.com" required>
        <span class="es-error"><i class="fa-solid fa-circle-exclamation"></i></span>
    </div>
    <button type="submit" class="es-btn es-btn--primary es-btn--lg es-btn--block">Send Reset Link <i class="fa-solid fa-paper-plane"></i></button>
</form>

<div class="mt-8 es-panel">
    <h3 class="font-bold text-gray-900 dark:text-white text-sm"><i class="fa-solid fa-shield-halved text-primary me-2"></i>Prefer to talk?</h3>
    <p class="mt-2 text-sm text-gray-500 dark:text-gray-400">Call our support line at <strong>1800-266-5432</strong> (7 AM – 9 PM) and we'll help you regain access.</p>
</div>
"""


def main():
    page(
        "login.html",
        "Login | EcoScrap",
        "Log in to your EcoScrap account to schedule scrap pickups, track requests and manage payouts.",
        "Login", login_left(),
        brand_panel(
            "hero-recycle.jpg",
            "Join the Green Revolution.",
            "Recycle your waste, earn rewards and help build a sustainable future for your city.",
            [("fa-truck-fast", "Doorstep pickup in as little as 40 minutes"),
             ("fa-scale-balanced", "Transparent, calibrated weighing every time"),
             ("fa-indian-rupee-sign", "Instant UPI, bank or cash payouts"),
             ("fa-leaf", "Certified recycling and a lower carbon footprint")],
            "42K+", "pickups completed"
        )
    )
    page(
        "signup.html",
        "Create Account | EcoScrap",
        "Create a free EcoScrap account to book scrap pickups, track collections and receive instant payouts.",
        "Sign Up", signup_left(),
        brand_panel(
            "collection.jpg",
            "Recycle. Earn. Repeat.",
            "Turn everyday household scrap into real money while keeping valuable material out of landfill.",
            [("fa-calendar-check", "Book a slot in under two minutes"),
             ("fa-arrows-rotate", "Set recurring weekly or monthly pickups"),
             ("fa-file-shield", "E-waste handover certificates on request"),
             ("fa-earth-asia", "Every kilo tracked to a certified recycler")],
            "6", "cities and growing"
        )
    )
    page(
        "forgot-password.html",
        "Forgot Password | EcoScrap",
        "Reset your EcoScrap password — enter your email and we'll send a secure reset link.",
        "Forgot Password", forgot_left(),
        brand_panel(
            "support.jpg",
            "We've got you covered.",
            "Locked out? It happens. We'll get you back to booking pickups in no time.",
            [("fa-envelope-open-text", "Reset link sent to your registered email"),
             ("fa-clock", "Support available 7 AM – 9 PM, every day"),
             ("fa-lock", "Your data is encrypted at rest and in transit"),
             ("fa-headset", "Toll-free helpline: 1800-266-5432")],
            "2 hrs", "average response time"
        )
    )


if __name__ == "__main__":
    main()
