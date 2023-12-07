v1 = 4
v2 = 5
v3 = 6
v4 = 7

# Twee waardes wisselen (efficient, maar dit kan niet in alle talen)
v1, v2 = v2, v1
print(v1, v2)

# Twee waardes wisselen
temp = v3
v3 = v4
v4 = temp
print(v3, v4)
