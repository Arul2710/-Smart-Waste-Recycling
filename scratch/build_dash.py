"""
EcoScrap â€” dashboard pages builder.

Generates customer-dashboard.html and admin-dashboard.html using the shared
.es-dash sidebar layout. All data is demo data rendered client-side by
js/dashboard.js (customer) and js/admin-dashboard.js (admin).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_base import BASE_DIR, TAILWIND_CFG, _theme_script  # noqa: E402

HEAD = """<!DOCTYPE html>
<html lang="en" dir="ltr" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <meta name="robots" content="noindex">
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
    <script src="js/data.js" defer></script>
    <script src="js/main.js" defer></script>
    <script src="js/auth.js" defer></script>
    <script src="js/dash-data.js" defer></script>
    <script src="{app}" defer></script>
</head>
<body data-no-backtop class="bg-slate-50 dark:bg-darkBg text-gray-800 dark:text-gray-200 font-sans antialiased">
"""


def sidebar(brand_sub, role_badge, nav_items, foot_links):
    nav = "".join(
        '<button type="button" class="es-navlink" data-dash-nav="%s"><i class="fa-solid %s"></i> <span>%s</span></button>'
        % (key, icon, label)
        for key, label, icon in nav_items
    )
    extra = "".join(foot_links)
    return """<aside class="es-dash__sidebar" id="dash-sidebar">
    <div class="flex items-center gap-2 px-5 py-5 border-b border-gray-100 dark:border-gray-800">
        <a href="index.html" class="es-logo" aria-label="EcoScrap home">
            <span class="es-logo__mark"><i class="fa-solid fa-recycle"></i></span>
            <span class="es-logo__text"><span class="es-logo__name">EcoScrap</span><span class="es-logo__tag">{brand_sub}</span></span>
        </a>
        <button type="button" class="es-iconbtn ms-auto lg:hidden" id="dash-close" aria-label="Close menu"><i class="fa-solid fa-xmark"></i></button>
    </div>
    <div class="px-5 py-3">
        <span class="es-badge es-badge--green"><i class="fa-solid fa-circle-check"></i> {role_badge}</span>
    </div>
    <nav class="flex-1 px-3 pb-4 space-y-0.5" aria-label="Dashboard sections">
        {nav}
    </nav>
    <div class="px-3 py-4 border-t border-gray-100 dark:border-gray-800 space-y-0.5">
        {extra}
        <a href="index.html" class="es-navlink"><i class="fa-solid fa-arrow-left rtl-flip"></i> <span>Back to Website</span></a>
        <button type="button" class="es-navlink text-red-500 dark:text-red-400" data-dash-logout><i class="fa-solid fa-right-from-bracket"></i> <span>Log Out</span></button>
    </div>
</aside>
<div class="es-dash__backdrop" id="dash-backdrop"></div>
""".format(brand_sub=brand_sub, role_badge=role_badge, nav=nav, extra=extra)


def topbar(role_title, role="customer"):
    # The customer dashboard has a real notifications view, so the bell
    # navigates there and shows a live unread badge. The admin dashboard has
    # no notifications view, so it gets a working "Messages" action instead
    # rather than a button that does nothing.
    if role == "admin":
        quick = """<button type="button" class="es-iconbtn" data-dash-nav="pickups" title="Pickup Requests" aria-label="Pickup Requests">
                <i class="fa-solid fa-truck-ramp-box"></i>
            </button>"""
    else:
        quick = """<button type="button" class="es-iconbtn relative" data-dash-nav="notifications" title="Notifications" aria-label="Notifications">
                <i class="fa-regular fa-bell"></i>
                <span class="absolute -top-0.5 -end-0.5 h-4 min-w-4 px-1 rounded-full bg-red-500 text-white text-[10px] font-bold flex items-center justify-center" data-notif-badge>3</span>
            </button>"""
    return """<header class="sticky top-0 z-40 bg-white/90 dark:bg-[#0f172a]/90 backdrop-blur border-b border-gray-100 dark:border-gray-800">
    <div class="flex items-center gap-3 px-4 sm:px-6 py-3.5">
        <button type="button" class="es-iconbtn lg:hidden flex-none" id="dash-burger" aria-label="Open menu"><i class="fa-solid fa-bars"></i></button>
        <div class="min-w-0 flex-1">
            <h1 class="text-lg sm:text-xl font-bold text-gray-900 dark:text-white truncate" id="dash-title">Dashboard</h1>
            <p class="hidden sm:block text-xs text-gray-500 dark:text-gray-400 truncate">{role_title}</p>
        </div>
        <div class="ms-auto flex items-center gap-1.5 flex-none">
            <a href="index.html" class="es-iconbtn hidden sm:inline-flex" title="Visit website" aria-label="Visit website"><i class="fa-solid fa-globe"></i></a>
            {quick}
            <button type="button" class="es-iconbtn es-iconbtn--pill" data-rtl-toggle title="Toggle RTL layout" aria-label="Toggle RTL layout">
                <i class="fa-solid fa-language"></i><span data-rtl-label>RTL</span>
            </button>
            <button type="button" class="es-iconbtn" data-theme-toggle title="Toggle dark mode" aria-label="Toggle dark mode">
                <i class="fa-solid fa-moon"></i><i class="fa-solid fa-sun hidden text-yellow-400"></i>
            </button>
            <div class="flex items-center gap-2 ps-2 ms-1 border-s border-gray-200 dark:border-gray-700">
                <span class="w-9 h-9 flex-none rounded-full bg-gradient-to-br from-primary to-primaryDark text-white flex items-center justify-center text-xs font-bold" data-user-initials>GU</span>
                <div class="hidden md:block leading-tight">
                    <p class="text-sm font-semibold text-gray-900 dark:text-white" data-user-name>Green User</p>
                    <p class="text-[11px] text-gray-500 dark:text-gray-400" data-user-email>demo@ecoscrap.in</p>
                </div>
            </div>
        </div>
    </div>
