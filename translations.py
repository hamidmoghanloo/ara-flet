TRANSLATIONS = {
    "en": {
        # Login
        "login_title": "Welcome Back",
        "login_subtitle": "Sign in to continue to your dashboard",
        "email_ph": "Email address",
        "password_ph": "Password",
        "login_btn": "LOG IN",
        "no_account": "Don't have an account?",
        "create_account_link": "Create Account",
        "missing_info_title": "Missing info",
        "missing_info_msg": "Please enter both email and password.",
        "login_failed_title": "Login failed",
        "login_failed_msg": "Incorrect email or password.",
        "lang_switch": "فارسی",

        # Register
        "register_title": "Create Account",
        "register_subtitle": "Fill in your details to get started",
        "name_ph": "Full name",
        "age_ph": "Age",
        "confirm_ph": "Confirm password",
        "captcha_ph": "Enter the code shown above",
        "register_btn": "CREATE ACCOUNT",
        "have_account": "Already have an account?",
        "login_link": "Log In",
        "register_missing_msg": "Please fill in every field.",
        "invalid_age_title": "Invalid age",
        "invalid_age_msg": "Age must be a whole number.",
        "invalid_email_title": "Invalid email",
        "invalid_email_msg": "Please enter a valid email address.",
        "mismatch_title": "Password mismatch",
        "mismatch_msg": "Passwords do not match.",
        "captcha_fail_title": "Captcha failed",
        "captcha_fail_msg": "The captcha code is incorrect.",
        "success_title": "Success",
        "register_success_msg": "Account created successfully.",
        "register_fail_title": "Registration failed",
        "already_registered_msg": "That email is already registered.",

        # Dashboard
        "dashboard_title": "Dashboard",
        "signed_in_as": "Signed in as {name}",
        "nav_section": "MAIN",
        "nav_users": "Registered Users",
        "logout": "Log Out",
        "search_ph": "Search by name or email...",
        "refresh_btn": "Refresh",
        "total_users": "Total registered users: {count}",
        "footer_text": "© 2026 AdminPanel — Built with PySide6",
        "col_id": "ID",
        "col_name": "Name",
        "col_age": "Age",
        "col_email": "Email",
        "col_password": "Password",
        "col_registered_at": "Registered At",
    },
    "fa": {
        # Login
        "login_title": "خوش آمدید",
        "login_subtitle": "برای ورود به داشبورد خود وارد شوید",
        "email_ph": "آدرس ایمیل",
        "password_ph": "رمز عبور",
        "login_btn": "ورود",
        "no_account": "حساب کاربری ندارید؟",
        "create_account_link": "ثبت‌نام",
        "missing_info_title": "اطلاعات ناقص",
        "missing_info_msg": "لطفاً ایمیل و رمز عبور را وارد کنید.",
        "login_failed_title": "ورود ناموفق",
        "login_failed_msg": "ایمیل یا رمز عبور اشتباه است.",
        "lang_switch": "English",

        # Register
        "register_title": "ایجاد حساب کاربری",
        "register_subtitle": "برای شروع، اطلاعات خود را وارد کنید",
        "name_ph": "نام کامل",
        "age_ph": "سن",
        "confirm_ph": "تکرار رمز عبور",
        "captcha_ph": "کد نمایش داده‌شده را وارد کنید",
        "register_btn": "ایجاد حساب",
        "have_account": "قبلاً حساب کاربری دارید؟",
        "login_link": "ورود",
        "register_missing_msg": "لطفاً همه فیلدها را پر کنید.",
        "invalid_age_title": "سن نامعتبر",
        "invalid_age_msg": "سن باید یک عدد صحیح باشد.",
        "invalid_email_title": "ایمیل نامعتبر",
        "invalid_email_msg": "لطفاً یک آدرس ایمیل معتبر وارد کنید.",
        "mismatch_title": "عدم تطابق رمز عبور",
        "mismatch_msg": "رمزهای عبور مطابقت ندارند.",
        "captcha_fail_title": "کد امنیتی اشتباه است",
        "captcha_fail_msg": "کد وارد شده صحیح نیست.",
        "success_title": "موفقیت",
        "register_success_msg": "حساب کاربری با موفقیت ایجاد شد.",
        "register_fail_title": "ثبت‌نام ناموفق",
        "already_registered_msg": "این ایمیل قبلاً ثبت شده است.",

        # Dashboard
        "dashboard_title": "داشبورد",
        "signed_in_as": "کاربر وارد شده: {name}",
        "nav_section": "بخش اصلی",
        "nav_users": "کاربران ثبت‌نام‌شده",
        "logout": "خروج",
        "search_ph": "جستجو بر اساس نام یا ایمیل...",
        "refresh_btn": "به‌روزرسانی",
        "total_users": "تعداد کل کاربران: {count}",
        "footer_text": "© ۲۰۲۶ پنل مدیریت — ساخته‌شده با PySide6",
        "col_id": "شناسه",
        "col_name": "نام",
        "col_age": "سن",
        "col_email": "ایمیل",
        "col_password": "رمز عبور",
        "col_registered_at": "تاریخ ثبت‌نام",
    },
}


def t(key, lang="en", **kwargs):
    """Look up a translated string, falling back to English then the raw key."""
    text = TRANSLATIONS.get(lang, TRANSLATIONS["en"]).get(key)
    if text is None:
        text = TRANSLATIONS["en"].get(key, key)
    if kwargs:
        try:
            text = text.format(**kwargs)
        except Exception:
            pass
    return text
