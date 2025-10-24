a = input("Expression: ")

q = a.split()
x = float(q[0])
y = q[1]
z = float(q[2])

if "+" in y:
    w = x + z
elif "-" in y:
    w = x - z
elif "*" in y:
    w = x * z
elif "/" in y:
    w = x / z

print(w)
