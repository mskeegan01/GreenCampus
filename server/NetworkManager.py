import _thread, socket, time
import Plant
import sqlite3

plants = {}


db = sqlite3.connect('mydb')
cursor = db.cursor()

def Listen():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 1995)) 
    s.listen(1)
    while True:
        conn, addr = s.accept()
        _thread.start_new_thread(_Communicate, (conn))

def _Communicate(conn):
    plant = Plant.Plant()
    while True:
        data = conn.recv(4)

        plant.temperature = 25.3

        #ts = time.gmtime()
        #cursor.execute('''INSERT INTO plants(name, temperature, moisture, light, timestamp) VALUES(?, ?, ?, ?, ?)''', ( 'Pepper', data['Temperature'], data['Moisture'], data['Lightintensity'],time.strftime("%Y-%m-%d %H:%M:%S", ts))) 
        #db.commit()