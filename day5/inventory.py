c = 3
p = 4

inv = []
for i in range(c):
    print("Category", i + 1)
    t= []
    for j in range(p):
        q = int(input(f"Product {j + 1}:"))
        t.append(q)
    inv.append(t)
print("\nInventory")

for i in range(c):
    print(f"Category {i + 1}")
    for j in range(p):
        print(f"Product {j + 1}: {inv[i][j]}")