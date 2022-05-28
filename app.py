from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1> Cara con sombrero de vaquero 🤠 </h1> <p>Flask en Heroku gaaa</p>'

if __name__=='__main__':
    app.run()