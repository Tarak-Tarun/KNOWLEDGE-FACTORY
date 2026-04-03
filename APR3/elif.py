def home(name,password):
    if(name=="Tarak" and password=="Coastal@7"):
        return "Authorized User"
    elif(name=="Tarak" and password!="Coastal@7"):
        return  "Password is Incorrect"
    else:
        return "Please Check your credentials"
name=input("Enter Your Name: ")
password=input("Enter Your Password: ")
print(home(name,password))