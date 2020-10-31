# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

mesesTotales=0

extra_payment_start_month = input("Introduzca el mes de inicio de paga extra ")
extra_payment_end_month = input("introduzca el mes de fin de paga extra ")
extra_payment = input("introduzca el cantidad de paga extra ")
extra_payment = int(extra_payment)
extra_payment_end_month=int(extra_payment_end_month)
extra_payment_start_month= int(extra_payment_start_month)
while mesesTotales < extra_payment_start_month:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    mesesTotales = mesesTotales + 1
    print (mesesTotales, round(principal,2))

while mesesTotales < extra_payment_end_month:
    principal = principal * (1+rate/12) - payment - extra_payment
    total_paid = total_paid + payment + extra_payment
    mesesTotales = mesesTotales + 1 
    print (mesesTotales, round(principal,2))
while principal > 2684.11:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    mesesTotales = mesesTotales + 1
    print (mesesTotales, round(principal,2))

print('Total paid', total_paid+principal, "en", mesesTotales, "meses")