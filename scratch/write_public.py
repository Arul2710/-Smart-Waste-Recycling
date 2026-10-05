import os

BASE_DIR = r"c:\Users\arulp\OneDrive\Desktop\Local Waste"
os.makedirs(BASE_DIR, exist_ok=True)

# -----------------
# SHARED LAYOUTS
# -----------------
HEAD = """<!DOCTYPE html>
<html lang="en" dir="ltr" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | EcoScrap</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script>
        tailwind.config = {{ darkMode: 'class', theme: {{ extend: {{ colors: {{ primary: '#16A34A', primaryDark: '#14532D', primaryLight: '#86EFAC', lightBg: '#F0FDF4', darkBg: '#0F172A' }}, fontFamily: {{ sans: ['Poppins', 'sans-serif'] }} }} }} }}
    </script>
</head>
<body class="bg-lightBg dark:bg-darkBg text-gray-800 dark:text-gray-200 transition-colors duration-300 font-sans flex flex-col min-h-screen">
"""

NAVBAR = """
    <header class="sticky top-0 z-50 bg-white dark:bg-gray-900 shadow-sm transition-colors duration-300">
        <div class="container mx-auto px-4"><div class="flex items-center justify-between h-20">
            <a href="index.html" class="flex items-center gap-2">
                <i class="fa-solid fa-recycle text-3xl text-primary"></i><span class="text-2xl font-bold text-primaryDark dark:text-primaryLight">EcoScrap</span>
            </a>
            <nav class="hidden lg:flex items-center gap-6">
                <div class="relative group">
                    <button class="flex items-center gap-1 font-medium hover:text-primary transition-colors">Home <i class="fa-solid fa-chevron-down text-xs"></i></button>
                    <div class="absolute left-0 mt-2 w-48 bg-white dark:bg-gray-800 shadow-lg rounded-md py-2 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all z-50">
                        <a href="index.html" class="block px-4 py-2 hover:bg-lightBg dark:hover:bg-gray-700">Home 1</a>
                        <a href="home2.html" class="block px-4 py-2 hover:bg-lightBg dark:hover:bg-gray-700">Home 2</a>
                    </div>
                </div>
                <a href="about.html" class="font-medium hover:text-primary transition-colors">About</a>
                <a href="services.html" class="font-medium hover:text-primary transition-colors">Services</a>
                <a href="rate-card.html" class="font-medium hover:text-primary transition-colors">Rate Card</a>
                <a href="how-it-works.html" class="font-medium hover:text-primary transition-colors">How It Works</a>
                <a href="blog.html" class="font-medium hover:text-primary transition-colors">Blog</a>
                <a href="contact.html" class="font-medium hover:text-primary transition-colors">Contact</a>
            </nav>
            <div class="hidden lg:flex items-center gap-4">
                <div class="relative group">
                    <button class="flex items-center gap-1 font-medium hover:text-primary transition-colors">Dashboard <i class="fa-solid fa-chevron-down text-xs"></i></button>
                    <div class="absolute right-0 mt-2 w-56 bg-white dark:bg-gray-800 shadow-lg rounded-md py-2 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all z-50">
                        <a href="customer-dashboard.html" class="block px-4 py-2 hover:bg-lightBg dark:hover:bg-gray-700">Customer Dashboard</a>
                        <a href="admin-dashboard.html" class="block px-4 py-2 hover:bg-lightBg dark:hover:bg-gray-700">Admin Dashboard</a>
                    </div>
                </div>
                <button id="rtl-toggle-btn" class="p-2 rounded-full bg-gray-100 dark:bg-gray-800 hover:text-primary transition-colors" title="Toggle RTL"><i class="fa-solid fa-language"></i></button>
                <button id="theme-toggle-btn" class="p-2 rounded-full bg-gray-100 dark:bg-gray-800 hover:text-primary transition-colors" title="Toggle Dark Mode"><i class="fa-solid fa-moon dark:hidden"></i><i class="fa-solid fa-sun hidden dark:block text-yellow-400"></i></button>
                <a href="login.html" class="font-medium hover:text-primary transition-colors"><i class="fa-solid fa-right-to-bracket"></i></a>
                <a href="signup.html" class="px-5 py-2 bg-primary hover:bg-primaryDark text-white rounded-full transition-colors font-medium shadow-md">Sign Up</a>
            </div>
            <button id="mobile-menu-btn" class="lg:hidden text-2xl p-2 text-gray-700 dark:text-gray-300"><i class="fa-solid fa-bars"></i></button>
        </div></div>
        <div id="mobile-menu" class="hidden lg:hidden bg-white dark:bg-gray-900 border-t border-gray-100 dark:border-gray-800 absolute w-full left-0 shadow-xl z-40 transition-all duration-300 ease-in-out">
            <div class="px-4 py-4 space-y-3 max-h-[80vh] overflow-y-auto">
                <div class="font-bold text-gray-400 uppercase text-xs mb-2">Home</div>
                <a href="index.html" class="block py-2 pl-4 border-l-2 border-primary text-gray-700 dark:text-gray-200">Home 1</a>
                <a href="home2.html" class="block py-2 pl-4 border-l-2 border-transparent hover:border-primary text-gray-700 dark:text-gray-200">Home 2</a>
                <div class="font-bold text-gray-400 uppercase text-xs mt-4 mb-2">Menu</div>
                <a href="about.html" class="block py-2 text-gray-700 dark:text-gray-200">About</a>
                <a href="services.html" class="block py-2 text-gray-700 dark:text-gray-200">Services</a>
                <a href="rate-card.html" class="block py-2 text-gray-700 dark:text-gray-200">Rate Card</a>
                <a href="how-it-works.html" class="block py-2 text-gray-700 dark:text-gray-200">How It Works</a>
                <a href="blog.html" class="block py-2 text-gray-700 dark:text-gray-200">Blog</a>
                <a href="contact.html" class="block py-2 text-gray-700 dark:text-gray-200">Contact</a>
                <div class="font-bold text-gray-400 uppercase text-xs mt-4 mb-2">Dashboards</div>
                <a href="customer-dashboard.html" class="block py-2 text-gray-700 dark:text-gray-200">Customer Dashboard</a>
                <a href="admin-dashboard.html" class="block py-2 text-gray-700 dark:text-gray-200">Admin Dashboard</a>
                <div class="flex items-center gap-4 py-4 border-t border-gray-100 dark:border-gray-800 mt-2">
                    <button id="mobile-rtl-toggle" class="flex-1 py-2 bg-gray-100 dark:bg-gray-800 text-gray-700 dark:text-gray-300 rounded font-medium"><i class="fa-solid fa-language"></i> RTL</button>
                    <button id="mobile-theme-toggle" class="flex-1 py-2 bg-gray-100 dark:bg-gray-800 text-gray-700 dark:text-gray-300 rounded font-medium"><i class="fa-solid fa-circle-half-stroke"></i> Theme</button>
                </div>
                <div class="flex flex-col gap-3 pt-2">
                    <a href="login.html" class="w-full text-center py-2.5 border border-primary text-primary rounded-lg font-bold">Login</a>
                    <a href="signup.html" class="w-full text-center py-2.5 bg-primary text-white rounded-lg font-bold">Sign Up</a>
                </div>
            </div>
        </div>
    </header>
    <main class="flex-grow">
"""

