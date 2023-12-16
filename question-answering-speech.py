# Autor: Juan Pablo Torres
#Texto a voz:
#pip install gtts


# Reconocimiento de voz:
# !pip install SpeechRecognition 

#TRANSFORMERS (DistillBERT, RoBERTa, LLama2, etc)
# !pip install transformers


import os 
import pyttsx3                  # Texto a voz  sin guardar archivos
import speech_recognition as sr # Reconocimiento de voz 
import random
import keyboard  # Añadido para la detección de teclas

# TRANSFORMERS BERT
# !pip install transformers
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline

def texto_a_voz(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

def texto_a_voz_no_stop(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.startLoop(False)
    engine.iterate()
    engine.endLoop()

def detener_bucle(e):
    if keyboard.is_pressed('esc'):
        print("Bucle detenido con la tecla 'Esc'.")
        exit()

def ejecutar_codigo(): 
    the_model = 'mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es' #Importacion del modelo DISTILLBERT en español desde el repositorio del usuario mrm8488 de huggingFace
    tokenizer = AutoTokenizer.from_pretrained(the_model, do_lower_case=False)
    model = AutoModelForQuestionAnswering.from_pretrained(the_model)

    while True:
        recognizer = sr.Recognizer()  # Reconocedor
        mic = sr.Microphone()         # Micrófono
        #Detectar la tecla 'Esc' para detener el bucle
        keyboard.hook(detener_bucle)
        # ENTRADA DE AUDIO - MICROFONO
        with mic as source:
            # Esperar a que el usuario presione una tecla antes de continuar
            texto_a_voz("Presione Enter y luego pregunte...")
            input("Presione Enter y luego pregunte...")
            print("Entendiendo audio los próximos 5 segundos...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=6)
           # AUDIO A TEXTO - recognizer
        text = recognizer.recognize_google(audio, language='es-ES')
        # Sinónimos de "es una buena pregunta."
        formas_respuestaa = ["voy a procesar esta interesante interrogante.", "Es una pregunta pertinente, voy a procesarla.", "Es un excelente planteamiento.",
                            "Es una pregunta interesante.", "Es una pregunta valiosa...", "Dejame pensar..",", Voy a pensar una respuesta..."]

        # Seleccionar una forma de "Dijiste" aleatoriamente
        forma_dijiste_seleccionada = random.choice(formas_respuestaa)
        texto_a_voz_no_stop(text+forma_dijiste_seleccionada)
        print(f'Has dicho: {text}')
        
        # PENSAR
        os.system("start procesing.mp3") #sonido de procesando para esperar el procesamiento de la respuesta en base a la pregunta y el contexto
        
        # tokenización
        contexto = '''
            COVID 2019
El 12 de enero de 2020, la Organización Mundial de la Salud (OMS) recibió el genoma secuenciado40 del nuevo virus causante
de la enfermedad y lo nombró temporalmente 2019-nCoV, del inglés 2019-novel coronavirus (nuevo coronavirus), mientras que
la enfermedad era llamada «infección por 2019-nCoV» en documentos médicos, y SARS de Wuhan o Wu Flu (gripe de Wu) en
Internet. El 30 de enero, la OMS recomendó que el nombre provisorio de la enfermedad fuera "enfermedad respiratoria aguda
por 2019-nCoV", hasta que la Clasificación Internacional de Enfermedades diera un nombre oficial.45 A pesar de esta
recomendación, los medios y agencias de noticias continuaron usando la denominación neumonía de Wuhan para referirse a la
enfermedad.
49 El nombre es un acrónimo de coronavirus disease 2019 (enfermedad por coronavirus 2019, en español). Se procuró que la
denominación no contuviera nombres de personas o referencias a ningún lugar, especie animal, tipo de comida, industria, cultura
o grupo de personas, en línea con las recomendaciones internacionales, para evitar que hubiera estigmatización contra algún
colectivo.
En español, el género de la denominación de la enfermedad puede ser tanto femenino como masculino; sin embargo, el femenino
fue desde un principio el preferido por la Fundéu BBVA y, posteriormente, por la Real Academia Española (RAE): La COVID-19,
debido a que «COVID-19» es el acrónimo en inglés de enfermedad por coronavirus de 2019, donde enfermedad (palabra
representada por la letra D, elemento principal del acrónimo) solo puede ser femenino en la lengua española.6 Aunque es el
femenino el que utiliza la OMS en todos sus escritos, el uso del masculino se halla más estandarizado en el discurso público,
según la RAE, por influencia del género de coronavirus y de otras enfermedades víricas: el dengue, el MERS, el SARS, el Zika,
y otras.52 La Fundéu BBVA también señala que se puede lexicalizar el nombre de la enfermedad en textos generales,
escribiéndolo todo en minúsculas (covid-19) por tratarse de un sustantivo, en lugar de mayúscula inicial (Covid-19), como se usa
en algunos escritos;6 y que no es infrecuente ni incorrecto usar solo el primer lexema de esta palabra compuesta (COVID en
lugar de COVID-19). Esta simplificación se explicaría por el fenómeno de la economía lingüística, especialmente en el registro
informal y discurso hablado.
Cuando se la escribe con dígitos («COVID-19» en vez de «COVID»), el uso del guion es obligatorio en español (es incorrecto
«COVID19» —todo junto— o «COVID 19» —con espacio), ya que lo posee en la denominación oficial, y, además, la lengua
española tiene la costumbre de separar las palabras que se componen de letras y números. Esto último lo lleva a cabo con un
guion.
Respecto a su acentuación, ambas instituciones indican que el uso mayoritario del primer lexema de la palabra es agudo /ko'βið/
(COVID-19) —y que la voz es, de hecho, aguda en español—, por lo que solo una población minoritaria de hispanohablantes la
acentúan como llana /'ko.βið/, por influencia del inglés, lengua de origen del término (COVID-19).5455 El nombre completo de
la enfermedad ha de leerse preferentemente como: [ko'βið.dje.si'nwe.βe] en zonas de seseo, y como: [ko'βið.dje.θi'nwe.βe] en
zonas no seseantes.
Descubrimiento
En diciembre de 2019 hubo un brote epidémico de neumonía de causa desconocida en Wuhan, provincia de Hubei, China; el
cual, según afirmó más tarde Reporteros Sin Fronteras, llegó a afectar a más de 60 personas el día 20 de ese mes.
Según el Centro Chino para el Control y Prevención de Enfermedades (CCDC), el 29 de diciembre un hospital en Wuhan
(Hospital Provincial de Medicina Integrada Tradicional China y Occidental, también conocido como el hospital de Xinhua,) admitió
a 4 individuos con neumonía, quienes trabajaban en un mercado de esa ciudad. El hospital informó esto al CCDC, cuyo equipo
en la ciudad inició una investigación. El equipo encontró más casos relacionados al mercado y el 30 de diciembre las autoridades
de salud de Wuhan comunicaron los casos al CCDC, que envió expertos a Wuhan para apoyar la investigación. Se obtuvieron
muestras de estos pacientes para realizar análisis de laboratorio.
El 31 de diciembre, el Comité de Salud Municipal de Wuhan informó a la Organización Mundial de la Salud (OMS) que 27
personas habían sido diagnosticadas con neumonía de causa desconocida, habiendo 7 en estado crítico; la mayoría de estos
casos eran trabajadores del mencionado mercado.57 Para el 1 de enero de 2020, el mercado había sido cerrado y se había
descartado que el causante de la neumonía fuera el SARS, el MERS, gripe, gripe aviaria u otras enfermedades respiratorias
comunes causadas por virus.
El 7 de enero de 2020 los científicos chinos habían aislado el virus causante de la enfermedad, y realizaron
la secuenciación del genoma. Esta secuenciación estuvo disponible para la OMS el 12 de enero de 2020, permitiendo a los
laboratorios de diferentes países producir diagnósticos específicos vía pruebas de PCR.
El 12 de enero de 2020, las autoridades chinas habían confirmado la existencia de 41 personas infectadas con el nuevo virus,
quienes comenzaron a sentir síntomas entre el 8 de diciembre de 2019 y el 2 de enero de 2020, los cuales incluían: fiebre,
malestar, tos seca, dificultad para respirar y fallos respiratorios;41 también se observaron infiltrados neumónicos invasivos en
ambos pulmones observables en las radiografías de tórax.
Tras el primer brote de COVID-19 en Wuhan en diciembre de 2019, donde las autoridades chinas confirmaron 41 casos
detectados entre el 8 de diciembre y el 2 de enero de 2020,42 la ciudad dejó de informar casos hasta el 19 de enero, cuando se
confirmaron 17 casos más. Para ese entonces ya se habían comunicado los primeros casos por COVID-19 fuera de China: dos
en Tailandia y uno en Japón.
La rápida expansión de la enfermedad hizo que la Organización Mundial de la Salud, el 30 de enero de 2020, la declarara
una emergencia sanitaria de preocupación internacional, basándose en el impacto que el virus podría tener en países
subdesarrollados con menos infraestructuras sanitarias.59 En esa fecha, la enfermedad se había detectado en todas las
provincias de China continental,60 y se diagnosticaban casos en otros 15 países.
El 11 de marzo la enfermedad se hallaba ya en más de 100 territorios a nivel mundial, y fue reconocida como una pandemia por
la OMS.61 El número de casos confirmados continuó creciendo hasta alcanzar los 500 mil casos a nivel mundial el 26 de marzo
de 2020.
Para prevenir la expansión del virus, los gobiernos han impuesto restricciones de viajes, cuarentenas, confinamientos,
aislamiento social, cancelación de eventos, y cierre de establecimientos. La pandemia está teniendo un efecto socioeconómico
disruptivo,63 y el miedo a la escasez de provisiones ha llevado a compras de pánico. Ha habido desinformación y teorías
conspirativas difundidas en línea sobre el virus,6465 e incidentes de xenofobia y racismo contra los ciudadanos chinos y de otros
países del este y sudeste asiático
Se ha comprobado que las cuarentenas, restricciones al tráfico de personas y los aislamientos que se están dando a causa de
la pandemia tienen efectos psicológicos negativos. A finales de enero, la Comisión Nacional de Salud de China publicó una guía
de manejo de las crisis psicológicas, en la que propugnaba la intervención de las personas afectadas, contactos cercanos, los
encerrados en sus hogares, los familiares y amigos de los pacientes, personal sanitario y el público general que lo requiriera.
Según estudios realizados en 2020, se confirma que ha afectado en mayor medida a la salud mental de las mujeres que a la de
los hombres. Entre los motivos se encuentra el aumento de la violencia de género y su situación socioeconómica más precaria.
Buena parte de las mujeres trabajan en el sector de la restauración y del turismo, de los más afectados por la pandemia, además
de ser las principales cuidadoras de personas enfermas, de niños y de personas de la tercera edad.
El aislamiento ha provocado que muchos enfermos no puedan continuar con sus tratamientos, agravando sus problemas de
salud. En estos escenarios, las mujeres, ya sean familiares o cuidadoras, suelen tener un papel fundamental.
          '''
        pregunta = text

        encode = tokenizer.encode_plus(pregunta, contexto, return_tensors='pt')
        input_ids = encode['input_ids'].tolist()
        tokens = tokenizer.convert_ids_to_tokens(input_ids[0])
        for id, token in zip(input_ids[0], tokens):
            print('{:<12} {:>6}'.format(token, id))
            print('')

        # Ejemplo de inferencia (pregunta-respuesta)
        nlp = pipeline('question-answering', model=model, tokenizer=tokenizer)
        salida = nlp({'question': pregunta, 'context': contexto})
        print(str(salida.get('answer')))

        # Sinónimos de "Dijiste"
        formas_dijiste = ["Te entendí","Escuché","Mencionaste", "Lo que expresaste fue ", "Lo que dijiste fue", "Dijiste que", "De lo dicho","De lo que dijiste","De lo que escuche","De lo que Entendí", "Preguntaste", "Enunciaste", "Explicaste"]

        # Sinónimos de "y la respuesta a esto es..."
        formas_respuesta = ["y lo que procesé como salida es...", "y la contestación es...", "y la explicación sería...", "y la respuesta que obtengo es...",
                            "y lo que quiero decir es...", "y aquí está la respuesta...", "y la conclusión es..."]

        # Seleccionar una forma de "Dijiste" aleatoriamente
        forma_dijiste_seleccionada = random.choice(formas_dijiste)

        # Seleccionar una forma de "y la respuesta a esto es..." aleatoriamente
        forma_respuesta_seleccionada = random.choice(formas_respuesta)

        # Ejemplo de uso en la respuesta de audio
        respuesta_audio = f"{forma_dijiste_seleccionada} {text} {forma_respuesta_seleccionada} {str(salida.get('answer'))}"
        texto_a_voz(respuesta_audio)
        #tts = gTTS(text=respuesta_audio, lang='es')
        #tts.save("output.mp3")
        #os.system("start output.mp3")
        # Añadido: Liberar el gancho de teclado para evitar problemas
        keyboard.unhook_all()
        # Llamar a la función para ejecutar el código
        ejecutar_codigo()
ejecutar_codigo()

