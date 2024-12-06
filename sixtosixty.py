x=input("enter a username=")
def validate_username(x):
    if x.isalnum() and 6<=len(x)<=15:
        print("valid username")
    else:
        print("invalid username")
validate_username(x)