FOOTER = """
    </main>
    <footer class="bg-primaryDark text-white pt-16 pb-8">
        <div class="container mx-auto px-4"><div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 mb-12">
            <div>
                <a href="index.html" class="flex items-center gap-2 mb-6"><i class="fa-solid fa-recycle text-3xl text-primaryLight"></i><span class="text-2xl font-bold text-white">EcoScrap</span></a>
                <p class="text-gray-300 mb-6 text-sm">Your trusted local waste pickup and scrap dealer. Turning waste into wealth while saving the planet.</p>
                <div class="flex gap-4">
                    <a href="#" class="text-gray-300 hover:text-white transition"><i class="fa-brands fa-facebook text-2xl"></i></a>
                    <a href="#" class="text-gray-300 hover:text-white transition"><i class="fa-brands fa-instagram text-2xl"></i></a>
                    <a href="#" class="text-gray-300 hover:text-white transition"><i class="fa-brands fa-twitter text-2xl"></i></a>
                </div>
            </div>
            <div>
                <h4 class="text-lg font-semibold mb-6">Quick Links</h4>
                <ul class="space-y-3 text-sm">
                    <li><a href="about.html" class="text-gray-300 hover:text-white">About Us</a></li>
                    <li><a href="services.html" class="text-gray-300 hover:text-white">Services</a></li>
                    <li><a href="rate-card.html" class="text-gray-300 hover:text-white">Scrap Rates</a></li>
                    <li><a href="how-it-works.html" class="text-gray-300 hover:text-white">How It Works</a></li>
                    <li><a href="contact.html" class="text-gray-300 hover:text-white">Contact Us</a></li>
                </ul>
            </div>
            <div>
                <h4 class="text-lg font-semibold mb-6">Scrap Categories</h4>
                <ul class="space-y-3 text-sm">
                    <li><a href="services.html" class="text-gray-300 hover:text-white">Paper & Cardboard</a></li>
                    <li><a href="services.html" class="text-gray-300 hover:text-white">Metal & Aluminum</a></li>
                    <li><a href="services.html" class="text-gray-300 hover:text-white">Plastic & Packaging</a></li>
                    <li><a href="services.html" class="text-gray-300 hover:text-white">E-Waste</a></li>
                </ul>
            </div>
            <div>
                <h4 class="text-lg font-semibold mb-6">Newsletter</h4>
                <p class="text-gray-300 text-sm mb-4">Subscribe for the latest rate updates and recycling tips.</p>
                <form class="flex flex-col gap-3">
                    <input type="email" placeholder="Email Address" class="px-4 py-2 rounded bg-white/10 text-white outline-none border border-white/20 focus:border-primaryLight transition">
                    <button type="button" onclick="alert('Subscribed successfully!')" class="px-4 py-2 bg-primary hover:bg-green-500 transition rounded text-white font-medium">Subscribe</button>
                </form>
            </div>
        </div>
        <div class="border-t border-white/20 pt-8 flex flex-col md:flex-row justify-between items-center gap-4 text-gray-400 text-sm">
            <p>&copy; 2026 EcoScrap. All rights reserved.</p>
            <div class="flex gap-4">
                <a href="privacy-policy.html" class="hover:text-white transition">Privacy Policy</a>
                <a href="terms.html" class="hover:text-white transition">Terms & Conditions</a>
            </div>
        </div></div>
    </footer>
    <script src="js/theme.js"></script><script src="js/rtl.js"></script><script src="js/main.js"></script>
</body>
</html>
"""

def make_page(title, body):
    return HEAD.format(title=title) + NAVBAR + body + FOOTER

PAGES = {}

