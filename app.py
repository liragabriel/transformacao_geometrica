import math
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
@app.route('/inicio')
def inicio():
    return render_template('inicio.html')


@app.route('/translacao', methods=['POST'])
def translacao():

    """
        Operação
        --------
            [x] + [dx]
            [y]   [dy]
    """

    x = request.form['x']
    y = request.form['y']
    dx = request.form['dx']
    dy = request.form['dy']

    matriz_original = [int(x), int(y)]
    matriz_altera = [int(dx), int(dy)]
    matriz_resultado = [0, 0]

    for i in range(2):
        matriz_resultado[i] += (matriz_original[i] + matriz_altera[i])

    return render_template('translacao.html', data=matriz_resultado)


@app.route('/escala', methods=['POST'])
def escala():

    """
        Operação
        --------
            [sx 0] * [x]
            [0 sy]   [y]
    """

    x = request.form['x']
    y = request.form['y']
    s1 = request.form['s1']
    s2 = request.form['s2']

    matriz_original = [int(x), int(y)]
    matriz_altera = [int(s1), int(s2)]
    matriz_resultado = [0, 0]

    for i in range(2):
        matriz_resultado[i] += (matriz_original[i] * matriz_altera[i])

    return render_template('escala.html', data=matriz_resultado)


@app.route('/rotacao', methods=['POST'])
def rotacao():

    """
        Operação
        --------
            [cos(ang) -sen(ang)] * [x]
            [sen(ang)  cos(ang)]   [y]
    """

    x = request.form['x']
    y = request.form['y']
    ang = request.form['ang']

    matriz_resultado = [
        (math.cos(int(ang))*int(x)) + ((math.sin(int(ang))*int(y))*-1),
        (math.sin(int(ang))*int(x)) + (math.cos(int(ang))*int(y))
        ]

    return render_template('rotacao.html', data=matriz_resultado)


if  __name__ == '__main__':
    app.run(debug=True)
