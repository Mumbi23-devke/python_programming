from database import User

try:
    jina = input("Enter your name \n ")
    arafa = input("Enter your email address \n ")
    siri = input("Enter your password \n ")

    User.create(name=jina, email=arafa, password=siri)
    print("User created successfully.")

except:
    print("Failed to create user.")
