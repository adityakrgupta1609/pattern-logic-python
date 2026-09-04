'''
            Output :
           
           * 
           * * 
           *   * 
           *     * 
           * * * * * 
'''

r = int(input("Enter the number of rows : "))

print("\n\tHollow left triangle Shape :")

for i in range (0,r):
    for j in range (0,i+1):
        if (j==0) or (i==r-1) or (i==j) or ():
            print("*", end=" ")
        else :
            print(" ",end=" ")
    print()
    
    
