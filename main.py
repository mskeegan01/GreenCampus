import serial
import sqlite3

db = sqlite3.connect('mydb')
cursor = db.cursor()
#cursor.execute(
#    "CREATE TABLE plants(id INTEGER PRIMARY KEY, name TEXT, temperature FLOAT, moisture INT, light INT)"
#)
#db.commit()

id1 = '0'
name1 = "Chilli"
temperature1 = '30.69'
moisture1 = '63'
light1 = '15'

id2 = '1'
name2 = "Basil"
temperature2 = '25.33'
moisture2 = '34'
light2 = '25'

#cursor.execute('''INSERT INTO plants(id, name, temperature, moisture, light)
#                  VALUES(?,?,?,?,?)''', (id1,name1, temperature1, moisture1, light1))
print("XYZ")

db.commit()

ser = serial.Serial('/dev/cu.usbmodem1421', 9600)
while True:
    x = ser.readline()
    print(x.decode('UTF-8')[:-2])
db.close()
