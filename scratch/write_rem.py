import os

BASE_DIR = r"c:\Users\arulp\OneDrive\Desktop\Local Waste"
os.makedirs(BASE_DIR, exist_ok=True)

AUTH_BASE = """<!DOCTYPE html>
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
<body class="bg-white dark:bg-darkBg text-gray-800 dark:text-gray-200 transition-colors duration-300 font-sans h-screen flex">
    <div class="w-full lg:w-1/2 flex flex-col justify-center px-8 md:px-16 lg:px-24">
        <div class="mb-10 flex justify-between items-center">
            <a href="index.html" class="flex items-center gap-2">
                <i class="fa-solid fa-recycle text-3xl text-primary"></i><span class="text-2xl font-bold text-gray-900 dark:text-white">EcoScrap</span>
            </a>
            <div class="flex gap-2 lg:hidden">
                <button id="mobile-theme-toggle" class="p-2 rounded bg-gray-100 dark:bg-gray-800"><i class="fa-solid fa-moon dark:hidden"></i><i class="fa-solid fa-sun hidden dark:block text-yellow-400"></i></button>
                <button id="mobile-rtl-toggle" class="p-2 rounded bg-gray-100 dark:bg-gray-800"><i class="fa-solid fa-language"></i></button>
            </div>
        </div>
        {content}
    </div>
    <div class="hidden lg:block lg:w-1/2 relative overflow-hidden">
        <div class="absolute inset-0 bg-[url('{img_url}')] bg-cover bg-center"></div>
        <div class="absolute inset-0 bg-primaryDark/80 flex flex-col justify-center p-20 z-10 text-white">
            <div class="absolute top-8 right-8 flex gap-4">
                <button id="theme-toggle-btn" class="p-3 bg-white/20 hover:bg-white/30 rounded-full transition"><i class="fa-solid fa-moon dark:hidden"></i><i class="fa-solid fa-sun hidden dark:block text-yellow-400"></i></button>
                <button id="rtl-toggle-btn" class="p-3 bg-white/20 hover:bg-white/30 rounded-full transition"><i class="fa-solid fa-language"></i></button>
            </div>
            <h2 class="text-5xl font-bold mb-6 leading-tight">{msg_title}</h2>
            <p class="text-xl text-gray-200">{msg_desc}</p>
        </div>
    </div>
    <script src="js/theme.js"></script>
    <script src="js/rtl.js"></script>
</body>
</html>
"""

forgot_content = """
<div>
    <h1 class="text-3xl font-bold mb-2 text-gray-900 dark:text-white">Forgot Password?</h1>
    <p class="text-gray-600 dark:text-gray-400 mb-8">No worries, we'll send you reset instructions.</p>
    <form class="space-y-4" onsubmit="event.preventDefault(); alert('Reset link sent!');">
        <div><label class="block text-sm font-medium mb-1">Email Address</label><input type="email" class="w-full p-3 border rounded dark:bg-gray-800 dark:border-gray-700 outline-none focus:border-primary" required></div>
        <button type="submit" class="w-full py-3 bg-primary hover:bg-primaryDark text-white text-center rounded-lg font-bold mt-4 transition">Send Reset Link</button>
    </form>
    <div class="mt-8 text-center text-sm text-gray-600 dark:text-gray-400">
        <a href="login.html" class="text-primary font-bold hover:underline"><i class="fa-solid fa-arrow-left mr-1"></i> Back to log in</a>
    </div>
</div>
"""
with open(os.path.join(BASE_DIR, "forgot-password.html"), "w", encoding="utf-8") as f:
    f.write(AUTH_BASE.format(title="Forgot Password", content=forgot_content, img_url="https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?auto=format&w=1920&q=80", msg_title="Secure Your Account.", msg_desc="We value your security and privacy."))

# -----------------
# PUBLIC PAGES 6 SECTIONS
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

PAGES['privacy-policy.html'] = """
<!-- 1 -->
<section class="relative bg-darkBg text-white py-24 overflow-hidden">
    <div class="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?auto=format&w=1920&q=80')] bg-cover bg-center opacity-40"></div>
    <div class="container mx-auto px-4 relative z-10 text-center"><h1 class="text-5xl font-bold mb-4">Privacy Policy</h1></div>
</section>
<!-- 2 -->
<section class="py-12 bg-white dark:bg-gray-900">
    <div class="container mx-auto px-4 max-w-4xl"><h2 class="text-2xl font-bold mb-4">1. Information Collection</h2><p>We collect information such as your name, contact details, and location for pickup services.</p></div>
</section>
<!-- 3 -->
<section class="py-12 bg-lightBg dark:bg-gray-800">
    <div class="container mx-auto px-4 max-w-4xl"><h2 class="text-2xl font-bold mb-4">2. Data Usage</h2><p>Your data is strictly used to fulfill pickup requests and communicate updates.</p></div>
</section>
<!-- 4 -->
<section class="py-12 bg-white dark:bg-gray-900">
    <div class="container mx-auto px-4 max-w-4xl"><h2 class="text-2xl font-bold mb-4">3. Data Protection</h2><p>We implement standard security measures to protect your information.</p></div>
</section>
<!-- 5 -->
<section class="py-12 bg-lightBg dark:bg-gray-800 text-center">
    <div class="container mx-auto px-4 max-w-4xl"><p class="text-gray-500 italic">Last Updated: October 2026</p></div>
</section>
<!-- 6 -->
<section class="py-20 bg-white dark:bg-gray-900 text-center">
    <div class="container mx-auto px-4"><div class="bg-primary text-white p-12 rounded-3xl"><h2 class="text-4xl font-bold mb-6">Have concerns?</h2><a href="contact.html" class="px-8 py-4 bg-white text-primary rounded-full font-bold">Contact Us</a></div></div>
</section>
"""

