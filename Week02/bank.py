# This program adds two amounts in cents & formats them as euro with a € sign and decimal place between the euro & cents.

Amount1 = int(input("Enter amount 1 (in cents): "))
Amount2 = int(input("Enter amount 2 (in cents): "))
Total = (Amount1 + Amount2)/100
print (f'The sum of these is €{Total}')