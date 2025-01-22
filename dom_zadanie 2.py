# задание 2

zarplata = float(input("Введите сумму вашей зарплаты: "))
kredit = float(input("Введите сумму ежемесячного платежа по кредиту: "))
kommunal = float(input("Введите сумму задолженности за коммунальные услуги: "))
itog = float(zarplata - kredit - kommunal)
print(itog)

zarplata = float(input("Введите сумму вашей зарплаты: "))
kredit = float(input("Введите сумму ежемесячного платежа по кредиту: "))
kommunal = float(input("Введите сумму задолженности за коммунальные услуги: "))
itog = float(zarplata - kredit - kommunal)
print(f"После всех выплат у вас останется {itog}")

zarplata = float(input("Введите сумму вашей зарплаты: "))
kredit = float(input("Введите сумму ежемесячного платежа по кредиту: "))
kommunal = float(input("Введите сумму задолженности за коммунальные услуги: "))
itog = float(zarplata - kredit - kommunal)
print("После внесения всех платежей у вас останется {}".format(itog))