PAGES['terms.html'] = """
<!-- 1 -->
<section class="relative bg-darkBg text-white py-24 overflow-hidden">
    <div class="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?auto=format&w=1920&q=80')] bg-cover bg-center opacity-40"></div>
    <div class="container mx-auto px-4 relative z-10 text-center"><h1 class="text-5xl font-bold mb-4">Terms & Conditions</h1></div>
</section>
<!-- 2 -->
<section class="py-12 bg-white dark:bg-gray-900">
    <div class="container mx-auto px-4 max-w-4xl"><h2 class="text-2xl font-bold mb-4">1. General</h2><p>These terms govern your use of the EcoScrap platform.</p></div>
</section>
<!-- 3 -->
<section class="py-12 bg-lightBg dark:bg-gray-800">
    <div class="container mx-auto px-4 max-w-4xl"><h2 class="text-2xl font-bold mb-4">2. Scrap Quality & Weight</h2><p>Final payout is dependent on physical verification and accurate digital weighing by our agents.</p></div>
</section>
<!-- 4 -->
<section class="py-12 bg-white dark:bg-gray-900">
    <div class="container mx-auto px-4 max-w-4xl"><h2 class="text-2xl font-bold mb-4">3. Payments</h2><p>All payments are processed instantly upon completion of the weighing process.</p></div>
</section>
<!-- 5 -->
<section class="py-12 bg-lightBg dark:bg-gray-800 text-center">
    <div class="container mx-auto px-4 max-w-4xl"><p class="text-gray-500 italic">Last Updated: October 2026</p></div>
</section>
<!-- 6 -->
<section class="py-20 bg-white dark:bg-gray-900 text-center">
    <div class="container mx-auto px-4"><div class="bg-primary text-white p-12 rounded-3xl"><h2 class="text-4xl font-bold mb-6">Questions?</h2><a href="contact.html" class="px-8 py-4 bg-white text-primary rounded-full font-bold">Contact Support</a></div></div>
</section>
"""

PAGES['404.html'] = """
<!-- 1 -->
<section class="relative bg-darkBg text-white py-24 overflow-hidden">
    <div class="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1604187351574-c75ca79f5807?auto=format&w=1920&q=80')] bg-cover bg-center opacity-40"></div>
    <div class="container mx-auto px-4 relative z-10 text-center"><h1 class="text-5xl font-bold mb-4">404 - Not Found</h1></div>
</section>
<!-- 2 -->
<section class="py-12 bg-white dark:bg-gray-900 text-center">
    <div class="container mx-auto px-4"><i class="fa-solid fa-dumpster text-9xl text-gray-300 dark:text-gray-700 mb-8"></i></div>
</section>
<!-- 3 -->
<section class="py-12 bg-lightBg dark:bg-gray-800 text-center">
    <div class="container mx-auto px-4"><h2 class="text-4xl font-bold mb-4">Oops! This Page Is Out of Recycling Range!</h2></div>
</section>
<!-- 4 -->
<section class="py-12 bg-white dark:bg-gray-900 text-center">
    <div class="container mx-auto px-4"><p class="text-xl text-gray-600 dark:text-gray-400">We couldn't find the page you're looking for. It might have been recycled or moved.</p></div>
</section>
<!-- 5 -->
<section class="py-12 bg-lightBg dark:bg-gray-800 text-center">
    <div class="container mx-auto px-4"><a href="index.html" class="px-6 py-3 bg-primary text-white rounded-lg hover:bg-primaryDark font-medium transition">Back to Home</a></div>
</section>
<!-- 6 -->
<section class="py-20 bg-white dark:bg-gray-900 text-center">
    <div class="container mx-auto px-4"><div class="bg-primary text-white p-12 rounded-3xl"><h2 class="text-4xl font-bold mb-6">Need to request a pickup?</h2><a href="customer-dashboard.html" class="px-8 py-4 bg-white text-primary rounded-full font-bold">Schedule Pickup</a></div></div>
</section>
"""

for fname, body in PAGES.items():
    with open(os.path.join(BASE_DIR, fname), 'w', encoding='utf-8') as f:
        f.write(make_page("EcoScrap", body))

print("Remaining pages updated")
