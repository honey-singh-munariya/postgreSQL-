import psycopg2
def table():

    connect = psycopg2.connect(dbname="postgres", user="postgres",password="983353",host="localhost",port="5432")

    print("Honey singh munariya")

    cursor = connect.cursor()
    cursor.execute('''create table Employees(Name text,Age int,Number int,ID int);''')
    print("Table created successful")

    connect.commit()
    connect.close()

def data():

    connect = psycopg2.connect(dbname="postgres", user="postgres",password="983353",host="localhost",port="5432")

    cursor = connect.cursor()
    Name = input(("Enter your name: "))
    Age = input("Enter your age: ")
    ID = input('Enter your id: ')
    Number = input('Enter your number: ')
    query = '''insert into Employees(Name,ID,Age,Number) values(%s,%s,%s,%s)'''
    cursor.execute(query,(Name,ID,Age,Number))
    print("Data succesfully added")

    connect.commit()
    connect.close() 
data()

