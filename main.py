import mysql.connector as connector

db = connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="retail"
)

mycursor = db.cursor()
mycursor.execute("drop table student;")
mycursor.execute("create table student(id int,name varchar(20),score int,city varchar(20));")
print("Student table created INSERT DATA\n")

for i in range(5):
    try:
        vals = input("id: "),input("name: "),input("score: "),input("city: ")
        print()
        mycursor.execute("insert into student values(%s,%s,%s,%s);",vals)
        db.commit()
    except:
        print("Insertion Failed")

id = int(input("Enter the id to delete: ")),
mycursor.execute("delete from student where id=%s;",id)
db.commit()
print("Deleted\n")

print("Enter the details to update")
vals = input("name: "),input("score: "),input("city: "),input("id: ")
mycursor.execute("update student set name=%s, score=%s, city=%s where id=%s;",vals)
db.commit()
print("Updated\n")

print("All the Students")
mycursor.execute("select * from student;")
res = mycursor.fetchall()
print(*res,sep="\n")
print()

print("All the Students In Ascending order by their Names")
mycursor.execute("select * from student order by name;")
res = mycursor.fetchall()
print(*res,sep="\n")
print()

print("All the Students Whose score are Between 70 and 90")
mycursor.execute("select * from student where score between 70 and 90;")
res = mycursor.fetchall()
print(*res,sep="\n")
print()

print("All the Students from Hyderabad")
mycursor.execute("select * from student where city = 'Hyderabad';")
res = mycursor.fetchall()
print(*res,sep="\n")
print()


