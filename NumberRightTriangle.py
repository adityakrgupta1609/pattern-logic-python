r = int(input("Enter the Numbers of row : "))

print("\tPattern 1 :")

'''
            Output :
           
          1 
          1 2 
          1 2 3 
          1 2 3 4 
          1 2 3 4 5  
'''

for i in range(1, r+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
print("\n\tPattern 2 :")

'''
            Output :
           
           1 
           2 2 
           3 3 3 
           4 4 4 4 
           5 5 5 5 5 
'''

for i in range(1, r+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()