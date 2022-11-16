x,y,z = map(int, input("輸入:").split(","))
m = 3000
if x == 1:
    m = m + 10
elif x == 2:
    m = m + 20
elif x == 3:
    m = m - 10
else :
    m = m - 40
    
if y == 1:
    m = m + 10
elif y == 2:
    m = m + 20
elif y == 3:
    m = m - 10
else :
    m = m - 40
    
if z == 1:
    m = m + 10
elif z == 2:
    m = m + 20
elif z == 3:
    m = m - 10
else :
    m = m - 40
print("輸出:", m)