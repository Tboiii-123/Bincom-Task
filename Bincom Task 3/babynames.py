

#Save baby names to postgres table
import  psycopg2 


Connect=psycopg2.connect(
    database="mydatabase",
    user="postgres",
    password="yinkus",
    host="localhost",
    port="5432",
)

cursor =Connect.cursor()

#Create Method
"""
cursor.execute('''CREATE TABLE Babyname(
               NameId SERIAL PRIMARY KEY,
               Name VARCHAR(255),
               
)''')

print("TABLE CREATED SUCCESSFULLY")

"""


#cursor.execute("INSERT INTO NAME VALUES (1,'Jacob')")
#cursor.execute("INSERT INTO NAME VALUES (2,'Mike')")
#cursor.execute("INSERT INTO NAME VALUES (3,'Mia')")
#cursor.execute("INSERT INTO NAME VALUES (4,'Emily')")
#cursor.execute("INSERT INTO NAME VALUES (5,'Daniel')")
#cursor.execute("INSERT INTO NAME VALUES (6,'Anthony')")
#cursor.execute("INSERT INTO NAME VALUES (7,'William')")
#cursor.execute("INSERT INTO NAME VALUES (8,'Jayden')")
#cursor.execute("INSERT INTO NAME VALUES (9,'Andrew')")
#cursor.execute("INSERT INTO NAME VALUES (10,'James')")
#cursor.execute("INSERT INTO NAME VALUES (11,'Taylor')")
#cursor.execute("INSERT INTO NAME VALUES (12,'Alexis')")
#cursor.execute("INSERT INTO NAME VALUES (13,'Nathan')")
#cursor.execute("INSERT INTO NAME VALUES (14,'Christian')")
#cursor.execute("INSERT INTO NAME VALUES (15,'Gabrile')")

print("DATA INSERTED TO THE DATABASE SUCCESSFULLY!!!!!!")