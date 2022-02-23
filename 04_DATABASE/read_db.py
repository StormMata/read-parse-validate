import mysql.connector

#  connection string
cnx = mysql.connector.connect(
    user        ='root',
    password    ='13500586',
    host        ='127.0.0.1',
    database    ='Farm',
    auth_plugin ='mysql_native_password')

# query
cursor = cnx.cursor()

# query = ('SELECT * FROM Customers')

# cursor.execute(query)

query = ("INSERT INTO `Customers` VALUES ('NEW','PERSON','NEWPERSON@MIT.EDU')")

cursor.execute(query)

# loop through data
for row in cursor.fetchall():
    print(row)

# clean up
cnx.commit()
cursor.close()
cnx.close()