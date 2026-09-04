'''
            Output :
           
           * 
           * * 
           * * * 
           * * * * 
           * * * * * 
'''

r = int(input("Enter the number of rows : "))

print("\tRight Angle Triangle :")

for i in range(1,r+1):
    for j in range(1,i+1) :
        print("*", end=" ")
    print()