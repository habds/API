from flask import Flask
from bdfalsa import productos
app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

@app.route('/')
def inicio():
    return 'hola'