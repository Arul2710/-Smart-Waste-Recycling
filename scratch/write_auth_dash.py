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

login_content = """
<div>
    <h1 class="text-3xl font-bold mb-2 text-gray-900 dark:text-white">Welcome Back!</h1>
    <p class="text-gray-600 dark:text-gray-400 mb-8">Please enter your details to sign in.</p>
    <form class="space-y-4" onsubmit="event.preventDefault(); window.location.href='customer-dashboard.html';">
        <div><label class="block text-sm font-medium mb-1">Email or Phone</label><input type="text" class="w-full p-3 border rounded dark:bg-gray-800 dark:border-gray-700 outline-none focus:border-primary" required></div>
        <div><label class="block text-sm font-medium mb-1">Password</label><div class="relative"><input type="password" class="w-full p-3 border rounded dark:bg-gray-800 dark:border-gray-700 outline-none focus:border-primary" required><button type="button" class="absolute right-3 top-3 text-gray-500"><i class="fa-solid fa-eye"></i></button></div></div>
        <div class="flex justify-between items-center">
            <label class="flex items-center gap-2 text-sm"><input type="checkbox"> Remember me</label>
            <a href="forgot-password.html" class="text-sm text-primary hover:underline">Forgot Password?</a>
        </div>
        <button type="submit" class="w-full py-3 bg-primary hover:bg-primaryDark text-white text-center rounded-lg font-bold mt-4 transition">Login</button>
    </form>
    <div class="my-6 flex items-center before:flex-1 before:border-t before:border-gray-200 dark:before:border-gray-700 after:flex-1 after:border-t after:border-gray-200 dark:after:border-gray-700"><span class="px-4 text-sm text-gray-500">or sign in with</span></div>
    <div class="flex gap-4">
        <button class="flex-1 py-2 border rounded-lg hover:bg-gray-50 dark:border-gray-700 dark:hover:bg-gray-800 transition"><i class="fa-brands fa-google text-red-500"></i></button>
        <button class="flex-1 py-2 border rounded-lg hover:bg-gray-50 dark:border-gray-700 dark:hover:bg-gray-800 transition"><i class="fa-brands fa-facebook text-blue-600"></i></button>
        <button class="flex-1 py-2 border rounded-lg hover:bg-gray-50 dark:border-gray-700 dark:hover:bg-gray-800 transition"><i class="fa-brands fa-apple text-gray-900 dark:text-white"></i></button>
    </div>
    <div class="mt-8 text-center text-sm text-gray-600 dark:text-gray-400">
        Don't have an account? <a href="signup.html" class="text-primary font-bold hover:underline">Sign up</a>
    </div>
</div>
"""

