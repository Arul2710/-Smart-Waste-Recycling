"""
EcoScrap — content pages builder (6 sections each).

about, services, rate-card, how-it-works, blog, blog-details,
contact, locations, privacy-policy, terms, 404
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_base import public_page  # noqa: E402

H = "assets/images/"


def hero(page, img, title, sub, eyebrow="", crumb=None, media_desc=""):
    crumb_html = ""
    if crumb:
        crumb_html = '<ol class="flex items-center justify-center gap-2 text-sm text-gray-300 mt-5 es-reveal" data-reveal-delay="240">' + crumb + "</ol>"
    return """
<section data-section="1" class="hero %s">
    <div class="hero__media" style="background-image:url('%s')" role="img" aria-label="%s"></div>
    <div class="hero__overlay hero__overlay--dark"></div>
    <div class="container-es relative z-10 py-20 lg:py-24 text-center">
        <span class="es-eyebrow es-reveal">%s</span>
        <h1 class="mt-5 text-4xl md:text-5xl font-extrabold text-white leading-tight es-reveal" data-reveal-delay="80">%s</h1>
        <p class="mx-auto mt-5 text-lg text-gray-200/95 max-w-2xl es-reveal" data-reveal-delay="160">%s</p>
        %s
    </div>
</section>
""" % ("text-center", H + img, media_desc or img, eyebrow or page, title, sub, crumb_html)


def cta_footer(title="Ready to Turn Your Scrap Into Cash?", sub="Schedule a doorstep pickup in under two minutes and get paid the same visit. Free to start, no minimum quantity.", img="green.jpg", primary=("<i class=\"fa-solid fa-calendar-check\"></i> Schedule Pickup", "customer-dashboard.html"), secondary=("Contact Us <i class=\"fa-solid fa-arrow-right rtl-flip\"></i>", "contact.html")):
    return """
<!-- 6 · CTA -->
<section data-section="6" class="section bg-white dark:bg-gray-900">
    <div class="container-es">
        <div class="relative overflow-hidden rounded-3xl bg-primaryDark es-reveal">
            <div class="absolute inset-0 opacity-15 hero__media" style="background-image:url('%s%s')"></div>
            <div class="relative z-10 px-6 sm:px-12 py-14 sm:py-16 text-center text-white">
                <h2 class="text-3xl sm:text-4xl font-extrabold text-white">%s</h2>
                <p class="mt-4 text-gray-200 max-w-xl mx-auto">%s</p>
                <div class="mt-8 flex flex-col sm:flex-row justify-center gap-3">
                    <a href="%s" class="es-btn es-btn--primary es-btn--lg">%s</a>
                    <a href="%s" class="es-btn es-btn--white es-btn--lg">%s</a>
                </div>
            </div>
        </div>
    </div>
</section>
""" % (H, img, title, sub, primary[1], primary[0], secondary[1], secondary[0])


FAQ_ITEMS = [
    ("How is my scrap actually weighed?",
     "Every collector carries a government-verified, tamper-proof digital scale calibrated to the nearest 100 grams. The weight is displayed in front of you, recorded in the app and printed on your receipt — so you always know exactly what was measured."),
    ("Can I see the rate before the pickup happens?",
     "Yes. The published rate card shows the indicative price for every material. The final payout is calculated from the published rate multiplied by the verified weight, with no hidden collection or transport charges."),
    ("What materials do you refuse to take?",
     "We do not accept hazardous or biomedical waste such as chemicals, medical sharps, pressurised containers, sealed fuel tanks or expired paint. E-waste and batteries are routed through a separate certified stream."),
    ("How quickly do I receive payment?",
     "Payments are released within 30 minutes of a completed verification. UPI is instant, bank transfers settle the same working day, and cash payouts are handed over on the spot by the collector."),
    ("Is there a minimum quantity for a pickup?",
     "There is no minimum. We collect anything from a single cardboard box upward. For bulk or society-level clear-outs we recommend a dedicated slot so a larger vehicle can be assigned."),
    ("What happens to the material after collection?",
     "Sorted material is dispatched to certified recyclers and authorised re-rollers within 48 hours. Every consignment carries a handover manifest, and registered users can request the summary from their dashboard."),
]


def faq_block():
    items = "".join(
        '<div class="es-acc__item">'
        '<button type="button" class="es-acc__btn" aria-expanded="false"><span>%s</span><i class="fa-solid fa-chevron-down"></i></button>'
        '<div class="es-acc__panel"><p>%s</p></div></div>' % (q, a)
        for q, a in FAQ_ITEMS
    )
    return """<div data-accordion class="max-w-3xl mx-auto">%s</div>""" % items


def about_main():
    return """
<!-- 1 · Hero -->
""" + hero("About", "scrapyard.jpg", "About EcoScrap",
    "From a neighbourhood doorstep service to a metro-wide recycling network — built on transparent weighing, fair rates and responsible disposal.",
    eyebrow="Who We Are",
    crumb='<li class="text-gray-400"><a href="index.html" class="hover:text-white">Home</a></li><li class="text-gray-500">/</li><li class="text-primaryLight font-semibold">About</li>',
    media_desc="Scrap collection operations at an EcoScrap facility") + """
<!-- 2 · Our Story -->
<section data-section="2" class="section bg-white dark:bg-gray-900">
    <div class="container-es grid lg:grid-cols-2 gap-12 items-center">
        <div>
            <span class="es-eyebrow es-reveal">Our Story</span>
            <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">Founded on a Simple Frustration</h2>
            <p class="es-subtitle text-lg mt-5 es-reveal" data-reveal-delay="120">In 2024 we started EcoScrap after watching neighbours haul heavy scrap bags to the nearest dealer — where weights were guessed, rates were opaque and payment was later than promised. We built the service we wished existed: a booked slot, a calibrated scale and cash on the spot.</p>
            <p class="es-subtitle mt-4 es-reveal" data-reveal-delay="180">Today our fleet of collection vehicles serves six metros, and every item we pick up is sorted and routed to certified recyclers with a recorded handover chain.</p>
            <div class="mt-8 grid grid-cols-3 gap-4 es-reveal" data-reveal-delay="240">
                <div><p class="text-3xl font-extrabold text-primary"><span data-count-to="42" data-count-suffix="K+">42K+</span></p><p class="text-xs text-gray-500 dark:text-gray-400 mt-1">Pickups completed</p></div>
                <div><p class="text-3xl font-extrabold text-primary"><span data-count-to="6">6</span></p><p class="text-xs text-gray-500 dark:text-gray-400 mt-1">Cities served</p></div>
                <div><p class="text-3xl font-extrabold text-primary"><span data-count-to="98" data-count-suffix="%">98%</span></p><p class="text-xs text-gray-500 dark:text-gray-400 mt-1">On-time arrivals</p></div>
            </div>
        </div>
        <div class="relative es-reveal" data-reveal-delay="120">
            <div class="es-card__media rounded-3xl aspect-[4/3] overflow-hidden">
                <img src="assets/images/plant.jpg" alt="EcoScrap team working at a certified recycling facility" loading="lazy" width="1600" height="900">
            </div>
            <div class="absolute -bottom-6 -left-4 bg-white dark:bg-gray-800 rounded-2xl shadow-2xl px-5 py-4 border border-gray-100 dark:border-gray-700">
                <p class="font-bold text-gray-900 dark:text-white">Est. 2024</p>
                <p class="text-xs text-gray-500 dark:text-gray-400">Zero-waste mission from day one</p>
            </div>
        </div>
    </div>
</section>

<!-- 3 · Mission, Vision & Values -->
<section data-section="3" class="section bg-lightBg dark:bg-[#0d1726]">
    <div class="container-es">
        <div class="text-center max-w-2xl mx-auto">
            <span class="es-eyebrow es-reveal">What Drives Us</span>
            <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">Mission, Vision &amp; Values</h2>
        </div>
        <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mt-12">
            <div class="es-panel es-panel--hover es-reveal"><span class="es-card__icon"><i class="fa-solid fa-bullseye"></i></span><h3 class="es-card__title mt-4">Our Mission</h3><p class="es-card__text mt-2">Make recycling as easy as ordering groceries — booked, transparent and rewarding for every household.</p></div>
            <div class="es-panel es-panel--hover es-reveal" data-reveal-delay="60"><span class="es-card__icon"><i class="fa-solid fa-eye"></i></span><h3 class="es-card__title mt-4">Our Vision</h3><p class="es-card__text mt-2">A zero-waste society where nothing valuable ever reaches landfill and every citizen is paid for recycling.</p></div>
            <div class="es-panel es-panel--hover es-reveal" data-reveal-delay="120"><span class="es-card__icon"><i class="fa-solid fa-scale-balanced"></i></span><h3 class="es-card__title mt-4">Fairness First</h3><p class="es-card__text mt-2">Verified weights, published rates and no last-minute deductions — trust is our only brand.</p></div>
            <div class="es-panel es-panel--hover es-reveal" data-reveal-delay="180"><span class="es-card__icon"><i class="fa-solid fa-leaf"></i></span><h3 class="es-card__title mt-4">Planet + People</h3><p class="es-card__text mt-2">Every pickup creates income for a citizen and keeps material in the circular economy.</p></div>
        </div>
    </div>
</section>

<!-- 4 · Environmental Responsibility -->
<section data-section="4" class="section bg-white dark:bg-gray-900">
    <div class="container-es grid lg:grid-cols-2 gap-12 items-center">
        <div class="relative es-reveal">
            <div class="es-card__media rounded-3xl aspect-[4/3] overflow-hidden">
                <img src="assets/images/sustain-city.jpg" alt="Sustainability and responsible recycling in urban India" loading="lazy" width="1600" height="900">
            </div>
        </div>
        <div>
            <span class="es-eyebrow es-reveal">Responsibility</span>
            <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">Every Kilogram Goes to a Certified Destination</h2>
            <p class="es-subtitle mt-5 es-reveal" data-reveal-delay="120">Recycling can be greenwashing if the chain isn't audited. We track each consignment from your doorstep to the receiver, and share the summary on request.</p>
            <ul class="mt-7 space-y-4 es-reveal" data-reveal-delay="180">
                <li class="flex items-start gap-3"><span class="es-card__icon"><i class="fa-solid fa-file-shield"></i></span><span><strong class="block text-gray-900 dark:text-white">Handover manifests</strong><span class="text-sm text-gray-500 dark:text-gray-400">Consignment-level records available in your dashboard.</span></span></li>
                <li class="flex items-start gap-3"><span class="es-card__icon"><i class="fa-solid fa-magnifying-glass-chart"></i></span><span><strong class="block text-gray-900 dark:text-white">Audited facilities</strong><span class="text-sm text-gray-500 dark:text-gray-400">Partner recyclers licensed under E-Waste and Hazardous Waste rules.</span></span></li>
                <li class="flex items-start gap-3"><span class="es-card__icon"><i class="fa-solid fa-recycle"></i></span><span><strong class="block text-gray-900 dark:text-white">Closed-loop reporting</strong><span class="text-sm text-gray-500 dark:text-gray-400">We measure energy saved, water saved and emissions avoided.</span></span></li>
            </ul>
        </div>
    </div>
