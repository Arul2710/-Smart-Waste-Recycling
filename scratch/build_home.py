"""
EcoScrap — index.html (Home 1) and home2.html (Home 2).

Both pages use exactly six <section> content blocks.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_base import public_page  # noqa: E402

H = "assets/images/"


def hero_common(eyebrow, title, sub, media, overlay="hero__overlay--dark", align="start"):
    align_cls = {"start": "text-start items-start", "center": "text-center items-center mx-auto"}
    return """
<section class="hero %s">
    <div class="hero__media" style="background-image:url('%s')" role="img" aria-label="Doorstep scrap pickup and recycling"></div>
    <div class="hero__overlay %s"></div>
    <div class="container-es relative z-10 py-20 lg:py-28 %s">
        <span class="es-eyebrow es-reveal">%s</span>
        <h1 class="text-4xl sm:text-5xl lg:text-6xl font-extrabold text-white leading-tight mt-5 es-reveal" data-reveal-delay="80">%s</h1>
        <p class="mt-6 text-lg text-gray-200/95 max-w-2xl es-reveal" data-reveal-delay="160">%s</p>
""" % (align_cls.get(align, "text-start items-start"), H + media, overlay, align_cls.get(align, "text-start items-start"), eyebrow, title, sub)


def cta_string(sections):
    caps = []
    for s in sections:
        caps.append(s[:1].upper() + s[1:])
    return caps


INDEX_HERO_TITLE = 'Turn Your Scrap Into Cash. <span class="text-primaryLight">We Pick It Up!</span>'
INDEX_HERO_SUB = (
    "Book a doorstep scrap pickup in under two minutes. Natural gas-free weighing on calibrated scales, "
    "transparent live rates and instant payment — while your recyclables head to certified facilities."
)

RATE_PREVIEW_ROWS = [
    ("Newspaper (White)", "Paper", "Kg", 14),
    ("Corrugated Cardboard", "Paper", "Kg", 16),
    ("Iron Scrap (Clean)", "Metal", "Kg", 28),
    ("Copper Scrap", "Metal", "Kg", 385),
    ("PET Bottles (Clear)", "Plastic", "Kg", 15),
    ("Laptop E-Waste", "E-Waste", "Kg", 45),
]


def rate_preview_table():
    rows = "".join(
        "<tr>"
        "<td class='font-medium text-gray-900 dark:text-gray-100'>%s</td>"
        "<td class='text-gray-500 dark:text-gray-400'>%s</td>"
        "<td class='text-gray-500 dark:text-gray-400'>per %s</td>"
        "<td class='text-end font-bold text-primary dark:text-primaryLight whitespace-nowrap'>₹ %s</td>"
        "</tr>" % (m, c, u, f"{p:,}")
        for m, c, u, p in RATE_PREVIEW_ROWS
    )
    return """<div class="es-card es-reveal overflow-hidden">
<table class="es-table">
    <thead><tr><th>Material</th><th>Category</th><th>Unit</th><th class="!text-right">Price</th></tr></thead>
    <tbody>%s</tbody>
</table>
<div class="px-5 py-4 text-xs text-gray-500 dark:text-gray-400 bg-gray-50 dark:bg-[#182130] rounded-b-2xl">
    <i class="fa-solid fa-circle-info me-1.5 text-primary"></i>
    Indicative rates. Actual payout depends on material quality, moisture and verified weight at pickup.
</div>
</div>""" % rows


def index_main():
    return r"""