signup_content = """
<div>
    <h1 class="text-3xl font-bold mb-2 text-gray-900 dark:text-white">Create an Account</h1>
    <p class="text-gray-600 dark:text-gray-400 mb-8">Join EcoScrap today and start earning.</p>
    <form class="space-y-4" onsubmit="event.preventDefault(); window.location.href='customer-dashboard.html';">
        <div class="grid grid-cols-2 gap-4">
            <div><label class="block text-sm font-medium mb-1">Full Name</label><input type="text" class="w-full p-2 border rounded dark:bg-gray-800 dark:border-gray-700 outline-none focus:border-primary" required></div>
            <div><label class="block text-sm font-medium mb-1">Phone</label><input type="tel" class="w-full p-2 border rounded dark:bg-gray-800 dark:border-gray-700 outline-none focus:border-primary" required></div>
        </div>
        <div><label class="block text-sm font-medium mb-1">Email</label><input type="email" class="w-full p-2 border rounded dark:bg-gray-800 dark:border-gray-700 outline-none focus:border-primary" required></div>
        <div><label class="block text-sm font-medium mb-1">Location</label><select class="w-full p-2 border rounded dark:bg-gray-800 dark:border-gray-700 outline-none focus:border-primary"><option>Delhi NCR</option><option>Mumbai</option><option>Bangalore</option><option>Pune</option></select></div>
        <div class="grid grid-cols-2 gap-4">
            <div><label class="block text-sm font-medium mb-1">Password</label><input type="password" class="w-full p-2 border rounded dark:bg-gray-800 dark:border-gray-700 outline-none focus:border-primary" required></div>
            <div><label class="block text-sm font-medium mb-1">Confirm</label><input type="password" class="w-full p-2 border rounded dark:bg-gray-800 dark:border-gray-700 outline-none focus:border-primary" required></div>
        </div>
        <label class="flex items-center gap-2 text-sm"><input type="checkbox" required> I agree to the Terms & Conditions</label>
        <button type="submit" class="w-full py-3 bg-primary hover:bg-primaryDark text-white text-center rounded-lg font-bold mt-4 transition">Create Account</button>
    </form>
    <div class="my-6 flex items-center before:flex-1 before:border-t before:border-gray-200 dark:before:border-gray-700 after:flex-1 after:border-t after:border-gray-200 dark:after:border-gray-700"><span class="px-4 text-sm text-gray-500">or sign up with</span></div>
    <div class="flex gap-4">
        <button class="flex-1 py-2 border rounded-lg hover:bg-gray-50 dark:border-gray-700 dark:hover:bg-gray-800 transition"><i class="fa-brands fa-google text-red-500"></i></button>
        <button class="flex-1 py-2 border rounded-lg hover:bg-gray-50 dark:border-gray-700 dark:hover:bg-gray-800 transition"><i class="fa-brands fa-facebook text-blue-600"></i></button>
        <button class="flex-1 py-2 border rounded-lg hover:bg-gray-50 dark:border-gray-700 dark:hover:bg-gray-800 transition"><i class="fa-brands fa-apple text-gray-900 dark:text-white"></i></button>
    </div>
    <div class="mt-8 text-center text-sm text-gray-600 dark:text-gray-400">
        Already have an account? <a href="login.html" class="text-primary font-bold hover:underline">Sign in</a>
    </div>
</div>
"""

with open(os.path.join(BASE_DIR, "login.html"), "w", encoding="utf-8") as f:
    f.write(AUTH_BASE.format(title="Login", content=login_content, img_url="https://images.unsplash.com/photo-1532996122724-e3c354a0b15b?auto=format&w=1920&q=80", msg_title="Join the Green Revolution.", msg_desc="Recycle your waste, earn rewards, and help build a sustainable future."))

with open(os.path.join(BASE_DIR, "signup.html"), "w", encoding="utf-8") as f:
    f.write(AUTH_BASE.format(title="Sign Up", content=signup_content, img_url="https://images.unsplash.com/photo-1604187351574-c75ca79f5807?auto=format&w=1920&q=80", msg_title="Start Earning Today.", msg_desc="Sign up to request pickups, track earnings, and make a real environmental impact."))


