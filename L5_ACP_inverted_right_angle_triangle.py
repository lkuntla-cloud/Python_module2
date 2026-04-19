print("this is the right angle triangle pattern for star: ")
n=int(input("Enter how many rows you want: " ))
for i in range(1,n+1): #loop for rows
    for j in range(n-i): #loop for columns
        print(" ",end="")
    for k in range(i):
        print("X",end="")    
    print()