<!-- 1 · Hero -->
<section data-section="1" class="hero">
    <div class="hero__media" style="background-image:url('assets/images/hero-pickup.jpg')" role="img" aria-label="Recycling collection vehicle on a doorstep scrap pickup"></div>
    <div class="hero__overlay hero__overlay--dark"></div>
    <div class="container-es relative z-10 py-24 lg:py-32">
        <div class="max-w-3xl">
            <span class="es-eyebrow es-reveal"><i class="fa-solid fa-hand-holding-dollar"></i> Doorstep Scrap Pickup Service</span>
            <h1 class="text-4xl sm:text-5xl lg:text-6xl font-extrabold text-white leading-[1.08] mt-5 es-reveal" data-reveal-delay="80">Turn Your Scrap Into Cash. <span class="text-primaryLight">We Pick It Up!</span></h1>
            <p class="mt-6 text-lg text-gray-200/95 max-w-2xl es-reveal" data-reveal-delay="160">Book a doorstep scrap pickup in under two minutes. Calibrated weighing on the spot, transparent live rates and instant UPI payment — while your recyclables head to certified facilities.</p>
            <div class="mt-8 flex flex-col sm:flex-row gap-3 es-reveal" data-reveal-delay="240">
                <a href="customer-dashboard.html" class="es-btn es-btn--primary es-btn--lg"><i class="fa-solid fa-truck-pickup"></i> Schedule a Pickup</a>
                <a href="rate-card.html" class="es-btn es-btn--glass es-btn--lg"><i class="fa-solid fa-tags"></i> View Scrap Rates</a>
            </div>
            <form id="hero-location-form" class="es-search es-reveal mt-9" data-reveal-delay="320" novalidate>
                <i class="fa-solid fa-location-dot text-primaryLight flex-none"></i>
                <input type="text" id="hero-location" name="location" placeholder="Enter pickup location — city, area or PIN code" autocomplete="off" aria-label="Pickup location">
                <button type="submit" class="es-btn es-btn--primary es-btn--sm flex-none"><i class="fa-solid fa-magnifying-glass"></i> Search Service</button>
            </form>
            <p id="hero-location-result" class="hidden mt-4 text-sm text-white/95 es-reveal gap-2 items-start"></p>
            <ul class="mt-9 flex flex-wrap gap-x-6 gap-y-2 text-sm text-gray-300 es-reveal" data-reveal-delay="400">
                <li class="flex items-center gap-2"><i class="fa-solid fa-circle-check text-primaryLight"></i> No minimum quantity</li>
                <li class="flex items-center gap-2"><i class="fa-solid fa-circle-check text-primaryLight"></i> Payment on the spot</li>
                <li class="flex items-center gap-2"><i class="fa-solid fa-circle-check text-primaryLight"></i> Certified recyclers</li>
            </ul>
        </div>
    </div>
</section>

<!-- 2 · About -->
<section data-section="2" class="section bg-white dark:bg-gray-900">
    <div class="container-es grid lg:grid-cols-2 gap-12 lg:gap-16 items-center">
        <div class="relative es-reveal">
            <div class="es-card__media rounded-3xl aspect-[4/3] overflow-hidden">
                <img src="assets/images/hero-recycle.jpg" alt="Recyclable materials being sorted at an EcoScrap processing facility" loading="lazy" width="1600" height="900" class="w-full h-full object-cover">
            </div>
            <div class="absolute -bottom-6 -right-4 sm:-right-6 bg-primary text-white rounded-2xl shadow-2xl px-6 py-5 hidden sm:block">
                <p class="text-3xl font-extrabold">5M+</p>
                <p class="text-xs text-gray-100">KG diverted from landfill</p>
            </div>
        </div>
        <div>
            <span class="es-eyebrow es-reveal">Why EcoScrap</span>
            <h2 class="es-title mt-4 text-3xl md:text-4xl es-reveal" data-reveal-delay="60">Responsible Recycling, Delivered to Your Door</h2>
            <p class="es-subtitle text-lg mt-5 es-reveal" data-reveal-delay="120">EcoScrap brings professional scrap collection to your doorstep. No more hauling heavy bags, haggling at local shops or wondering if the scale was fair. We publish our rates, verify every kilogram in front of you, and pay instantly.</p>
            <ul class="mt-7 grid sm:grid-cols-2 gap-4 es-reveal" data-reveal-delay="180">
                <li class="flex items-start gap-3"><span class="es-card__icon"><i class="fa-solid fa-scale-balanced"></i></span><span><strong class="block text-gray-900 dark:text-white">Transparent Pricing</strong><span class="text-sm text-gray-500 dark:text-gray-400">Rates published, weights verified.</span></span></li>
                <li class="flex items-start gap-3"><span class="es-card__icon"><i class="fa-solid fa-house-circle-check"></i></span><span><strong class="block text-gray-900 dark:text-white">Doorstep Pickup</strong><span class="text-sm text-gray-500 dark:text-gray-400">We come to you, on schedule.</span></span></li>
                <li class="flex items-start gap-3"><span class="es-card__icon"><i class="fa-solid fa-money-bill-transfer"></i></span><span><strong class="block text-gray-900 dark:text-white">Instant Payment</strong><span class="text-sm text-gray-500 dark:text-gray-400">UPI, bank transfer or cash.</span></span></li>
                <li class="flex items-start gap-3"><span class="es-card__icon"><i class="fa-solid fa-earth-asia"></i></span><span><strong class="block text-gray-900 dark:text-white">Responsible Recycling</strong><span class="text-sm text-gray-500 dark:text-gray-400">Certified disposal, audited chain.</span></span></li>
            </ul>
            <div class="mt-8 es-reveal" data-reveal-delay="240">
                <a href="about.html" class="es-btn es-btn--dark">Learn More <i class="fa-solid fa-arrow-right rtl-flip"></i></a>
            </div>
        </div>
    </div>
