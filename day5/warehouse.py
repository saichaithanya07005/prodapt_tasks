p = ["Laptop", "Mouse", "Keyboard"]

# Add urgent product
p.append("Monitor")
print("After append:", p)

# Combine with another warehouse
n = ["Tablet", "Webcam"]
p.extend(n)
print("After extend:", p)

# Remove discontinued product
p.remove("Mouse")
print("After remove:", p)

# Process shipped product
s = p.pop()
print("Shipped product:", s)
print("After pop:", p)

# Count occurrences
print("Laptop count:", p.count("Laptop"))

# Find Monitor position
print("Monitor index:", p.index("Monitor"))

# Sort products
p.sort()
print("Sorted:", p)

# Reverse display order
p.reverse()
print("Reversed:", p)

# Backup copy
b = p.copy()
print("Backup:", b)

# Clear temporary inventory
t = b.copy()
t.clear()
print("Temporary list after clear:", t)