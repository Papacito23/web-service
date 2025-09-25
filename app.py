import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hola():
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
                h1 {
                    color: #2e8b57;
                    font-size: 36px;
                    margin: 0;
                }
                p {
                    color: #333;
                    font-size: 24px;
                    margin: 10px 0 0 0;
                }
            </style>
        </head>
        <body>
            <div>
                <h1>Hola, soy omar, mamasota69_ en fortnite</h1>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