</section>

<!-- 3 · Scrap Categories -->
<section data-section="3" class="section bg-lightBg dark:bg-[#0d1726]">
    <div class="container-es">
        <div class="text-center max-w-2xl mx-auto">
            <span class="es-eyebrow es-reveal">What We Collect</span>
            <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">Scrap Categories We Pick Up</h2>
            <p class="es-subtitle mt-4 es-reveal" data-reveal-delay="120">Six well-sorted categories covered by trained collectors and certified recyclers. Rates update daily on the live rate card.</p>
        </div>
        <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-7 mt-12" data-render="categories"></div>
        <div class="text-center mt-10 es-reveal">
            <a href="rate-card.html" class="es-btn es-btn--ghost es-btn--lg">View the Full Rate Card <i class="fa-solid fa-arrow-right rtl-flip"></i></a>
        </div>
    </div>
</section>

<!-- 4 · How It Works -->
<section data-section="4" class="section bg-white dark:bg-gray-900">
    <div class="container-es">
        <div class="text-center max-w-2xl mx-auto">
            <span class="es-eyebrow es-reveal">Simple Process</span>
            <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">From Clutter to Cash in Four Steps</h2>
            <p class="es-subtitle mt-4 es-reveal" data-reveal-delay="120">A transparent journey you can follow live from your dashboard at every stage.</p>
        </div>
        <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-10 lg:gap-6 mt-14">
            <div class="es-reveal relative" data-reveal-delay="0">
                <span class="es-step__line hidden lg:block"></span>
                <div class="text-center">
                    <div class="es-step__num mx-auto">1</div>
                    <h3 class="font-bold text-lg mt-4 text-gray-900 dark:text-white">Select Your Scrap</h3>
                    <p class="text-sm text-gray-500 dark:text-gray-400 mt-2">Choose material categories and an estimated weight range.</p>
                </div>
            </div>
            <div class="es-reveal relative" data-reveal-delay="80">
                <span class="es-step__line hidden lg:block"></span>
                <div class="text-center">
                    <div class="es-step__num mx-auto">2</div>
                    <h3 class="font-bold text-lg mt-4 text-gray-900 dark:text-white">Schedule a Pickup</h3>
                    <p class="text-sm text-gray-500 dark:text-gray-400 mt-2">Pick a convenient slot — morning, afternoon or evening.</p>
                </div>
            </div>
            <div class="es-reveal relative" data-reveal-delay="160">
                <span class="es-step__line hidden lg:block"></span>
                <div class="text-center">
                    <div class="es-step__num mx-auto">3</div>
                    <h3 class="font-bold text-lg mt-4 text-gray-900 dark:text-white">Weigh &amp; Verify</h3>
                    <p class="text-sm text-gray-500 dark:text-gray-400 mt-2">Calibrated digital scale, weight confirmed in front of you.</p>
                </div>
            </div>
            <div class="es-reveal relative" data-reveal-delay="240">
                <div class="text-center">
                    <div class="es-step__num mx-auto">4</div>
                    <h3 class="font-bold text-lg mt-4 text-gray-900 dark:text-white">Receive Your Payment</h3>
                    <p class="text-sm text-gray-500 dark:text-gray-400 mt-2">Instant payout via UPI, bank transfer or cash on the spot.</p>
                </div>
            </div>
        </div>
        <div class="text-center mt-12 es-reveal">
            <a href="how-it-works.html" class="es-btn es-btn--ghost es-btn--lg">See the Detailed Process <i class="fa-solid fa-arrow-right rtl-flip"></i></a>
        </div>
    </div>
</section>

<!-- 5 · Rate Card Preview -->
<section data-section="5" class="section bg-lightBg dark:bg-[#0d1726]">
    <div class="container-es grid lg:grid-cols-5 gap-10 items-center">
        <div class="lg:col-span-2">
            <span class="es-eyebrow es-reveal">Live Rates</span>
            <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">Sample Scrap Rates</h2>
            <p class="es-subtitle mt-4 es-reveal" data-reveal-delay="120">A snapshot of today's indicative rates. Metals track exchange markets, paper and plastic adjust weekly — the full card lets you filter by category and search any item.</p>
            <ul class="mt-6 space-y-3 text-sm text-gray-600 dark:text-gray-300 es-reveal" data-reveal-delay="180">
                <li class="flex items-center gap-3"><i class="fa-solid fa-check-circle text-primary"></i> Rates quoted per verified kilogram</li>
                <li class="flex items-center gap-3"><i class="fa-solid fa-check-circle text-primary"></i> No hidden collection or transport fees</li>
                <li class="flex items-center gap-3"><i class="fa-solid fa-check-circle text-primary"></i> Payout matched to the published rate</li>
            </ul>
            <div class="mt-8 es-reveal" data-reveal-delay="240">
                <a href="rate-card.html" class="es-btn es-btn--primary es-btn--lg">View Full Rate Card <i class="fa-solid fa-arrow-right rtl-flip"></i></a>
            </div>
        </div>
        <div class="lg:col-span-3 es-reveal" data-reveal-delay="120">
            {RATE_TABLE}
        </div>
    </div>