</header>
""".format(role_title=role_title, quick=quick)


def stat(icon, tone, value_attr, label):
    return """<div class="es-stat">
    <span class="es-stat__icon bg-{tone}/10 text-{tone}"><i class="fa-solid {icon}"></i></span>
    <div>
        <p class="es-stat__value" data-stat="{attr}">â€”</p>
        <p class="es-stat__label">{label}</p>
    </div>
</div>""".format(icon=icon, tone=tone, attr=value_attr, label=label)


def section_card(title, body, action=""):
    return """<div class="es-card">
    <div class="flex items-center justify-between gap-3 p-5 border-b border-gray-100 dark:border-gray-700">
        <h2 class="font-bold text-gray-900 dark:text-white">""" + title + """</h2>
        <div class="flex items-center gap-2">""" + action + """</div>
    </div>
    <div class="p-5">""" + body + """</div>
</div>"""


def table(headers, body_id, extra_class="min-w-[720px]"):
    head = "".join("<th>" + h + "</th>" for h in headers)
    return """<div class="overflow-x-auto"><table class="es-table {cls}">
    <thead><tr>{head}</tr></thead>
    <tbody id="{bid}"><tr><td colspan="{cols}" class="es-empty">Loadingâ€¦</td></tr></tbody>
</table></div>""".format(cls=extra_class, head=head, bid=body_id, cols=len(headers))


CUSTOMER_VIEWS_TEMPLATE = """
<!-- Overview -->
<section class="es-dash__view is-active" data-dash-view="overview">
    <div class="grid sm:grid-cols-2 xl:grid-cols-4 gap-4">
        {s_pickups}{s_weight}{s_earn}{s_co2}
    </div>
    <div class="grid lg:grid-cols-3 gap-5 mt-5">
        <div class="lg:col-span-2 min-w-0">
            {recent}
        </div>
        <div class="space-y-5 min-w-0">
            {quick}
            {impact}
        </div>
    </div>
</section>

<!-- Schedule pickup -->
<section class="es-dash__view" data-dash-view="schedule">
    <div class="grid lg:grid-cols-3 gap-5">
        <div class="lg:col-span-2 min-w-0">
            {schedule_form}
        </div>
        <div class="space-y-5 min-w-0">
            {price_guide}
        </div>
    </div>
</section>

<!-- My requests -->
<section class="es-dash__view" data-dash-view="requests">
    {requests_card}
</section>

<!-- Live status -->
<section class="es-dash__view" data-dash-view="status">
    <div class="grid lg:grid-cols-3 gap-5">
        <div class="lg:col-span-2 min-w-0">{tracker}</div>
        <div class="space-y-5 min-w-0">{tracker_side}</div>
    </div>
</section>

<!-- Weight history -->
<section class="es-dash__view" data-dash-view="weights">
    <div class="grid lg:grid-cols-3 gap-5">
        <div class="lg:col-span-2 min-w-0">{weight_chart_card}</div>
        <div class="min-w-0">{weight_side}</div>
    </div>
    <div class="mt-5">{weight_table}</div>
</section>

<!-- Payout history -->
<section class="es-dash__view" data-dash-view="payouts">
    <div class="grid sm:grid-cols-3 gap-4">
        {pay_total}{pay_pending}{pay_avg}
    </div>
    <div class="mt-5">{payout_table}</div>
</section>

<!-- Payment preferences -->
<section class="es-dash__view" data-dash-view="payment">
    <div class="grid lg:grid-cols-2 gap-5">
        <div class="min-w-0">{payment_form}</div>
        <div class="space-y-5 min-w-0">{payment_info}</div>
    </div>
</section>

<!-- Notifications -->
<section class="es-dash__view" data-dash-view="notifications">
    <div class="grid lg:grid-cols-3 gap-5">
        <div class="lg:col-span-2 min-w-0">{notif_list}</div>
        <div class="min-w-0">{notif_prefs}</div>
    </div>
</section>

<!-- Profile -->
<section class="es-dash__view" data-dash-view="profile">
    <div class="grid lg:grid-cols-3 gap-5">
        <div class="lg:col-span-2 min-w-0">{profile_form}</div>
        <div class="space-y-5 min-w-0">{profile_side}</div>
    </div>
