num=int(input("Enter a number you want to covert into the binary system: "))
binary_str=""
if num==0:
    binary_str="0"
    print(binary_str)
else:
    while 0<num:
        rem=num%2
        binary_str=str(rem)+binary_str
        num=num//2
print("The binary version of",num,"is equal to",binary_str)
    