# DASHBOARDS
DASH_BASE = """<!DOCTYPE html>
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
<body class="bg-lightBg dark:bg-darkBg text-gray-800 dark:text-gray-200 transition-colors duration-300 font-sans flex h-screen overflow-hidden">
    <!-- Sidebar -->
    <aside class="w-64 bg-white dark:bg-gray-900 border-r border-gray-200 dark:border-gray-800 hidden lg:flex flex-col h-full shrink-0">
        <div class="h-20 flex items-center px-6 border-b border-gray-200 dark:border-gray-800 shrink-0">
            <a href="index.html" class="flex items-center gap-2">
                <i class="fa-solid fa-recycle text-2xl text-primary"></i><span class="text-xl font-bold text-primaryDark dark:text-primaryLight">EcoScrap</span>
            </a>
        </div>
        <div class="flex-grow overflow-y-auto py-4 px-3 space-y-1">
            {nav_items}
        </div>
        <div class="p-4 border-t border-gray-200 dark:border-gray-800 shrink-0">
            <button id="theme-toggle-btn" class="w-full flex items-center gap-3 px-3 py-2 rounded-lg text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800 transition">
                <i class="fa-solid fa-moon dark:hidden"></i><i class="fa-solid fa-sun hidden dark:block text-yellow-400"></i> Dark Mode
            </button>
            <button id="rtl-toggle-btn" class="w-full flex items-center gap-3 px-3 py-2 rounded-lg text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800 transition">
                <i class="fa-solid fa-language"></i> RTL Toggle
            </button>
            <a href="login.html" class="w-full flex items-center gap-3 px-3 py-2 mt-2 text-red-600 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-lg transition">
                <i class="fa-solid fa-right-from-bracket"></i> Logout
            </a>
        </div>
    </aside>
    
    <!-- Main Content -->
    <div class="flex-1 flex flex-col h-full overflow-hidden">
        <!-- Top Header -->
        <header class="h-20 bg-white dark:bg-gray-900 border-b border-gray-200 dark:border-gray-800 flex items-center justify-between px-6 shrink-0">
            <div class="flex items-center gap-4">
                <button class="lg:hidden text-2xl text-gray-700 dark:text-gray-300"><i class="fa-solid fa-bars"></i></button>
                <h2 class="text-xl font-bold">{page_name}</h2>
            </div>
            <div class="flex items-center gap-4">
                <button class="p-2 text-gray-500 hover:text-primary relative"><i class="fa-solid fa-bell"></i><span class="absolute top-1 right-1 w-2 h-2 bg-red-500 rounded-full"></span></button>
                <div class="w-10 h-10 bg-primary text-white flex items-center justify-center rounded-full font-bold">U</div>
            </div>
        </header>
        <main class="flex-1 overflow-y-auto p-4 md:p-6 space-y-6">
            {content}
        </main>
    </div>
    <script src="js/theme.js"></script>
    <script src="js/rtl.js"></script>
    <script src="js/dashboard.js"></script>
</body>
</html>
"""

customer_nav = """
<a href="#" class="flex items-center gap-3 px-3 py-2 bg-primary/10 text-primary rounded-lg font-medium"><i class="fa-solid fa-chart-pie w-5"></i> Dashboard Overview</a>
<a href="#" class="flex items-center gap-3 px-3 py-2 text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800 rounded-lg transition"><i class="fa-solid fa-truck-pickup w-5"></i> Schedule Scrap Pickup</a>
<a href="#" class="flex items-center gap-3 px-3 py-2 text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800 rounded-lg transition"><i class="fa-solid fa-list-ul w-5"></i> My Pickup Requests</a>
<a href="#" class="flex items-center gap-3 px-3 py-2 text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800 rounded-lg transition"><i class="fa-solid fa-spinner w-5"></i> Pickup Status</a>
<a href="#" class="flex items-center gap-3 px-3 py-2 text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800 rounded-lg transition"><i class="fa-solid fa-scale-balanced w-5"></i> Scrap Weight History</a>
<a href="#" class="flex items-center gap-3 px-3 py-2 text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800 rounded-lg transition"><i class="fa-solid fa-money-bill-wave w-5"></i> Payout History</a>
<a href="#" class="flex items-center gap-3 px-3 py-2 text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800 rounded-lg transition"><i class="fa-solid fa-credit-card w-5"></i> Payment Preferences</a>
<a href="#" class="flex items-center gap-3 px-3 py-2 text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800 rounded-lg transition"><i class="fa-solid fa-map-location-dot w-5"></i> Saved Addresses</a>
<a href="#" class="flex items-center gap-3 px-3 py-2 text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800 rounded-lg transition"><i class="fa-solid fa-bell w-5"></i> Notifications</a>
<a href="#" class="flex items-center gap-3 px-3 py-2 text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800 rounded-lg transition"><i class="fa-solid fa-gear w-5"></i> Profile Settings</a>
"""

