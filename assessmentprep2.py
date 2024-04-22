num1 = int(input("Enter a number "))
num2 = int(input("Enter a second number "))

print("Enter a, A, s, S")
choice = input()

if choice == 'a':
    print (num1 + num2)
elif choice == 'A':
    print (num1 - num2)
elif choice == 's':
    print (num1 - num2)
elif choice == 'S':
    print (num1 - num2)
else:
    print ("Invalid Option")