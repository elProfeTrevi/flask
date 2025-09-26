from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    mensaje =   '''   
    <h1>Este es el tema 1</h1>
    <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quod sint sequi dolorem animi? Voluptatem quod, asperiores exercitationem fuga delectus recusandae incidunt enim maxime possimus voluptatibus error nulla deserunt veniam laborum.</p>
    <p>Sed vel quis exercitationem. Delectus, voluptate iure debitis suscipit tempora quo assumenda saepe rem animi consequuntur. Omnis earum rerum quia voluptate facilis? Dolorum, corporis. Nihil praesentium in voluptates modi dolorum.</p>
    <p>Possimus saepe suscipit, neque molestiae sint, atque numquam cumque soluta earum, veritatis corporis eum illum ducimus tempora nobis dolorum illo! Odio, nobis iste maiores blanditiis ullam pariatur quidem non accusamus.</p>
    <p>Exercitationem est, explicabo inventore, atque eaque officia ea harum nobis veritatis id fugit sapiente earum quaerat! Aspernatur labore iste, explicabo magni ipsa sunt quae molestias assumenda ullam quaerat natus beatae.</p>
    <p>Molestias ea commodi optio in voluptatem. Atque unde esse at vitae quisquam, sequi eos tempore qui aperiam consequatur nemo officia cumque non assumenda exercitationem, ut repudiandae. Esse ex nostrum omnis?</p>
    '''
    return mensaje

@app.route('/sumar/<v1>/<v2>')
def sumar(v1,v2):
    s = str(float(v1) + float(v2))
    mensaje = f"<h1>La suma de {v1} + {v2} es {s} </h1>"
    return mensaje

@app.route('/restar/<v1>/<v2>')
def restar(v1,v2):
    s = str(float(v1) - float(v2))
    mensaje = f"<h1>La resta de {v1} - {v2} es {s} </h1>"
    return mensaje

@app.route('/multiplicar/<v1>/<v2>')
def multiplicar(v1,v2):
    s = str(float(v1) * float(v2))
    mensaje = f"<h1>La multiplicacion de {v1} * {v2} es {s} </h1>"
    return mensaje

@app.route('/dividir/<v1>/<v2>')
def dividir(v1,v2):
    s = str(float(v1) / float(v2))
    mensaje = f"<h1>La division de {v1} / {v2} es {s} </h1>"
    return mensaje

@app.route('/minimo/<v1>/<v2>')
def minimo(v1,v2):
    if v1 < v2:
        return f"<h1> {v1} es menor que {v2} </h1>"
    else:
        return f"<h1> {v2} es menor que {v1} </h1>"

@app.route('/maximo/<v1>/<v2>')
def maximo(v1,v2):
    if v1 > v2:
        return f"<h1> {v1} es mayor que {v2} </h1>"
    else:
        return f"<h1> {v2} es mayor que {v1} </h1>"


if __name__ == '__main__':
    app.run(debug=True)