</section>

<!-- 5 · Our Team -->
<section data-section="5" class="section bg-lightBg dark:bg-[#0d1726]">
    <div class="container-es">
        <div class="text-center max-w-2xl mx-auto">
            <span class="es-eyebrow es-reveal">The People</span>
            <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">Meet the Core Team</h2>
            <p class="es-subtitle mt-4 es-reveal" data-reveal-delay="120">Ops-led, tech-enabled and ground-tested — the team behind 42,000+ pickups.</p>
        </div>
        <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-7 mt-12">
            <div class="es-card es-reveal"><div class="es-card__body items-center text-center">
                <div class="w-20 h-20 rounded-full bg-gradient-to-br from-primary to-primaryDark text-white flex items-center justify-center text-2xl font-bold">RS</div>
                <h3 class="es-card__title">Rahul Sharma</h3><p class="text-xs text-primary font-semibold uppercase tracking-wide">Founder &amp; CEO</p>
                <p class="es-card__text text-sm text-center">Built the first pickup route by hand in 2024.</p>
            </div></div>
            <div class="es-card es-reveal" data-reveal-delay="60"><div class="es-card__body items-center text-center">
                <div class="w-20 h-20 rounded-full bg-gradient-to-br from-primary to-primaryDark text-white flex items-center justify-center text-2xl font-bold">AK</div>
                <h3 class="es-card__title">Anita Kulkarni</h3><p class="text-xs text-primary font-semibold uppercase tracking-wide">Operations</p>
                <p class="es-card__text text-sm text-center">Runs field teams and the certified recycler network.</p>
            </div></div>
            <div class="es-card es-reveal" data-reveal-delay="120"><div class="es-card__body items-center text-center">
                <div class="w-20 h-20 rounded-full bg-gradient-to-br from-primary to-primaryDark text-white flex items-center justify-center text-2xl font-bold">DM</div>
                <h3 class="es-card__title">David Mehta</h3><p class="text-xs text-primary font-semibold uppercase tracking-wide">Logistics</p>
                <p class="es-card__text text-sm text-center">Schedules every slot and every collection route.</p>
            </div></div>
            <div class="es-card es-reveal" data-reveal-delay="180"><div class="es-card__body items-center text-center">
                <div class="w-20 h-20 rounded-full bg-gradient-to-br from-primary to-primaryDark text-white flex items-center justify-center text-2xl font-bold">NB</div>
                <h3 class="es-card__title">Neha Bansal</h3><p class="text-xs text-primary font-semibold uppercase tracking-wide">Compliance</p>
                <p class="es-card__text text-sm text-center">Owns audits, manifests and e-waste certificates.</p>
            </div></div>
        </div>
    </div>
</section>

""" + cta_footer("Join Us in Making a Difference", "Create a free account, book your first pickup and become part of the zero-waste movement — it takes two minutes and costs nothing to start.", primary=("<i class=\"fa-solid fa-user-plus\"></i> Sign Up Today", "signup.html"), secondary=("About Our Rates", "rate-card.html"))


def services_main():
    return """
<!-- 1 · Hero -->
""" + hero("Services", "collection.jpg", "Scrap Collection Services",
    "Household pickups, corporate clear-outs and society-wide drives — handled by trained collectors with transparent weighing and instant payment.",
    eyebrow="What We Do",
    crumb='<li class="text-gray-400"><a href="index.html" class="hover:text-white">Home</a></li><li class="text-gray-500">/</li><li class="text-primaryLight font-semibold">Services</li>',
    media_desc="EcoScrap collection vehicle arriving for a doorstep pickup") + """
<!-- 2 · Main Service Cards -->
<section data-section="2" class="section bg-white dark:bg-gray-900">
    <div class="container-es">
        <div class="text-center max-w-2xl mx-auto">
            <span class="es-eyebrow es-reveal">Core Offerings</span>
            <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">Pick a Model That Fits You</h2>
            <p class="es-subtitle mt-4 es-reveal" data-reveal-delay="120">Every programme includes calibrated weighing, published rates and same-visit settlement.</p>
        </div>
        <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-7 mt-12">
            <article class="es-card es-card--hover es-reveal">
                <div class="es-card__body">
                    <span class="es-card__icon"><i class="fa-solid fa-house-chimney"></i></span>
                    <h3 class="es-card__title">Household Pickup</h3>
                    <p class="es-card__text">One-off or weekly doorstep collection for homes and apartment flats. Covers all six material categories with no minimum quantity.</p>
                    <div class="es-card__foot"><a href="customer-dashboard.html" class="es-btn es-btn--primary es-btn--sm es-btn--block">Book a Pickup</a></div>
                </div>
            </article>
            <article class="es-card es-card--hover es-reveal" data-reveal-delay="60">
                <div class="es-card__body">
                    <span class="es-card__icon"><i class="fa-solid fa-building"></i></span>
                    <h3 class="es-card__title">Corporate Clearouts</h3>
                    <p class="es-card__text">Office and retail scrap disposal — cardboard, metal shelving, old IT and furniture — with GST invoicing and data-wiped e-waste.</p>
                    <div class="es-card__foot"><a href="#corporate" class="es-btn es-btn--primary es-btn--sm es-btn--block">Explore Clearouts</a></div>
                </div>
            </article>
            <article class="es-card es-card--hover es-reveal" data-reveal-delay="120">
                <div class="es-card__body">
                    <span class="es-card__icon"><i class="fa-solid fa-people-group"></i></span>
                    <h3 class="es-card__title">Society Scrap Drives</h3>
                    <p class="es-card__text">RWA-hosted collection days with a weighing station, per-flat payout reports and a certificate for your green initiative.</p>
                    <div class="es-card__foot"><a href="#society" class="es-btn es-btn--primary es-btn--sm es-btn--block">Organise a Drive</a></div>
                </div>
            </article>
            <article class="es-card es-card--hover es-reveal">
                <div class="es-card__body">
                    <span class="es-card__icon"><i class="fa-solid fa-microchip"></i></span>
                    <h3 class="es-card__title">E-Waste &amp; Data Safety</h3>
                    <p class="es-card__text">Laptops, phones and peripherals collected separately, logged, and accepted with a certificate of destruction from the recycler.</p>
                    <div class="es-card__foot"><a href="rate-card.html#ewaste" class="es-btn es-btn--primary es-btn--sm es-btn--block">E-Waste Rates</a></div>
                </div>
            </article>
            <article class="es-card es-card--hover es-reveal" data-reveal-delay="60">
                <div class="es-card__body">
                    <span class="es-card__icon"><i class="fa-solid fa-arrows-rotate"></i></span>
                    <h3 class="es-card__title">Recurring Pickups</h3>
                    <p class="es-card__text">A fixed weekly slot for homes and businesses with consistent scrap volume. Adjust or pause anytime from your dashboard.</p>
                    <div class="es-card__foot"><a href="how-it-works.html" class="es-btn es-btn--primary es-btn--sm es-btn--block">See Schedules</a></div>
                </div>
            </article>
            <article class="es-card es-card--hover es-reveal" data-reveal-delay="120">
                <div class="es-card__body">
                    <span class="es-card__icon"><i class="fa-solid fa-truck-ramp-box"></i></span>
                    <h3 class="es-card__title">Bulk &amp; Commercial</h3>
                    <p class="es-card__text">Construction-site metal, factory offcuts and warehouse surplus. Quoted in 24 hours with a dedicated dumping vehicle.</p>
                    <div class="es-card__foot"><a href="contact.html" class="es-btn es-btn--primary es-btn--sm es-btn--block">Request a Quote</a></div>
                </div>
            </article>
        </div>
    </div>
</section>

<!-- 3 · Programme details -->
<section data-section="3" class="section bg-lightBg dark:bg-[#0d1726]">
    <div class="container-es">
        <div class="grid lg:grid-cols-2 gap-10">
            <div id="corporate" class="es-panel es-reveal">
                <div class="flex items-center gap-3 mb-4"><span class="es-card__icon"><i class="fa-solid fa-building"></i></span><h3 class="text-2xl font-bold text-gray-900 dark:text-white">Corporate Clearout</h3></div>
                <p class="es-card__text mb-5">A single audit call that ends with a paperless, compliant disposal. We scan your site, produce a binding quote and collect on a negotiated slot.</p>
                <ul class="space-y-3 text-sm text-gray-600 dark:text-gray-400">
                    <li class="flex gap-3"><i class="fa-solid fa-circle-check text-primary mt-1"></i>Free site survey within 48 hours</li>
                    <li class="flex gap-3"><i class="fa-solid fa-circle-check text-primary mt-1"></i>GST invoice matched to the manifest</li>
                    <li class="flex gap-3"><i class="fa-solid fa-circle-check text-primary mt-1"></i>Certificate of destruction for e-waste &amp; media</li>
                    <li class="flex gap-3"><i class="fa-solid fa-circle-check text-primary mt-1"></i>Bank transfer settled in 1 working day</li>
                </ul>
                <a href="contact.html" class="es-btn es-btn--dark mt-6">Get Corporate Quote <i class="fa-solid fa-arrow-right rtl-flip"></i></a>
            </div>
            <div id="society" class="es-panel es-reveal" data-reveal-delay="80">
                <div class="flex items-center gap-3 mb-4"><span class="es-card__icon"><i class="fa-solid fa-people-group"></i></span><h3 class="text-2xl font-bold text-gray-900 dark:text-white">Society Scrap Drive</h3></div>
                <p class="es-card__text mb-5">We set up a weighing station at your society gate, generate a payout report per flat, and credit each household instantly — making the drive self-funding.</p>
                <ul class="space-y-3 text-sm text-gray-600 dark:text-gray-400">
                    <li class="flex gap-3"><i class="fa-solid fa-circle-check text-primary mt-1"></i>Zero upfront cost, revenue shared fairly</li>
                    <li class="flex gap-3"><i class="fa-solid fa-circle-check text-primary mt-1"></i>Per-flat weight &amp; payout ledger</li>
                    <li class="flex gap-3"><i class="fa-solid fa-circle-check text-primary mt-1"></i>Posters and WhatsApp templates included</li>
                    <li class="flex gap-3"><i class="fa-solid fa-circle-check text-primary mt-1"></i>Green-drive certificate for your RWA</li>
                </ul>
                <a href="contact.html" class="es-btn es-btn--dark mt-6">Plan a Society Drive <i class="fa-solid fa-arrow-right rtl-flip"></i></a>
            </div>
        </div>
        <div class="mt-10 es-reveal">
            <div class="es-card es-reveal overflow-hidden rounded-2xl">
                <div class="grid md:grid-cols-4 divide-y md:divide-y-0 md:divide-x divide-gray-100 dark:divide-gray-700">
                    <div class="p-6 text-center"><i class="fa-solid fa-hand-holding-dollar text-primary text-2xl mb-2"></i><h4 class="font-bold text-gray-900 dark:text-white">UPI</h4><p class="text-xs text-gray-500 dark:text-gray-400 mt-1">Instant settlement</p></div>
                    <div class="p-6 text-center"><i class="fa-solid fa-building-columns text-primary text-2xl mb-2"></i><h4 class="font-bold text-gray-900 dark:text-white">Bank Transfer</h4><p class="text-xs text-gray-500 dark:text-gray-400 mt-1">Same working day</p></div>
                    <div class="p-6 text-center"><i class="fa-solid fa-wallet text-primary text-2xl mb-2"></i><h4 class="font-bold text-gray-900 dark:text-white">Cash</h4><p class="text-xs text-gray-500 dark:text-gray-400 mt-1">Handed over on site</p></div>
                    <div class="p-6 text-center"><i class="fa-solid fa-arrow-trend-up text-primary text-2xl mb-2"></i><h4 class="font-bold text-gray-900 dark:text-white">Premium for Bulk</h4><p class="text-xs text-gray-500 dark:text-gray-400 mt-1">Quoted per consignment</p></div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- 4 · Coverage table -->
