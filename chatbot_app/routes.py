# """Routes for parent Flask app."""
# import flask
# import mysql
# import mysql.connector
# from flask import render_template, request, jsonify
# from flask import current_app as app
# import os

# # from chat2 import get_response

# # Iniciar el modelo BERT / Cargar en memoria
# def init_model():
#     from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
#     modelo = 'mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es'
#     tokenizer = AutoTokenizer.from_pretrained(modelo, do_lower_case=False)
#     model = AutoModelForQuestionAnswering.from_pretrained(modelo)
#     nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
#     return nlp;


# def conexion(conexion_switch = 2):
#     import mysql
#     import mysql.connector
#     if conexion_switch == 1:
#         cnx = mysql.connector.connect(user='u650849267_chatbot', password='Chatbot1',
#                                   host='45.93.101.1',
#                                   database='u650849267_chatbot')
#     elif conexion_switch == 2:
#         cnx = mysql.connector.connect(user='chatbot_app', password='analitica_datos_UNI_E12',
#                                   host='127.0.0.1',
#                                   database='chatbot_admision')
#     return cnx


# # Insertar contexto en la BD
# def lee_contexto(conexion_switch=2):
#     contexto = ""
#     cnx = conexion(conexion_switch)
#     cursor = cnx.cursor()

#     # Leyendo los hechos de la BD
#     cursor.execute("SELECT hecho FROM hecho")
#     result_set = cursor.fetchall()
#     for hecho in result_set:
#         contexto += hecho[0]

#     cursor.close()
#     cnx.close()

#     return contexto


# def inserta(json_data,conexion_switch=2):
#     # json_data = json.loads(json_text)

#     preg = json_data['pregunta']
#     resp_object = json_data["respuesta"]
#     score = resp_object['score']
#     start = resp_object['start']
#     end = resp_object['end']
#     answer = resp_object['answer']
#     entendio = False
#     # Umbral de aceptaci??n
#     if (score > 0.002):
#         entendio = True

#     cnx = conexion(conexion_switch)
#     cursor = cnx.cursor()
#     add_data = ("INSERT INTO pregunta "
#                 "(pregunta, entendio)"
#                 "VALUES (%s, %s)")
#     value_data = (preg, entendio)
#     cursor.execute(add_data, value_data)
#     last_id = cursor.lastrowid

#     add_data = ("INSERT INTO respuesta "
#                 "(score, start, end, answer, id_pregunta)"
#                 "VALUES (%s, %s, %s, %s, %s)")
#     value_data = (score, start, end, answer, last_id)
#     cursor.execute(add_data, value_data)
#     cnx.commit()
#     # cnx.rollback()
#     cursor.close()
#     cnx.close()


