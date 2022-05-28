from flask import Flask

app = Flask(__name__)

@app.rout('/')
def home():
    return 'Flask en Heroku gaaa'

if __name__=='__main__':
    app.run()