<section data-section="4" class="section bg-white dark:bg-gray-900">
    <div class="container-es grid lg:grid-cols-5 gap-10 items-center">
        <div class="lg:col-span-2">
            <span class="es-eyebrow es-reveal">Coverage</span>
            <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">Service Areas &amp; Slots</h2>
            <p class="es-subtitle mt-4 es-reveal" data-reveal-delay="120">Morning, afternoon and evening slots across six metros. Every zone has its own collection roster and contact number.</p>
            <ul class="mt-7 space-y-3 text-sm text-gray-600 dark:text-gray-300 es-reveal" data-reveal-delay="180">
                <li class="flex items-center gap-3"><i class="fa-solid fa-bolt text-primary"></i> Same-day slots for metros</li>
                <li class="flex items-center gap-3"><i class="fa-solid fa-bolt text-primary"></i> Free rescheduling up to 3 hours before</li>
                <li class="flex items-center gap-3"><i class="fa-solid fa-bolt text-primary"></i> Around-the-clock call support</li>
            </ul>
            <div class="mt-8 es-reveal" data-reveal-delay="240"><a href="locations.html" class="es-btn es-btn--primary es-btn--lg">See All Locations <i class="fa-solid fa-arrow-right rtl-flip"></i></a></div>
        </div>
        <div class="lg:col-span-3 es-reveal" data-reveal-delay="120">
            <div class="es-card overflow-hidden">
                <table class="es-table min-w-[520px]">
                    <thead><tr><th>City</th><th>Coverage</th><th>Slots / day</th><th>Hours</th></tr></thead>
                    <tbody>
                        <tr><td class="font-medium text-gray-900 dark:text-gray-100">Delhi NCR</td><td><span class="es-badge es-badge--green">Full</span></td><td>6</td><td>7:00 – 20:00</td></tr>
                        <tr><td class="font-medium text-gray-900 dark:text-gray-100">Mumbai</td><td><span class="es-badge es-badge--blue">Selected</span></td><td>5</td><td>8:00 – 21:00</td></tr>
                        <tr><td class="font-medium text-gray-900 dark:text-gray-100">Bangalore</td><td><span class="es-badge es-badge--green">Full</span></td><td>6</td><td>7:30 – 20:30</td></tr>
                        <tr><td class="font-medium text-gray-900 dark:text-gray-100">Pune</td><td><span class="es-badge es-badge--amber">Partial</span></td><td>4</td><td>8:00 – 19:00</td></tr>
                        <tr><td class="font-medium text-gray-900 dark:text-gray-100">Hyderabad</td><td><span class="es-badge es-badge--green">Full</span></td><td>5</td><td>7:00 – 20:00</td></tr>
                        <tr><td class="font-medium text-gray-900 dark:text-gray-100">Chennai</td><td><span class="es-badge es-badge--blue">Selected</span></td><td>4</td><td>8:00 – 19:30</td></tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</section>

<!-- 5 · FAQ -->
<section data-section="5" class="section bg-lightBg dark:bg-[#0d1726]">
    <div class="container-es">
        <div class="text-center max-w-2xl mx-auto es-reveal">
            <span class="es-eyebrow">Service FAQs</span>
            <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">Common Questions</h2>
        </div>
        <div class="mt-12">%s</div>
    </div>
</section>

""" + faq_block() + "\n\n" + cta_footer()


def rate_card_main():
    table_head = """<div class="es-card es-reveal overflow-hidden">
    <div class="p-5 border-b border-gray-100 dark:border-gray-700 flex flex-col lg:flex-row gap-4 justify-between items-start lg:items-center">
        <div class="relative w-full max-w-sm">
            <i class="fa-solid fa-magnifying-glass absolute inset-y-0 left-4 flex items-center text-gray-400"></i>
            <input data-rate-search type="search" placeholder="Search materials… e.g. copper" class="es-input !ps-11" aria-label="Search rate card">
        </div>
        <select data-rate-sort class="es-select w-full sm:w-52" aria-label="Sort rate card">
            <option value="category:asc">Sort: Category</option>
            <option value="material:asc">Sort: Name (A–Z)</option>
            <option value="material:desc">Sort: Name (Z–A)</option>
            <option value="price:asc">Sort: Price (Low → High)</option>
            <option value="price:desc">Sort: Price (High → Low)</option>
        </select>
    </div>
    <div class="px-5 pt-4 flex flex-wrap gap-2" data-rate-filters></div>
    <div class="overflow-x-auto">
        <table id="rate-table" class="es-table min-w-[560px]">
            <thead><tr><th>Material</th><th>Category</th><th>Unit</th><th class="!text-right">Price / Kg</th></tr></thead>
            <tbody><!-- populated by data.js --></tbody>
        </table>
    </div>
    <div class="px-5 py-4 border-t border-gray-100 dark:border-gray-700 bg-gray-50 dark:bg-[#182130] flex flex-col sm:flex-row justify-between gap-2 items-center">
        <p class="text-xs text-gray-500 dark:text-gray-400"><span data-rate-count>0</span> · Prices may vary with material quality and verified weight.</p>
        <p class="text-xs text-gray-500 dark:text-gray-400"><i class="fa-solid fa-rotate me-1 text-primary"></i>Updated daily · DEMO data</p>
    </div>
</div>"""
    return """
<!-- 1 · Hero -->
""" + hero("Rate Card", "paper-hero.jpg", "Live Scrap Rates",
    "Search, filter and compare indicative rates across six material categories. Prices update daily, and final payout is always matched to the published rate.",
    eyebrow="Transparent Pricing",
    crumb='<li class="text-gray-400"><a href="index.html" class="hover:text-white">Home</a></li><li class="text-gray-500">/</li><li class="text-primaryLight font-semibold">Rate Card</li>',
    media_desc="Baled recycled paper ready for reprocessing at a mill") + """
<!-- 2 · Live rate table -->
<section data-section="2" class="section bg-white dark:bg-gray-900">
    <div class="container-es">
        <div class="text-center max-w-2xl mx-auto">
            <span class="es-eyebrow es-reveal">Search &amp; Filter</span>
            <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">Today's Indicative Rates</h2>
            <p class="es-subtitle mt-4 es-reveal" data-reveal-delay="120">Type to search, tap a category chip to filter, and sort by name or price. All amounts in Indian Rupees.</p>
        </div>
        <div class="mt-10">%s</div>
    </div>
</section>

<!-- 3 · Category spotlights -->
<section data-section="3" id="category-spotlights" class="section bg-lightBg dark:bg-[#0d1726]">
    <div class="container-es">
        <div class="text-center max-w-2xl mx-auto">
            <span class="es-eyebrow es-reveal">By Category</span>
            <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">Category Spotlights</h2>
        </div>
        <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-7 mt-12" data-render="categories"></div>
    </div>
</section>

<!-- 4 · How pricing works + estimator -->
<section data-section="4" class="section bg-white dark:bg-gray-900">
    <div class="container-es grid lg:grid-cols-2 gap-12 items-start">
        <div>
            <span class="es-eyebrow es-reveal">Transparency</span>
            <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">How We Set Rates</h2>
            <p class="es-subtitle mt-4 es-reveal" data-reveal-delay="120">Indicative prices are derived from exchange-traded scrap benchmarks plus local demand, then verified at your doorstep.</p>
            <div class="mt-8 space-y-5">
                <div class="es-panel es-panel--hover es-reveal flex gap-4"><span class="es-card__icon"><i class="fa-solid fa-link"></i></span><div><h3 class="font-bold text-gray-900 dark:text-white">Market-linked metals</h3><p class="text-sm text-gray-500 dark:text-gray-400 mt-1">Copper, aluminium and steel track international futures with a daily refresh.</p></div></div>
                <div class="es-panel es-panel--hover es-reveal flex gap-4" data-reveal-delay="60"><span class="es-card__icon"><i class="fa-solid fa-droplet"></i></span><div><h3 class="font-bold text-gray-900 dark:text-white">Quality &amp; moisture</h3><p class="text-sm text-gray-500 dark:text-gray-400 mt-1">Clean, dry material earns the top rate; contamination adjusts the payout.</p></div></div>
                <div class="es-panel es-panel--hover es-reveal flex gap-4" data-reveal-delay="120"><span class="es-card__icon"><i class="fa-solid fa-weight-hanging"></i></span><div><h3 class="font-bold text-gray-900 dark:text-white">Verified weight</h3><p class="text-sm text-gray-500 dark:text-gray-400 mt-1">Calibrated scales, displayed live. The number you see is the number you're paid.</p></div></div>
                <div class="es-panel es-panel--hover es-reveal flex gap-4" data-reveal-delay="180"><span class="es-card__icon"><i class="fa-solid fa-sack-dollar"></i></span><div><h3 class="font-bold text-gray-900 dark:text-white">No deductions</h3><p class="text-sm text-gray-500 dark:text-gray-400 mt-1">Collection, weighing and transport are always free of charge.</p></div></div>
            </div>
        </div>
        <div class="es-panel es-reveal lg:sticky lg:top-28" data-reveal-delay="120">
            <span class="es-card__icon"><i class="fa-solid fa-calculator"></i></span>
            <h3 class="text-2xl font-bold mt-4 text-gray-900 dark:text-white">Quick Rate Estimator</h3>
            <p class="text-sm text-gray-500 dark:text-gray-400 mt-2 mb-6">Pick a material and enter the approximate quantity for an indicative payout.</p>
            <form id="rate-calculator" class="space-y-4" novalidate>
                <div class="es-field"><label class="es-label" for="calc-material">Material</label>
                    <select id="calc-material" class="es-select" aria-label="Material"></select></div>
                <div class="es-field"><label class="es-label" for="calc-weight">Approx. quantity (kg / pieces)</label>
                    <input id="calc-weight" type="number" min="0" step="0.5" value="10" class="es-input" aria-label="Approximate quantity" required></div>
                <div id="calc-result" class="hidden mt-4 rounded-xl bg-lightBg dark:bg-[#0d1726] border border-primary/25 p-5">
                    <div class="grid grid-cols-2 gap-3 text-sm">
                        <div><p class="text-xs text-gray-500 dark:text-gray-400">Material</p><p id="calc-material-name" class="font-bold text-gray-900 dark:text-white">—</p></div>
                        <div><p class="text-xs text-gray-500 dark:text-gray-400">Rate</p><p id="calc-rate" class="font-bold text-primary">—</p></div>
                        <div><p class="text-xs text-gray-500 dark:text-gray-400">Quantity</p><p id="calc-weight-display" class="font-bold text-gray-900 dark:text-white">—</p></div>
                        <div><p class="text-xs text-gray-500 dark:text-gray-400">Est. payout</p><p id="calc-amount" class="font-bold text-primary text-lg">—</p></div>
                    </div>
                    <p class="text-[11px] text-gray-400 mt-3">Estimates only. Final payout uses verified weight and inspected quality.</p>
                </div>
                <a href="customer-dashboard.html" class="es-btn es-btn--primary es-btn--block">Schedule Pickup at This Rate</a>
            </form>
        </div>
    </div>
