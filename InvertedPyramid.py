'''
               Output :
           
               * * * * * 
                * * * * 
                 * * * 
                  * * 
                   * 
'''


r = int(input("Enter the number of rows : "))

print("\n\tInverted Pyramid Shape :")

for i in range (r,0,-1):
    for j in range (0,r-i):
        print(end=" ")
    for j in range (0,i):
        print("*", end=" ")
    print()