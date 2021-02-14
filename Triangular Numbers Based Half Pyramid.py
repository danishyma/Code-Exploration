#Print a triangle that follows a pattern with triangular numbers at the base starting from left bottom up. Exemple:

# 7
# 4 8
# 2 5 9
# 1 3 6 10


#Set number of triangle sides
x = 10  

#Find the nth triangular number (given in x) - n*(n+1)/2
n = int((x*(x+1)/2)) 

#The first number on the top of the pyramid is found by subtracting the nth triangular number by hight - 1 
n1 = n - (x-1)

#Create the rows and columns
for row in range(0, x):
    #initiate a new row having the first number according to the column's
    n2 = n1 
    for col in range(0, row+1):
        if col == 0:
            #First column where each number is itself minus x -> where x is the hight -1 descreasing one number each time 
            print(n1, end=" ")
        else:
            #Each row is based on the first entry of the column where each number from the row is itself plus x -> where x is increasingly up until numbere of x
            n2 = n2+(x-(row-col))
            print(n2, end=" ")
            
    n1 = n1 - (x-(row+1))
    print()
    