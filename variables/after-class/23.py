paidAmount = float(input("Enter the amount you paid: "))
vat = paidAmount * 0.23
# Display amount and vat rounded to 2nd decimal position
print(f"Amount:{paidAmount:10.2f} zł ")
print(f"VAT 23%:{vat:10.2f} zł ")