from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return "<hi>¡Hola Mundo desde Flask!</hi>"

if __name__ == '__main__':
    app.run(debug=True)