PAGES['index.html'] = """
<!-- 1. Hero -->
<section class="relative bg-darkBg text-white py-32 lg:py-48 overflow-hidden">
    <div class="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1604187351574-c75ca79f5807?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80')] bg-cover bg-center"></div>
    <div class="absolute inset-0 bg-black/60"></div>
    <div class="container mx-auto px-4 relative z-10">
        <div class="max-w-2xl">
            <h1 class="text-4xl md:text-6xl font-bold mb-6">Turn Your Scrap Into Cash. <span class="text-primaryLight">We Pick It Up!</span></h1>
            <p class="text-lg text-gray-200 mb-8">EcoScrap provides a seamless doorstep scrap collection service. Enjoy transparent pricing, reliable weights, and responsible recycling.</p>
            <div class="flex gap-4 mb-8">
                <a href="customer-dashboard.html" class="px-8 py-3 bg-primary hover:bg-green-500 rounded-full font-bold shadow-lg text-white transition">Schedule Pickup</a>
                <a href="rate-card.html" class="px-8 py-3 bg-white/20 hover:bg-white/30 rounded-full font-bold text-white transition">View Scrap Rates</a>
            </div>
            <div class="bg-white/10 p-2 rounded-full flex items-center max-w-md border border-white/20 backdrop-blur-sm">
                <i class="fa-solid fa-location-dot ml-4 mr-2 text-primaryLight"></i>
                <input type="text" placeholder="Enter pickup location..." class="bg-transparent border-none outline-none w-full text-white px-2">
                <button class="bg-primary px-6 py-2 rounded-full font-bold text-white">Search</button>
            </div>
        </div>
    </div>
</section>
<!-- 2. About -->
<section class="py-20 bg-white dark:bg-gray-900">
    <div class="container mx-auto px-4 flex flex-col lg:flex-row gap-12 items-center">
        <div class="lg:w-1/2">
            <img src="https://images.unsplash.com/photo-1532996122724-e3c354a0b15b?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="About EcoScrap" class="rounded-2xl shadow-xl w-full h-[400px] object-cover">
        </div>
        <div class="lg:w-1/2">
            <h2 class="text-3xl md:text-4xl font-bold mb-6 text-gray-900 dark:text-white">Responsible Recycling, Delivered to Your Door</h2>
            <p class="text-gray-600 dark:text-gray-300 mb-6 text-lg">We bring professional scrap collection directly to you. Say goodbye to hauling heavy materials or haggling with local dealers. Our transparent process ensures you get the best value.</p>
            <ul class="space-y-4 mb-8">
                <li class="flex items-center gap-3 text-lg"><i class="fa-solid fa-scale-balanced text-primary text-2xl w-8"></i> Transparent Pricing & Weighing</li>
                <li class="flex items-center gap-3 text-lg"><i class="fa-solid fa-money-bill-transfer text-primary text-2xl w-8"></i> Instant Digital Payments</li>
                <li class="flex items-center gap-3 text-lg"><i class="fa-solid fa-earth-americas text-primary text-2xl w-8"></i> Eco-Friendly Disposal</li>
            </ul>
            <a href="about.html" class="text-primary font-bold hover:text-primaryDark flex items-center gap-2">Learn More <i class="fa-solid fa-arrow-right"></i></a>
        </div>
    </div>
</section>
<!-- 3. Categories -->
<section class="py-20 bg-lightBg dark:bg-gray-800">
    <div class="container mx-auto px-4">
        <h2 class="text-3xl md:text-4xl font-bold mb-12 text-center text-gray-900 dark:text-white">What We Collect</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div class="bg-white dark:bg-gray-900 rounded-2xl shadow overflow-hidden flex flex-col">
                <img src="https://images.unsplash.com/photo-1603415526960-f7e0328c63b1?auto=format&w=600&q=80" class="w-full h-48 object-cover">
                <div class="p-6 flex-grow flex flex-col">
                    <h3 class="text-xl font-bold mb-2 flex items-center gap-2"><i class="fa-solid fa-newspaper text-primary"></i> Paper & Cardboard</h3>
                    <p class="text-gray-600 dark:text-gray-400 mb-6 flex-grow">Newspapers, books, magazines, cartons, corrugated boxes.</p>
                    <a href="rate-card.html" class="w-full text-center py-2 border border-primary text-primary rounded-lg font-bold">View Rates</a>
                </div>
            </div>
            <div class="bg-white dark:bg-gray-900 rounded-2xl shadow overflow-hidden flex flex-col">
                <img src="https://images.unsplash.com/photo-1558590390-e793ea5ce6b0?auto=format&w=600&q=80" class="w-full h-48 object-cover">
                <div class="p-6 flex-grow flex flex-col">
                    <h3 class="text-xl font-bold mb-2 flex items-center gap-2"><i class="fa-solid fa-cubes text-primary"></i> Metal & Aluminum</h3>
                    <p class="text-gray-600 dark:text-gray-400 mb-6 flex-grow">Iron, steel, copper wire, brass, aluminum cans, mixed metals.</p>
                    <a href="rate-card.html" class="w-full text-center py-2 border border-primary text-primary rounded-lg font-bold">View Rates</a>
                </div>
            </div>
            <div class="bg-white dark:bg-gray-900 rounded-2xl shadow overflow-hidden flex flex-col">
                <img src="https://images.unsplash.com/photo-1611288875791-561fc726058e?auto=format&w=600&q=80" class="w-full h-48 object-cover">
                <div class="p-6 flex-grow flex flex-col">
                    <h3 class="text-xl font-bold mb-2 flex items-center gap-2"><i class="fa-solid fa-bottle-water text-primary"></i> Plastic & Packaging</h3>
                    <p class="text-gray-600 dark:text-gray-400 mb-6 flex-grow">PET bottles, PVC pipes, HDPE containers, soft plastics.</p>
                    <a href="rate-card.html" class="w-full text-center py-2 border border-primary text-primary rounded-lg font-bold">View Rates</a>
                </div>
            </div>
        </div>
    </div>
</section>
<!-- 4. How It Works -->
<section class="py-20 bg-white dark:bg-gray-900">
    <div class="container mx-auto px-4">
        <h2 class="text-3xl md:text-4xl font-bold mb-12 text-center text-gray-900 dark:text-white">How It Works</h2>
        <div class="grid grid-cols-1 md:grid-cols-4 gap-8 text-center relative">
            <div class="relative z-10"><div class="w-20 h-20 mx-auto bg-primary text-white rounded-full flex items-center justify-center text-3xl mb-4"><i class="fa-solid fa-boxes-packing"></i></div><h3 class="font-bold text-xl">1. Select Scrap</h3></div>
            <div class="relative z-10"><div class="w-20 h-20 mx-auto bg-primary text-white rounded-full flex items-center justify-center text-3xl mb-4"><i class="fa-regular fa-calendar-check"></i></div><h3 class="font-bold text-xl">2. Schedule Pickup</h3></div>
            <div class="relative z-10"><div class="w-20 h-20 mx-auto bg-primary text-white rounded-full flex items-center justify-center text-3xl mb-4"><i class="fa-solid fa-weight-scale"></i></div><h3 class="font-bold text-xl">3. Weigh & Verify</h3></div>
            <div class="relative z-10"><div class="w-20 h-20 mx-auto bg-primary text-white rounded-full flex items-center justify-center text-3xl mb-4"><i class="fa-solid fa-wallet"></i></div><h3 class="font-bold text-xl">4. Receive Payment</h3></div>
        </div>
    </div>
</section>
<!-- 5. Rate Card -->
<section class="py-20 bg-lightBg dark:bg-gray-800">
    <div class="container mx-auto px-4">
        <h2 class="text-3xl md:text-4xl font-bold mb-8 text-gray-900 dark:text-white">Live Scrap Rates</h2>
        <div class="bg-white dark:bg-gray-900 rounded-2xl shadow overflow-hidden">
            <table class="w-full text-left">
                <thead class="bg-gray-50 dark:bg-gray-800"><tr class="text-gray-700 dark:text-gray-300"><th class="p-4">Material</th><th class="p-4">Category</th><th class="p-4">Unit</th><th class="p-4 text-right">Price</th></tr></thead>
                <tbody class="divide-y divide-gray-100 dark:divide-gray-700">
                    <tr><td class="p-4">Newspaper</td><td class="p-4">Paper</td><td class="p-4">1 KG</td><td class="p-4 text-right font-bold text-primary">₹ 14.00</td></tr>
                    <tr><td class="p-4">Iron Scrap</td><td class="p-4">Metal</td><td class="p-4">1 KG</td><td class="p-4 text-right font-bold text-primary">₹ 28.00</td></tr>
                </tbody>
            </table>
            <div class="p-4 text-sm text-gray-500 italic text-center">* Prices vary by quality and final weight.</div>
        </div>
        <div class="mt-6 text-center"><a href="rate-card.html" class="px-6 py-2 bg-primary text-white rounded-lg font-bold">View Full Rate Card</a></div>
    </div>
</section>
<!-- 6. Locations CTA -->
<section class="py-20 bg-white dark:bg-gray-900">
    <div class="container mx-auto px-4">
        <h2 class="text-3xl md:text-4xl font-bold mb-8 text-center text-gray-900 dark:text-white">Our Service Locations</h2>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-6 mb-12">
            <div class="bg-lightBg dark:bg-gray-800 p-6 rounded-2xl text-center shadow"><h3 class="font-bold text-xl mb-2">Delhi NCR</h3><p class="text-sm">Full Coverage</p></div>
            <div class="bg-lightBg dark:bg-gray-800 p-6 rounded-2xl text-center shadow"><h3 class="font-bold text-xl mb-2">Mumbai</h3><p class="text-sm">Selected Zones</p></div>
            <div class="bg-lightBg dark:bg-gray-800 p-6 rounded-2xl text-center shadow"><h3 class="font-bold text-xl mb-2">Bangalore</h3><p class="text-sm">Full Coverage</p></div>
            <div class="bg-lightBg dark:bg-gray-800 p-6 rounded-2xl text-center shadow"><h3 class="font-bold text-xl mb-2">Pune</h3><p class="text-sm">Partial Coverage</p></div>
        </div>
        <div class="bg-primaryDark rounded-3xl p-12 text-center text-white relative overflow-hidden shadow-2xl">
            <div class="absolute inset-0 opacity-20 bg-[url('https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?auto=format&w=1920&q=80')] bg-cover bg-center"></div>
            <div class="relative z-10">
                <h2 class="text-3xl md:text-4xl font-bold mb-6">Ready to Clear Your Scrap?</h2>
                <div class="flex flex-col sm:flex-row justify-center gap-4">
                    <a href="customer-dashboard.html" class="px-8 py-4 bg-primary text-white rounded-full font-bold shadow-lg">Schedule Pickup</a>
                    <a href="contact.html" class="px-8 py-4 bg-white text-primaryDark rounded-full font-bold shadow-lg">Contact Us</a>
                </div>
            </div>
        </div>
    </div>
</section>
"""

