s = ["Geeks", "for", "Geeks"]
for i in s:
    print(i)
    
print("=============================")
s = "Reggin"
for i in s:
    print(i)

print("=============================")
for i in range(5):
    print(i)
    
print("=============================")
for i in range(2,5):
    print(i)
    
print("=============================")
for i in range(1,10,3):
    print(i)
    
print("=============================")
for i in 'geeksforgeeks':
    if i == 'e' or i == 's':
        continue
    print(i)
    
print("=============================")
for i in 'geeksforgeeks':
    if i == 'e' or i == 's':
        break
print(i)

print("=============================")
for i in 'geeksforgeeks':
    pass
print(i)

print("=============================")
for i in range(1,4):
    print(i)
else:
    print("No break\n")
    
print("=============================")
li = ["eat", "sleep", "repeat"]
for i,j in enumerate(li):
    print(i,j)

print("=============================")
for i in range(1,4):
    for j in range(1,4):
        print(i, j)
        
print("=============================")
a = ["shirt", "sock", "pants", "sock", "towel"]
b = []
for i in a:
    if a == "sock":
        continue
    else:
        print(f"Washing {i}")
b.append("socks")
print(f"Washing {b}")

print("=====================================")
for i in range(1, 8):
    d = 3 + (i - 1) * 0.5
    print(f"Day {i}: Run {d:.1f} miles")