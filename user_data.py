# user-data.py

# حساب‌ها
# username -> password
USERS = {}


# اطلاعات پروفایل کاربران
# username -> profile information
USER_PROFILES = {}


# کاربر فعلی
CURRENT_USER = {
    "username": ""
}


def create_user(username, password):
    """
    ساخت حساب جدید
    """
    USERS[username] = password

    USER_PROFILES[username] = {
        "name": "",
        "username": username,
        "phone": "",
    }


def set_profile(username, name, phone):
    """
    ذخیره اطلاعات پروفایل
    """
    if username not in USER_PROFILES:
        USER_PROFILES[username] = {
            "name": "",
            "username": username,
            "phone": "",
        }

    USER_PROFILES[username]["name"] = name
    USER_PROFILES[username]["phone"] = phone


def get_profile(username):
    """
    دریافت اطلاعات پروفایل
    """
    if username not in USER_PROFILES:
        USER_PROFILES[username] = {
            "name": "",
            "username": username,
            "phone": "",
        }

    return USER_PROFILES[username]