PAGES['home2.html'] = """
<!-- 1. Hero -->
<section class="relative bg-darkBg text-white py-32 lg:py-48 overflow-hidden">
    <div class="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?auto=format&fit=crop&w=1920&q=80')] bg-cover bg-center opacity-50"></div>
    <div class="container mx-auto px-4 relative z-10 text-center">
        <h1 class="text-5xl md:text-7xl font-bold mb-6">Smart Waste Recycling</h1>
        <p class="text-xl mb-8 max-w-2xl mx-auto">Get the best value for your recyclables while contributing to a greener planet.</p>
        <a href="customer-dashboard.html" class="px-8 py-4 bg-primary text-white rounded-full font-bold shadow-lg text-lg">Book a Pickup Now</a>
    </div>
</section>
<!-- 2. Services -->
<section class="py-20 bg-white dark:bg-gray-900">
    <div class="container mx-auto px-4 text-center">
        <h2 class="text-4xl font-bold mb-12">Our Core Services</h2>
        <div class="grid md:grid-cols-3 gap-8">
            <div class="p-8 border border-gray-100 dark:border-gray-800 shadow rounded-2xl"><i class="fa-solid fa-house text-4xl text-primary mb-4"></i><h3 class="text-xl font-bold">Household Pickup</h3></div>
            <div class="p-8 border border-gray-100 dark:border-gray-800 shadow rounded-2xl"><i class="fa-solid fa-building text-4xl text-primary mb-4"></i><h3 class="text-xl font-bold">Corporate Clearouts</h3></div>
            <div class="p-8 border border-gray-100 dark:border-gray-800 shadow rounded-2xl"><i class="fa-solid fa-city text-4xl text-primary mb-4"></i><h3 class="text-xl font-bold">Society Scrap Drives</h3></div>
        </div>
    </div>
</section>
<!-- 3. Categories -->
<section class="py-20 bg-lightBg dark:bg-gray-800">
    <div class="container mx-auto px-4">
        <h2 class="text-4xl font-bold mb-12 text-center">Recyclable Categories</h2>
        <div class="grid md:grid-cols-4 gap-6">
            <div class="bg-white dark:bg-gray-900 p-6 rounded-2xl shadow text-center"><img src="https://images.unsplash.com/photo-1603415526960-f7e0328c63b1?auto=format&w=400&q=80" class="h-32 w-full object-cover rounded mb-4"><h3 class="font-bold">Paper</h3></div>
            <div class="bg-white dark:bg-gray-900 p-6 rounded-2xl shadow text-center"><img src="https://images.unsplash.com/photo-1558590390-e793ea5ce6b0?auto=format&w=400&q=80" class="h-32 w-full object-cover rounded mb-4"><h3 class="font-bold">Metals</h3></div>
            <div class="bg-white dark:bg-gray-900 p-6 rounded-2xl shadow text-center"><img src="https://images.unsplash.com/photo-1550005973-5843066c92cb?auto=format&w=400&q=80" class="h-32 w-full object-cover rounded mb-4"><h3 class="font-bold">E-Waste</h3></div>
            <div class="bg-white dark:bg-gray-900 p-6 rounded-2xl shadow text-center"><img src="https://images.unsplash.com/photo-1626071465934-2e21b7dfeb86?auto=format&w=400&q=80" class="h-32 w-full object-cover rounded mb-4"><h3 class="font-bold">Appliances</h3></div>
        </div>
    </div>
</section>
<!-- 4. How It Works -->
<section class="py-20 bg-white dark:bg-gray-900 text-center">
    <div class="container mx-auto px-4">
        <h2 class="text-4xl font-bold mb-12">How It Works</h2>
        <div class="flex flex-col md:flex-row justify-center gap-8">
            <div><div class="text-3xl text-primary font-bold mb-2">01</div><h3 class="font-bold">Schedule</h3></div>
            <div><div class="text-3xl text-primary font-bold mb-2">02</div><h3 class="font-bold">Weigh</h3></div>
            <div><div class="text-3xl text-primary font-bold mb-2">03</div><h3 class="font-bold">Get Paid</h3></div>
        </div>
    </div>
</section>
<!-- 5. Impact -->
<section class="py-20 bg-lightBg dark:bg-gray-800 text-center">
    <div class="container mx-auto px-4">
        <h2 class="text-4xl font-bold mb-12">Our Environmental Impact</h2>
        <div class="grid md:grid-cols-3 gap-8">
            <div><h3 class="text-5xl font-bold text-primary mb-2">5M+</h3><p>KG Recycled</p></div>
            <div><h3 class="text-5xl font-bold text-primary mb-2">50k+</h3><p>Trees Saved</p></div>
            <div><h3 class="text-5xl font-bold text-primary mb-2">10k+</h3><p>Happy Users</p></div>
        </div>
    </div>
</section>
<!-- 6. Locations CTA -->
<section class="py-20 bg-white dark:bg-gray-900">
    <div class="container mx-auto px-4">
        <div class="bg-primaryDark rounded-3xl p-12 text-center text-white relative shadow-2xl">
            <h2 class="text-4xl font-bold mb-6">Available in Delhi, Mumbai, Bangalore</h2>
            <a href="customer-dashboard.html" class="px-8 py-4 bg-primary text-white rounded-full font-bold inline-block">Book a Pickup</a>
        </div>
    </div>
</section>
"""

