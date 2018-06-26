import sqlite3
conn = sqlite3.connect( 'test.db')
print("opened database successfully")


""""
conn.execute ('''create table company (
ID INT PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR(50),
SALARY REAL);''')

"""
print("table created")
#conn.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY)VALUES(14,'NAV',22,'MODEL TOWN',100000000)")
#conn.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY)VALUES(24,'BAJWA',23,'NEW TOWN',20000000)")
#conn.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY)VALUES(34,'PREET',24,'OLD TOWN',3000000)")
#conn.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY)VALUES(45,'SINGH',22,'CENTRAL TOWN',400000)")
#conn.commit()
#print("inserted")

cursor=conn.execute("SELECT id,name,address,salary from company")
for row in cursor:
    print("ID=",row[0])
    print("NAME=",row[1])
    print("ADDRESS=",row[2])
    print("SALARY=",row[3],"\n")
print("records created sucessful")

conn.execute("UPDATE COMPANY set SALARY = 25000000 where ID = 14")
conn.commit()
cursor=conn.execute("SELECT id,name,address,salary from company")
for row in cursor:
    print("ID=",row[0])
    print("NAME=",row[1])
    print("ADDRESS=",row[2])
    print("SALARY=",row[3],"\n")
print("records created sucessful")

conn.execute("DELETE from COMPANY where ID=14")
conn.commit()
cursor=conn.execute("SELECT id,name,address,salary from company")
for row in cursor:
    print("ID=",row[0])
    print("NAME=",row[1])
    print("ADDRESS=",row[2])
    print("SALARY=",row[3],"\n")
print("records created sucessful")