</section>

<!-- 6 · Locations & Final CTA -->
<section data-section="6" id="locations" class="section bg-white dark:bg-gray-900">
    <div class="container-es">
        <div class="text-center max-w-2xl mx-auto">
            <span class="es-eyebrow es-reveal">Where We Operate</span>
            <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">Service Locations</h2>
            <p class="es-subtitle mt-4 es-reveal" data-reveal-delay="120">Live in six metro regions. Search your area or city to confirm doorstep availability and the pickup slots nearest you.</p>
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
        <p id="locations-empty" class="es-empty hidden">No locations match that search. Try a city name like "Mumbai".</p>
        <p data-location-summary class="hidden mt-6 text-center text-sm font-medium text-primary bg-primary/10 border border-primary/20 rounded-full px-5 py-3 max-w-md mx-auto"></p>

        <div class="relative overflow-hidden rounded-3xl bg-primaryDark mt-16 es-reveal">
            <div class="absolute inset-0 opacity-15 hero__media" style="background-image:url('assets/images/green.jpg')"></div>
            <div class="relative z-10 px-6 sm:px-12 py-14 sm:py-16 text-center text-white">
                <h2 class="text-3xl sm:text-4xl font-extrabold text-white">Ready to Clear Your Scrap?</h2>
                <p class="mt-4 text-gray-200 max-w-xl mx-auto">Book a pickup today. Our collectors reach your doorstep within your chosen slot and you leave with cash in hand — and a cleaner home.</p>
                <div class="mt-8 flex flex-col sm:flex-row justify-center gap-3">
                    <a href="customer-dashboard.html" class="es-btn es-btn--primary es-btn--lg"><i class="fa-solid fa-calendar-check"></i> Schedule Pickup</a>
                    <a href="contact.html" class="es-btn es-btn--white es-btn--lg">Contact Us <i class="fa-solid fa-arrow-right rtl-flip"></i></a>
                </div>
            </div>
        </div>
    </div>
</section>
""".replace("{RATE_TABLE}", rate_preview_table())


def home2_main():
    return r"""
<!-- 1 · Hero (recycling background) -->
<section data-section="1" class="hero text-center">
    <div class="hero__media" style="background-image:url('assets/images/hero-recycle.jpg')" role="img" aria-label="Material recovery facility recycling conveyor"></div>
    <div class="hero__overlay hero__overlay--green"></div>
    <div class="container-es relative z-10 py-24 lg:py-32">
        <span class="es-eyebrow es-reveal"><i class="fa-solid fa-leaf"></i> Smart Waste, Better Planet</span>
        <h1 class="mt-5 text-4xl sm:text-5xl lg:text-6xl font-extrabold text-white leading-tight es-reveal" data-reveal-delay="80">Every Kilogram Recycled <span class="text-primaryLight">Counts Twice</span></h1>
        <p class="mx-auto mt-6 text-lg text-gray-200/95 max-w-2xl es-reveal" data-reveal-delay="160">Earn the best value for your paper, metal, plastic and e-waste while keeping thousands of tonnes out of landfill each year — all from the comfort of your home.</p>
        <div class="mt-8 flex flex-col sm:flex-row justify-center gap-3 es-reveal" data-reveal-delay="240">
            <a href="customer-dashboard.html" class="es-btn es-btn--primary es-btn--lg"><i class="fa-solid fa-truck-fast"></i> Book a Pickup Now</a>
            <a href="how-it-works.html" class="es-btn es-btn--glass es-btn--lg">How It Works <i class="fa-solid fa-arrow-right rtl-flip"></i></a>
        </div>
        <div class="mt-14 grid grid-cols-3 gap-4 max-w-2xl mx-auto es-reveal" data-reveal-delay="320">
            <div class="bg-white/10 border border-white/15 rounded-2xl px-4 py-5 backdrop-blur-sm">
                <p class="text-2xl sm:text-3xl font-extrabold text-white"><span data-count-to="5200000" data-count-suffix=" KG+">5.2M KG+</span></p>
                <p class="text-xs text-gray-300 mt-1">Recycled to date</p>
            </div>
            <div class="bg-white/10 border border-white/15 rounded-2xl px-4 py-5 backdrop-blur-sm">
                <p class="text-2xl sm:text-3xl font-extrabold text-white"><span data-count-to="84000" data-count-suffix="+">84,000+</span></p>
                <p class="text-xs text-gray-300 mt-1">Tree-equivalents saved</p>
            </div>
            <div class="bg-white/10 border border-white/15 rounded-2xl px-4 py-5 backdrop-blur-sm">
                <p class="text-2xl sm:text-3xl font-extrabold text-white"><span data-count-to="42000" data-count-suffix="+">42,000+</span></p>
                <p class="text-xs text-gray-300 mt-1">Happy households</p>
            </div>
        </div>
    </div>
