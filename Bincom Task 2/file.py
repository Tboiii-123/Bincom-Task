

#Create a text file that has your full name, and write code to read it and extract first name, middle name and last name.

try:
        
    with open('name.txt','w') as handler:
        handler.write("Lawal Hussein Taiwo")
        print("Written Successfully!!!")
        

except FileNotFoundError :
    print("File Not found")


try:
    with open('name.txt','r') as handler2:
        Read =handler2.read()
        print(Read)
except FileNotFoundError:
    print("File Not Found")



Eachname =Read.strip()

Eachname=Eachname.split()

print("First Name:",Eachname[0])
print("First Name:",Eachname[1])
print("First Name:",Eachname[2])
