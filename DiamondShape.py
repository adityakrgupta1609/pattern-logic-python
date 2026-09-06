'''
               Output :
           
                   * 
                  * * 
                 * * * 
                * * * * 
               * * * * * 
                * * * * 
                 * * * 
                  * * 
                   * 
'''


r = int(input("Enter the number of rows : "))

print("\n\tDiamond Shape :")

for i in range (0,r):
    for j in range (0,r-i-1):
        print(end=" ")
    for j in range (0,i+1):
        print("*", end=" ")
    print()
for i in range (r-1,0,-1):
    for j in range (0,r-i):
        print(end=" ")
    for j in range (0,i):
        print("*", end=" ")
    print()