PAGES['about.html'] = """
<!-- 1 -->
<section class="relative bg-darkBg text-white py-24 overflow-hidden">
    <div class="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1532996122724-e3c354a0b15b?auto=format&w=1920&q=80')] bg-cover bg-center opacity-40"></div>
    <div class="container mx-auto px-4 relative z-10 text-center">
        <h1 class="text-5xl font-bold mb-4">About EcoScrap</h1>
    </div>
</section>
<!-- 2 -->
<section class="py-20 bg-white dark:bg-gray-900">
    <div class="container mx-auto px-4 grid md:grid-cols-2 gap-12 items-center">
        <div><h2 class="text-4xl font-bold mb-6">Our Story</h2><p class="text-lg">Founded in 2024 to revolutionize local scrap collection.</p></div>
        <div><img src="https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?auto=format&w=800&q=80" class="rounded-2xl shadow-xl w-full"></div>
    </div>
</section>
<!-- 3 -->
<section class="py-20 bg-lightBg dark:bg-gray-800 text-center">
    <div class="container mx-auto px-4">
        <h2 class="text-4xl font-bold mb-8">Mission & Vision</h2>
        <div class="grid md:grid-cols-2 gap-8">
            <div class="bg-white dark:bg-gray-900 p-8 rounded-2xl shadow"><h3 class="text-2xl font-bold mb-4">Mission</h3><p>Make recycling easy and transparent.</p></div>
            <div class="bg-white dark:bg-gray-900 p-8 rounded-2xl shadow"><h3 class="text-2xl font-bold mb-4">Vision</h3><p>A zero waste society.</p></div>
        </div>
    </div>
</section>
<!-- 4 -->
<section class="py-20 bg-white dark:bg-gray-900 text-center">
    <div class="container mx-auto px-4">
        <h2 class="text-4xl font-bold mb-8">Environmental Responsibility</h2>
        <p class="max-w-2xl mx-auto text-lg">Every kilogram of scrap collected goes to certified recycling facilities.</p>
    </div>
</section>
<!-- 5 -->
<section class="py-20 bg-lightBg dark:bg-gray-800 text-center">
    <div class="container mx-auto px-4">
        <h2 class="text-4xl font-bold mb-8">Our Team</h2>
        <div class="grid md:grid-cols-3 gap-8">
            <div class="bg-white dark:bg-gray-900 p-6 rounded-2xl shadow"><div class="w-24 h-24 bg-gray-300 rounded-full mx-auto mb-4"></div><h3 class="font-bold">Rahul S.</h3><p>Founder</p></div>
            <div class="bg-white dark:bg-gray-900 p-6 rounded-2xl shadow"><div class="w-24 h-24 bg-gray-300 rounded-full mx-auto mb-4"></div><h3 class="font-bold">Anita K.</h3><p>Operations</p></div>
            <div class="bg-white dark:bg-gray-900 p-6 rounded-2xl shadow"><div class="w-24 h-24 bg-gray-300 rounded-full mx-auto mb-4"></div><h3 class="font-bold">David M.</h3><p>Logistics</p></div>
        </div>
    </div>
</section>
<!-- 6 -->
<section class="py-20 bg-white dark:bg-gray-900">
    <div class="container mx-auto px-4 text-center">
        <div class="bg-primary text-white p-12 rounded-3xl"><h2 class="text-4xl font-bold mb-6">Join Us in Making a Difference</h2><a href="signup.html" class="px-8 py-4 bg-white text-primary rounded-full font-bold">Sign Up Today</a></div>
    </div>
</section>
"""

