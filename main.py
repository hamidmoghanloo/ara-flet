
    print("\nماشین حساب")
    print("1. جمع")
    print("2. تفریق")
    print("3. ضرب")
    print("4. تقسیم")
    print("5. خروج")

    choice = input("انتخاب: ")

    if choice == "5":
        break

    a = float(input("عدد اول: "))
    b = float(input("عدد دوم: "))

    if choice == "1":
        print("نتیجه:", a + b)
    elif choice == "2":
        print("نتیجه:", a - b
    elif choice == "3":
        print("نتیجه:", a * b)
    elif choice == "4":
        if b != 0:
            print("نتیجه:", a / b)
        else:
            print("تقسیم بر صفر مجاز نیست.")
    else:
        print("انتخاب نامعتبر.")