admin_nav = """
<a href="#" class="flex items-center gap-3 px-3 py-2 bg-primary/10 text-primary rounded-lg font-medium"><i class="fa-solid fa-gauge w-5"></i> Dashboard Overview</a>
<a href="#" class="flex items-center gap-3 px-3 py-2 text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800 rounded-lg transition"><i class="fa-solid fa-users w-5"></i> Customer Management</a>
<a href="#" class="flex items-center gap-3 px-3 py-2 text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800 rounded-lg transition"><i class="fa-solid fa-clipboard-list w-5"></i> Pickup Requests</a>
<a href="#" class="flex items-center gap-3 px-3 py-2 text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800 rounded-lg transition"><i class="fa-solid fa-calendar-check w-5"></i> Pickup Scheduling</a>
<a href="#" class="flex items-center gap-3 px-3 py-2 text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800 rounded-lg transition"><i class="fa-solid fa-user-tie w-5"></i> Collector Management</a>
<a href="#" class="flex items-center gap-3 px-3 py-2 text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800 rounded-lg transition"><i class="fa-solid fa-boxes-stacked w-5"></i> Scrap Categories</a>
<a href="#" class="flex items-center gap-3 px-3 py-2 text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800 rounded-lg transition"><i class="fa-solid fa-tags w-5"></i> Rate Card Management</a>
<a href="#" class="flex items-center gap-3 px-3 py-2 text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800 rounded-lg transition"><i class="fa-solid fa-scale-balanced w-5"></i> Weight Verification</a>
<a href="#" class="flex items-center gap-3 px-3 py-2 text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800 rounded-lg transition"><i class="fa-solid fa-money-check-dollar w-5"></i> Payout Management</a>
<a href="#" class="flex items-center gap-3 px-3 py-2 text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800 rounded-lg transition"><i class="fa-solid fa-wallet w-5"></i> Payment History</a>
<a href="#" class="flex items-center gap-3 px-3 py-2 text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800 rounded-lg transition"><i class="fa-solid fa-map-location-dot w-5"></i> Locations Management</a>
<a href="#" class="flex items-center gap-3 px-3 py-2 text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800 rounded-lg transition"><i class="fa-solid fa-chart-line w-5"></i> Reports & Analytics</a>
<a href="#" class="flex items-center gap-3 px-3 py-2 text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800 rounded-lg transition"><i class="fa-solid fa-newspaper w-5"></i> Blog Management</a>
<a href="#" class="flex items-center gap-3 px-3 py-2 text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800 rounded-lg transition"><i class="fa-solid fa-envelope w-5"></i> Contact Messages</a>
<a href="#" class="flex items-center gap-3 px-3 py-2 text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800 rounded-lg transition"><i class="fa-solid fa-gear w-5"></i> Website Settings</a>
<a href="#" class="flex items-center gap-3 px-3 py-2 text-gray-600 dark:text-gray-400 hover:bg-gray-50 dark:hover:bg-gray-800 rounded-lg transition"><i class="fa-solid fa-user-gear w-5"></i> Profile Settings</a>
"""