</section>
"""


def customer_content():
    s_pickups = stat("fa-box-open", "green", "pickups", "Total pickups")
    s_weight = stat("fa-weight-hanging", "blue", "weight", "Total weight (kg)")
    s_earn = stat("fa-indian-rupee-sign", "amber", "earnings", "Total earnings")
    s_co2 = stat("fa-leaf", "emerald", "co2", "COâ‚‚ saved (kg)")

    recent = section_card(
        "Recent Pickups",
        table(["Request", "Material", "Weight", "Payout", "Status"], "cust-recent-body"),
        action='<button type="button" class="es-btn es-btn--ghost es-btn--sm" data-dash-nav="requests">View all</button>'
    )
    quick = section_card(
        "Quick Actions",
        """<div class="grid grid-cols-2 gap-3">
        <button type="button" class="es-panel es-panel--hover flex flex-col items-center gap-2 py-5" data-dash-nav="schedule"><i class="fa-solid fa-calendar-plus text-2xl text-primary"></i><span class="text-sm font-semibold">Book Pickup</span></button>
        <button type="button" class="es-panel es-panel--hover flex flex-col items-center gap-2 py-5" data-dash-nav="status"><i class="fa-solid fa-truck-fast text-2xl text-primary"></i><span class="text-sm font-semibold">Track Live</span></button>
        <button type="button" class="es-panel es-panel--hover flex flex-col items-center gap-2 py-5" data-dash-nav="payouts"><i class="fa-solid fa-indian-rupee-sign text-2xl text-primary"></i><span class="text-sm font-semibold">Payouts</span></button>
        <a href="rate-card.html" class="es-panel es-panel--hover flex flex-col items-center gap-2 py-5"><i class="fa-solid fa-tags text-2xl text-primary"></i><span class="text-sm font-semibold">Rate Card</span></a>
        </div>"""
    )
    impact = section_card(
        "Your Green Impact",
        """<p class="text-sm text-gray-500 dark:text-gray-400">You have kept <strong class="text-primary" data-stat="weight">0</strong> kg of material in circulation.</p>
        <div class="es-progress mt-4"><span class="es-progress__fill block" style="width:68%"></span></div>
        <p class="text-xs text-gray-400 mt-2">68% toward your next Green Ambassador badge.</p>"""
    )

    schedule_form = """<div class="es-card">
        <div class="p-5 border-b border-gray-100 dark:border-gray-700">
            <h2 class="font-bold text-gray-900 dark:text-white">Schedule a New Pickup</h2>
            <p class="text-sm text-gray-500 dark:text-gray-400 mt-1">Fill in the details and we'll confirm a collector for your slot.</p>
        </div>
        <form id="schedule-form" data-validate class="p-5 space-y-5">
            <div data-form-alert class="es-alert es-alert--error"></div>
            <div class="grid sm:grid-cols-2 gap-4">
                <div class="es-field"><label class="es-label" for="sc-cat">Primary category</label>
                    <select id="sc-cat" name="category" class="es-select">
                        <option>Paper &amp; Cardboard</option><option>Metal &amp; Aluminum</option><option>Plastic &amp; Packaging</option>
                        <option>E-Waste</option><option>Old Appliances</option><option>Batteries &amp; Recyclables</option><option>Mixed Scrap</option>
                    </select>
                </div>
                <div class="es-field"><label class="es-label" for="sc-weight">Estimated weight (kg)</label>
                    <input id="sc-weight" name="weight" type="number" min="0.5" step="0.5" value="10" class="es-input" data-label="Estimated weight" required>
                    <span class="es-error"><i class="fa-solid fa-circle-exclamation"></i></span>
                </div>
            </div>
            <div class="grid sm:grid-cols-3 gap-4">
                <div class="es-field"><label class="es-label" for="sc-date">Date</label>
                    <input id="sc-date" name="date" type="date" class="es-input" data-label="Pickup date" required>
                    <span class="es-error"><i class="fa-solid fa-circle-exclamation"></i></span>
                </div>
                <div class="es-field"><label class="es-label" for="sc-slot">Time slot</label>
                    <select id="sc-slot" name="slot" class="es-select"><option>Morning (7â€“11 AM)</option><option>Afternoon (12â€“4 PM)</option><option>Evening (5â€“8 PM)</option></select>
                </div>
                <div class="es-field"><label class="es-label" for="sc-city">City</label>
                    <select id="sc-city" name="city" class="es-select"><option>Delhi NCR</option><option>Mumbai</option><option>Bangalore</option><option>Pune</option><option>Hyderabad</option><option>Chennai</option></select>
                </div>
            </div>
            <div class="es-field"><label class="es-label" for="sc-address">Pickup address</label>
                <textarea id="sc-address" name="address" class="es-textarea !min-h-[5rem]" data-label="Pickup address" data-minlen="8" placeholder="Flat / house, street, landmark, PIN" required></textarea>
                <span class="es-error"><i class="fa-solid fa-circle-exclamation"></i></span>
            </div>
            <div class="es-field"><label class="es-label" for="sc-notes">Notes for the collector <span class="text-gray-400 font-normal">(optional)</span></label>
                <input id="sc-notes" name="notes" type="text" class="es-input" placeholder="e.g. Ring the bell twice, ground floor"></div>
            <div class="flex flex-col sm:flex-row gap-3">
                <button type="submit" class="es-btn es-btn--primary es-btn--lg"><i class="fa-solid fa-calendar-check"></i> Confirm Pickup</button>
                <button type="reset" class="es-btn es-btn--ghost es-btn--lg">Reset</button>
            </div>
        </form>
    </div>"""

    price_guide = section_card(
        "Estimated Value",
        """<p class="text-sm text-gray-500 dark:text-gray-400">Based on today's rates, a <strong>10 kg</strong> mixed load is worth roughly:</p>
        <p class="text-3xl font-extrabold text-primary mt-2" id="est-value">â‚¹180</p>
        <ul class="mt-4 space-y-2 text-sm text-gray-500 dark:text-gray-400">
            <li class="flex justify-between"><span>Paper</span><span>â‚¹14/kg</span></li>
            <li class="flex justify-between"><span>Metal</span><span>â‚¹28/kg+</span></li>
            <li class="flex justify-between"><span>E-Waste</span><span>â‚¹45/kg</span></li>
            <li class="flex justify-between"><span>Batteries</span><span>â‚¹180/kg</span></li>
        </ul>
        <a href="rate-card.html" class="es-btn es-btn--ghost es-btn--sm es-btn--block mt-4">Full Rate Card</a>"""
    )

    requests_card = section_card(
        "My Pickup Requests",
        """<div class="flex flex-wrap gap-2 mb-4" id="cust-req-filters"></div>"""
        + table(["Request", "Category", "Date", "Weight", "Amount", "Status", ""], "cust-requests-body"),
        action='<button type="button" class="es-btn es-btn--primary es-btn--sm" data-dash-nav="schedule"><i class="fa-solid fa-plus"></i> New</button>'
    )

    tracker = """<div class="es-card">
        <div class="flex flex-wrap items-center justify-between gap-3 p-5 border-b border-gray-100 dark:border-gray-700">
            <div>
                <h2 class="font-bold text-gray-900 dark:text-white">Live Pickup Tracker</h2>
                <p class="text-sm text-gray-500 dark:text-gray-400 mt-1" id="tracker-req">Request #REQ-1042</p>
            </div>
            <span class="es-badge es-badge--amber" data-tracker-badge><i class="fa-solid fa-truck-fast"></i> En route</span>
        </div>
        <div class="p-5">
            <div class="es-stepper pt-2">
                <div class="es-stepper__track">
                    <div class="es-stepper__step is-done"><span class="es-stepper__dot"><i class="fa-solid fa-check"></i></span><span class="es-stepper__label">Booked</span></div>
                    <div class="es-stepper__step is-done"><span class="es-stepper__dot"><i class="fa-solid fa-check"></i></span><span class="es-stepper__label">Dispatched</span></div>
                    <div class="es-stepper__step is-current"><span class="es-stepper__dot">3</span><span class="es-stepper__label">En route</span></div>
                    <div class="es-stepper__step"><span class="es-stepper__dot">4</span><span class="es-stepper__label">Verify</span></div>
                    <div class="es-stepper__step"><span class="es-stepper__dot">5</span><span class="es-stepper__label">Paid</span></div>
                </div>
            </div>
            <div class="grid sm:grid-cols-3 gap-4 mt-8">
                <div class="es-panel text-center"><p class="text-xs text-gray-500 dark:text-gray-400">Collector</p><p class="font-bold text-gray-900 dark:text-white mt-1">David M.</p></div>
                <div class="es-panel text-center"><p class="text-xs text-gray-500 dark:text-gray-400">Vehicle</p><p class="font-bold text-gray-900 dark:text-white mt-1">DL-8C-2201</p></div>
                <div class="es-panel text-center"><p class="text-xs text-gray-500 dark:text-gray-400">ETA</p><p class="font-bold text-green-600 dark:text-primaryLight mt-1">â‰ˆ 18 min</p></div>
            </div>
            <div class="es-progress mt-6"><span class="es-progress__fill block" style="width:64%"></span></div>
            <p class="text-xs text-gray-400 mt-2">64% of the journey complete</p>
        </div>
    </div>"""

    tracker_side = section_card(
        "Notification Timeline",
        """<ol class="space-y-4 text-sm">
        <li class="flex gap-3"><span class="w-2 h-2 rounded-full bg-primary mt-1.5"></span><div><p class="font-semibold text-gray-900 dark:text-white">Collector dispatched</p><p class="text-xs text-gray-500 dark:text-gray-400">2:10 PM</p></div></li>
        <li class="flex gap-3"><span class="w-2 h-2 rounded-full bg-primary mt-1.5"></span><div><p class="font-semibold text-gray-900 dark:text-white">Pickup confirmed</p><p class="text-xs text-gray-500 dark:text-gray-400">1:45 PM</p></div></li>
        <li class="flex gap-3"><span class="w-2 h-2 rounded-full bg-gray-300 dark:bg-gray-600 mt-1.5"></span><div><p class="font-semibold text-gray-500 dark:text-gray-400">Awaiting weighing</p><p class="text-xs text-gray-400">Pending</p></div></li>
        </ol>"""
    )

    weight_chart_card = """<div class="es-card">
        <div class="p-5 border-b border-gray-100 dark:border-gray-700">
            <h2 class="font-bold text-gray-900 dark:text-white">Monthly Collected Weight</h2>
            <p class="text-sm text-gray-500 dark:text-gray-400 mt-1">Kilograms diverted from landfill each month.</p>
        </div>
        <div class="p-5"><div class="es-bar" id="cust-weight-chart"></div></div>
    </div>"""

    weight_side = section_card(
        "Category Split",
        """<div class="space-y-4" id="cust-category-split"></div>"""
    )

    weight_table = section_card(
        "Weight Ledger",
        table(["Date", "Category", "Verified weight", "Rate", "Value"], "cust-weights-body")
    )

    pay_total = stat("fa-indian-rupee-sign", "green", "pay-total", "Total earned")
    pay_pending = stat("fa-hourglass-half", "amber", "pay-pending", "Pending")
    pay_avg = stat("fa-chart-simple", "blue", "pay-avg", "Avg/pickup")

    payout_table = section_card(
        "Payout History",
        table(["Date", "Request", "Method", "Weight", "Amount", "Status"], "cust-payouts-body")
    )

    payment_form = """<div class="es-card">
        <div class="p-5 border-b border-gray-100 dark:border-gray-700">
            <h2 class="font-bold text-gray-900 dark:text-white">Payment Preferences</h2>
            <p class="text-sm text-gray-500 dark:text-gray-400 mt-1">Choose how you'd like to receive your payouts.</p>
        </div>
        <form id="payment-form" data-validate class="p-5 space-y-5">
            <div data-form-alert class="es-alert es-alert--error"></div>
            <div class="space-y-3">
                <label class="flex items-start gap-3 es-panel cursor-pointer"><input type="radio" name="method" value="UPI" checked class="mt-1 text-primary focus:ring-primary"><span><strong class="block text-gray-900 dark:text-white">UPI (recommended)</strong><span class="text-sm text-gray-500 dark:text-gray-400">Instant settlement to your UPI ID.</span></span></label>
                <label class="flex items-start gap-3 es-panel cursor-pointer"><input type="radio" name="method" value="Bank" class="mt-1 text-primary focus:ring-primary"><span><strong class="block text-gray-900 dark:text-white">Bank transfer</strong><span class="text-sm text-gray-500 dark:text-gray-400">Settles the same working day.</span></span></label>
                <label class="flex items-start gap-3 es-panel cursor-pointer"><input type="radio" name="method" value="Cash" class="mt-1 text-primary focus:ring-primary"><span><strong class="block text-gray-900 dark:text-white">Cash on pickup</strong><span class="text-sm text-gray-500 dark:text-gray-400">Handed over by the collector.</span></span></label>
            </div>
            <div class="grid sm:grid-cols-2 gap-4">
                <div class="es-field"><label class="es-label" for="pay-upi">UPI ID</label><input id="pay-upi" name="upi" type="text" class="es-input" placeholder="name@bank" value="greenuser@upi"></div>
                <div class="es-field"><label class="es-label" for="pay-phone">Linked phone</label><input id="pay-phone" name="phone" type="tel" class="es-input" data-label="Phone number" value="+91 98100 11223"><span class="es-error"><i class="fa-solid fa-circle-exclamation"></i></span></div>
            </div>
            <button type="submit" class="es-btn es-btn--primary es-btn--lg"><i class="fa-solid fa-floppy-disk"></i> Save Preferences</button>
        </form>
    </div>"""

    payment_info = section_card(
        "Payout SLAs",
        """<ul class="space-y-3 text-sm text-gray-600 dark:text-gray-300">
        <li class="flex items-center gap-3"><i class="fa-solid fa-bolt text-primary"></i> UPI credited within 30 minutes</li>
        <li class="flex items-center gap-3"><i class="fa-solid fa-building-columns text-primary"></i> Bank transfers same working day</li>
        <li class="flex items-center gap-3"><i class="fa-solid fa-shield-halved text-primary"></i> No deductions, ever</li>
        <li class="flex items-center gap-3"><i class="fa-solid fa-receipt text-primary"></i> Digital receipt for every pickup</li>
        </ul>"""
    ) + section_card(
        "Need an Invoice?",
        """<p class="text-sm text-gray-500 dark:text-gray-400">Download consolidated statements for tax or society records.</p>
        <button type="button" class="es-btn es-btn--ghost es-btn--sm es-btn--block mt-4" data-demo-action="Statement download">Download Statement</button>"""
    )

    address_form = """<div class="es-card">
        <div class="p-5 border-b border-gray-100 dark:border-gray-700"><h2 class="font-bold text-gray-900 dark:text-white">Add an Address</h2></div>
        <form id="address-form" data-validate class="p-5 space-y-4">
            <div data-form-alert class="es-alert es-alert--error"></div>
            <div class="es-field"><label class="es-label" for="ad-label">Label</label><input id="ad-label" name="label" type="text" class="es-input" data-label="Label" placeholder="Home / Office" required><span class="es-error"><i class="fa-solid fa-circle-exclamation"></i></span></div>
            <div class="es-field"><label class="es-label" for="ad-city">City</label>
                <select id="ad-city" name="city" class="es-select"><option>Delhi NCR</option><option>Mumbai</option><option>Bangalore</option><option>Pune</option><option>Hyderabad</option><option>Chennai</option></select>
            </div>
            <div class="es-field"><label class="es-label" for="ad-address">Full address</label><textarea id="ad-address" name="address" class="es-textarea !min-h-[5rem]" data-label="Address" data-minlen="8" required></textarea><span class="es-error"><i class="fa-solid fa-circle-exclamation"></i></span></div>
            <button type="submit" class="es-btn es-btn--primary es-btn--block"><i class="fa-solid fa-plus"></i> Save Address</button>
        </form>
    </div>"""

    notif_list = """<div class="es-card">
        <div class="flex items-center justify-between p-5 border-b border-gray-100 dark:border-gray-700">
            <h2 class="font-bold text-gray-900 dark:text-white">Recent Notifications</h2>
            <button type="button" class="es-btn es-btn--ghost es-btn--sm" data-clear-notifs>Mark all read</button>
        </div>
        <div class="divide-y divide-gray-100 dark:divide-gray-700" id="cust-notif-list"></div>
    </div>"""

    notif_prefs = section_card(
        "Notification Preferences",
        """<div class="space-y-4">
        <label class="flex items-center justify-between gap-3"><span class="text-sm font-medium text-gray-700 dark:text-gray-200">Pickup status updates</span><span class="es-switch"><input type="checkbox" checked><span class="es-switch__track"></span></span></label>
        <label class="flex items-center justify-between gap-3"><span class="text-sm font-medium text-gray-700 dark:text-gray-200">Payout confirmations</span><span class="es-switch"><input type="checkbox" checked><span class="es-switch__track"></span></span></label>
        <label class="flex items-center justify-between gap-3"><span class="text-sm font-medium text-gray-700 dark:text-gray-200">Rate-change alerts</span><span class="es-switch"><input type="checkbox"><span class="es-switch__track"></span></span></label>
        <label class="flex items-center justify-between gap-3"><span class="text-sm font-medium text-gray-700 dark:text-gray-200">Marketing &amp; tips</span><span class="es-switch"><input type="checkbox"><span class="es-switch__track"></span></span></label>
        </div>"""
    )

    profile_form = """<div class="es-card">
        <div class="p-5 border-b border-gray-100 dark:border-gray-700"><h2 class="font-bold text-gray-900 dark:text-white">Profile Settings</h2><p class="text-sm text-gray-500 dark:text-gray-400 mt-1">Keep your details up to date for smooth pickups.</p></div>
        <form id="profile-form" data-validate class="p-5 space-y-5">
            <div data-form-alert class="es-alert es-alert--error"></div>
            <div class="flex items-center gap-4">
                <span class="w-16 h-16 rounded-full bg-gradient-to-br from-primary to-primaryDark text-white flex items-center justify-center text-xl font-bold" data-user-initials-lg>GU</span>
                <div><p class="font-semibold text-gray-900 dark:text-white" data-user-name-lg>Green User</p><p class="text-sm text-gray-500 dark:text-gray-400">Member since 2026</p></div>
            </div>
            <div class="grid sm:grid-cols-2 gap-4">
                <div class="es-field"><label class="es-label" for="pf-name">Full name</label><input id="pf-name" name="name" type="text" class="es-input" data-label="Full name" required><span class="es-error"><i class="fa-solid fa-circle-exclamation"></i></span></div>
                <div class="es-field"><label class="es-label" for="pf-phone">Phone</label><input id="pf-phone" name="phone" type="tel" class="es-input" data-label="Phone number" required><span class="es-error"><i class="fa-solid fa-circle-exclamation"></i></span></div>
            </div>
            <div class="es-field"><label class="es-label" for="pf-email">Email</label><input id="pf-email" name="email" type="email" class="es-input" data-label="Email address" required><span class="es-error"><i class="fa-solid fa-circle-exclamation"></i></span></div>
            <div class="es-field"><label class="es-label" for="pf-city">Preferred city</label>
                <select id="pf-city" name="city" class="es-select"><option>Delhi NCR</option><option>Mumbai</option><option>Bangalore</option><option>Pune</option><option>Hyderabad</option><option>Chennai</option></select>
            </div>
            <button type="submit" class="es-btn es-btn--primary es-btn--lg"><i class="fa-solid fa-floppy-disk"></i> Save Changes</button>
        </form>
    </div>"""

    profile_side = section_card(
        "Security",
        """<div class="space-y-3">
        <div class="es-field"><label class="es-label" for="pf-old">Current password</label><input id="pf-old" type="password" class="es-input" placeholder="â€¢â€¢â€¢â€¢â€¢â€¢â€¢â€¢"></div>
        <div class="es-field"><label class="es-label" for="pf-new">New password</label><input id="pf-new" type="password" class="es-input" placeholder="6+ characters"></div>
        <button type="button" class="es-btn es-btn--ghost es-btn--sm es-btn--block" data-demo-action="Password change">Update Password</button>
        </div>"""
    ) + section_card(
        "Danger Zone",
        """<p class="text-sm text-gray-500 dark:text-gray-400">Deactivating hides your account and cancels reminders. This demo can be reversed by refreshing.</p>
        <button type="button" class="es-btn es-btn--sm es-btn--block mt-4 !bg-red-50 !text-red-600 hover:!bg-red-100 dark:!bg-red-500/10 dark:!text-red-400" data-demo-action="Account deactivation">Deactivate Account</button>"""
    )

    return CUSTOMER_VIEWS_TEMPLATE.format(
        s_pickups=s_pickups, s_weight=s_weight, s_earn=s_earn, s_co2=s_co2,
        recent=recent, quick=quick, impact=impact,
        schedule_form=schedule_form, price_guide=price_guide,
        requests_card=requests_card,
        tracker=tracker, tracker_side=tracker_side,
        weight_chart_card=weight_chart_card, weight_side=weight_side, weight_table=weight_table,
        pay_total=pay_total, pay_pending=pay_pending, pay_avg=pay_avg, payout_table=payout_table,
        payment_form=payment_form, payment_info=payment_info,
        address_form=address_form,
        notif_list=notif_list, notif_prefs=notif_prefs,
        profile_form=profile_form, profile_side=profile_side,
    )


ADMIN_VIEWS_TEMPLATE = """
<!-- Overview -->
<section class="es-dash__view is-active" data-dash-view="overview">
    <div class="grid sm:grid-cols-2 xl:grid-cols-4 gap-4">
        {a_requests}{a_customers}{a_weight}{a_revenue}
    </div>
    <div class="grid lg:grid-cols-3 gap-5 mt-5">
        <div class="lg:col-span-2 min-w-0">{a_chart}</div>
        <div class="min-w-0">{a_split}</div>
    </div>
    <div class="mt-5">{a_recent}</div>
