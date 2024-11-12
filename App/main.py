from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restorants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mi_secreto_super_secreto'
app.config['TEMPLATES_AUTO_RELOAD'] = True
db = SQLAlchemy(app)


ICONOS_CATEGORIAS = [
    {'nombre': 'Sandwiche', 'icono': 'fa-solid fa-burger'},
    {'nombre': 'Desayuno', 'icono': 'fa-solid fa-coffee'},
    {'nombre': 'Cafe', 'icono': 'fa-solid fa-mug-hot'},
    {'nombre': 'Dulce', 'icono': 'fa-solid fa-candy-cane'},
    {'nombre': 'Completo', 'icono': 'fa-solid fa-hotdog'},
    {'nombre': 'Empanada', 'icono': 'fa-solid fa-pastafarianism'},
    {'nombre': 'Hamburguesa', 'icono': 'fa-solid fa-hamburger'},
    {'nombre': 'Pizza', 'icono': 'fa-solid fa-pizza-slice'},
    {'nombre': 'Vegana', 'icono': 'fa-solid fa-carrot'},
    {'nombre': 'Fajita', 'icono': 'fa-utensils'},
    {'nombre': 'Churrasco', 'icono': 'fa-solid fa-drumstick-bite'},
    {'nombre': 'Ensalada', 'icono': 'fa-solid fa-leaf'},
    {'nombre': 'Papas Frita', 'icono': 'fa-utensils'},
    {'nombre': 'Gohan', 'icono': 'fa-utensils'},
    {'nombre': 'Handroll', 'icono': 'fa-utensils'},
    {'nombre': 'Vegano', 'icono': 'fa-solid fa-seedling'},
    {'nombre': 'Sushi', 'icono': 'fa-solid fa-fish'},
    {'nombre': 'General', 'icono': 'fa-solid fa-utensils'},
    {'nombre': 'Lasaña', 'icono': 'fa-solid fa-layer-group'},
    {'nombre': 'Ravioli', 'icono': 'fa-utensils'},
    {'nombre': 'Colacion', 'icono': 'fa-solid fa-utensil-spoon'},
    {'nombre': 'Sopaipilla', 'icono': 'fa-solid fa-cookie'}
]

# Modelo de base de datos para los restaurantes
class Restorant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    horario_semana = db.Column(db.String(50), nullable=False)
    horario_sabado = db.Column(db.String(50), nullable=False)
    horario_domingo = db.Column(db.String(50), nullable=False)
    horario_festivos = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.String(50), nullable=False)
    latitud = db.Column(db.Float, nullable=False)
    longitud = db.Column(db.Float, nullable=False)
    imagenes = db.relationship('Menu', backref='restorant', lazy=True)
    categoria = db.Column(db.String(50), nullable=False)

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imagen_url = db.Column(db.String(255), nullable=False)
    restorant_id = db.Column(db.Integer, db.ForeignKey('restorant.id'), nullable=False)

@app.route('/')
def index():
    # Consultar todos los restaurantes en la base de datos
    restorants = Restorant.query.all()

    return render_template('index.html', restorants=restorants, iconos = ICONOS_CATEGORIAS)

with app.app_context():
    # Crear las tablas de la base de datos
    db.create_all()

    # Cargar datos desde el archivo JSON si las tablas están vacías
    if not Restorant.query.first():
        with open('restaurantes_todos.json', 'r') as f:
            datos_prueba = json.load(f)
        
        for dato in datos_prueba:
            restaurador = Restorant(
                nombre=dato["nombre"],
                horario_semana=dato["horario_semana"],
                horario_sabado=dato["horario_sabado"],
                horario_domingo=dato["horario_domingo"],
                horario_festivos=dato["horario_festivos"],
                direccion=dato["direccion"],
                latitud=dato["latitud"],
                longitud=dato["longitud"],
                categoria=dato["categoria"]
            )
            db.session.add(restaurador)
            db.session.commit()

            # Agregar múltiples imágenes para cada restaurante
            for imagen in dato["imagenes"]:
                # Dividir las URLs usando el delimitador "|"
                urls = imagen["imagen_url"].split('|')
                for url in urls:
                    menu = Menu(imagen_url=url.strip(), restorant_id=restaurador.id)
                    db.session.add(menu)
<<<<<<< HEAD
=======
        


>>>>>>> diego
        db.session.commit()



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050, debug=True)