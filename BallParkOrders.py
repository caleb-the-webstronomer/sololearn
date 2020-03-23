''' Ballpark Orders :: Getting the total cost of four items ordered:
        Items and prices: 
            Cheeseburger: $10;
            Nachos and Pizza : $6.00;
            Coke: $5.00;
            Water: $4.00;
            Tax: 7%;
'''

orders = input().split()
total = 0
tax = 1.07
menu = {
    'Cheeseburger': 10,
    'Nachos': 6,
    'Pizza': 6,
    'Coke': 5,
    'Water': 4
}
    

for order in orders: 
    if order in menu:
        total += menu[order]
    else:
        total += menu['Coke']
        
total *= tax 

print(round(total, 2))
