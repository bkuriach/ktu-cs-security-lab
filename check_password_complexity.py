import re

def check_password_complexity(password):
    if len(password) < 8:
        return "Password should be at least 8 characters long"
    elif not re.search("[a-z]", password):
        return "Password should contain at least one lowercase letter"
    elif not re.search("[A-Z]", password):
        return "Password should contain at least one uppercase letter"
    elif not re.search("[0-9]", password):
        return "Password should contain at least one number"
    elif not re.search("[!@#$%^&*]", password):
        return "Password should contain at least one special character (!@#$%^&*)"
    else:
        return "Password is complex enough"

password = "qwerty"
print(check_password_complexity(password))


password = "Qwerty123!"
print(check_password_complexity(password))