</section>

<!-- 5 · Get better rates -->
<section data-section="5" class="section bg-lightBg dark:bg-[#0d1726]">
    <div class="container-es">
        <div class="text-center max-w-2xl mx-auto">
            <span class="es-eyebrow es-reveal">Pro Tips</span>
            <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">Get the Best Rate at the Scale</h2>
        </div>
        <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6 mt-12">
            <div class="es-card es-reveal"><div class="es-card__body items-center text-center"><span class="es-step__num mx-auto">01</span><h3 class="es-card__title">Separate by type</h3><p class="es-card__text text-sm text-center">Copper apart from steel, clear PET apart from mixed plastic — sorted loads rate higher.</p></div></div>
            <div class="es-card es-reveal" data-reveal-delay="60"><div class="es-card__body items-center text-center"><span class="es-step__num mx-auto">02</span><h3 class="es-card__title">Keep it dry</h3><p class="es-card__text text-sm text-center">Moisture is deducted from the weight. Air-dry paper and bottles before pickup.</p></div></div>
            <div class="es-card es-reveal" data-reveal-delay="120"><div class="es-card__body items-center text-center"><span class="es-step__num mx-auto">03</span><h3 class="es-card__title">Flatten boxes</h3><p class="es-card__text text-sm text-center">Collapse cartons so your vehicle slot carries more material in each trip.</p></div></div>
            <div class="es-card es-reveal" data-reveal-delay="180"><div class="es-card__body items-center text-center"><span class="es-step__num mx-auto">04</span><h3 class="es-card__title">Bundle e-waste</h3><p class="es-card__text text-sm text-center">Include chargers and cables with devices for one clean e-waste payout.</p></div></div>
        </div>
    </div>
</section>

""" + table_head + "\n\n" + cta_footer("Lock In Today's Rates", "Schedule a pickup now and payouts are calculated at the rate card price active at your arrival time.")


def how_main():
    return """
<!-- 1 · Hero -->
""" + hero("How It Works", "scale.jpg", "How It Works",
    "Book, route, weigh, get paid — a transparent four-step journey you can follow live from your dashboard.",
    eyebrow="Step-by-Step",
    crumb='<li class="text-gray-400"><a href="index.html" class="hover:text-white">Home</a></li><li class="text-gray-500">/</li><li class="text-primaryLight font-semibold">How It Works</li>',
    media_desc="Calibrated weighing scale used at EcoScrap doorstep pickups") + """
<!-- 2 · The four steps -->
<section data-section="2" class="section bg-white dark:bg-gray-900">
    <div class="container-es">
        <div class="text-center max-w-2xl mx-auto">
            <span class="es-eyebrow es-reveal">The Journey</span>
            <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">Four Steps to Cash in Hand</h2>
        </div>
        <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-7 mt-12">
            <div class="es-card es-card--hover es-reveal"><div class="es-card__body items-center text-center"><span class="es-step__num mx-auto">1</span><h3 class="es-card__title mt-4">Select Your Scrap</h3><p class="es-card__text text-sm text-center">Choose categories and an estimated weight band online — rates appear instantly.</p></div></div>
            <div class="es-card es-card--hover es-reveal" data-reveal-delay="60"><div class="es-card__body items-center text-center"><span class="es-step__num mx-auto">2</span><h3 class="es-card__title mt-4">Schedule a Pickup</h3><p class="es-card__text text-sm text-center">Pick a morning, afternoon or evening slot. The collector's ETA updates live.</p></div></div>
            <div class="es-card es-card--hover es-reveal" data-reveal-delay="120"><div class="es-card__body items-center text-center"><span class="es-step__num mx-auto">3</span><h3 class="es-card__title mt-4">Weigh &amp; Verify</h3><p class="es-card__text text-sm text-center">Calibrated digital scale, weight shown beside the vehicle and logged to your ID.</p></div></div>
            <div class="es-card es-card--hover es-reveal" data-reveal-delay="180"><div class="es-card__body items-center text-center"><span class="es-step__num mx-auto">4</span><h3 class="es-card__title mt-4">Receive Payment</h3><p class="es-card__text text-sm text-center">UPI in seconds, bank credit in a day, or cash on the spot — your choice.</p></div></div>
        </div>
    </div>
</section>

<!-- 3 · What to prepare -->
<section data-section="3" class="section bg-lightBg dark:bg-[#0d1726]">
    <div class="container-es grid lg:grid-cols-2 gap-10 items-start">
        <div class="es-reveal">
            <span class="es-eyebrow">Checklist</span>
            <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">What to Prepare Before Pickup</h2>
            <div class="mt-8 space-y-3">
                <div class="es-panel flex items-center gap-3"><i class="fa-solid fa-circle-check text-primary text-xl"></i><span class="text-gray-700 dark:text-gray-200">Bundle paper and cardboard, keep dry</span></div>
                <div class="es-panel flex items-center gap-3"><i class="fa-solid fa-circle-check text-primary text-xl"></i><span class="text-gray-700 dark:text-gray-200">Separate metals from plastics for a better rate</span></div>
                <div class="es-panel flex items-center gap-3"><i class="fa-solid fa-circle-check text-primary text-xl"></i><span class="text-gray-700 dark:text-gray-200">Keep e-waste in one box, cables included</span></div>
                <div class="es-panel flex items-center gap-3"><i class="fa-solid fa-circle-check text-primary text-xl"></i><span class="text-gray-700 dark:text-gray-200">Keep heavy items near the entrance or ground floor</span></div>
                <div class="es-panel flex items-center gap-3"><i class="fa-solid fa-circle-check text-primary text-xl"></i><span class="text-gray-700 dark:text-gray-200">Have photo ID ready for the weighing record</span></div>
            </div>
        </div>
        <div class="es-reveal" data-reveal-delay="120">
            <span class="es-eyebrow">Not Accepted</span>
            <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">Items We Can't Take</h2>
            <div class="mt-8 grid sm:grid-cols-2 gap-3">
                <div class="es-panel flex items-center gap-3"><i class="fa-solid fa-circle-xmark text-red-500 text-xl"></i><span class="text-gray-700 dark:text-gray-200">Hazardous chemicals</span></div>
                <div class="es-panel flex items-center gap-3"><i class="fa-solid fa-circle-xmark text-red-500 text-xl"></i><span class="text-gray-700 dark:text-gray-200">Biomedical waste</span></div>
                <div class="es-panel flex items-center gap-3"><i class="fa-solid fa-circle-xmark text-red-500 text-xl"></i><span class="text-gray-700 dark:text-gray-200">Pressurised gas cylinders</span></div>
                <div class="es-panel flex items-center gap-3"><i class="fa-solid fa-circle-xmark text-red-500 text-xl"></i><span class="text-gray-700 dark:text-gray-200">Sealed fuel &amp; paint tins</span></div>
                <div class="es-panel flex items-center gap-3"><i class="fa-solid fa-circle-xmark text-red-500 text-xl"></i><span class="text-gray-700 dark:text-gray-200">Medical sharps</span></div>
                <div class="es-panel flex items-center gap-3"><i class="fa-solid fa-circle-xmark text-red-500 text-xl"></i><span class="text-gray-700 dark:text-gray-200">Radioactive &amp; biohazard waste</span></div>
            </div>
            <p class="text-sm text-gray-500 dark:text-gray-400 mt-5">Not sure? <a href="contact.html" class="text-primary font-semibold underline underline-offset-2">Message us a photo</a> before booking.</p>
        </div>
    </div>
</section>

<!-- 4 · Live status tracker -->
<section data-section="4" class="section bg-white dark:bg-gray-900">
    <div class="container-es grid lg:grid-cols-2 gap-12 items-center">
        <div class="es-reveal">
            <span class="es-eyebrow">Track Live</span>
            <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">Follow Every Stage in Real Time</h2>
            <p class="es-subtitle mt-4 es-reveal" data-reveal-delay="120">Once your request is confirmed, a status tracker updates automatically: booked, collector dispatched, en route, verified and paid. Your dashboard shows the exact tread of each stage.</p>
            <ul class="mt-7 space-y-3 text-sm text-gray-600 dark:text-gray-300 es-reveal" data-reveal-delay="180">
                <li class="flex items-center gap-3"><i class="fa-solid fa-bell text-primary"></i> Push + WhatsApp status updates</li>
                <li class="flex items-center gap-3"><i class="fa-solid fa-location-dot text-primary"></i> Collector ETA and route preview</li>
                <li class="flex items-center gap-3"><i class="fa-solid fa-file-invoice text-primary"></i> Digital receipt + weight record</li>
            </ul>
            <div class="mt-8 es-reveal" data-reveal-delay="240"><a href="customer-dashboard.html" class="es-btn es-btn--primary es-btn--lg">Open Sample Tracker <i class="fa-solid fa-arrow-right rtl-flip"></i></a></div>
        </div>
        <div class="es-panel es-reveal" data-reveal-delay="120">
            <div class="flex justify-between items-center mb-6">
                <h3 class="font-bold text-gray-900 dark:text-white">Pickup #REQ-101 — live</h3>
                <span class="es-badge es-badge--amber"><i class="fa-solid fa-truck-fast"></i> En route</span>
            </div>
            <div class="es-stepper pt-2">
                <div class="es-stepper__track">
                    <div class="es-stepper__step is-done"><span class="es-stepper__dot"><i class="fa-solid fa-check"></i></span><span class="es-stepper__label">Booked</span></div>
                    <div class="es-stepper__step is-done"><span class="es-stepper__dot"><i class="fa-solid fa-check"></i></span><span class="es-stepper__label">Dispatched</span></div>
                    <div class="es-stepper__step is-current"><span class="es-stepper__dot">3</span><span class="es-stepper__label">En route</span></div>
                    <div class="es-stepper__step"><span class="es-stepper__dot">4</span><span class="es-stepper__label">Verify</span></div>
                    <div class="es-stepper__step"><span class="es-stepper__dot">5</span><span class="es-stepper__label">Paid</span></div>
                </div>
            </div>
            <div class="mt-6 space-y-3">
                <div class="flex justify-between text-sm"><span class="text-gray-500 dark:text-gray-400">Category</span><span class="font-semibold text-gray-900 dark:text-white">Mixed — paper, metal</span></div>
                <div class="flex justify-between text-sm"><span class="text-gray-500 dark:text-gray-400">Slot</span><span class="font-semibold text-gray-900 dark:text-white">Today, 5:00 – 6:30 PM</span></div>
                <div class="flex justify-between text-sm"><span class="text-gray-500 dark:text-gray-400">ETA</span><span class="font-semibold text-green-600 dark:text-primaryLight">≈ 18 min away</span></div>
                <div class="es-progress mt-2"><span class="es-progress__fill block" style="width:64%"></span></div>
            </div>
        </div>
    </div>
