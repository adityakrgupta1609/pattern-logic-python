r = int(input("Enter the number of rows : "))

print("\tFilled Star Pattern")

for i in range(1,r+1):
    for j in range(1,i+1) :
        print("*", end=" ")
    print()
    
print("\n\tHollow Star Pattern")

for i in range (0,r):
    for j in range (0,i+1):
        if (j==0) or (i==r-1) or (i==j) :
            print("*", end=" ")
        else :
            print(" ",end=" ")
    print()