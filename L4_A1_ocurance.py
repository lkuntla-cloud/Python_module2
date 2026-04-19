string=input("What string do you want?: ")
char=input("What Char do you want?: ")
count=0
i=0
while(i<len(string)):
    if string[i]==char:
        count=count+1
    i=i+1
print("The total number of times", char,"has occured in the string =",count)