</section>

<!-- 5 · FAQ -->
<section data-section="5" class="section bg-lightBg dark:bg-[#0d1726]">
    <div class="container-es">
        <div class="text-center max-w-2xl mx-auto es-reveal">
            <span class="es-eyebrow">Questions</span>
            <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">Before You Book</h2>
        </div>
        <div class="mt-12">%s</div>
    </div>
</section>

""" + faq_block() + "\n\n" + cta_footer()


def blog_main():
    return """
<!-- 1 · Hero -->
""" + hero("Blog", "boxes.jpg", "EcoScrap Blog",
    "Rates, e-waste rules, home recycling hacks and the stories behind India's circular economy.",
    eyebrow="Insights &amp; Stories",
    crumb='<li class="text-gray-400"><a href="index.html" class="hover:text-white">Home</a></li><li class="text-gray-500">/</li><li class="text-primaryLight font-semibold">Blog</li>',
    media_desc="Cardboard and recyclables prepared for collection at an Indian home") + """
<!-- 2 · Featured post -->
<section data-section="2" class="section bg-white dark:bg-gray-900">
    <div class="container-es max-w-4xl" data-render="featured-post"></div>
</section>

<!-- 3 · Topic filter + grid -->
<section data-section="3" class="section bg-lightBg dark:bg-[#0d1726]">
    <div class="container-es">
        <div class="flex flex-col lg:flex-row gap-4 justify-between items-start lg:items-center">
            <div>
                <span class="es-eyebrow es-reveal">All Articles</span>
                <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">Latest from the Blog</h2>
            </div>
            <div class="relative w-full sm:w-72 es-reveal" data-reveal-delay="80">
                <i class="fa-solid fa-magnifying-glass absolute inset-y-0 left-4 flex items-center text-gray-400"></i>
                <input data-post-search type="search" placeholder="Search articles…" class="es-input !ps-11" aria-label="Search blog posts">
            </div>
        </div>
        <div class="mt-8 flex flex-wrap gap-2" data-post-filters></div>
        <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-7 mt-8" data-render="posts"></div>
        <p id="posts-empty" class="es-empty hidden">No articles match that selection. Clear the search or pick another topic.</p>
    </div>
</section>

<!-- 4 · Topics to explore -->
<section data-section="4" class="section bg-white dark:bg-gray-900">
    <div class="container-es grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
        <a href="blog.html" class="es-panel es-panel--hover es-reveal block"><span class="es-card__icon"><i class="fa-solid fa-tags"></i></span><h3 class="es-card__title mt-3">Rates &amp; Pricing</h3><p class="es-card__text text-sm mt-1">Why metal moves and how paper is priced.</p></a>
        <a href="blog-details.html?post=ewaste-recycling-india" class="es-panel es-panel--hover es-reveal block" data-reveal-delay="60"><span class="es-card__icon"><i class="fa-solid fa-microchip"></i></span><h3 class="es-card__title mt-3">E-Waste Rules</h3><p class="es-card__text text-sm mt-1">Compliance, certificates and handover.</p></a>
        <a href="blog-details.html?post=cardboard-recycling-tips" class="es-panel es-panel--hover es-reveal block" data-reveal-delay="120"><span class="es-card__icon"><i class="fa-solid fa-house-chimney"></i></span><h3 class="es-card__title mt-3">Home &amp; Hacks</h3><p class="es-card__text text-sm mt-1">Everyday habits that shrink your bin.</p></a>
        <a href="blog-details.html?post=battery-disposal-safety" class="es-panel es-panel--hover es-reveal block" data-reveal-delay="180"><span class="es-card__icon"><i class="fa-solid fa-triangle-exclamation"></i></span><h3 class="es-card__title mt-3">Safety</h3><p class="es-card__text text-sm mt-1">Batteries, sharps and the do-not-bin list.</p></a>
    </div>
</section>

<!-- 5 · Why follow us -->
<section data-section="5" class="section bg-lightBg dark:bg-[#0d1726]">
    <div class="container-es grid md:grid-cols-3 gap-6">
        <div class="es-panel es-reveal text-center"><span class="es-pin mx-auto mb-3"><i class="fa-solid fa-bell text-xl"></i></span><h3 class="font-bold text-gray-900 dark:text-white">Rate alerts</h3><p class="text-sm text-gray-500 dark:text-gray-400 mt-2">Get notified when metal or paper prices jump in your city.</p></div>
        <div class="es-panel es-reveal text-center" data-reveal-delay="60"><span class="es-pin mx-auto mb-3"><i class="fa-solid fa-envelope-open-text text-xl"></i></span><h3 class="font-bold text-gray-900 dark:text-white">Weekly digest</h3><p class="text-sm text-gray-500 dark:text-gray-400 mt-2">One email a week — recycling news, tips and pickups.</p></div>
        <div class="es-panel es-reveal text-center" data-reveal-delay="120"><span class="es-pin mx-auto mb-3"><i class="fa-solid fa-newspaper text-xl"></i></span><h3 class="font-bold text-gray-900 dark:text-white">Founder notes</h3><p class="text-sm text-gray-500 dark:text-gray-400 mt-2">Occasional long reads on building a zero-waste India.</p></div>
    </div>
</section>

""" + cta_footer("Want Rates Like a Pro?", "Subscribe to the newsletter for weekly scrap price updates and recycling guides — no spam, unsubscribe anytime.", primary=("Browse The Blog", "blog.html"), secondary=("Talk to Sales", "contact.html"))


def blog_details_main():
    return r"""
<!-- 1 · Hero -->
<section data-section="1" class="hero">
    <div class="hero__media" style="background-image:url('assets/images/boxes.jpg')" role="img" aria-label="Recyclable material on a doorstep pickup"></div>
    <div class="hero__overlay hero__overlay--dark"></div>
    <div class="container-es relative z-10 py-20 lg:py-24 text-center">
        <span class="es-eyebrow es-reveal" id="bd-category">Insights</span>
        <h1 class="mt-5 text-3xl md:text-5xl font-extrabold text-white leading-tight max-w-4xl mx-auto es-reveal" data-reveal-delay="80" id="bd-title">Understanding Scrap Rates in India: A Complete Guide</h1>
        <div class="mt-6 flex items-center justify-center gap-3 text-sm text-gray-300 es-reveal" data-reveal-delay="160">
            <span class="flex items-center gap-2"><span class="w-8 h-8 rounded-full bg-primary flex items-center justify-center text-xs font-bold text-white" id="bd-author">RM</span>Rohit Mehra</span>
            <span id="bd-date" class="flex items-center gap-1.5"><i class="fa-regular fa-calendar"></i>Aug 28, 2026</span>
            <span id="bd-read" class="flex items-center gap-1.5"><i class="fa-regular fa-clock"></i>7 min read</span>
        </div>
    </div>
</section>

<!-- 2 · Article body -->
<section data-section="2" class="section bg-white dark:bg-gray-900">
    <div class="container-es max-w-4xl">
        <div class="es-card__media es-card__media--wide rounded-3xl overflow-hidden es-reveal">
            <img src="assets/images/boxes.jpg" alt="Illustrative article banner — recyclable materials" width="1600" height="900" id="bd-banner" class="w-full h-full object-cover">
        </div>
        <div class="es-prose pt-10 es-reveal" id="bd-body">
            <h2>The quiet economics of your bin</h2>
            <p>Every month, the average Indian household discards between 8 and 12 kilograms of material that a scrap dealer would happily buy. The catch has never been the material — it is the friction: heavy bags, opaque rates and guessing games at the weight.</p>
            <p>EcoScrap removes that friction by publishing rates, calibrating scales and paying on the spot. This article walks through how those published numbers are actually decided, and how you can use that knowledge to earn more from every pickup.</p>
            <h2>Why metal prices swing every day</h2>
            <p>Copper, aluminium and steel follow international futures markets plus port-side demand in India. A spike on the London Metal Exchange usually shows up in local dealer boards within 24 hours. Paper, by contrast, moves on domestic pulp demand and festive season packaging cycles.</p>
            <h2>What actually changes your payout</h2>
            <ul>
                <li><strong>Separation.</strong> Copper sorted away from steel prices as copper; mixed metal prices as the lowest common denominator.</li>
                <li><strong>Moisture.</strong> Wet paper is heavy paper — payouts are based on material, not water weight.</li>
                <li><strong>Contamination.</strong> Food residue, plastic-coated boards and glued laminates knock paper into lower grades.</li>
                <li><strong>Verified weight.</strong> A calibrated scale versus a hand guess is often a 10–15% difference.</li>
            </ul>
            <h2>Reading a rate card like a pro</h2>
            <p>The published rate is a starting point. For clean, dry, well-separated loads you are entitled to the top of the band. Ask for a category-specific estimate before the collector arrives — it makes the weighing conversation honest and fast.</p>
            <h2>The takeaway</h2>
            <p>Scrap value is real money. A modest household that bundles responsibly can add a few thousand rupees a year from material it would otherwise lose — while the environment keeps the material in circulation.</p>
        </div>
    </div>
</section>

<!-- 3 · Author -->
<section data-section="3" class="section bg-lightBg dark:bg-[#0d1726]">
    <div class="container-es max-w-4xl">
        <div class="es-panel es-reveal flex flex-col sm:flex-row gap-5 items-start sm:items-center">
            <div class="w-16 h-16 rounded-full bg-gradient-to-br from-primary to-primaryDark text-white flex items-center justify-center text-xl font-bold flex-none" id="bd-author-lg">RM</div>
            <div class="flex-1">
                <h3 class="font-bold text-gray-900 dark:text-white">Rohit Mehra <span class="text-xs font-normal text-gray-400">· Author</span></h3>
                <p class="text-sm text-gray-500 dark:text-gray-400 mt-1">Rohit co-founded EcoScrap and writes about scrap markets, e-waste policy and practical home recycling. He has personally weighed over 2,000 doorstep pickups.</p>
            </div>
            <a href="blog.html" class="es-btn es-btn--ghost es-btn--sm flex-none"><i class="fa-solid fa-arrow-left rtl-flip"></i> Back to Blog</a>
        </div>
    </div>
</section>

<!-- 4 · Share & actions -->
<section data-section="4" class="section bg-white dark:bg-gray-900">
    <div class="container-es max-w-4xl">
        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 es-reveal">
            <h3 class="font-bold text-lg text-gray-900 dark:text-white">Enjoyed this read?</h3>
            <div class="flex gap-2">
                <button type="button" class="es-chip" data-share-link><i class="fa-brands fa-linkedin"></i> LinkedIn</button>
                <button type="button" class="es-chip" data-share-link><i class="fa-brands fa-x-twitter"></i> X</button>
                <button type="button" class="es-chip" data-share-link><i class="fa-brands fa-whatsapp"></i> WhatsApp</button>
                <button type="button" class="es-chip" data-copy-link><i class="fa-solid fa-link"></i> Copy link</button>
            </div>
        </div>
    </div>
