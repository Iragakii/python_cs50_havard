#split user name into f name and l name
# first, last = name.split(" ")
name = input("What's your name : ")
#renmove white space from str
name = name.strip()
#capitalize user's name first letter 
name = name.capitalize()
#capitalize user's all letter name
name = name.title()
#other way to write funct
name = name.strip().title()


print("Hello",name)