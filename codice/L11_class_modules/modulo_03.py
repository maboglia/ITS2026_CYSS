import datetime as dt

oggi = dt.date.today()


print(oggi)

print(oggi.year)
print(oggi.month)
print(oggi.day)

adesso = dt.datetime.now()
print(adesso)
print(adesso.year, adesso.month, adesso.day)
print(adesso.hour, adesso.minute, adesso.second)

print(adesso.strftime("%d/%m/%Y"))      # 11/04/2026
print(adesso.strftime("%H:%M:%S"))      # 15:30:10
print(adesso.strftime("%d/%m/%Y %H:%M"))

s = "11/04/2026 15:30"
ddt = dt.datetime.strptime(s, "%d/%m/%Y %H:%M")

print(ddt)

d1 = dt.date(2026, 4, 11)
d2 = dt.date(2026, 4, 20)

diff = d2 - d1
print(diff.days)   # 9

fra_7_giorni = adesso + dt.timedelta(days=7)
ieri = adesso - dt.timedelta(days=1)
fine_pausa = adesso + dt.timedelta(minutes=20)


print(fra_7_giorni)
print(ieri)
print(fine_pausa)