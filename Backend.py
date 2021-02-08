#!/usr/bin/python
# -*- coding: utf-8 -*-

#Ist die Route / (o.ä.) nicht komplett überflussig wenn der NodeJS-Server alles regelt?
import mariadb
import json
from datetime import datetime
from flask import Flask, request, jsonify, redirect, render_template
from flask_cors import CORS
from flask import g

app = Flask(__name__)
# Cross-Origin-Request zulassen (Kommunikation zwischen Frontend und Backend ermöglichen)
CORS(app, resources={r'/*': {'Access-Control-Allow-Origin': '*'}})

# Datenbank-Verbindung abbauen beim Beenden
@app.teardown_appcontext
def close_connection(exception):
    db = g.get("database", None)
    if db is not None:
        db.close()

# Datenbank-Zugriff erfragen        
def getDB():
    db = g.get("co2", None)
    if db is None:
        db = g.database = mariadb.connect(host="localhost", user="co2", password="apHxU48Ac:IH-Znrhhx-", database="co2")
    print("Database gefunden")
    return db

@app.route("/", methods=["GET"])
def index():
    return redirect("/login")

@app.route("/statusNow/<raumNr>", methods=["GET"])
def getStatusNow(raumNr):
    db = getDB()
    cursor = db.cursor()
    jetzt = datetime.now().strftime("%Y-%m-%d %H:%M")
    cursor.execute("SELECT id, raum, temp, co2, h2o, score, datumuhrzeit FROM Messwerte WHERE raum=? ORDER BY datumuhrzeit ASC", (raumNr))
    ergebnis = []
    #for (id, raum, temp, co2, h20, score, datumuhrzeit) in cursor:
     #   ergebnis.append({"id":id, "raum":raum, "temp":temp, "co2":co2, "h2O":h2O, "score":score, "datumuhrzeit":datumuhrzeit}) 
    for (id, raum, temp, co2, h2o, score, datumuhrzeit) in cursor:
        ergebnis.append({"Raum": raum, "ID": id, "Temp": temp, "co2": co2, "h2o": h2o, "score": score, "DatumZeit": datumuhrzeit})

    return jsonify(ergebnis)

@app.route("/postNow/<raumNr>/<temp>", methods=["GET"])
def postNow(raumNr, temp):
    db = getDB()
    cursor = db.cursor()
    jetzt = datetime.now().strftime("%Y-%m-%d %H:%M")
    cursor.execute("INSERT INTO Messwerte(raum, temp, DatumUhrzeit) VALUES(?,?,?);", (raumNr, temp, jetzt))
    db.commit()
    return 'success'

@app.route("/statusNow", methods=["POST"])
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

@app.route('/login', methods=['POST'])
def login():
    data = json.loads(request.data.decode('UTF-8'))
    users = {'test@abc.de': 'Test1234'}
    if data.get('email') in users:
        if data.get('password') == users[data.get('email')]:
            return json.dumps({'login': True})
    return json.dumps({'login': False}) #Use jsonify?
    #return 'Hallo'

@app.route('/db', methods=["GET"])
def db():
	db = getDB()
	cursor = db.cursor()
	cursor.execute("SELECT DISTINCT raum FROM Messwerte ORDER BY raum ASC")
	ergebnis = []
	for raum in cursor:
	    ergebnis.append(raum[0])
	with open('./test.log', 'w') as f:
       	    f.write(str(ergebnis))
	return jsonify({'Raeume': ergebnis})

@app.route("/app/statusNow/<raumNr>", methods=["GET"])
def appGetStatusNow(raumNr):
    db = getDB()
    cursor = db.cursor()
    jetzt = datetime.now().strftime("%Y-%m-%d %H:%M")
    cursor.execute("SELECT id, raum, temp, co2, h2o, score, datumuhrzeit FROM Messwerte WHERE raum=? ORDER BY id DESC", (raumNr, ))
    ergebnis = []
    #for (id, raum, temp, co2, h20, score, datumuhrzeit) in cursor:
     #   ergebnis.append({"id":id, "raum":raum, "temp":temp, "co2":co2, "h2O":h2O, "score":score, "datumuhrzeit":datumuhrzeit}) 
    for (id, raum, temp, co2, h2o, score, datumuhrzeit) in cursor:
        ergebnis.append({"Raum": raum, "ID": id, "Temp": temp, "co2": co2, "h2o": h2o, "score": score, "DatumZeit": datumuhrzeit})
    return jsonify(ergebnis)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=62001)