</section>

<!-- 5 · Related posts -->
<section data-section="5" class="section bg-lightBg dark:bg-[#0d1726]">
    <div class="container-es">
        <div class="flex items-end justify-between gap-4">
            <div><span class="es-eyebrow es-reveal">Keep Reading</span><h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">Related Articles</h2></div>
            <a href="blog.html" class="es-btn es-btn--ghost es-btn--sm flex-none es-reveal">View All <i class="fa-solid fa-arrow-right rtl-flip"></i></a>
        </div>
        <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-7 mt-10" data-render="related-posts"></div>
    </div>
</section>

""" + cta_footer("Empowered by Better Rates?", "Create an account to convert what you just read into a booked doorstep pickup — and a payout to match.", primary=("Schedule a Pickup", "customer-dashboard.html"), secondary=("Explore Services", "services.html"))


def contact_main():
    return """
<!-- 1 · Hero -->
""" + hero("Contact", "support.jpg", "Contact Us",
    "Bookings, quotes, partnerships or just a recycling question — the EcoScrap team responds within one business day.",
    eyebrow="We're Here to Help",
    crumb='<li class="text-gray-400"><a href="index.html" class="hover:text-white">Home</a></li><li class="text-gray-500">/</li><li class="text-primaryLight font-semibold">Contact</li>',
    media_desc="EcoScrap customer support team ready to help") + """
<!-- 2 · Contact channels -->
<section data-section="2" class="section bg-white dark:bg-gray-900">
    <div class="container-es grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
        <div class="es-card es-reveal"><div class="es-card__body items-center text-center"><span class="es-card__icon"><i class="fa-solid fa-phone"></i></span><h3 class="es-card__title mt-3">Call Us</h3><p class="es-card__text text-sm text-center">1800-266-5432<br>(toll-free, 7 AM – 9 PM)</p><div class="es-card__foot w-full"><a href="tel:18002665432" class="es-btn es-btn--ghost es-btn--sm es-btn--block">Call Now</a></div></div></div>
        <div class="es-card es-reveal" data-reveal-delay="60"><div class="es-card__body items-center text-center"><span class="es-card__icon"><i class="fa-brands fa-whatsapp"></i></span><h3 class="es-card__title mt-3">WhatsApp</h3><p class="es-card__text text-sm text-center">Message a photo of your scrap for a fast estimate.</p><div class="es-card__foot w-full"><a target="_blank" rel="noopener" href="https://wa.me/9118002665432" class="es-btn es-btn--ghost es-btn--sm es-btn--block">Chat Now</a></div></div></div>
        <div class="es-card es-reveal" data-reveal-delay="120"><div class="es-card__body items-center text-center"><span class="es-card__icon"><i class="fa-solid fa-envelope"></i></span><h3 class="es-card__title mt-3">Email</h3><p class="es-card__text text-sm text-center">hello@ecoscrap.in — quotes in 24 hours.</p><div class="es-card__foot w-full"><a href="mailto:hello@ecoscrap.in" class="es-btn es-btn--ghost es-btn--sm es-btn--block">Write to Us</a></div></div></div>
        <div class="es-card es-reveal" data-reveal-delay="180"><div class="es-card__body items-center text-center"><span class="es-card__icon"><i class="fa-solid fa-location-dot"></i></span><h3 class="es-card__title mt-3">Head Office</h3><p class="es-card__text text-sm text-center">42, Green Avenue, Okhla, New Delhi 110020</p><div class="es-card__foot w-full"><a href="locations.html" class="es-btn es-btn--ghost es-btn--sm es-btn--block">All Locations</a></div></div></div>
    </div>
</section>

<!-- 3 · Form + info -->
<section data-section="3" class="section bg-lightBg dark:bg-[#0d1726]">
    <div class="container-es grid lg:grid-cols-5 gap-10">
        <div class="lg:col-span-3 es-reveal">
            <div class="es-panel">
                <span class="es-eyebrow">Send a Message</span>
                <h2 class="es-title mt-4 text-2xl md:text-3xl">Tell Us What You Need</h2>
                <form id="contact-form" data-validate class="mt-8 space-y-5">
                    <div data-form-alert class="es-alert es-alert--error"></div>
                    <div class="grid sm:grid-cols-2 gap-4">
                        <div class="es-field"><label class="es-label" for="c-name">Full Name</label><input id="c-name" name="name" type="text" class="es-input" data-label="Your name" required><span class="es-error"><i class="fa-solid fa-circle-exclamation"></i></span></div>
                        <div class="es-field"><label class="es-label" for="c-phone">Phone</label><input id="c-phone" name="phone" type="tel" class="es-input" data-label="Phone number" required><span class="es-error"><i class="fa-solid fa-circle-exclamation"></i></span></div>
                    </div>
                    <div class="grid sm:grid-cols-2 gap-4">
                        <div class="es-field"><label class="es-label" for="c-email">Email</label><input id="c-email" name="email" type="email" class="es-input" data-label="Email address" required><span class="es-error"><i class="fa-solid fa-circle-exclamation"></i></span></div>
                        <div class="es-field"><label class="es-label" for="c-topic">Topic</label><select id="c-topic" name="topic" class="es-select"><option>General enquiry</option><option>Book a pickup</option><option>Corporate quote</option><option>Society drive</option><option>Partnership</option><option>Complaint / feedback</option></select></div>
                    </div>
                    <div class="es-field"><label class="es-label" for="c-message">Message</label><textarea id="c-message" name="message" class="es-textarea" data-label="Message" data-minlen="10" required placeholder="Tell us about the scrap you have, quantities, and your area…"></textarea><span class="es-error"><i class="fa-solid fa-circle-exclamation"></i></span></div>
                    <button type="submit" class="es-btn es-btn--primary es-btn--lg"><i class="fa-solid fa-paper-plane"></i> Send Message</button>
                    <p class="text-xs text-gray-500 dark:text-gray-400">Demo form — messages are stored locally in your browser. Live messaging requires a backend.</p>
                </form>
            </div>
        </div>
        <div class="lg:col-span-2 space-y-6">
            <div class="es-card es-reveal"><div class="es-card__body">
                <h3 class="es-card__title">Office Hours</h3>
                <ul class="text-sm text-gray-500 dark:text-gray-400 space-y-2 mt-3">
                    <li class="flex justify-between"><span>Monday – Friday</span><span class="font-semibold text-gray-900 dark:text-white">7 AM – 9 PM</span></li>
                    <li class="flex justify-between"><span>Saturday</span><span class="font-semibold text-gray-900 dark:text-white">8 AM – 8 PM</span></li>
                    <li class="flex justify-between"><span>Sunday</span><span class="font-semibold text-gray-900 dark:text-white">8 AM – 6 PM</span></li>
                </ul>
                <div class="es-progress mt-3"><span class="es-progress__fill block" style="width:78%"></span></div>
                <p class="text-xs text-gray-400 mt-2">Most messages answered within 2 working hours</p>
            </div></div>
            <div class="es-panel es-reveal" data-reveal-delay="80">
                <h3 class="font-bold text-gray-900 dark:text-white">Prefer to Talk Scrap?</h3>
                <p class="text-sm text-gray-500 dark:text-gray-400 mt-2 mb-4">Book a pickup directly — the fastest route to a payout.</p>
                <a href="customer-dashboard.html" class="es-btn es-btn--primary es-btn--block">Go to Dashboard</a>
                <a href="rate-card.html" class="es-btn es-btn--ghost es-btn--block mt-3">Check Scrap Rates</a>
            </div>
        </div>
    </div>
</section>

<!-- 4 · Map preview -->
<section data-section="4" class="section bg-white dark:bg-gray-900">
    <div class="container-es">
        <div class="text-center max-w-2xl mx-auto es-reveal">
            <span class="es-eyebrow">Find Us</span>
            <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">Head Office on the Map</h2>
        </div>
        <div class="mt-10 es-card es-reveal overflow-hidden aspect-[21/9]">
            <iframe title="EcoScrap head office map" src="https://www.openstreetmap.org/export/embed.html?bbox=77.20%2C28.54%2C77.34%2C28.62&amp;layer=mapnik&amp;marker=28.5800%2C77.2700" class="w-full h-full border-0" loading="lazy"></iframe>
        </div>
    </div>
</section>

<!-- 5 · Response promise -->
<section data-section="5" class="section bg-lightBg dark:bg-[#0d1726]">
    <div class="container-es grid sm:grid-cols-3 gap-6">
        <div class="es-panel es-reveal text-center"><span class="es-pin mx-auto mb-3"><i class="fa-solid fa-bolt text-xl"></i></span><h3 class="font-bold text-gray-900 dark:text-white">Within 2 hours</h3><p class="text-sm text-gray-500 dark:text-gray-400 mt-2">Response time for enquiries during working hours.</p></div>
        <div class="es-panel es-reveal text-center" data-reveal-delay="60"><span class="es-pin mx-auto mb-3"><i class="fa-solid fa-file-contract text-xl"></i></span><h3 class="font-bold text-gray-900 dark:text-white">Quotes in 24 hrs</h3><p class="text-sm text-gray-500 dark:text-gray-400 mt-2">Corporate and bulk scrap estimates within one working day.</p></div>
        <div class="es-panel es-reveal text-center" data-reveal-delay="120"><span class="es-pin mx-auto mb-3"><i class="fa-solid fa-shield-halved text-xl"></i></span><h3 class="font-bold text-gray-900 dark:text-white">No-spam promise</h3><p class="text-sm text-gray-500 dark:text-gray-400 mt-2">We never share your details. Marketing emails are opt-in only.</p></div>
    </div>
</section>

""" + cta_footer("Talk Is Cheap — Let's Collect", "Skip the mail thread. Schedule a pickup and see your scrap turn into cash today.", primary=("<i class=\"fa-solid fa-calendar-check\"></i> Schedule Pickup", "customer-dashboard.html"), secondary=("View Live Rates", "rate-card.html"))


def locations_main():
    return """
<!-- 1 · Hero -->
""" + hero("Locations", "delhi.jpg", "Service Locations",
    "Six metros, growing every quarter. Search your area to confirm doorstep availability, pickup slots and the categories we accept near you.",
    eyebrow="Where We Operate",
    crumb='<li class="text-gray-400"><a href="index.html" class="hover:text-white">Home</a></li><li class="text-gray-500">/</li><li class="text-primaryLight font-semibold">Locations</li>',
    media_desc="Aerial view representing the Delhi NCR service region") + """
