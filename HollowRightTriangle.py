'''
            Output :
           
           * * * * * 
             *     * 
               *   * 
                 * * 
                   * 
'''

r = int(input("Enter the number of rows : "))

print("\tHollow Right Triangle Shape :")

for i in range(0,r):
    for j in range(0,r) :
        if (j==r-1) or (i==0) or (i==j):
            print("*", end=" ")
        else :
            print(" ",end=" ")
    print()