# contexto = lee_contexto(1)
# print(contexto)
# # TODO: CARGAR A BASE DE DATOS
# contexto_total = """La tasa de selectividad o admisi??n es de un ingresante por cada nueve postulantes. 
# La Oficina de Central de Admisi??n (OCAD) inici?? sus actividades en 1980. 
# La Universidad Nacional de Ingenier??a (UNI) es una universidad p??blica peruana.
# La OCAD se encarga de organizar, ejecutar y evaluar el proceso de ingreso a la Universidad, asegurando la incorporaci??n de alumnos por sus m??ritos, que tengan las capacidades requeridas para seguir estudios universitarios.
# El proceso autom??tico de calificaci??n de los ex??menes se lleva a cabo en el Centro de C??mputo de la Oficina de Admisi??n bajo la supervisi??n de las autoridades de la universidad.
# Las modalidades de admisi??n a la UNI son ordinario y extraordinario.
# La carrera m??s demandada es ingenier??a civil.
# El proceso de admisi??n consta de tres ex??menes que eval??an matem??ticas, letras y f??sica y qu??mica, cada examen dura tres horas.
# El examen de admisi??n consta de tres partes que son evaluadas en tres fechas (lunes, mi??rcoles y viernes) y tienen una duraci??n de tres horas cada una.
# Son 10 modalidades extraordinarias.
# Las inscripciones para la modalidad IEN comienzan el lunes 18/10/2021 y terminan el jueves 25/11/2021. El examen de admisi??n general 2022-I es el Lunes 01/03/2022.
# El prospecto cuesta S/ 90.00. El pago para dar o rendir el examen es de S/ 550.00.
# Los pagos se realizar??n en el banco BCP, agentes BCP o banca por internet BCP.
# El tel??fono para consultas es 981607508.
# El correo para informes es informes@admisionuni.edu.pe.
# La UNI ofrece 28 especialidades.
# Se puede postular varias veces a la UNI, no hay l??mites para postular.
# La UNI queda en Av. Tupac Amaru 210 R??mac
# Hay 52 vacantes para Arquitectura.
# Hay 25 vacantes para F??sica.
# Hay 25 vacantes para Matem??tica.
# Hay 25 vacantes para Qu??mica.
# Hay 25 vacantes para Ingenier??a f??sica.
# Hay 25 vacantes para Ciencias de la Computaci??n.
# Hay 28 vacantes para Ingenier??a Sanitaria
# Hay 28 vacantes para Ingenier??a de Higiene.
# Hay 28 vacantes para Ingenier??a Ambiental.
# Hay 126 vacantes para Ingenier??a Civil.
# Hay 39 vacantes para Ingenier??a Econ??mica.
# Hay 37 vacantes para Ingenier??a Estad??stica.
# Hay 28 vacantes para Ingenier??a El??ctrica.
# Hay 28 vacantes para Ingenier??a Electr??nica.
# Hay 28 vacantes para Ingenier??a de Telecomunicaciones.
# Hay 23 vacantes para Ingenier??a Geol??gica.
# Hay 30 vacantes para Ingenier??a Metal??rgica.
# Hay 27 vacantes para Ingenier??a de Minas.
# Hay 70 vacantes para Ingenier??a Industrial.
# Hay 70 vacantes para Ingenier??a de Sistemas.
# Hay 27 vacantes para Ingenier??a Mec??nica.
# Hay 27 vacantes para Ingenier??a Mec??nica El??ctrica.
# Hay 27 vacantes para Ingenier??a Naval.
# Hay 27 vacantes para Ingenier??a Mecatr??nica.
# Hay 13 vacantes para Ingenier??a Petroqu??mica.
# Hay 13 vacantes para Ingenier??a de Petr??leo y Gas Natural.
# Hay 31 vacantes para Ingenier??a Qu??mica.
# Hay 18 vacantes para Ingenier??a Textil.
# El orden de m??rito en cada Especialidad se determina mediante la nota final que obtenga el postulante.
# El examen de letras tiene 745 puntos.
# El examen de matem??ticas tiene 600 puntos.
# El examen de f??sica y qu??mica tiene 500 puntos.
# Los puntos en total son 1845.
# El puntaje m??nimo para ingresar es 11.
# Los resultados se publican en la p??gina de la OCAD.
# El Concurso de Admisi??n consiste en la evaluaci??n de conocimientos, aptitudes, intereses vocacionales y la formaci??n integral de los postulantes.
# La UNI ofrece en total 754 vacantes.
# El examen de IEN fue el Domingo 05/12/2022.
# La tasa de ingreso para arquitectura es 8%.
# La tasa de ingreso para f??sica es 20.20%.
# La tasa de ingreso para matem??tica es 27.60%.
# La tasa de ingreso para qu??mica es 21.10%.
# La tasa de ingreso para ingenier??a f??sica es 29.80%.
# La tasa de ingreso para ciencia de la computaci??n es 19.80%.
# La tasa de ingreso para ingenier??a sanitaria es 39.50%.
# La tasa de ingreso para ingenier??a de higiene y seguridad industrial es 46.70%.
# La tasa de ingreso para ingenier??a ambiental es 27%.
# La tasa de ingreso para ingenier??a civil es 14.80%.
# La tasa de ingreso para ingenier??a econ??mica es 22.40%.
# La tasa de ingreso para ingenier??a estad??stica es 31.03%.
# La tasa de ingreso para ingenier??a el??ctrica es 28.72%.
# La tasa de ingreso para ingenier??a electr??nica es 17.30%.
# La tasa de ingreso para ingenier??a de telecomunicaciones es 25.47%.
# La tasa de ingreso para ingenier??a geol??gica es 30.26%.
# La tasa de ingreso para ingenier??a metal??rgica es 93.75%.
# La tasa de ingreso para ingenier??a de minas es 16.02%.
# La tasa de ingreso para ingenier??a industrial es 15.83%.
# La tasa de ingreso para ingenier??a de sistemas es 12.11%.
# La tasa de ingreso para ingenier??a mec??nica es 19.07%.
# La tasa de ingreso para ingenier??a mec??nica-el??ctrica es 34.66%.
# La tasa de ingreso para ingenier??a naval es 80%.
# La tasa de ingreso para ingenier??a mecatr??nica es 7.87%.
# La tasa de ingreso para ingenier??a petroqu??mica es 27.27%.
# La tasa de ingreso para ingenier??a de petr??leo y gas natural es 29.41%.
# La tasa de ingreso para ingenier??a qu??mica es 19.56%.
# La tasa de ingreso para ingenier??a textil es 42.85%.
# La nota m??nima promedio para ingresar a Arquitectura es 11.573.
# La nota m??nima promedio para ingresar a F??sica es 12.135.
# La nota m??nima promedio para ingresar a Matem??tica es 11.004.
# La nota m??nima promedio para ingresar a Qu??mica es 12.183.
# La nota m??nima promedio para ingresar a Ingenier??a F??sica es 11.199.
# La nota m??nima promedio para ingresar a Ciencia de la Computaci??n es 11.337.
# La nota m??nima promedio para ingresar a Ingenier??a Sanitaria es 11.127.
# La nota m??nima promedio para ingresar a Ingenier??a de Higiene y Seguridad Industrial es 11.039.
# La nota m??nima promedio para ingresar a Ingenier??a Ambiental es 13.146.
# La nota m??nima promedio para ingresar a Ingenier??a Civil es 14.38.
# La nota m??nima promedio para ingresar a Ingenier??a Econ??mica es 11.331.
# La nota m??nima promedio para ingresar a Ingenier??a Estad??stica es 11.001.
# La nota m??nima promedio para ingresar a Ingenier??a El??ctrica es 13.023.
# La nota m??nima promedio para ingresar a Ingenier??a Electr??nica es 13.627.
# La nota m??nima promedio para ingresar a Ingenier??a de Telecomunicaciones es 13.324.
# La nota m??nima promedio para ingresar a Ingenier??a Geol??gica es 12.556.
# La nota m??nima promedio para ingresar a Ingenier??a Metal??rgica es 12.115.
# La nota m??nima promedio para ingresar a Ingenier??a de Minas es 12.478.
# La nota m??nima promedio para ingresar a Ingenier??a Industrial es 14.419.
# La nota m??nima promedio para ingresar a Ingenier??a de Sistemas es 13.654.
# La nota m??nima promedio para ingresar a Ingenier??a Mec??nica es 13.768.
# La nota m??nima promedio para ingresar a Ingenier??a Mec??nica-el??ctrica es 13.109.
# La nota m??nima promedio para ingresar a Ingenier??a Naval es 12.205.
# La nota m??nima promedio para ingresar a Ingenier??a Mecatr??nica es 14.304.
# La nota m??nima promedio para ingresar a Ingenier??a Petroqu??mica es 11.011.
# La nota m??nima promedio para ingresar a Ingenier??a de Petr??leo y gas natural es 11.781.
# La nota m??nima promedio para ingresar a Ingenier??a Qu??mica es 12.275.
# La nota m??nima promedio para ingresar a Ingenier??a Textil es 11.186.
# """

# nlp = init_model();


# # Obtener respuesta del modelo BERT
# def get_response(msg):
#     response = nlp({'question': msg, 'context': contexto})
#     print(response)
#     if response['score'] < 0.0001: # La probabilidad de haber respondido correctamente es menor que 10%
#         response['answer'] = "No estoy muy seguro de mi respuesta"
#     return response


# @app.get("/")
# def index_get():
#     return render_template("base.html")


# @app.post("/predict")
# def predict():
#     text = request.get_json().get("message")
#     response_object = get_response(text)
#     response = response_object['answer']
#     datos_bd = {'pregunta': text, 'respuesta': response_object}
#     inserta(datos_bd,1) # 1: BD en VPS/ 2: BD local
#     message = {"answer": response}
#     return jsonify(message)
