# TC2008B. Sistemas Multiagentes y Gráficas Computacionales
# Python flask server para interactuar con Unity
# Equipo 5. Noviembre 2022

from flask import Flask, request, jsonify
from trafficModel import *

# Tamaño del tablero:
numeroCarros = 1
numeroSemaforos = 12
tiempo = 0
ancho = 24
alto = 24
trafficModel = None
stepActual = 0

app = Flask("Traffic Model")


@app.route('/init', methods=['POST', 'GET'])
def initModel():
    global numeroCarros, numeroSemaforos, tiempo, ancho, alto, trafficModel, stepActual

    if request.method == 'POST':
        numeroCarros = int(request.form.get('carros'))
        numeroSemaforos = int(request.form.get('semaforos'))
        tiempo = int(request.form.get('time'))
        ancho = int(request.form.get('width'))
        alto = int(request.form.get('height'))
        stepActual = 0

        print(request.form)
        print(numeroCarros, ancho, alto)
        trafficModel = TrafficModel(numeroCarros, numeroSemaforos,
                                    tiempo, ancho, alto)

        return jsonify({"message": "Parametros recibidos, modelo iniciado."})


@app.route('/getCarro', methods=['GET'])
def getCarro():
    global trafficModel

    if request.method == 'GET':
        pocisionesCarro = [{"id": str(c.unique_id),
                           "x": x, "y": 0, "z": z}
                           for (c, x, z) in trafficModel.grid.coord_iter()
                           for a in c if isinstance(a, Carro)]

        return jsonify({'positions': pocisionesCarro})


@app.route('/getSemaforo', methods=['GET'])
def getSemaforo():
    global trafficModel

    if request.method == 'GET':
        posicionesSemaforo = [{"id": str(s.unique_id),
                              "x": x, "y": 0, "z": z}
                              for (s, x, z) in trafficModel.grid.coord_iter()
                              for a in s if isinstance(a, Semaforo)]

        return jsonify({'positions': posicionesSemaforo})


@app.route('/getParking', methods=['GET'])
def getParking():
    global trafficModel

    if request.method == 'GET':
        posicionesParking = [{"id": str(p.unique_id),
                             "x": x, "y": 0, "z": z}
                             for (p, x, z) in trafficModel.grid.coord_iter()
                             for a in p if isinstance(a, Parking)]

        return jsonify({'positions': posicionesParking})


@app.route('/getRoads', methods=['GET'])
def GetRoads():
    global trafficModel

    if request.method == 'GET':
        posicionesRoads = [{"id": str(r.unique_id),
                            "x": x, "y": 0, "z": z}
                           for (r, x, z) in trafficModel.grid.coord_iter()
                           for a in r if isinstance(a, Roads)]

        return jsonify({'positions': posicionesRoads})


@app.route('/getEdificios', methods=['GET'])
def getEdificios():
    global trafficModel

    if request.method == 'GET':
        posicionesEdificios = [{"id": str(e.unique_id),
                                "x": x, "y": 0, "z": z}
                               for (e, x, z) in trafficModel.grid.coord_iter()
                               for a in e if isinstance(a, Edificios)]

        return jsonify({'positions': posicionesEdificios})


@app.route('/update', methods=['GET'])
def updateModel():
    global currentStep, almacenModel
    if request.method == 'GET':
        almacenModel.step()
        currentStep += 1
        return jsonify({'message': f'Model updated to step {currentStep}.',
                        'currentStep': currentStep})


if __name__ == '__main__':
    app.run(host="localhost", port=8585, debug=True)
