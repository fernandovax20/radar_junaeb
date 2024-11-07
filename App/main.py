from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restorants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mi_secreto_super_secreto'
app.config['TEMPLATES_AUTO_RELOAD'] = True
db = SQLAlchemy(app)

# Modelo de base de datos para los restaurantes
class Restorant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(100), nullable=True)

@app.route('/')
def index():
    # Consultar todos los restaurantes en la base de datos
    restorants = Restorant.query.all()
    return render_template('index.html', restorants=restorants)

with app.app_context():
    # Crear las tablas de la base de datos
    db.create_all()

    # Cargar datos de prueba si la tabla está vacía
    if not Restorant.query.first():
        datos_prueba = [
            Restorant(nombre="Ikigai", descripcion="Café, Sándwiches, más"),
            Restorant(nombre="Subway", descripcion="Sándwiches"),
            Restorant(nombre="Dunkin Donuts", descripcion="Café, Sándwiches"),
            Restorant(nombre="Cafetería Rumary", descripcion="Completos, Papas, Café, más"),
            Restorant(nombre="Queen Papas", descripcion="Papas, Completos")
        ]

        db.session.bulk_save_objects(datos_prueba)
        db.session.commit()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050, debug=True)
