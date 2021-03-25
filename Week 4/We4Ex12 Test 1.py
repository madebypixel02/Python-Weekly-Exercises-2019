amount = float(input("Enter the amount of money you'd like to convert: "))

if amount // 500 >= 1:
    print(f"500€: {int(amount // 500)}")
    amount = amount - 500 * (amount // 500)

if amount // 200 >= 1:
    print(f"200€: {int(amount // 200)}")
    amount = amount - 200 * (amount // 200)

if amount // 100 >= 1:
     print(f"100€: {int(amount // 100)}")
     amount = amount - 100 * (amount // 100)

if amount // 50 >= 1:
    print(f"50€: {int(amount // 50)}")
    amount = amount - 50 * (amount // 50)

if amount // 20 >= 1:
    print(f"20€: {int(amount // 20)}")
    amount = amount - 20 * (amount // 20)

if amount // 10 >= 1:
    print(f"10€: {int(amount // 10)}")
    amount = amount - 10 * (amount // 10)

if amount // 5 >= 1:
    print(f"5€: {int(amount // 5)}")
    amount = amount - 5 * (amount // 5)

if amount // 2 >= 1:
    print(f"2€: {int(amount // 2)}")
    amount = amount - 2 * (amount // 2)

if amount // 1 >= 1:
    print(f"1€: {int(amount // 1)}")
    amount = amount - 1 * (amount // 1)

if amount // 0.5 >= 1:
    print(f"0.5€: {int(amount // 0.5)}")
    amount = amount - 0.5 * (amount // 0.5) + 0.00001

if amount // 0.2 >= 1:
    print(f"0.2€: {int(amount // 0.2)}")
    amount = amount - 0.2 * (amount // 0.2) + 0.00001
# Note: I added + 0.00001 in the line above because I noticed that otherwise the resulting amount would be 0.00001 (approximately) less than it should be.

if amount // 0.1 >= 1:
    print(f"0.1€: {int(amount // 0.1)}")
    amount = amount - 0.1 * (amount // 0.1) + 0.00001

if amount // 0.05 >= 1:
    print(f"0.05€: {int(amount // 0.05)}")
    amount = amount - 0.05 * (amount // 0.05) + 0.00001

if amount // 0.02 >= 1:
    print(f"0.02€: {int(amount // 0.02)}")
    amount = amount - 0.02 * (amount // 0.02) + 0.00001

if amount // 0.01 >= 1:
    print(f"0.01€: {int(amount // 0.01)}")
    amount = amount - 0.01 * (amount // 0.01) + 0.00001
# Note to self: amount * 100 everywhere, and /100 when printing.