<!-- 2 · Location browser -->
<section data-section="2" class="section bg-white dark:bg-gray-900">
    <div class="container-es">
        <div class="text-center max-w-2xl mx-auto">
            <span class="es-eyebrow es-reveal">Live Coverage</span>
            <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">Browse Service Areas</h2>
            <p class="es-subtitle mt-4 es-reveal" data-reveal-delay="120">Search by name, area or city and filter by coverage. Select your location to reserve a pickup slot.</p>
        </div>
        <div class="mt-10 flex flex-col md:flex-row gap-3 justify-center es-reveal" data-reveal-delay="120">
            <div class="relative flex-1 max-w-md">
                <i class="fa-solid fa-magnifying-glass absolute inset-y-0 left-4 flex items-center text-gray-400"></i>
                <input data-location-search type="search" placeholder="Search location, area or city…" class="es-input !ps-11" aria-label="Search locations">
            </div>
            <select data-location-coverage class="es-select md:w-56" aria-label="Filter by coverage">
                <option value="All">All coverage</option>
                <option value="Full Coverage">Full coverage</option>
                <option value="Selected Zones">Selected zones</option>
                <option value="Partial Coverage">Partial coverage</option>
            </select>
        </div>
        <p class="text-center text-xs text-gray-500 dark:text-gray-400 mt-3 es-reveal"><span data-location-count>6</span> service areas listed</p>
        <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-7 mt-8" data-render="locations"></div>
        <p id="locations-empty" class="es-empty hidden">No matching service area yet. Tell us where you are and we'll prioritise your neighbourhood.</p>
        <p data-location-summary class="hidden mt-6 text-center text-sm font-medium text-primary bg-primary/10 border border-primary/20 rounded-full px-5 py-3 max-w-md mx-auto"></p>
    </div>
</section>

<!-- 3 · How pickup works per location -->
<section data-section="3" class="section bg-lightBg dark:bg-[#0d1726]">
    <div class="container-es grid lg:grid-cols-2 gap-10 items-center">
        <div class="es-reveal">
            <span class="es-eyebrow">Local Operations</span>
            <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">A Dedicated Fleet in Every City</h2>
            <p class="es-subtitle mt-4 es-reveal" data-reveal-delay="120">Each metro runs its own collection roster, local weighing centres and city WhatsApp support — so response times stay fast and standards stay identical.</p>
            <ul class="mt-7 space-y-3 text-sm text-gray-600 dark:text-gray-300 es-reveal" data-reveal-delay="180">
                <li class="flex items-center gap-3"><i class="fa-solid fa-truck text-primary"></i> EVs + tippers, GPS-tracked for ETA</li>
                <li class="flex items-center gap-3"><i class="fa-solid fa-city text-primary"></i> City-specific WhatsApp support lines</li>
                <li class="flex items-center gap-3"><i class="fa-solid fa-location-crosshairs text-primary"></i> Same-day slots in full-coverage zones</li>
                <li class="flex items-center gap-3"><i class="fa-solid fa-arrows-rotate text-primary"></i> Free rescheduling up to 3 hours before</li>
            </ul>
        </div>
        <div class="grid grid-cols-2 gap-4 es-reveal" data-reveal-delay="120">
            <div class="es-panel es-panel--hover text-center"><p class="text-3xl font-extrabold text-primary">6</p><p class="text-sm text-gray-500 dark:text-gray-400 mt-1">Cities live</p></div>
            <div class="es-panel es-panel--hover text-center" ><p class="text-3xl font-extrabold text-primary">180+</p><p class="text-sm text-gray-500 dark:text-gray-400 mt-1">Neighbourhoods covered</p></div>
            <div class="es-panel es-panel--hover text-center"><p class="text-3xl font-extrabold text-primary">98%</p><p class="text-sm text-gray-500 dark:text-gray-400 mt-1">On-time arrivals</p></div>
            <div class="es-panel es-panel--hover text-center"><p class="text-3xl font-extrabold text-primary">4.7★</p><p class="text-sm text-gray-500 dark:text-gray-400 mt-1">Average rating</p></div>
        </div>
    </div>
</section>

<!-- 4 · Expansion roadmap + request -->
<section data-section="4" class="section bg-white dark:bg-gray-900">
    <div class="container-es grid lg:grid-cols-2 gap-10 items-start">
        <div>
            <span class="es-eyebrow es-reveal">Expansion</span>
            <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">Where We're Headed Next</h2>
            <div class="mt-8 space-y-0">
                <div class="flex gap-4 es-reveal"><span class="es-step__num !h-12 !w-12 !text-sm">Q4 26</span><div class="pb-6 border-s border-dashed border-gray-200 dark:border-gray-700 ps-4 -mt-1"><h3 class="font-bold text-gray-900 dark:text-white">Surat &amp; Ahmedabad</h3><p class="text-sm text-gray-500 dark:text-gray-400 mt-1">Textile-surplus recycling tie-ups in planning.</p></div></div>
                <div class="flex gap-4 es-reveal"><span class="es-step__num !h-12 !w-12 !text-sm">Q1 27</span><div class="pb-6 border-s border-dashed border-gray-200 dark:border-gray-700 ps-4 -mt-1"><h3 class="font-bold text-gray-900 dark:text-white">Kolkata &amp; Lucknow</h3><p class="text-sm text-gray-500 dark:text-gray-400 mt-1">Roster and local partner onboarding underway.</p></div></div>
                <div class="flex gap-4 es-reveal"><span class="es-step__num !h-12 !w-12 !text-sm">Q3 27</span><div class="ps-4 -mt-1"><h3 class="font-bold text-gray-900 dark:text-white">20 more Tier-2 cities</h3><p class="text-sm text-gray-500 dark:text-gray-400 mt-1">Number of slots depends on demand you register.</p></div></div>
            </div>
        </div>
        <div class="es-panel es-reveal" data-reveal-delay="120">
            <span class="es-card__icon"><i class="fa-solid fa-location-arrow"></i></span>
            <h3 class="text-2xl font-bold mt-4 text-gray-900 dark:text-white">Request Your City</h3>
            <p class="text-sm text-gray-500 dark:text-gray-400 mt-2 mb-6">Not on the list yet? Register interest and we'll fast-track your neighbourhood.</p>
            <form data-validate class="space-y-4">
                <div data-form-alert class="es-alert es-alert--error"></div>
                <div class="es-field"><label class="es-label">City / Area</label><input type="text" class="es-input" data-label="City or area" placeholder="e.g. Chandigarh, Sector 22" required><span class="es-error"><i class="fa-solid fa-circle-exclamation"></i></span></div>
                <div class="es-field"><label class="es-label">Email</label><input type="email" class="es-input" data-label="Email address" placeholder="you@example.com" required><span class="es-error"><i class="fa-solid fa-circle-exclamation"></i></span></div>
                <button type="submit" class="es-btn es-btn--primary es-btn--block es-btn--lg">Notify Me When Live</button>
                <p class="text-xs text-gray-400 text-center">We email once, when your city launches. No spam.</p>
            </form>
        </div>
    </div>
</section>

<!-- 5 · Location FAQ -->
<section data-section="5" class="section bg-lightBg dark:bg-[#0d1726]">
    <div class="container-es">
        <div class="text-center max-w-2xl mx-auto es-reveal">
            <span class="es-eyebrow">Location FAQs</span>
            <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">Common Questions</h2>
        </div>
        <div class="mt-12">%s</div>
    </div>
</section>

""" + faq_block() + "\n\n" + cta_footer("Your Neighbourhood, Served", "Check coverage, select your zone and schedule a doorstep pickup today.", primary=("<i class=\"fa-solid fa-magnifying-glass-location\"></i> Find My Area", "#locations"), secondary=("Schedule Pickup", "customer-dashboard.html"))


def legal_main(title, subtitle, sections, eyebrow):
    chunks = []
    for i, s in enumerate(sections):
        bg = "bg-white dark:bg-gray-900" if i % 2 == 0 else "bg-lightBg dark:bg-[#0d1726]"
        chunks.append(
            '<section data-section="' + str(i + 2) + '" class="section ' + bg + '">\n'
            + '    <div class="container-es max-w-4xl">\n        '
            + s
            + "\n    </div>\n</section>\n"
        )
    body = "".join(chunks)
    cta_bg = "bg-lightBg dark:bg-[#0d1726]" if len(sections) % 2 == 1 else "bg-white dark:bg-gray-900"
    cta = (
        '<section data-section="6" class="section ' + cta_bg + '">\n'
        + '    <div class="container-es max-w-4xl text-center">\n'
        + '        <div class="relative overflow-hidden rounded-3xl bg-primaryDark px-6 sm:px-12 py-14 es-reveal">\n'
        + '            <div class="absolute inset-0 opacity-15 hero__media" style="background-image:url(\'assets/images/green.jpg\')"></div>\n'
        + '            <div class="relative z-10">\n'
        + '                <h2 class="text-3xl sm:text-4xl font-extrabold text-white">Questions About This Document?</h2>\n'
        + '                <p class="mt-4 text-gray-200 max-w-xl mx-auto">Our compliance team is happy to clarify — reach out any day between 7 AM and 9 PM.</p>\n'
        + '                <div class="mt-8 flex flex-col sm:flex-row justify-center gap-3">\n'
        + '                    <a href="contact.html" class="es-btn es-btn--primary es-btn--lg">Contact Compliance</a>\n'
        + '                    <a href="index.html" class="es-btn es-btn--white es-btn--lg">Back to Home</a>\n'
        + "                </div>\n            </div>\n        </div>\n    </div>\n</section>\n"
    )
    return (
        """