</section>

<!-- 2 · Scrap collection services -->
<section data-section="2" class="section bg-lightBg dark:bg-[#0d1726]">
    <div class="container-es">
        <div class="text-center max-w-2xl mx-auto">
            <span class="es-eyebrow es-reveal">Our Services</span>
            <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">Scrap Collection, Sized to You</h2>
            <p class="es-subtitle mt-4 es-reveal" data-reveal-delay="120">Three collection programmes built around how much scrap you have and where you're producing it.</p>
        </div>
        <div class="grid md:grid-cols-3 gap-7 mt-12">
            <article class="es-card es-card--hover es-reveal">
                <div class="es-card__body">
                    <div class="flex items-start justify-between">
                        <span class="es-card__icon"><i class="fa-solid fa-house-chimney"></i></span>
                        <span class="es-badge es-badge--green">Most popular</span>
                    </div>
                    <h3 class="es-card__title">Household Pickup</h3>
                    <p class="es-card__text">Weekly or one-off doorstep collection for apartments, houses and flats. No minimum quantity — one box or a full balcony works.</p>
                    <ul class="text-sm text-gray-600 dark:text-gray-400 space-y-1.5">
                        <li><i class="fa-solid fa-check text-primary me-2"></i>Same-day slot options</li>
                        <li><i class="fa-solid fa-check text-primary me-2"></i>UPI or cash on the spot</li>
                        <li><i class="fa-solid fa-check text-primary me-2"></i>Proof of disposal for e-waste</li>
                    </ul>
                    <div class="es-card__foot"><a href="services.html" class="es-btn es-btn--primary es-btn--sm es-btn--block">Book Household Pickup</a></div>
                </div>
            </article>
            <article class="es-card es-card--hover es-reveal" data-reveal-delay="80">
                <div class="es-card__body">
                    <div class="flex items-start justify-between">
                        <span class="es-card__icon"><i class="fa-solid fa-building"></i></span>
                        <span class="es-badge es-badge--blue">Business</span>
                    </div>
                    <h3 class="es-card__title">Corporate Clearouts</h3>
                    <p class="es-card__text">One-time and recurring clearance for offices and retail — cardboard, e-waste, IT assets and old equipment with full documentation.</p>
                    <ul class="text-sm text-gray-600 dark:text-gray-400 space-y-1.5">
                        <li><i class="fa-solid fa-check text-primary me-2"></i>GST invoice with every job</li>
                        <li><i class="fa-solid fa-check text-primary me-2"></i>Data-wiped IT asset pickup</li>
                        <li><i class="fa-solid fa-check text-primary me-2"></i>Deferred scheduling on request</li>
                    </ul>
                    <div class="es-card__foot"><a href="services.html#corporate" class="es-btn es-btn--primary es-btn--sm es-btn--block">Book Corporate Clearout</a></div>
                </div>
            </article>
            <article class="es-card es-card--hover es-reveal" data-reveal-delay="160">
                <div class="es-card__body">
                    <div class="flex items-start justify-between">
                        <span class="es-card__icon"><i class="fa-solid fa-people-group"></i></span>
                        <span class="es-badge es-badge--amber">Community</span>
                    </div>
                    <h3 class="es-card__title">Society Scrap Drives</h3>
                    <p class="es-card__text">Apartment societies and RWAs host a scheduled drive — we set up a weighing station, collect from every flat and split earnings instantly.</p>
                    <ul class="text-sm text-gray-600 dark:text-gray-400 space-y-1.5">
                        <li><i class="fa-solid fa-check text-primary me-2"></i>Per-flat payout reports</li>
                        <li><i class="fa-solid fa-check text-primary me-2"></i>Certificates for green drives</li>
                        <li><i class="fa-solid fa-check text-primary me-2"></i>Zero upfront cost to society</li>
                    </ul>
                    <div class="es-card__foot"><a href="services.html#society" class="es-btn es-btn--primary es-btn--sm es-btn--block">Organise a Drive</a></div>
                </div>
            </article>
        </div>
    </div>
