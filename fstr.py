x = "kota"

y = f"Ala ma {x}"
print(y)

y = f"Ala ma {x * 5}"
print(y)

y = f"Ala ma ~~~~{x * 5:>30}~~"
print(y)


y = f"Ala ma ~~~~{x * 5:^30}~~"
print(y)

z = x * 5 # kotakotakota

no_spaces_left = (30 - len(z)) // 2
no_spaces_right = 30 - no_spaces_left - len(z)
print(no_spaces_left, no_spaces_right)
print((" " * no_spaces_left) + z + (" " * no_spaces_right))