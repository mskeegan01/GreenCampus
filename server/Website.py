from flask import Flask, render_template
import socket, NetworkManager


def Start():
    app = Flask(__name__)
    
    @app.route('/<string:page_name>/')
    def blabla(page_name):
        #cursor.execute('''SELECT * FROM plants ''')
        #rows = cursor.fetchall()
        #for row in rows:
        #print(row)
        plants = NetworkManager.plants
        #plants = [ "Frank", "Steve", "Alice", "Bruce"]
        return render_template(page_name, **locals())
        
    app.run(port=80)