</section>

<!-- 3 · Recyclable material categories -->
<section data-section="3" class="section bg-white dark:bg-gray-900">
    <div class="container-es">
        <div class="text-center max-w-2xl mx-auto">
            <span class="es-eyebrow es-reveal">Recyclables</span>
            <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">What We Recycle</h2>
            <p class="es-subtitle mt-4 es-reveal" data-reveal-delay="120">Six material streams, sorted and dispatched to the right facility within 48 hours.</p>
        </div>
        <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-7 mt-12" data-render="categories"></div>
    </div>
</section>

<!-- 4 · How It Works -->
<section data-section="4" class="section bg-lightBg dark:bg-[#0d1726]">
    <div class="container-es">
        <div class="grid lg:grid-cols-2 gap-12 items-center">
            <div>
                <span class="es-eyebrow es-reveal">Four Steps</span>
                <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">From Booking to Bank Credit in One Visit</h2>
                <p class="es-subtitle mt-4 es-reveal" data-reveal-delay="120">No back-and-forth with dealers, no guesswork on weights. Follow the live status from your dashboard and get paid within minutes of weighing.</p>
                <div class="mt-9 space-y-6 es-reveal" data-reveal-delay="180">
                    <div class="flex gap-4">
                        <span class="es-step__num !h-12 !w-12 !text-base">1</span>
                        <div><h3 class="font-bold text-gray-900 dark:text-white">Select scrap &amp; book a slot</h3><p class="text-sm text-gray-500 dark:text-gray-400 mt-1">Choose categories and an arrival window that suits you.</p></div>
                    </div>
                    <div class="flex gap-4">
                        <span class="es-step__num !h-12 !w-12 !text-base">2</span>
                        <div><h3 class="font-bold text-gray-900 dark:text-white">Collector reaches your door</h3><p class="text-sm text-gray-500 dark:text-gray-400 mt-1">Get a live ETA with the collector's route on your dashboard.</p></div>
                    </div>
                    <div class="flex gap-4">
                        <span class="es-step__num !h-12 !w-12 !text-base">3</span>
                        <div><h3 class="font-bold text-gray-900 dark:text-white">Weigh &amp; verify materials</h3><p class="text-sm text-gray-500 dark:text-gray-400 mt-1">Certified digital scale, weight confirmed beside the vehicle.</p></div>
                    </div>
                    <div class="flex gap-4">
                        <span class="es-step__num !h-12 !w-12 !text-base">4</span>
                        <div><h3 class="font-bold text-gray-900 dark:text-white">Get paid instantly</h3><p class="text-sm text-gray-500 dark:text-gray-400 mt-1">UPI settles in seconds; bank transfer the same working day.</p></div>
                    </div>
                </div>
            </div>
            <div class="relative es-reveal" data-reveal-delay="120">
                <div class="es-card__media rounded-3xl aspect-[4/3] overflow-hidden">
                    <img src="assets/images/scale.jpg" alt="EcoScrap collector using a calibrated digital weighing scale at a doorstep pickup" loading="lazy" width="1600" height="900">
                </div>
                <div class="absolute -bottom-6 -left-4 bg-white dark:bg-gray-800 rounded-2xl shadow-2xl px-5 py-4 flex items-center gap-4 border border-gray-100 dark:border-gray-700">
                    <span class="es-card__icon"><i class="fa-solid fa-video"></i></span>
                    <div><p class="font-bold text-gray-900 dark:text-white text-sm">Live status tracking</p><p class="text-xs text-gray-500 dark:text-gray-400">Request → Route → Verify → Paid</p></div>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- 5 · Environmental impact + testimonials -->
