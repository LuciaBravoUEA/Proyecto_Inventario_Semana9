from flask import Flask, jsonify

app = Flask(__name__)

# Lista de productos
inventario = {
    "001": {"nombre": "Arroz", "precio": 1.50, "cantidad": 20},
    "002": {"nombre": "Azúcar", "precio": 1.20, "cantidad": 15},
    "003": {"nombre": "Aceite", "precio": 3.00, "cantidad": 10}
}

# Ruta principal
@app.route("/")
def inicio():
    return "Bienvenido al inventario de Viveres TENZIN"

# Ruta para mostrar TODOS los productos
@app.route("/inventario")
def mostrar_inventario():
    return jsonify(inventario)

# Ruta dinámica para mostrar un producto por código
@app.route("/item/<codigo>")
def mostrar_item(codigo):
    if codigo in inventario:
        return jsonify(inventario[codigo])
    else:
        return "Producto no encontrado"

if __name__ == "__main__":
    app.run(debug=True)