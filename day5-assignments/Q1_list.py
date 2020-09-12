lst = [1, 1, 5]

lst1 = []

l = int(input("\nEnter the length of the list : "))

j = 0;

# creating a list from user value

for i in range (0,l):

    lst1.append(int(input("\nEnter the number for the list : ")))

print()

print("List is : ", lst1)

for i in range(0,l):
    
    if( lst1[i] == lst[j] ):
        
        j += 1
        
        i += 1
        
    else:
        
        i +=1
    
if( j == 3 ):
     print ("\nIt's a match")

else:

    print ("\nIt's Gone")