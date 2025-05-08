def month_to_season(month):
    if  month == 1 or month == 2 or month == 12 :
        return "зима, одевайся теплее, пей горячий чайочек и не болей"
    elif 3 <= month <= 5:
        return "весна, время готовится к лету, начинаем худеть"
    elif 6 <= month <= 8:
        return "лето. Кайф"
    elif 9 <= month <= 11:
        return "осень, не забудь взять зонтик и витаминки"
    else:
        return "Чел, реально?"

try:
    month = int(input("Введите номер месяца (1-12): "))
    print(month_to_season(month))
except ValueError:
    print("А что ещё придумаешь?")