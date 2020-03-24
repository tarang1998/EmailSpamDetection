import mysql.connector
mydb = mysql.connector.connect(host="35.194.28.160", user="root", passwd="tarangrahul", database="sys")
cursor = mydb.cursor()
#cursor.execute("")
print(cursor)
