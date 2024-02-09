import random

number = "0123456789"  
lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()                                                 # copies lowerc and makes it uppercase
symbols = "!@#$%^&*()_+-=[]{};':,./<>?"

string = number + lower + upper + symbols

length = int(input("Enter the length of password: "))                   # user inputs length

password = "".join(random.sample(string, length))                       # joins the random characters together
totalpasswords = int(input("Enter the total number of passwords: "))    # user inputs number of passwords

for i in range(totalpasswords):                                         # prints the number of passwords based on user input
    print("Password: ", "".join(random.sample(string,length)))