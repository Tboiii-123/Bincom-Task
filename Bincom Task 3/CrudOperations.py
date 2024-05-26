#Creating a postgres database with tables and perform crud operation
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
cursor.execute('''CREATE TABLE NAME(
               NameId SERIAL PRIMARY KEY,
               Fname VARCHAR(255),
               Lname VARCHAR(255)
)''')

print("TABLE CREATED SUCCESSFULLY")

"""

#Read what inside the database
#result=cursor.execute("SELECT * FROM NAME")
#row =cursor.fetchall()
#for i in row:
#    print(i)

#Insert Method
# cursor.execute("INSERT INTO NAME VALUES (1,'lawal','hussein')")
# cursor.execute("INSERT INTO NAME VALUES (2,'lawal','hussein')")
#cursor.execute("INSERT INTO NAME VALUES (4,'Fatai','Wakil')")



#Delete Method
#cursor.execute("DELETE FROM NAME WHERE nameid=4")


#Update Method
#cursor.execute("UPDATE NAME SET fname='Muiz' WHERE nameid=3")



Connect.commit()
Connect.close()
