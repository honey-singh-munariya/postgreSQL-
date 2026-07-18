# this the assignment file we have to complete a task
# Create a python script that connect to a postgreSQL database and perform basic database opreation using the psycopg2 library.
import psycopg2
def table():

    connect = psycopg2.connect(dbname="postgres", host="localhost",port="5432",user="postgres",password="983353",)
    cursor = connect.cursor()
    cursor.execute('''create table Students(Name text,Age int,ID int,Number int);''')
    print("Tabel has been created succesfully")

    connect.commit()
    cursor.close()
    connect.close()

def data():

    connect = psycopg2.connect(dbname="postgres",host="localhost",user="postgres",password="983353",port="5432")
    cursor =connect.cursor()
    Name = input("Enter your name: ")
    Age = input("Enter your age: ")
    ID = input("Enter your id: ")
    Number = input("Enter your number: ")
    query = '''insert into Students(Name,Age,ID,Number) values(%s,%s,%s,%s);'''
    cursor.execute(query(Name,ID,Age,Number))
    print("Data succesfully added")
    connect.commit()
    cursor.close()
    connect.close()

data()


