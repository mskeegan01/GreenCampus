import serial
import sqlite3
import time
import calendar

#Database is created 
db = sqlite3.connect('mydb')
cursor = db.cursor()

#cursor.execute(
#    "CREATE TABLE plants(id INTEGER PRIMARY KEY, name TEXT, temperature FLOAT, moisture INT, light INT)"
#)
#db.commit()

#Create timestamp column in database
#cursor.execute(
#    "ALTER TABLE plants ADD COLUMN timestamp TEXT"
#)
#db.commit()

data = {}
i = 0

#Connection to the Arduino
serialConnection = serial.Serial('/dev/cu.usbmodem1421')
#Transforms received data into readable format for the database and adds a timestamp
lineCount = 4
while i < lineCount:
    x = serialConnection.readline()

    #Replacing unnessesary characters
    x = x.decode('UTF-8')
    if ':' in x:
        split = x.split(':')
        split[1] = split[1].replace('\r\n', '')
        split[1] = split[1].replace(' ', '')
        data.update({split[0]: split[1]})
print(data)
#Create timestamp when data is transmitted

# 2018-10-11 12:23:12
ts = time.gmtime()
#print(time.strftime("%Y-%m-%d %H:%M:%S", ts))
#Inserting the data into the table 
#Deleted id from values to check for autoincrement 
cursor.execute('''INSERT INTO plants(name, temperature, moisture, light, timestamp)
                  VALUES(?, ?, ?, ?, ?)''', ( 'Pepper', data['Temperature'], data['Moisture'], data['Lightintensity'],time.strftime("%Y-%m-%d %H:%M:%S", ts))) 
db.commit()
#Displaying all data in the database 

cursor.execute('''SELECT * FROM plants ''')
rows = cursor.fetchall()
for row in rows:
    print(row)
db.close()