PAGES['services.html'] = """
<!-- 1 -->
<section class="relative bg-darkBg text-white py-24 overflow-hidden">
    <div class="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1604187351574-c75ca79f5807?auto=format&w=1920&q=80')] bg-cover bg-center opacity-40"></div>
    <div class="container mx-auto px-4 relative z-10 text-center">
        <h1 class="text-5xl font-bold mb-4">Our Services</h1>
    </div>
</section>
<!-- 2 -->
<section class="py-20 bg-white dark:bg-gray-900">
    <div class="container mx-auto px-4">
        <h2 class="text-4xl font-bold mb-8 text-center">Standard Collection</h2>
        <div class="grid md:grid-cols-2 gap-8">
            <div class="bg-lightBg dark:bg-gray-800 p-8 rounded-2xl shadow flex gap-4"><i class="fa-solid fa-newspaper text-4xl text-primary"></i><div><h3 class="text-2xl font-bold mb-2">Paper & Plastics</h3><p>Recycle common household waste securely.</p></div></div>
            <div class="bg-lightBg dark:bg-gray-800 p-8 rounded-2xl shadow flex gap-4"><i class="fa-solid fa-cubes text-4xl text-primary"></i><div><h3 class="text-2xl font-bold mb-2">Metals & Alloys</h3><p>Get best rates for iron, copper, and brass.</p></div></div>
        </div>
    </div>
</section>
<!-- 3 -->
<section class="py-20 bg-lightBg dark:bg-gray-800">
    <div class="container mx-auto px-4">
        <h2 class="text-4xl font-bold mb-8 text-center">Specialized Collection</h2>
        <div class="grid md:grid-cols-2 gap-8">
            <div class="bg-white dark:bg-gray-900 p-8 rounded-2xl shadow flex gap-4"><i class="fa-solid fa-computer text-4xl text-primary"></i><div><h3 class="text-2xl font-bold mb-2">E-Waste Disposal</h3><p>Safe and certified disposal of electronics.</p></div></div>
            <div class="bg-white dark:bg-gray-900 p-8 rounded-2xl shadow flex gap-4"><i class="fa-solid fa-car-battery text-4xl text-primary"></i><div><h3 class="text-2xl font-bold mb-2">Heavy Appliances</h3><p>We handle heavy lifting for ACs and fridges.</p></div></div>
        </div>
    </div>
</section>
<!-- 4 -->
<section class="py-20 bg-white dark:bg-gray-900 text-center">
    <div class="container mx-auto px-4"><h2 class="text-4xl font-bold mb-8">Transparent Process</h2><p class="text-lg">Digital weighing scales and instant UPI payments guarantee transparency.</p></div>
</section>
<!-- 5 -->
<section class="py-20 bg-lightBg dark:bg-gray-800 text-center">
    <div class="container mx-auto px-4"><h2 class="text-4xl font-bold mb-8">Service Areas</h2><p class="text-lg">Operating across major metropolitan cities including Delhi NCR, Mumbai, and Bangalore.</p></div>
</section>
<!-- 6 -->
<section class="py-20 bg-white dark:bg-gray-900">
    <div class="container mx-auto px-4 text-center">
        <div class="bg-primary text-white p-12 rounded-3xl"><h2 class="text-4xl font-bold mb-6">Need a Pickup?</h2><a href="customer-dashboard.html" class="px-8 py-4 bg-white text-primary rounded-full font-bold">Schedule Now</a></div>
    </div>
</section>
"""

PAGES['rate-card.html'] = """
<!-- 1 -->
<section class="relative bg-darkBg text-white py-24 overflow-hidden">
    <div class="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1558590390-e793ea5ce6b0?auto=format&w=1920&q=80')] bg-cover bg-center opacity-40"></div>
    <div class="container mx-auto px-4 relative z-10 text-center">
        <h1 class="text-5xl font-bold mb-4">Scrap Rate Card</h1>
    </div>
</section>
<!-- 2 -->
<section class="py-12 bg-white dark:bg-gray-900 text-center">
    <div class="container mx-auto px-4">
        <input type="text" placeholder="Search Material..." class="px-6 py-3 border rounded-full w-full max-w-md dark:bg-gray-800 dark:border-gray-700">
        <div class="flex flex-wrap justify-center gap-4 mt-6">
            <button class="px-4 py-2 bg-primary text-white rounded-full">All</button>
            <button class="px-4 py-2 bg-gray-200 dark:bg-gray-800 rounded-full">Paper</button>
            <button class="px-4 py-2 bg-gray-200 dark:bg-gray-800 rounded-full">Metal</button>
            <button class="px-4 py-2 bg-gray-200 dark:bg-gray-800 rounded-full">E-Waste</button>
        </div>
    </div>
</section>
<!-- 3 -->
<section class="py-12 bg-lightBg dark:bg-gray-800">
    <div class="container mx-auto px-4 max-w-4xl">
        <h2 class="text-2xl font-bold mb-6">Paper & Plastics</h2>
        <div class="bg-white dark:bg-gray-900 rounded-2xl shadow overflow-hidden">
            <table class="w-full text-left">
                <tr class="border-b dark:border-gray-700"><th class="p-4">Material</th><th class="p-4">Unit</th><th class="p-4 text-right">Price</th></tr>
                <tr class="border-b dark:border-gray-700"><td class="p-4">Newspaper</td><td class="p-4">1 KG</td><td class="p-4 text-right font-bold text-primary">₹ 14.00</td></tr>
                <tr><td class="p-4">PET Bottles</td><td class="p-4">1 KG</td><td class="p-4 text-right font-bold text-primary">₹ 12.00</td></tr>
            </table>
        </div>
    </div>
</section>
<!-- 4 -->
<section class="py-12 bg-white dark:bg-gray-900">
    <div class="container mx-auto px-4 max-w-4xl">
        <h2 class="text-2xl font-bold mb-6">Metals & E-Waste</h2>
        <div class="bg-lightBg dark:bg-gray-800 rounded-2xl shadow overflow-hidden">
            <table class="w-full text-left">
                <tr class="border-b dark:border-gray-700"><th class="p-4">Material</th><th class="p-4">Unit</th><th class="p-4 text-right">Price</th></tr>
                <tr class="border-b dark:border-gray-700"><td class="p-4">Iron</td><td class="p-4">1 KG</td><td class="p-4 text-right font-bold text-primary">₹ 28.00</td></tr>
                <tr><td class="p-4">Laptops</td><td class="p-4">1 Piece</td><td class="p-4 text-right font-bold text-primary">₹ 300.00</td></tr>
            </table>
        </div>
    </div>
</section>
<!-- 5 -->
<section class="py-12 bg-lightBg dark:bg-gray-800 text-center">
    <div class="container mx-auto px-4"><p class="text-gray-500 italic">Prices last updated today. Final price subject to verification by our collector.</p></div>
</section>
<!-- 6 -->
<section class="py-20 bg-white dark:bg-gray-900 text-center">
    <div class="container mx-auto px-4">
        <div class="bg-primary text-white p-12 rounded-3xl"><h2 class="text-4xl font-bold mb-6">Happy with the rates?</h2><a href="customer-dashboard.html" class="px-8 py-4 bg-white text-primary rounded-full font-bold">Schedule Pickup</a></div>
    </div>
</section>
"""

