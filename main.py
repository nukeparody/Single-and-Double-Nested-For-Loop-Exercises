for a in range(6):
    print("*" * a)

print()

for b in range(5):
    print("*" * (-b + 5))

print()

for c in range(5, 0, -1):
    for d in range(1, c + 1):
        print(d, end = "")

    print()

for e in range(6):
    for f in range(e):
        print(e, end = "")

    print()

print()

for g in range(6):
    print("    *")