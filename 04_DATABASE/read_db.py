import mysql.connector
from faker import Faker
import random
fake = Faker()

#  connection string
cnx = mysql.connector.connect(
    user        ='root',
    password    ='13500586',
    host        ='127.0.0.1',
    database    ='BarnesAndIgnoble',
    auth_plugin ='mysql_native_password')

# query
cursor = cnx.cursor()

NumData = 10

# Publishers

AddPublishers = "INSERT INTO Publishers ( Name, City) VALUES ( %(Name)s, %(City)s)"

for x in range(NumData):
    DataPublishers = {
    'Name': fake.company(),
    'City': fake.city(),
    }

    cursor.execute(AddPublishers,DataPublishers)

# Authors

AddAuthors = "INSERT INTO Authors (Name) VALUES (%(Name)s)"

for x in range(NumData):
    DataAuthors = {
    'Name': fake.name(),
    }

    cursor.execute(AddAuthors,DataAuthors)

# Books

genre_list = [
'Action','adventure','Autobiography','Anthology','Biography',
'Crafts/hobbies','Classic','Cookbook','Diary','Dictionary','Crime',
'Encyclopedia','Drama','Fairytale','Health/fitness','Fantasy',
'History','Graphic novel' ]

isbn_list = [
'1-942652-80-1',
'1-77925-566-7',
'0-8468-4877-5',
'1-81712-997-X',
'0-7451-2778-9',
'1-5228-6187-4',
'0-8053-4436-5',
'1-348-60060-8',
'0-241-41547-0',
'1-08-178914-X',
'1-65289-274-5',
'0-87860-927-X',
'0-7613-1837-2',
'0-8295-0938-0',
'1-924056-80-1',
'1-81250-000-9',
'0-461-88452-6',
'1-397-97211-4',
'1-254-35307-0',
'0-03-585233-X',
'0-373-78388-4',
'1-123-86083-1',
'1-337-40078-5',
'0-10-553601-6',
'0-13-391590-5',
'0-302-76711-8',
'1-874618-83-6',
'1-188-69671-8',
'0-9628936-5-X',
'1-392-22775-5',
'1-79458-254-1',
'0-09-435867-2',
'1-72135-884-6',
'1-387-40207-2',
'1-4367-4895-X',
'1-371-64702-X',
'1-340-78919-1',
'1-65081-704-5',
'0-448-67309-6',
'1-67329-936-9',
'0-906963-71-0',
'1-4566-9852-4',
'1-76279-395-4',
'1-170-15924-9',
'0-85173-872-9',
'0-522-85473-7',
'0-587-16753-X',
'1-287-61104-4',
'1-05-311311-0',
'0-475-51315-0']

AddBooks = "INSERT INTO Books (ISBN, Title, Genre, PubDate, Price, PublisherID) VALUES (%(ISBN)s, %(Title)s, %(Genre)s, %(PubDate)s, %(Price)s, %(PublisherID)s)"

for x in range(NumData):
    DataBooks = {
    'ISBN': isbn_list[x],
    'Title': fake.sentence(),
    'Genre': random.choice(genre_list),
    'PubDate': fake.date(),
    'Price': fake.pricetag(),
    'PublisherID': random.randint(1, NumData)
    }

    cursor.execute(AddBooks,DataBooks)

# Editors

AddEditors = "INSERT INTO Editors (Name, PublisherID) VALUES (%(Name)s, %(PublisherID)s)"

for x in range(NumData):
    DataEditors = {
    'Name': fake.name(),
    'PublisherID': random.randint(1, NumData)
    }

    cursor.execute(AddEditors,DataEditors)

# Customers

AddCustomers = "INSERT INTO Customers ( Name) VALUES (%(Name)s)"

for x in range(NumData):
    DataCustomers = {
    'Name': fake.name()
    }

    cursor.execute(AddCustomers,DataCustomers)

# Orders

AddOrders = "INSERT INTO Orders (Date, Total, CustomerID) VALUES (%(Date)s, %(Total)s, %(CustomerID)s)"

for x in range(NumData):
    DataOrders = {
    'Date': fake.date(),
    'Total': fake.pricetag(),
    'CustomerID': random.randint(1, NumData)
    }

    cursor.execute(AddOrders,DataOrders)

# Shipments

AddShipments = "INSERT INTO Shipments (ISBN) VALUES (%(ISBN)s)"

for x in range(NumData):
    DataShipments = {
    'ISBN': random.choice(isbn_list[0:NumData-1])
    }

    cursor.execute(AddShipments,DataShipments)

# Book Editors

AddBookEditors = "INSERT INTO BookEditors (ISBN) VALUES (%(ISBN)s)"

for x in range(NumData):
    DataBookEditors = {
    'ISBN': random.choice(isbn_list[0:NumData-1])
    }

    cursor.execute(AddBookEditors,DataBookEditors)

# Book Authors

AddBookAuthors = "INSERT INTO BookAuthors (ISBN, Royalty) VALUES (%(ISBN)s, %(Royalty)s)"

for x in range(NumData):
    DataBookAuthors = {
    'ISBN': random.choice(isbn_list[0:NumData-1]),
    'Royalty': fake.pricetag()
    }

    cursor.execute(AddBookAuthors,DataBookAuthors)

# clean up
cnx.commit()
cursor.close()
cnx.close()