PAGES['how-it-works.html'] = """
<!-- 1 -->
<section class="relative bg-darkBg text-white py-24 overflow-hidden">
    <div class="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?auto=format&w=1920&q=80')] bg-cover bg-center opacity-40"></div>
    <div class="container mx-auto px-4 relative z-10 text-center"><h1 class="text-5xl font-bold mb-4">How It Works</h1></div>
</section>
<!-- 2 -->
<section class="py-20 bg-white dark:bg-gray-900">
    <div class="container mx-auto px-4 grid md:grid-cols-2 gap-12 text-center">
        <div class="p-8"><div class="w-20 h-20 bg-primary text-white mx-auto rounded-full flex items-center justify-center text-3xl mb-4">1</div><h3 class="text-2xl font-bold mb-4">Choose Scrap Categories</h3><p>Select what you have to sell.</p></div>
        <div class="p-8"><div class="w-20 h-20 bg-primary text-white mx-auto rounded-full flex items-center justify-center text-3xl mb-4">2</div><h3 class="text-2xl font-bold mb-4">Schedule Pickup</h3><p>Pick a date and time.</p></div>
    </div>
</section>
<!-- 3 -->
<section class="py-20 bg-lightBg dark:bg-gray-800">
    <div class="container mx-auto px-4 grid md:grid-cols-2 gap-12 text-center">
        <div class="p-8"><div class="w-20 h-20 bg-primary text-white mx-auto rounded-full flex items-center justify-center text-3xl mb-4">3</div><h3 class="text-2xl font-bold mb-4">Weighing</h3><p>Accurate digital scales used at your door.</p></div>
        <div class="p-8"><div class="w-20 h-20 bg-primary text-white mx-auto rounded-full flex items-center justify-center text-3xl mb-4">4</div><h3 class="text-2xl font-bold mb-4">Get Paid</h3><p>Instant UPI, Bank, or Cash payments.</p></div>
    </div>
</section>
<!-- 4 -->
<section class="py-20 bg-white dark:bg-gray-900 text-center">
    <div class="container mx-auto px-4"><h2 class="text-4xl font-bold mb-8">Payment Methods</h2><div class="flex justify-center gap-8 text-4xl text-primary"><i class="fa-solid fa-building-columns"></i><i class="fa-solid fa-mobile-screen"></i><i class="fa-solid fa-money-bill-1-wave"></i></div></div>
</section>
<!-- 5 -->
<section class="py-20 bg-lightBg dark:bg-gray-800 text-center">
    <div class="container mx-auto px-4 max-w-3xl"><h2 class="text-4xl font-bold mb-8">FAQ</h2><div class="space-y-4 text-left"><div class="bg-white dark:bg-gray-900 p-6 rounded"><h4 class="font-bold">Is pickup free?</h4><p>Yes, absolutely free.</p></div></div></div>
</section>
<!-- 6 -->
<section class="py-20 bg-white dark:bg-gray-900 text-center">
    <div class="container mx-auto px-4"><a href="customer-dashboard.html" class="px-8 py-4 bg-primary text-white rounded-full font-bold">Schedule Pickup Now</a></div>
</section>
"""

PAGES['blog.html'] = """
<!-- 1 -->
<section class="relative bg-darkBg text-white py-24 overflow-hidden">
    <div class="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1532996122724-e3c354a0b15b?auto=format&w=1920&q=80')] bg-cover bg-center opacity-40"></div>
    <div class="container mx-auto px-4 relative z-10 text-center"><h1 class="text-5xl font-bold mb-4">Our Blog</h1></div>
</section>
<!-- 2 -->
<section class="py-20 bg-white dark:bg-gray-900">
    <div class="container mx-auto px-4"><h2 class="text-4xl font-bold mb-8">Featured Post</h2><div class="bg-lightBg dark:bg-gray-800 rounded-2xl overflow-hidden shadow md:flex"><img src="https://images.unsplash.com/photo-1603415526960-f7e0328c63b1?auto=format&w=600&q=80" class="md:w-1/2 object-cover"><div class="p-8 md:w-1/2"><h3 class="text-2xl font-bold mb-4">10 Ways to Recycle Better</h3><p class="mb-6">Improve your recycling habits today...</p><a href="blog-details.html" class="text-primary font-bold">Read More</a></div></div></div>
</section>
<!-- 3 -->
<section class="py-20 bg-lightBg dark:bg-gray-800">
    <div class="container mx-auto px-4"><h2 class="text-4xl font-bold mb-8">Recent Posts</h2><div class="grid md:grid-cols-3 gap-8"><div class="bg-white dark:bg-gray-900 rounded-2xl shadow p-6"><h3 class="font-bold mb-2">E-Waste Hazards</h3><a href="blog-details.html" class="text-primary text-sm">Read More</a></div></div></div>
</section>
<!-- 4 -->
<section class="py-20 bg-white dark:bg-gray-900 text-center">
    <div class="container mx-auto px-4"><h2 class="text-4xl font-bold mb-8">Categories</h2><div class="flex justify-center gap-4"><span class="px-4 py-2 bg-lightBg dark:bg-gray-800 rounded">Recycling</span><span class="px-4 py-2 bg-lightBg dark:bg-gray-800 rounded">Tips</span></div></div>
</section>
<!-- 5 -->
<section class="py-20 bg-lightBg dark:bg-gray-800 text-center">
    <div class="container mx-auto px-4"><h2 class="text-4xl font-bold mb-8">Newsletter</h2><input type="email" placeholder="Enter Email" class="p-3 rounded border dark:bg-gray-900 dark:border-gray-700 max-w-sm w-full"><button class="bg-primary text-white p-3 rounded">Subscribe</button></div>
</section>
<!-- 6 -->
<section class="py-20 bg-white dark:bg-gray-900 text-center">
    <div class="container mx-auto px-4"><div class="bg-primary text-white p-12 rounded-3xl"><h2 class="text-4xl font-bold mb-6">Ready to Recycle?</h2><a href="customer-dashboard.html" class="px-8 py-4 bg-white text-primary rounded-full font-bold">Schedule Pickup</a></div></div>
</section>
"""