</section>

<!-- Pickup requests -->
<section class="es-dash__view" data-dash-view="pickups">
    {a_pickups}
</section>

<!-- Customers -->
<section class="es-dash__view" data-dash-view="customers">
    {a_customers_view}
</section>

<!-- Collectors -->
<section class="es-dash__view" data-dash-view="collectors">
    {a_collectors}
</section>

<!-- Rate card -->
<section class="es-dash__view" data-dash-view="ratecard">
    {a_ratecard}
</section>

<!-- Weight verification -->
<section class="es-dash__view" data-dash-view="verification">
    {a_verification}
</section>

<!-- Payment history -->
<section class="es-dash__view" data-dash-view="payments">
    {a_payments}
</section>

<!-- Locations -->
<section class="es-dash__view" data-dash-view="locations">
    {a_locations}
</section>

<!-- Reports -->
<section class="es-dash__view" data-dash-view="reports">
    {a_reports}
</section>
"""


def admin_content():
    a_requests = stat("fa-truck-ramp-box", "green", "a-requests", "Active requests")
    a_customers = stat("fa-users", "blue", "a-customers", "Customers")
    a_weight = stat("fa-weight-hanging", "amber", "a-weight", "Collected (kg)")
    a_revenue = stat("fa-indian-rupee-sign", "emerald", "a-revenue", "Payouts (â‚¹)")

    a_chart = """<div class="es-card">
        <div class="flex items-center justify-between p-5 border-b border-gray-100 dark:border-gray-700">
            <div><h2 class="font-bold text-gray-900 dark:text-white">Pickups This Week</h2><p class="text-sm text-gray-500 dark:text-gray-400 mt-1">Daily collection volume.</p></div>
            <span class="es-badge es-badge--green">Live</span>
        </div>
        <div class="p-5"><div class="es-bar" id="admin-pickup-chart"></div></div>
    </div>"""
    a_split = """<div class="es-card">
        <div class="p-5 border-b border-gray-100 dark:border-gray-700"><h2 class="font-bold text-gray-900 dark:text-white">Category Mix</h2></div>
        <div class="p-5 space-y-4" id="admin-category-split"></div>
    </div>"""

    a_pickups = section_card(
        "Pickup Requests",
        """<div class="flex flex-col lg:flex-row gap-3 justify-between mb-4">
            <input type="search" data-table-search="pickups" placeholder="Search request, customer, cityâ€¦" class="es-input lg:max-w-xs">
            <div class="flex flex-wrap gap-2" data-table-filters="pickups"></div>
        </div>"""
        + table(["Request", "Customer", "Category", "Slot", "Weight", "Status", "Actions"], "admin-pickups-body", "min-w-[900px]"),
        action='<button type="button" class="es-btn es-btn--primary es-btn--sm" data-open-modal="pickup"><i class="fa-solid fa-plus"></i> New</button>'
    )

    a_customers_view = section_card(
        "Customers",
        """<div class="flex flex-col lg:flex-row gap-3 justify-between mb-4">
            <input type="search" data-table-search="customers" placeholder="Search name, email, cityâ€¦" class="es-input lg:max-w-xs">
            <div class="flex gap-2"><button type="button" class="es-btn es-btn--ghost es-btn--sm" data-demo-action="Export CSV"><i class="fa-solid fa-download"></i> Export</button></div>
        </div>"""
        + table(["Customer", "City", "Pickups", "Total weight", "Lifetime value", "Status"], "admin-customers-body", "min-w-[820px]")
    )

    a_collectors = section_card(
        "Collector Fleet",
        table(["Collector", "City", "Vehicle", "Assignments", "Rating", "Status", ""], "admin-collectors-body", "min-w-[820px]"),
        action='<button type="button" class="es-btn es-btn--primary es-btn--sm" data-open-modal="collector"><i class="fa-solid fa-plus"></i> Add</button>'
    )

    a_ratecard = section_card(
        "Rate Card Management",
        """<div class="flex flex-col lg:flex-row gap-3 justify-between mb-4">
            <input type="search" data-table-search="ratecard" placeholder="Search materialâ€¦" class="es-input lg:max-w-xs">
            <button type="button" class="es-btn es-btn--ghost es-btn--sm" data-reset-rates><i class="fa-solid fa-rotate"></i> Reset to defaults</button>
        </div>"""
        + table(["Material", "Category", "Unit", "Price (â‚¹)", "Updated", "Actions"], "admin-ratecard-body", "min-w-[860px]"),
        action='<button type="button" class="es-btn es-btn--primary es-btn--sm" data-open-modal="rate"><i class="fa-solid fa-plus"></i> Add Rate</button>'
    )

    a_verification = section_card(
        "Weight Verification Queue",
        """<p class="text-sm text-gray-500 dark:text-gray-400 mb-4">Confirm field weights against the collector-scale reading before releasing payouts.</p>"""
        + table(["Request", "Collector", "Claimed", "Verified", "Variance", "Result", ""], "admin-verification-body", "min-w-[820px]")
    )

    a_payments = section_card(
        "Payment History",
        table(["Txn ID", "Customer", "Method", "Amount", "Date", "Status"], "admin-payments-body", "min-w-[860px]")
    )

    a_locations = """<div class="es-card">
        <div class="flex items-center justify-between p-5 border-b border-gray-100 dark:border-gray-700">
            <h2 class="font-bold text-gray-900 dark:text-white">Service Locations</h2>
            <button type="button" class="es-btn es-btn--primary es-btn--sm" data-open-modal="location"><i class="fa-solid fa-plus"></i> Add Location</button>
        </div>
        <div class="p-5 grid sm:grid-cols-2 xl:grid-cols-3 gap-4" id="admin-locations-grid"></div>
    </div>"""

    a_reports = """<div class="grid lg:grid-cols-3 gap-5">
        <div class="lg:col-span-2 es-card">
            <div class="p-5 border-b border-gray-100 dark:border-gray-700"><h2 class="font-bold text-gray-900 dark:text-white">Revenue Trend</h2><p class="text-sm text-gray-500 dark:text-gray-400 mt-1">Monthly payout value (â‚¹ thousands).</p></div>
            <div class="p-5"><div class="es-bar" id="admin-revenue-chart"></div></div>
        </div>
        <div class="es-card"><div class="p-5 border-b border-gray-100 dark:border-gray-700"><h2 class="font-bold text-gray-900 dark:text-white">Key Ratios</h2></div>
            <div class="p-5 space-y-5" id="admin-ratios"></div>
        </div>
    </div>
    <div class="mt-5 es-card"><div class="p-5 border-b border-gray-100 dark:border-gray-700"><h2 class="font-bold text-gray-900 dark:text-white">City Performance</h2></div>
        <div class="p-5" id="admin-city-report"></div>
    </div>"""

    return ADMIN_VIEWS_TEMPLATE.format(
        a_requests=a_requests, a_customers=a_customers, a_weight=a_weight, a_revenue=a_revenue,
        a_chart=a_chart, a_split=a_split, a_recent='''<div class="es-card"><div class="flex items-center justify-between p-5 border-b border-gray-100 dark:border-gray-700"><h2 class="font-bold text-gray-900 dark:text-white">Latest Requests</h2><button type="button" class="es-btn es-btn--ghost es-btn--sm" data-dash-nav="pickups">View all</button></div><div class="p-5">''' + table(["Request", "Customer", "Category", "Status"], "admin-recent-body") + "</div></div>",
        a_pickups=a_pickups, a_customers_view=a_customers_view, a_collectors=a_collectors,
        a_ratecard=a_ratecard, a_verification=a_verification,
        a_payments=a_payments, a_locations=a_locations, a_reports=a_reports,
    )


def page(filename, title, desc, app_script, brand_sub, role_badge, nav_items, role_title, body_views):
    role = "admin" if "admin" in app_script else "customer"
    html = (
        HEAD.format(title=title, desc=desc, theme=_theme_script(), cfg=TAILWIND_CFG, app=app_script)
        + '<div class="es-dash">\n'
        + sidebar(brand_sub, role_badge, nav_items, [])
        + '  <div class="es-dash__main flex-1 min-w-0 flex flex-col">\n'
        + "    " + topbar(role_title, role)
        + '    <main class="flex-1 p-4 sm:p-6 lg:p-8 space-y-5">\n'
        + body_views
        + "\n    </main>\n"
        + '    <footer class="px-4 sm:px-6 py-5 text-center text-xs text-gray-400 dark:text-gray-500 border-t border-gray-100 dark:border-gray-800">Â© 2026 EcoScrap Â· Demo dashboard â€” data is stored only in your browser.</footer>\n'
        + "  </div>\n</div>\n"
        + "</body>\n</html>\n"
    )
    out = os.path.join(BASE_DIR, filename)
    with open(out, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(html)
    print("wrote", filename)


CUSTOMER_NAV = [
    ("overview", "Dashboard", "fa-gauge-high"),
    ("schedule", "Schedule Pickup", "fa-calendar-plus"),
    ("requests", "My Requests", "fa-list-check"),
    ("status", "Live Status", "fa-truck-fast"),
    ("weights", "Weight History", "fa-weight-hanging"),
    ("payouts", "Payout History", "fa-indian-rupee-sign"),
    ("payment", "Payment Preferences", "fa-wallet"),
    ("addresses", "Saved Addresses", "fa-location-dot"),
    ("notifications", "Notifications", "fa-bell"),
    ("profile", "Profile Settings", "fa-user-gear"),
]

ADMIN_NAV = [
    ("overview", "Dashboard", "fa-gauge-high"),
    ("pickups", "Pickup Requests", "fa-truck-ramp-box"),
    ("customers", "Customers", "fa-users"),
    ("collectors", "Collectors", "fa-people-carry-box"),
    ("ratecard", "Rate Card", "fa-tags"),
    ("verification", "Weight Verification", "fa-scale-balanced"),
    ("payments", "Payment History", "fa-receipt"),
    ("locations", "Locations", "fa-map-location-dot"),
    ("reports", "Reports & Analytics", "fa-chart-line"),
]



def main():
    page("customer-dashboard.html", "Customer Dashboard | EcoScrap",
         "Book scrap pickups, track live status, review weight history and manage payouts.",
         "js/dashboard.js", "Customer Portal", "Customer account",
         CUSTOMER_NAV, "Customer dashboard Â· bookings, tracking & payouts", customer_content())
    page("admin-dashboard.html", "Admin Dashboard | EcoScrap",
         "Manage pickup requests, customers, collectors, rate card, payouts, locations and reports.",
         "js/admin-dashboard.js", "Admin Console", "Administrator",
         ADMIN_NAV, "Admin console Â· operations, rate card & payouts", admin_content())


if __name__ == "__main__":
    main()
