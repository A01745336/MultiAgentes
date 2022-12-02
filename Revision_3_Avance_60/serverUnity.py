# TC2008B. Sistemas Multiagentes y Gráficas Computacionales
# Python flask server para interactuar con Unity
# Equipo 5. Noviembre 2022

from flask import Flask, request, jsonify
from model import *
from agent import *

# Tamaño del tablero:
nAgents = 0
numeroCarros = 100
numeroSemaforos = 12
tiempo = 0
ancho = 24
alto = 24
trafficModel = None
currentStep = 0

app = Flask("Traffic Model")


@app.route('/init', methods=['POST', 'GET'])
def initModel():
    global numeroCarros, numeroSemaforos, tiempo
    global ancho, alto, trafficModel, currentStep, nAgents

    if request.method == 'POST':
        numeroCarros = int(request.form.get('numeroCarros'))
        ancho = int(request.form.get('ancho'))
        alto = int(request.form.get('alto'))
        currentStep = 0

        print(request.form)
        print(numeroCarros, ancho, alto)
        trafficModel = RandomModel(nAgents)

        return jsonify({"message": "Parametros recibidos, modelo iniciado."})


@app.route('/getCarro', methods=['GET'])
def getCarro():
    global trafficModel

    if request.method == 'GET':
        pocisionesCarro = [{"id": str(a.unique_id),
                           "x": x, "y": 0, "z": z}
                           for (c, x, z) in trafficModel.grid.coord_iter()
                           for a in c if isinstance(a, Car)]

        return jsonify({'positions': pocisionesCarro})


@app.route('/getSemaforo', methods=['GET'])
def getSemaforo():
    global trafficModel

    if request.method == 'GET':
        posicionesSemaforo = [{"id": str(a.unique_id),
                              "x": x, "y": 0, "z": z,
                               "semaforoActive": a.state}
                              for (s, x, z) in trafficModel.grid.coord_iter()
                              for a in s if isinstance(a, Traffic_Light)]

        return jsonify({'positions': posicionesSemaforo})


@app.route('/getParking', methods=['GET'])
def getParking():
    global trafficModel

    if request.method == 'GET':
        posicionesParking = [{"id": str(p.unique_id),
                             "x": x, "y": 0, "z": z}
                             for (p, x, z) in trafficModel.grid.coord_iter()
                             for a in p if isinstance(a, Destination)]

        return jsonify({'positions': posicionesParking})


@app.route('/getRoads', methods=['GET'])
def GetRoads():
    global trafficModel

    if request.method == 'GET':
        posicionesRoads = [{"id": str(r.unique_id),
                            "x": x, "y": 0, "z": z}
                           for (r, x, z) in trafficModel.grid.coord_iter()
                           for a in r if isinstance(a, Road)]

        return jsonify({'positions': posicionesRoads})


@app.route('/getEdificios', methods=['GET'])
def getEdificios():
    global trafficModel

    if request.method == 'GET':
        posicionesEdificios = [{"id": str(e.unique_id),
                                "x": x, "y": 0, "z": z}
                               for (e, x, z) in trafficModel.grid.coord_iter()
                               for a in e if isinstance(a, Obstacle)]

        return jsonify({'positions': posicionesEdificios})


@app.route('/update', methods=['GET'])
def updateModel():
    global currentStep, trafficModel
    if request.method == 'GET':
        trafficModel.step()
        currentStep += 1
        return jsonify({'message': f'Model updated to step {currentStep}.',
                        'currentStep': currentStep})


if __name__ == '__main__':
    app.run(host="localhost", port=8585, debug=True)
