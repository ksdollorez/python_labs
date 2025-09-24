price = int(input("price (₽): "))
discount = int(input("discount (%): "))
vat = int(input("vat (%): "))

base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

print('База после скидки: '+ str(base)+' ₽')
print('НДС: ' + str(vat_amount) +' ₽')
print("Итого к оплате: "+  str(total) +" ₽")