PAGES['blog-details.html'] = """
<!-- 1 -->
<section class="relative bg-darkBg text-white py-24 overflow-hidden">
    <div class="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1603415526960-f7e0328c63b1?auto=format&w=1920&q=80')] bg-cover bg-center opacity-40"></div>
    <div class="container mx-auto px-4 relative z-10 text-center"><h1 class="text-5xl font-bold mb-4">10 Ways to Recycle Better</h1></div>
</section>
<!-- 2 -->
<section class="py-20 bg-white dark:bg-gray-900">
    <div class="container mx-auto px-4 max-w-3xl"><p class="text-xl leading-relaxed">Introduction to better recycling habits and keeping our environment safe.</p></div>
</section>
<!-- 3 -->
<section class="py-12 bg-lightBg dark:bg-gray-800">
    <div class="container mx-auto px-4 max-w-3xl"><p class="text-lg leading-relaxed">Detailed guide on separating paper, metals, and plastics correctly. Always ensure bottles are clean.</p></div>
</section>
<!-- 4 -->
<section class="py-12 bg-white dark:bg-gray-900">
    <div class="container mx-auto px-4 max-w-3xl border-t dark:border-gray-800 pt-8"><h4 class="font-bold">By John Doe</h4><p class="text-gray-500 text-sm">Oct 20, 2026</p></div>
</section>
<!-- 5 -->
<section class="py-20 bg-lightBg dark:bg-gray-800 text-center">
    <div class="container mx-auto px-4"><h2 class="text-3xl font-bold mb-8">Related Posts</h2><p>Check out our guide on E-Waste.</p></div>
</section>
<!-- 6 -->
<section class="py-20 bg-white dark:bg-gray-900 text-center">
    <div class="container mx-auto px-4"><div class="bg-primary text-white p-12 rounded-3xl"><h2 class="text-4xl font-bold mb-6">Start Recycling Today</h2><a href="customer-dashboard.html" class="px-8 py-4 bg-white text-primary rounded-full font-bold">Schedule Pickup</a></div></div>
</section>
"""

PAGES['contact.html'] = """
<!-- 1 -->
<section class="relative bg-darkBg text-white py-24 overflow-hidden">
    <div class="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?auto=format&w=1920&q=80')] bg-cover bg-center opacity-40"></div>
    <div class="container mx-auto px-4 relative z-10 text-center"><h1 class="text-5xl font-bold mb-4">Contact Us</h1></div>
</section>
<!-- 2 -->
<section class="py-20 bg-white dark:bg-gray-900">
    <div class="container mx-auto px-4 max-w-2xl text-center"><h2 class="text-3xl font-bold mb-8">Send a Message</h2><form class="space-y-4 text-left"><input type="text" placeholder="Name" class="w-full p-3 border rounded dark:bg-gray-800 dark:border-gray-700"><input type="email" placeholder="Email" class="w-full p-3 border rounded dark:bg-gray-800 dark:border-gray-700"><textarea placeholder="Message" class="w-full p-3 border rounded dark:bg-gray-800 dark:border-gray-700 h-32"></textarea><button type="button" class="bg-primary text-white px-8 py-3 rounded font-bold">Send</button></form></div>
</section>
<!-- 3 -->
<section class="py-20 bg-lightBg dark:bg-gray-800 text-center">
    <div class="container mx-auto px-4"><h2 class="text-3xl font-bold mb-8">Our Info</h2><p>Email: support@ecoscrap.com | Phone: 1800-SCRAP</p></div>
</section>
<!-- 4 -->
<section class="py-20 bg-white dark:bg-gray-900 text-center">
    <div class="container mx-auto px-4"><div class="bg-gray-300 dark:bg-gray-800 h-64 rounded-2xl flex items-center justify-center text-gray-500">Map Placeholder</div></div>
</section>
<!-- 5 -->
<section class="py-20 bg-lightBg dark:bg-gray-800 text-center">
    <div class="container mx-auto px-4"><h2 class="text-3xl font-bold mb-8">FAQ</h2><p>Check our How It Works page for common questions.</p></div>
</section>
<!-- 6 -->
<section class="py-20 bg-white dark:bg-gray-900 text-center">
    <div class="container mx-auto px-4"><div class="bg-primary text-white p-12 rounded-3xl"><h2 class="text-4xl font-bold mb-6">Want to schedule instead?</h2><a href="customer-dashboard.html" class="px-8 py-4 bg-white text-primary rounded-full font-bold">Schedule Pickup</a></div></div>
</section>
"""

# WRITE ALL PUBLIC PAGES
for fname, body in PAGES.items():
    with open(os.path.join(BASE_DIR, fname), 'w', encoding='utf-8') as f:
        f.write(make_page("EcoScrap", body))

print("Public pages written")
