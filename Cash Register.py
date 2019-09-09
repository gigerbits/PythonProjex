#Logan cannon
#9/9/2019
#Cash register

#Variables for reciept printing
num_items = 4
cost_per_item = 10.00
tax_rate = 0.08
sub_total = num_items*cost_per_item
tax_amount = sub_total*tax_rate
total_price = tax_amount + sub_total
sep1 = ": "
sep2 = ": $"
#Reciept
print('''Thank you for shopping at
pymart
We hope you come again!

Sales Recipt''')
print("_________________________")
print("Number of items        ",num_items,sep=sep1)
print("Cost per item             ",cost_per_item,sep=sep2)
print("Taxation rate             ",tax_rate,sep=sep1)
print("Total Tax                    ",tax_amount,sep=sep2)
print("_____________________±___")
print("TOTAL SALE PRICE ",total_price,sep=sep2)
print('''

Sign Here ↓
_________________________''')
input("Enter to close")
