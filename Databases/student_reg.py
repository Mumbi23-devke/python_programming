from database import Student

try:
    jina = input("Enter your name \n")
    namba = int(input("Enter your phone number \n"))
    miaka = int(input("Enter your age \n"))
    jinsia = input("Enter your gender \n")
    kodi = int(input("Input your student code \n"))

    Student.create(name=jina, number=namba, age=miaka, gender=jinsia, code=kodi)
    print("User successfully created. ")

except:
    print("User not successfully created!!")
