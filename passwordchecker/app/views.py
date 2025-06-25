from django.shortcuts import render
import re 

# Function to check password strength
def check_password_strength(password):
    length = len(password)
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[@$!%*?&#]', password)

    if length >= 8 and has_upper and has_lower and has_digit and has_special:
        return "Strong"
    elif length >= 6 and ((has_upper or has_lower) and has_digit):
        return "Medium"
    else:
        return "Weak"

#  Home page view
def index(request):
    strength = None
    if request.method == "POST":
        password = request.POST.get("password")
        strength = check_password_strength(password)
    return render(request, "checker/index.html", {"strength": strength})