cust_content = """
<!-- Stats -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
    <div class="bg-white dark:bg-gray-800 p-4 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700 flex items-center gap-4">
        <div class="w-12 h-12 rounded-full bg-blue-100 text-blue-600 flex items-center justify-center text-xl"><i class="fa-solid fa-clipboard-list"></i></div>
        <div><h4 class="text-sm text-gray-500">Total Pickups</h4><div class="text-2xl font-bold">12</div></div>
    </div>
    <div class="bg-white dark:bg-gray-800 p-4 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700 flex items-center gap-4">
        <div class="w-12 h-12 rounded-full bg-orange-100 text-orange-600 flex items-center justify-center text-xl"><i class="fa-solid fa-clock"></i></div>
        <div><h4 class="text-sm text-gray-500">Upcoming</h4><div class="text-2xl font-bold">1</div></div>
    </div>
    <div class="bg-white dark:bg-gray-800 p-4 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700 flex items-center gap-4">
        <div class="w-12 h-12 rounded-full bg-purple-100 text-purple-600 flex items-center justify-center text-xl"><i class="fa-solid fa-weight-scale"></i></div>
        <div><h4 class="text-sm text-gray-500">Total Weight</h4><div class="text-2xl font-bold">125 KG</div></div>
    </div>
    <div class="bg-white dark:bg-gray-800 p-4 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700 flex items-center gap-4">
        <div class="w-12 h-12 rounded-full bg-green-100 text-green-600 flex items-center justify-center text-xl"><i class="fa-solid fa-indian-rupee-sign"></i></div>
        <div><h4 class="text-sm text-gray-500">Total Payout</h4><div class="text-2xl font-bold">₹ 4,500</div></div>
    </div>
</div>

<div class="grid lg:grid-cols-3 gap-6">
    <div class="lg:col-span-1 bg-white dark:bg-gray-800 p-6 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700">
        <h3 class="font-bold text-lg mb-4">Schedule a Pickup</h3>
        <form class="space-y-4" onsubmit="event.preventDefault(); alert('Pickup scheduled successfully!');">
            <div><label class="block text-sm mb-1">Categories</label><select class="w-full p-2 border rounded dark:bg-gray-700 dark:border-gray-600"><option>Mixed</option><option>Paper</option><option>Metal</option></select></div>
            <div><label class="block text-sm mb-1">Est. Weight</label><select class="w-full p-2 border rounded dark:bg-gray-700 dark:border-gray-600"><option>10-20 KG</option><option>20-50 KG</option></select></div>
            <div><label class="block text-sm mb-1">Date</label><input type="date" class="w-full p-2 border rounded dark:bg-gray-700 dark:border-gray-600"></div>
            <div><label class="block text-sm mb-1">Payment Pref.</label><select class="w-full p-2 border rounded dark:bg-gray-700 dark:border-gray-600"><option>UPI</option><option>Bank Transfer</option><option>Cash</option></select></div>
            <button class="w-full py-2 bg-primary text-white rounded font-bold hover:bg-primaryDark transition">Confirm Pickup</button>
        </form>
    </div>
    <div class="lg:col-span-2 bg-white dark:bg-gray-800 p-6 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 overflow-x-auto">
        <h3 class="font-bold text-lg mb-4">My Pickup Requests</h3>
        <table class="w-full text-left min-w-[600px]">
            <thead><tr class="text-gray-500 text-sm border-b dark:border-gray-700"><th class="pb-2">ID</th><th class="pb-2">Date</th><th class="pb-2">Status</th><th class="pb-2">Weight</th><th class="pb-2">Payout</th><th class="pb-2">Action</th></tr></thead>
            <tbody>
                <tr class="border-b dark:border-gray-700"><td class="py-3 font-medium">#REQ-101</td><td>15 Oct</td><td><span class="bg-orange-100 text-orange-600 px-2 py-1 rounded text-xs">Collector on Way</span></td><td>~15 KG</td><td>Pending</td><td><button class="text-red-500 text-sm hover:underline">Cancel</button></td></tr>
                <tr class="border-b dark:border-gray-700"><td class="py-3 font-medium">#REQ-098</td><td>01 Oct</td><td><span class="bg-green-100 text-green-600 px-2 py-1 rounded text-xs">Completed</span></td><td>22.5 KG</td><td>₹ 650</td><td><button class="text-primary text-sm hover:underline">View</button></td></tr>
            </tbody>
        </table>
    </div>
</div>
"""

