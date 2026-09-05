'''
            Output :
           
               * 
              * * 
             * * * 
            * * * * 
           * * * * * 
'''


r = int(input("Enter the number of rows : "))

print("\n\tPyramid Shape :")

for i in range (0,r):
    for j in range (0,r-i-1):
        print(end=" ")
    for j in range (0,i+1):
        print("*", end=" ")
    print()