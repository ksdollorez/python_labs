def parse_number(s):
    return float(s.replace(",", "."))


a = input("a:")
b = input("b:")
a = parse_number(a)
b = parse_number(b)
sum = a + b
avg = round((a + b) / 2, 2)
print("sum=" + str(sum) + "; avg=" + str(avg))