admin_content = """
<!-- Stats -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
    <div class="bg-white dark:bg-gray-800 p-4 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700 flex items-center gap-4">
        <div class="w-12 h-12 rounded-full bg-blue-100 text-blue-600 flex items-center justify-center text-xl"><i class="fa-solid fa-users"></i></div>
        <div><h4 class="text-sm text-gray-500">Total Customers</h4><div class="text-2xl font-bold">1,402</div></div>
    </div>
    <div class="bg-white dark:bg-gray-800 p-4 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700 flex items-center gap-4">
        <div class="w-12 h-12 rounded-full bg-orange-100 text-orange-600 flex items-center justify-center text-xl"><i class="fa-solid fa-clock"></i></div>
        <div><h4 class="text-sm text-gray-500">Pending Pickups</h4><div class="text-2xl font-bold">34</div></div>
    </div>
    <div class="bg-white dark:bg-gray-800 p-4 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700 flex items-center gap-4">
        <div class="w-12 h-12 rounded-full bg-purple-100 text-purple-600 flex items-center justify-center text-xl"><i class="fa-solid fa-weight-scale"></i></div>
        <div><h4 class="text-sm text-gray-500">Total Weight</h4><div class="text-2xl font-bold">28.5k KG</div></div>
    </div>
    <div class="bg-white dark:bg-gray-800 p-4 rounded-xl shadow-sm border border-gray-100 dark:border-gray-700 flex items-center gap-4">
        <div class="w-12 h-12 rounded-full bg-green-100 text-green-600 flex items-center justify-center text-xl"><i class="fa-solid fa-money-bill-wave"></i></div>
        <div><h4 class="text-sm text-gray-500">Total Payouts</h4><div class="text-2xl font-bold">₹ 4.2M</div></div>
    </div>
</div>

<div class="grid lg:grid-cols-2 gap-6">
    <div class="bg-white dark:bg-gray-800 p-6 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 overflow-x-auto">
        <h3 class="font-bold text-lg mb-4 flex justify-between">Pickup Requests <button class="text-sm text-primary">View All</button></h3>
        <table class="w-full text-left min-w-[500px]">
            <thead><tr class="text-gray-500 text-sm border-b dark:border-gray-700"><th class="pb-2">Req ID</th><th class="pb-2">Customer</th><th class="pb-2">Location</th><th class="pb-2">Action</th></tr></thead>
            <tbody>
                <tr class="border-b dark:border-gray-700"><td class="py-3 font-medium">#REQ-101</td><td>Rahul S.</td><td>Delhi NCR</td><td><button onclick="this.innerText='Assigned';this.classList.add('opacity-50')" class="bg-primary text-white px-3 py-1 rounded text-sm hover:bg-primaryDark">Assign</button></td></tr>
                <tr class="border-b dark:border-gray-700"><td class="py-3 font-medium">#REQ-102</td><td>Priya K.</td><td>Mumbai</td><td><button onclick="this.innerText='Assigned';this.classList.add('opacity-50')" class="bg-primary text-white px-3 py-1 rounded text-sm hover:bg-primaryDark">Assign</button></td></tr>
            </tbody>
        </table>
    </div>
    <div class="bg-white dark:bg-gray-800 p-6 rounded-2xl shadow-sm border border-gray-100 dark:border-gray-700 overflow-x-auto">
        <h3 class="font-bold text-lg mb-4">Rate Card Management</h3>
        <table class="w-full text-left min-w-[400px]">
            <thead><tr class="text-gray-500 text-sm border-b dark:border-gray-700"><th class="pb-2">Material</th><th class="pb-2">Price</th><th class="pb-2">Update</th></tr></thead>
            <tbody>
                <tr class="border-b dark:border-gray-700"><td class="py-3 font-medium">Paper</td><td class="font-bold text-primary">₹ 14 / KG</td><td><div class="flex gap-2"><input type="number" value="14" class="w-16 p-1 border rounded dark:bg-gray-700 dark:border-gray-600"><button class="text-blue-500"><i class="fa-solid fa-save"></i></button></div></td></tr>
                <tr class="border-b dark:border-gray-700"><td class="py-3 font-medium">Iron</td><td class="font-bold text-primary">₹ 28 / KG</td><td><div class="flex gap-2"><input type="number" value="28" class="w-16 p-1 border rounded dark:bg-gray-700 dark:border-gray-600"><button class="text-blue-500"><i class="fa-solid fa-save"></i></button></div></td></tr>
            </tbody>
        </table>
    </div>
</div>
"""

with open(os.path.join(BASE_DIR, "customer-dashboard.html"), "w", encoding="utf-8") as f:
    f.write(DASH_BASE.format(title="Customer Dashboard", nav_items=customer_nav, page_name="Customer Dashboard Overview", content=cust_content))

with open(os.path.join(BASE_DIR, "admin-dashboard.html"), "w", encoding="utf-8") as f:
    f.write(DASH_BASE.format(title="Admin Dashboard", nav_items=admin_nav, page_name="Admin Dashboard Overview", content=admin_content))

print("Auth and Dash pages written")
