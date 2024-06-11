'''prgm to build login system using functions. The fn. name should be login and register --
1. ask user to enter the details for registration and out of all his details only username and password 
should be stored.
2.now this fn. shld ask user to enter user name and password. If these match with the registered details 
login successful otherwise repeat this login process saying invalid credentials'''
def Login_details():
    d={}
    name=input()
    a_id=input()
    un=input("Enter name")
    pwd=input("Enter password")
    d[un]=pwd
    while True:
        print("Name is"+name)
        print("Aadhar ID is"+a_id)
        l_nm=input("Enter the login user name")
        l_pwd=input("Enter login password")
        if l_nm in d:
           if d[l_nm]==l_pwd:
               print("Login success")
               break
           else:
               print("Enter valid passcode")
        else:
            print("User not found")
            break    
Login_details()