#!/usr/bin/python
# -*- coding: utf-8 -*-
#import mariadb
import json
from datetime import datetime
from flask import Flask, request, jsonify, redirect
from flask_cors import CORS
from flask import g

app = Flask(__name__)
# Cross-Origin-Request zulassen (Kommunikation zwischen Frontend und Backend ermöglichen)
CORS(app, resources={r'/*': {'origins': '*'}})
'''
# Datenbank-Verbindung abbauen beim Beenden
@app.teardown_appcontext
def close_connection(exception):
    db = g.get("database", None)
    if db is not None:
        db.close()

# Datenbank-Zugriff erfragen        
def getDB():
    db = g.get("database", None)
    if db is None:
        db = g.database = mariadb.connect(host="localhost", user="name", password="passwort", database="dbname")
    return db
'''
@app.route("/", methods=["GET"])
def index():
    #Loginseite
    return redirect('/login')
    #return "Up and running"
'''
app.route("/statusNow/<raumNr>", methods=["GET"])
def getStatusNow(raum):
    db = getDB()
    cursor = db.cursor()
    jetzt = datetime.now().strftime("%Y-%m-%d %H:%M")
    cursor.execute("""SELECT co2, temp, feuchtigkeit, lautstaerke
                    FROM Raum
                    WHERE timestamp = ?
                    AND nr=?; """, (jetzt, raumNr))
    ergebnis = []
    for (co2, temp, feuchtigkeit, lautstaerke) in cursor:
        ergebnis.append({"CO2":co2, "temp":temp, "feuchtigkeit":feuchtigkeit, "lautstaerke":lautstaerke})
    return jsonify(ergebnis) 

app.route("/statusNow", methods=["POST"])
def setStatusNow(raum):
    db = getDB()
    cursor = db.cursor()
    jetzt = datetime.now().strftime("%Y-%m-%d %H:%M")
    post_data = request.get_json()
    nr = post_data.get("nr")
    co2 = post_data.get("co2")
    temp = post_data.get("temp")
    feuchtigkeit = post_data.get("feuchtigkeit")
    lautstaerke = post_data.get("lautstaerke")
    try:     
        cursor.execute("""INSERT INTO Raum(nr, co2, temp, feuchtigkeit, lautstaerke) 
                          VALUES(?, ?, ?, ?);""", (nr, co2, temp, feuchtigkeit, lautstaerke))
        db.commit()
        return jsonify({"success":True})
    except mariadb.Error as e:
        return jsonify({"success":False, "errMsg":str(e)})
'''

@app.route("/home", methods=["GET", 'POST'])
def home():
    #ListeView wenn login richtig
    if request.method == 'GET':
        print (request.args.get('name'))
    elif request.method == 'POST':
        data = json.loads(request.data.decode('UTF-8'))
        print (data['name'])
        print (data.get('name'))
    return "Up and running"

@app.route('/login', methods=['POST'])
def login():
    data = json.loads(request.data.decode('UTF-8'))
    #data = request.args
    users = {'test@abc.de': 'Test1234'}
    if data.get('email') in users:
        if data.get('password') == users[data.get('email')]:
            #return redirect(f'/home?name={data.get("email")}')
            return json.dumps('{"login": True}')
    return json.dumps('{"login": False}')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=62001)

#C:\\Program Files (x86)\\Python38-32\\pythonw.exe