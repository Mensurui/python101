def tax_rate_calculator (bill, taxRate):
    return round(bill * taxRate)/100.00


bill = input("Enter your bill: ")
tax_rate = input("Enter tax rate: ")
print("Total tax " ,tax_rate_calculator(int(bill), int(tax_rate)))