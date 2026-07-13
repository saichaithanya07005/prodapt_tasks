dusername="unknownuser"
dpassword="password"

i=0
while i<3:
    username=input("Enter your username: ")
    password=input("Enter your password: ")
    if username==dusername and password==dpassword:
        print("Login successful")
        break
    else:
        print("Login failed. Please check your username and password.")
        i+=1
        if i==3:
            print("Too many failed attempts. Please try again later.")