import _thread, socket, time
import Plant
import sqlite3

plants = []

p = Plant.Plant()
p.name = "Franklin"
p.location = "Desk in Spock"
plants.append(p)

p = Plant.Plant()
p.name = "Einstein"
p.location = "Kitchen"
plants.append(p)

p = Plant.Plant()
p.name = "Curie"
p.location = "Teamroom"
plants.append(p)

p = Plant.Plant()
p.name = "Dawkins"
p.location = "Roomy McRoomface"
plants.append(p)

p = Plant.Plant()
p.name = "Dawkins"
p.location = "Roomy McRoomface"
plants.append(p)

p = Plant.Plant()
p.name = "Hopper"
p.location = "Quiet space"
plants.append(p)

p = Plant.Plant()
p.name = "Edison"
p.location = "Secret location"
plants.append(p)

for i in range(0,250):
    p = Plant.Plant()
    p.name = "Sample data"
    p.location = "eternal void"
    plants.append(p)

p = Plant.Plant()
p.name = "Did you really scroll all the way down here? Were you that bored?"
p.location = "What did you expect to find here? Some sort of easter egg?"
plants.append(p)

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

        #TODO

        #ts = time.gmtime()
        #cursor.execute('''INSERT INTO plants(name, temperature, moisture, light, timestamp) VALUES(?, ?, ?, ?, ?)''', ( 'Pepper', data['Temperature'], data['Moisture'], data['Lightintensity'],time.strftime("%Y-%m-%d %H:%M:%S", ts))) 
        #db.commit()