<!-- 1 · Hero -->
""" + hero(eyebrow, "green.jpg", title, subtitle, eyebrow=eyebrow, media_desc="Green sustainability backdrop for legal pages") + body + cta
    )


PRIVACY_SECTIONS = [
    """<span class="es-eyebrow es-reveal">1 · Overview</span>
    <h2 class="es-title mt-4 text-2xl md:text-3xl es-reveal" data-reveal-delay="60">Data We Collect</h2>
    <div class="es-prose mt-6 es-reveal">
        <p>EcoScrap ("we", "us") collects the minimum data needed to run a pickup: your name, contact number, email, pickup address, transaction records and — where you choose to provide it — payment detail for settlements. This policy explains what we hold, why we hold it and the controls you have.</p>
        <ul><li><strong>Account &amp; profile data</strong> — name, phone, email, saved addresses.</li><li><strong>Transaction data</strong> — pickup requests, weights, rates, payouts.</li><li><strong>Usage data</strong> — device, browser and pages visited for service improvement.</li><li><strong>Communications</strong> — support interactions and newsletter preferences.</li></ul>
    </div>""",
    """<span class="es-eyebrow es-reveal">2 · Use</span>
    <h2 class="es-title mt-4 text-2xl md:text-3xl es-reveal" data-reveal-delay="60">How Your Data Is Used</h2>
    <div class="es-prose mt-6 es-reveal">
        <p>We use your information to book pickups, schedule collectors, settle payments, send status updates, meet regulatory documentation obligations and — with your consent — share rates and tips. We do not sell personal data, and we never share it for advertising-based activity.</p>
        <h3>Legal grounds</h3>
        <p>Processing is grounded in contract (providing the pickup), legal obligation (E-Waste Management Rules returns), consent (marketing) and legitimate interest (fraud prevention).</p>
    </div>""",
    """<span class="es-eyebrow es-reveal">3 · Sharing</span>
    <h2 class="es-title mt-4 text-2xl md:text-3xl es-reveal" data-reveal-delay="60">Who Sees Your Data</h2>
    <div class="es-prose mt-6 es-reveal">
        <p>Limited categories of recipients may access data strictly on a need-to-know basis: payment processors, certified recycling facilities (for consignment manifests), logistics partners and government authorities where legally required. Every processor signs a data-protection agreement.</p>
    </div>""",
    """<span class="es-eyebrow es-reveal">4 · Security</span>
    <h2 class="es-title mt-4 text-2xl md:text-3xl es-reveal" data-reveal-delay="60">Security, Retention &amp; Your Rights</h2>
    <div class="es-prose mt-6 es-reveal">
        <p>Transmission is encrypted in transit and at rest; access is role-scoped and audited. Transaction records are retained as required by tax and e-waste rules, then securely deleted or anonymised.</p>
        <p>You may access, rectify, restrict processing of, or delete your personal data at any time. To exercise any right, email compliance@ecoscrap.in or write to 42, Green Avenue, Okhla, New Delhi 110020. This page also acts as our demo privacy statement for this front-end prototype.</p>
    </div>""",
]


def privacy_main():
    return legal_main(
        "Privacy Policy", "How EcoScrap collects, uses and safeguards your information across pickups, payments and support.",
        PRIVACY_SECTIONS, "Privacy Policy")


TERMS_SECTIONS = [
    """<span class="es-eyebrow es-reveal">1 · Scope</span>
    <h2 class="es-title mt-4 text-2xl md:text-3xl es-reveal" data-reveal-delay="60">Agreement &amp; Eligibility</h2>
    <div class="es-prose mt-6 es-reveal">
        <p>These Terms govern your use of EcoScrap's website, dashboard and doorstep pickup services. By creating an account or booking a pickup you agree to these Terms. You must be at least 18 years old, or have a guardian's consent, to use paid pickup services.</p>
    </div>""",
    """<span class="es-eyebrow es-reveal">2 · Service</span>
    <h2 class="es-title mt-4 text-2xl md:text-3xl es-reveal" data-reveal-delay="60">Bookings, Weights &amp; Payments</h2>
    <div class="es-prose mt-6 es-reveal">
        <p>Pickups are booked for a time slot; arrivals may vary with traffic. Weights are verified on calibrated scales and are the basis for payout. Rates are indicative and final payout follows the published rate at your material's verified weight and inspected quality. Payments are settled via UPI, bank transfer or cash as selected. Hazardous, biomedical and other excluded items (see How It Works) are not collected.</p>
    </div>""",
    """<span class="es-eyebrow es-reveal">3 · User Duties</span>
    <h2 class="es-title mt-4 text-2xl md:text-3xl es-reveal" data-reveal-delay="60">Your Responsibilities</h2>
    <div class="es-prose mt-6 es-reveal">
        <p>You agree to provide accurate contact and address details; ensure the scrap is legally yours; keep items accessible for the collector; not include prohibited waste; and confirm identity at weighing. EcoScrap is not liable for items misdescribed by the user.</p>
    </div>""",
    """<span class="es-eyebrow es-reveal">4 · Liability</span>
    <h2 class="es-title mt-4 text-2xl md:text-3xl es-reveal" data-reveal-delay="60">Liability &amp; Changes</h2>
    <div class="es-prose mt-6 es-reveal">
        <p>The website and dashboards are provided "as is". This is a demonstration front end: bookings, payouts and management screens use locally stored demo data and are not a live marketplace. To the maximum extent permitted by law, EcoScrap's aggregate liability for a pickup is limited to the payout value of that pickup.</p>
        <p>We may update these Terms from time to time. Material changes are notified on this page and, where practicable, by email. Continued use after changes constitutes acceptance. For any question, contact support at hello@ecoscrap.in.</p>
    </div>""",
]


def terms_main():
    return legal_main(
        "Terms & Conditions", "The rules that govern EcoScrap pickups, weights, payments and your use of the platform.",
        TERMS_SECTIONS, "Terms & Conditions")


def notfound_main():
    return """
<!-- 1 · Hero -->
<section data-section="1" class="hero">
    <div class="hero__media" style="background-image:url('assets/images/scrapyard.jpg')"></div>
    <div class="hero__overlay hero__overlay--dark"></div>
    <div class="container-es relative z-10 text-center py-24">
        <p class="es-eyebrow es-reveal">Error 404</p>
        <h1 class="mt-5 text-6xl md:text-8xl font-extrabold text-white es-reveal" data-reveal-delay="80">404</h1>
        <p class="mx-auto mt-5 text-xl text-gray-200 max-w-xl es-reveal" data-reveal-delay="160">This page went to the recycling bin — but it wasn't sorted properly. Let's get you back on track.</p>
        <div class="mt-8 flex flex-col sm:flex-row justify-center gap-3 es-reveal" data-reveal-delay="240">
            <a href="index.html" class="es-btn es-btn--primary es-btn--lg"><i class="fa-solid fa-house"></i> Back to Home</a>
            <a href="contact.html" class="es-btn es-btn--glass es-btn--lg">Contact Support</a>
        </div>
    </div>
</section>

<!-- 2 · Popular links -->
<section data-section="2" class="section bg-white dark:bg-gray-900">
    <div class="container-es">
        <div class="text-center max-w-2xl mx-auto es-reveal">
            <span class="es-eyebrow">Popular Pages</span>
            <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">Where Would You Like to Go?</h2>
        </div>
        <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6 mt-10">
            <a href="rate-card.html" class="es-panel es-panel--hover es-reveal block"><span class="es-card__icon"><i class="fa-solid fa-tags"></i></span><h3 class="es-card__title mt-3">Scrap Rates</h3><p class="es-card__text text-sm mt-1">Live rates for paper, metal, plastic and more.</p></a>
            <a href="services.html" class="es-panel es-panel--hover es-reveal block" data-reveal-delay="60"><span class="es-card__icon"><i class="fa-solid fa-truck-pickup"></i></span><h3 class="es-card__title mt-3">Services</h3><p class="es-card__text text-sm mt-1">Household, corporate and society programmes.</p></a>
            <a href="customer-dashboard.html" class="es-panel es-panel--hover es-reveal block" data-reveal-delay="120"><span class="es-card__icon"><i class="fa-solid fa-gauge-high"></i></span><h3 class="es-card__title mt-3">My Dashboard</h3><p class="es-card__text text-sm mt-1">Book pickups and track your payouts.</p></a>
        </div>
    </div>
</section>

<!-- 3 · How it works recap -->
<section data-section="3" class="section bg-lightBg dark:bg-[#0d1726]">
    <div class="container-es grid sm:grid-cols-4 gap-6">
        <div class="es-card es-reveal"><div class="es-card__body items-center text-center"><span class="es-step__num mx-auto">1</span><h3 class="es-card__title mt-4">Select scrap</h3></div></div>
        <div class="es-card es-reveal" data-reveal-delay="60"><div class="es-card__body items-center text-center"><span class="es-step__num mx-auto">2</span><h3 class="es-card__title mt-4">Book slot</h3></div></div>
        <div class="es-card es-reveal" data-reveal-delay="120"><div class="es-card__body items-center text-center"><span class="es-step__num mx-auto">3</span><h3 class="es-card__title mt-4">Weigh &amp; verify</h3></div></div>
        <div class="es-card es-reveal" data-reveal-delay="180"><div class="es-card__body items-center text-center"><span class="es-step__num mx-auto">4</span><h3 class="es-card__title mt-4">Get paid</h3></div></div>
    </div>
</section>

<!-- 4 · Categories -->
<section data-section="4" class="section bg-white dark:bg-gray-900">
    <div class="container-es">
        <h2 class="es-title text-2xl md:text-3xl mb-8 es-reveal">Materials We Collect</h2>
        <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-7" data-render="categories"></div>
    </div>
</section>

<!-- 5 · Locations -->
<section data-section="5" class="section bg-lightBg dark:bg-[#0d1726]">
    <div class="container-es">
        <h2 class="es-title text-2xl md:text-3xl mb-8 es-reveal">Serving Six Metros</h2>
        <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-7" data-render="locations"></div>
    </div>
</section>
""" + cta_footer("Found What You Needed?", "If you're looking for a pickup, we're ready — book it in minutes.", primary=("<i class=\"fa-solid fa-calendar-check\"></i> Schedule Pickup", "customer-dashboard.html"), secondary=("Browse Blog", "blog.html"))


def main():
    public_page("about.html", "About EcoScrap | Mission, Team & Responsible Recycling", "EcoScrap's story — a doorstep scrap pickup network built on transparent weighing, fair rates and certified recycling across six Indian metros.", about_main(), active="About")
    public_page("services.html", "Scrap Collection Services | Household, Corporate & Society", "EcoScrap's scrap collection services: household pickups, corporate clearouts, society drives, e-waste handling and bulk commercial collection.", services_main(), active="Services")
    public_page("rate-card.html", "Live Scrap Rates | Paper, Metal, Plastic, E-Waste", "Searchable scrap rate card with daily indicative prices for paper, metal, plastic, e-waste, appliances and batteries across all EcoScrap metros.", rate_card_main(), active="Rate Card")
    public_page("how-it-works.html", "How EcoScrap Works | Steps, Weighing & Payment", "The four-step EcoScrap process: select scrap, book a slot, weigh and verify, receive payment — with live status tracking and full FAQ.", how_main(), active="How It Works")
    public_page("blog.html", "EcoScrap Blog | Scrap Rates, Recycling Tips & Stories", "Articles on scrap market rates, e-waste rules, home recycling hacks and India's circular economy — from the EcoScrap team.", blog_main(), active="Blog")
    public_page("blog-details.html", "EcoScrap Blog Article | Insights & Guides", "Deep-dive guide on scrap prices, e-waste rules, battery safety and recycling habits — with author notes and related reads.", blog_details_main(), active="Blog")
    public_page("contact.html", "Contact EcoScrap | Support, Quotes & Partnerships", "Reach EcoScrap by phone, WhatsApp, email or form. Corporate quotes and society drives answered within one business day.", contact_main(), active="Contact")
    public_page("locations.html", "Service Locations | EcoScrap Doorstep Coverage", "EcoScrap's live service areas across Delhi NCR, Mumbai, Bangalore, Pune, Hyderabad and Chennai — search coverage and book a slot.", locations_main(), active="Locations")
    public_page("privacy-policy.html", "Privacy Policy | EcoScrap", "How EcoScrap collects, uses, shares and protects personal data, and the rights you hold under transparency commitments.", privacy_main(), active="Privacy Policy")
    public_page("terms.html", "Terms & Conditions | EcoScrap", "Terms governing EcoScrap pickups, weighing, payments, user duties and liability limits for this demonstration platform.", terms_main(), active="Terms")
    public_page("404.html", "Page Not Found | EcoScrap", "The page you requested couldn't be found — explore popular EcoScrap pages instead.", notfound_main(), active="")


if __name__ == "__main__":
    main()