<section data-section="5" class="section bg-white dark:bg-gray-900">
    <div class="container-es">
        <div class="text-center max-w-2xl mx-auto">
            <span class="es-eyebrow es-reveal">Impact &amp; Trust</span>
            <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">The Real-World Difference</h2>
            <p class="es-subtitle mt-4 es-reveal" data-reveal-delay="120">Numbers you can measure, and stories you can trust — from the households that recycle with us.</p>
        </div>
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-5 mt-12">
            <div class="es-stat es-reveal"><span class="es-stat__icon bg-green-100 text-primary"><i class="fa-solid fa-weight-scale"></i></span><div><p class="es-stat__value" data-count-to="5.2" data-count-decimals="1" data-count-suffix="M">5.2M</p><p class="es-stat__label">KG recycled</p></div></div>
            <div class="es-stat es-reveal" data-reveal-delay="60"><span class="es-stat__icon bg-blue-100 text-blue-600"><i class="fa-solid fa-tree-city"></i></span><div><p class="es-stat__value" data-count-to="84" data-count-suffix="K">84K</p><p class="es-stat__label">Trees saved</p></div></div>
            <div class="es-stat es-reveal" data-reveal-delay="120"><span class="es-stat__icon bg-amber-100 text-amber-600"><i class="fa-solid fa-bolt"></i></span><div><p class="es-stat__value" data-count-to="3.1" data-count-decimals="1" data-count-suffix="M">3.1M</p><p class="es-stat__label">KWH energy saved</p></div></div>
            <div class="es-stat es-reveal" data-reveal-delay="180"><span class="es-stat__icon bg-violet-100 text-violet-600"><i class="fa-solid fa-car"></i></span><div><p class="es-stat__value" data-count-to="1.6" data-count-decimals="1" data-count-suffix="M">1.6M</p><p class="es-stat__label">KM of trips avoided</p></div></div>
        </div>

        <div class="mt-16 grid lg:grid-cols-2 gap-10 items-center">
            <div>
                <span class="es-eyebrow es-reveal">Testimonials</span>
                <h3 class="es-title mt-4 text-2xl md:text-3xl es-reveal" data-reveal-delay="60">What Customers Say</h3>
                <div class="relative mt-8 es-reveal" data-reveal-delay="120" data-slider>
                    <div class="overflow-hidden rounded-2xl">
                        <div class="es-slider__track" data-slider-track>
                            {TESTIMONIAL_SLIDES}
                        </div>
                    </div>
                    <div class="flex items-center justify-between mt-6">
                        <div class="flex gap-2" data-slider-dots></div>
                        <div class="flex gap-2">
                            <button type="button" class="es-iconbtn" data-slider-prev aria-label="Previous testimonial"><i class="fa-solid fa-arrow-left"></i></button>
                            <button type="button" class="es-iconbtn" data-slider-next aria-label="Next testimonial"><i class="fa-solid fa-arrow-right"></i></button>
                        </div>
                    </div>
                </div>
            </div>
            <div class="grid sm:grid-cols-2 gap-6">
                <div class="es-panel es-panel--hover es-reveal text-center"><span class="es-pin mx-auto mb-3"><i class="fa-solid fa-medal text-xl"></i></span><h4 class="font-bold text-gray-900 dark:text-white">Certified Recyclers</h4><p class="text-sm text-gray-500 dark:text-gray-400 mt-2">Every stream moves through a audited, licensed facility.</p></div>
                <div class="es-panel es-panel--hover es-reveal text-center" data-reveal-delay="60"><span class="es-pin mx-auto mb-3"><i class="fa-solid fa-shield-halved text-xl"></i></span><h4 class="font-bold text-gray-900 dark:text-white">Verified Weighing</h4><p class="text-sm text-gray-500 dark:text-gray-400 mt-2">Calibrated scales with weight shown before payment.</p></div>
                <div class="es-panel es-panel--hover es-reveal text-center" data-reveal-delay="120"><span class="es-pin mx-auto mb-3"><i class="fa-solid fa-handshake-angle text-xl"></i></span><h4 class="font-bold text-gray-900 dark:text-white">Fair Rates</h4><p class="text-sm text-gray-500 dark:text-gray-400 mt-2">Published live without hidden deductions.</p></div>
                <div class="es-panel es-panel--hover es-reveal text-center" data-reveal-delay="180"><span class="es-pin mx-auto mb-3"><i class="fa-solid fa-headset text-xl"></i></span><h4 class="font-bold text-gray-900 dark:text-white">Local Support</h4><p class="text-sm text-gray-500 dark:text-gray-400 mt-2">WhatsApp and call support, 7 days a week.</p></div>
            </div>
        </div>
    </div>
</section>

