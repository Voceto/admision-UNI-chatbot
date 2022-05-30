import mysql.connector
# Se carga el modelo BERT preentrenado
def init_model():
    from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
    the_model = 'mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es'
    tokenizer = AutoTokenizer.from_pretrained(the_model, do_lower_case=False)
    model = AutoModelForQuestionAnswering.from_pretrained(the_model)
    nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
    return nlp;


def conexion(conexion_switch = 1):
    import mysql
    import mysql.connector
    if conexion_switch == 1:
        cnx = mysql.connector.connect(user='sql10496327', password='yBzj62dSxP',
                                  host='sql10.freesqldatabase.com',
                                  database='sql10496327')
    elif conexion_switch == 2:
        cnx = mysql.connector.connect(user='chatbot_app', password='analitica_datos_UNI_E12',
                                  host='127.0.0.1',
                                  database='chatbot_admision')
    return cnx


def leer_contexto(conexion_switch=2):
    contexto = ""
    cnx = conexion(conexion_switch)
    cursor = cnx.cursor()

    # Leyendo los hechos de la BD
    cursor.execute("SELECT hecho FROM hechos")
    result_set = cursor.fetchall()
    for hecho in result_set:
        contexto += hecho[0]

    cursor.close()
    cnx.close()

    return contexto


def inserta(json_data,conexion_switch=2):
    # json_data = json.loads(json_text)

    preg = json_data['pregunta']
    resp_object = json_data["respuesta"]
    score = resp_object['score']
    start = resp_object['start']
    end = resp_object['end']
    answer = resp_object['answer']
    entendio = False
    # Umbral de aceptación
    if (score > 0.002):
        entendio = True

    cnx = conexion(conexion_switch)
    cursor = cnx.cursor()
    add_data = ("INSERT INTO preguntas "
                "(pregunta, entendio)"
                "VALUES (%s, %s)")
    value_data = (preg, entendio)
    cursor.execute(add_data, value_data)
    last_id = cursor.lastrowid

    add_data = ("INSERT INTO respuestas "
                "(score, start, end, answer, id_pregunta)"
                "VALUES (%s, %s, %s, %s, %s)")
    value_data = (score, start, end, answer, last_id)
    cursor.execute(add_data, value_data)
    cnx.commit()
    # cnx.rollback()
    cursor.close()
    cnx.close()
contexto = leer_contexto(1)
nlp = init_model();
#Respodemos la pregunta usando a BERT
def get_response(msg):
    response = nlp({'question': msg, 'context': contexto})
    print(response)
    if response['score'] < 0.0001:
        response['answer'] = "No estoy muy seguro de mi respuesta"
    return response
