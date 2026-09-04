r = int(input("Enter the Numbers of row : "))

print("\tPattern 1 ")

for i in range(1, r+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
print("\n\tPattern 2 ")

for i in range(1, r+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()