<!-- 6 · Service locations + final CTA -->
<section data-section="6" id="locations" class="section bg-lightBg dark:bg-[#0d1726]">
    <div class="container-es">
        <div class="text-center max-w-2xl mx-auto">
            <span class="es-eyebrow es-reveal">Coverage</span>
            <h2 class="es-title mt-4 es-reveal" data-reveal-delay="60">Service Locations</h2>
            <p class="es-subtitle mt-4 es-reveal" data-reveal-delay="120">Expanding city by city. Check your neighbourhood below and select it to reserve a pickup slot.</p>
        </div>
        <div class="flex flex-col md:flex-row gap-3 justify-center mt-10 es-reveal" data-reveal-delay="120">
            <div class="relative flex-1 max-w-md">
                <i class="fa-solid fa-magnifying-glass absolute inset-y-0 left-4 flex items-center text-gray-400"></i>
                <input data-location-search type="search" placeholder="Find your area or city…" class="es-input !ps-11" aria-label="Search locations">
            </div>
            <select data-location-coverage class="es-select md:w-56" aria-label="Filter by coverage">
                <option value="All">All coverage</option>
                <option value="Full Coverage">Full coverage</option>
                <option value="Selected Zones">Selected zones</option>
                <option value="Partial Coverage">Partial coverage</option>
            </select>
        </div>
        <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-7 mt-8" data-render="locations"></div>
        <p id="locations-empty" class="es-empty hidden">No matching service area — check back soon, we launch new metros monthly.</p>
        <div class="relative overflow-hidden rounded-3xl bg-primaryDark mt-16 es-reveal text-center">
            <div class="absolute inset-0 opacity-15 hero__media" style="background-image:url('assets/images/sustain-city.jpg')"></div>
            <div class="relative z-10 px-6 sm:px-12 py-14 sm:py-16 text-white">
                <h2 class="text-3xl sm:text-4xl font-extrabold text-white">Join the Recycling Movement</h2>
                <p class="mt-4 text-gray-200 max-w-xl mx-auto">Create a free account, schedule your first doorstep pickup and watch your scrap become societal value — cash for you, materials for the economy.</p>
                <div class="mt-8 flex flex-col sm:flex-row justify-center gap-3">
                    <a href="signup.html" class="es-btn es-btn--primary es-btn--lg">Create Free Account</a>
                    <a href="customer-dashboard.html" class="es-btn es-btn--white es-btn--lg"><i class="fa-solid fa-calendar-check"></i> Schedule Pickup</a>
                </div>
            </div>
        </div>
    </div>
</section>
""".replace(
        "{TESTIMONIAL_SLIDES}",
        """"
<div class="px-1" data-slider-slide>
    <div class="es-panel"><div class="flex gap-1 text-amber-400 mb-4"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i></div>
    <p class="text-gray-600 dark:text-gray-300 leading-relaxed">“I booked a pickup on a Sunday morning and the collector reached my gate within 40 minutes. Weighing was done on a calibrated scale in front of me and the payment hit my UPI immediately.”</p>
    <div class="flex items-center gap-3 mt-5"><div class="w-10 h-10 rounded-full bg-primary text-white flex items-center justify-center font-bold">RM</div><div><p class="font-bold text-gray-900 dark:text-white">Rohit Mehra</p><p class="text-xs text-gray-500 dark:text-gray-400">Flat owner, Whitefield</p></div></div></div>
</div>
<div class="px-1" data-slider-slide>
    <div class="es-panel"><div class="flex gap-1 text-amber-400 mb-4"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i></div>
    <p class="text-gray-600 dark:text-gray-300 leading-relaxed">“We ran a society-wide scrap drive with EcoScrap. Around 380 kg was collected in a single morning and the payout summary was in our hands the same day.”</p>
    <div class="flex items-center gap-3 mt-5"><div class="w-10 h-10 rounded-full bg-primary text-white flex items-center justify-center font-bold">FS</div><div><p class="font-bold text-gray-900 dark:text-white">Fatima Sheikh</p><p class="text-xs text-gray-500 dark:text-gray-400">Society secretary, Powai</p></div></div></div>
</div>
<div class="px-1" data-slider-slide>
    <div class="es-panel"><div class="flex gap-1 text-amber-400 mb-4"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star-half-stroke"></i></div>
    <p class="text-gray-600 dark:text-gray-300 leading-relaxed">“The E-Waste pickup is what sold me. Two old laptops and a desktop went to a certified recycler instead of a scrap bin, and I got a fair rate for the working parts.”</p>
    <div class="flex items-center gap-3 mt-5"><div class="w-10 h-10 rounded-full bg-primary text-white flex items-center justify-center font-bold">AN</div><div><p class="font-bold text-gray-900 dark:text-white">Arjun Nair</p><p class="text-xs text-gray-500 dark:text-gray-400">IT professional, Kothrud</p></div></div></div>
</div>"""
    )


def main():
    public_page(
        "index.html",
        "EcoScrap | Doorstep Scrap Pickup, Recycling & Cash for Scrap",
        "EcoScrap picks up your scrap from your doorstep with transparent weighing, live scrap rates and instant payment — turning waste into cash and keeping it out of landfill.",
        index_main(),
        active="index",
    )
    public_page(
        "home2.html",
        "EcoScrap | Smart Waste Recycling — Recycle More, Waste Less",
        "Explore EcoScrap's recycling-first homepage: household, corporate and society scrap collection programmes with environmental impact metrics and customer stories.",
        home2_main(),
        active="home2",
    )


if __name__ == "__main__":
    main()