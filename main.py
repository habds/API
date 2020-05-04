from flask import Flask
from bdfalsa import productos
app = Flask(__name__)



@app.route('/')
def inicio():
    return 'hola'

if __name__ == '__main__':
    app.run(debug=True, port=5000)