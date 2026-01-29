print("Choose on way of transport: ")
print("1.Bike")
print("2.Car")
choice=int(input("What do you want: "))
if choice==1:
    print("Choose your bike ride")
    print("1.Scooty")
    print("2.Scooter")
    bike=int(input("Enter which bike ride you want: "))
    if bike==1:
        print("You have choosen Scooty as your ride")
    else:
        print("You have choosen Scooter as your ride")
        
elif choice==2:
    print("Choose your car ride")
    print("1.Susuki")
    print("2.Toyota")
    bike=int(input("Enter which car ride you want: "))
    if bike==1:
        print("You have choosen Susuki as your ride")
    else:
        print("You have choosen Toyota as your ride")
        
else:
    print("Your choice is wrong")