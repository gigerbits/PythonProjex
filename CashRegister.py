#Logan cannon
#9/9/2019
#Cash register

#Variables
num_items = 4
cost_per_item = 10.00
tax_rate = 0.08
sub_total = num_items*cost_per_item
tax_amount = sub_total*tax_rate
total_price = tax_amount + sub_total

#Reciept
print('''Thank you for shopping at
pymart
We hope you come again!

Sales Recipt''')
print("_________________________")
print("Number of items        : "+str(num_items))
print("Cost per item             : $"+str(cost_per_item))
print("Taxation rate             : "+str(tax_rate))
print("Total Tax                    : $"+str(tax_amount))
print("_____________________±___")
print("TOTAL SALE PRICE : $"+str(total_price))
print('''

Sign Here ↓
_________________________''')
