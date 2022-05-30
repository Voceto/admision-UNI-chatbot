from flask import Flask, render_template,request,jsonify
from chatbot_app.chat import get_response,inserta
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response_object = get_response(text)
    response = response_object['answer']
    datos_bd = {'pregunta': text, 'respuesta': response_object}
    inserta(datos_bd,1)
    message = {"answer": response}
    return jsonify(message)
if __name__=='__main__':
    app.run(debug=True, port=5000)