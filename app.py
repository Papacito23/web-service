import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Página con formulario
@app.route("/", methods=["GET"])
def index():
    return """
    <html>
        <head>
            <title>Servicio Web</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f8ff;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    text-align: center;
                }
                form {
                    background: #fff;
                    padding: 20px;
                    border-radius: 15px;
                    box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
                }
                input[type=text] {
                    padding: 10px;
                    font-size: 16px;
                    border-radius: 8px;
                    border: 1px solid #ccc;
                    width: 250px;
                }
                input[type=submit] {
                    padding: 10px 20px;
                    font-size: 16px;
                    border: none;
                    border-radius: 8px;
                    background: #2e8b57;
                    color: white;
                    cursor: pointer;
                    margin-top: 10px;
                }
                input[type=submit]:hover {
                    background: #246b45;
                }
            </style>
        </head>
        <body>
            <form action="/saludo" method="post">
                <h2>Escribe tu nombre:</h2>
                <input type="text" name="nombre" placeholder="Tu nombre aquí" required>
                <br>
                <input type="submit" value="Enviar">
            </form>
        </body>
    </html>
    """

# Ruta que procesa el formulario y devuelve JSON
@app.route("/saludo", methods=["POST"])
def saludo():
    nombre = request.form.get("nombre", "invitado")

    # Estructura: usamos el parámetro
    if nombre.lower() == "omar":
        mensaje = "¡Bienvenido, Omar! Veo que eres  Mamasota69_ en el Fortnite Ggrr"
    else:
        mensaje = f"Hola {nombre}, bienvenido a este servicio web Ggrr"

    # Respuesta en formato JSON
    return jsonify({
        "usuario": nombre,
        "mensaje": mensaje,
        "status": "success"
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
