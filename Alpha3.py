import streamlit as st
from sympy import symbols, integrate, sin, cos, tan, sec, csc, cot
import random

# Función para generar problemas de práctica
def generar_problema(dificultad):
    x = symbols('x')

    # Seleccionar un tipo de problema aleatorio
    tipo_problema = random.choice(['algebraico', 'trigonometrico', 'mezclado'])

    # Configurar la dificultad
    if dificultad == "Fácil":
        coeficiente_max = 5
        grado_max = 2
    elif dificultad == "Intermedio":
        coeficiente_max = 10
        grado_max = 3
    else:  # Dificultad "Difícil"
        coeficiente_max = 15
        grado_max = 4

    # Generar una expresión aleatoria
    if tipo_problema == 'algebraico':
        expr = sum(random.randint(-coeficiente_max, coeficiente_max) * x**random.randint(1, grado_max) for _ in range(3))
    elif tipo_problema == 'trigonometrico':
        expr = random.choice([sin(x), cos(x), tan(x), sec(x), csc(x), cot(x)])
    else:  # Problema mezclado
        expr = random.choice([sin(x), cos(x), tan(x), sec(x), csc(x), cot(x)]) * sum(random.randint(-coeficiente_max, coeficiente_max) * x**random.randint(1, grado_max) for _ in range(2))

    # Calcular la integral indefinida
    integral_result = integrate(expr, x)

    # Generar una pregunta basada en la expresión
    pregunta = f"Calcule la integral indefinida de la siguiente expresión:"

    # Devolver la expresión, la pregunta y la solución
    return expr, pregunta, integral_result, tipo_problema

# Función para generar pistas personalizadas
def generar_pistas(tipo_problema):
    pistas_algebraico = [
        "Recuerda factorizar la expresión antes de integrar.",
        "Verifica si hay términos comunes que puedan simplificar la integral.",
        "Considera completar el cuadrado en expresiones cuadráticas.",
        "Presta atención a los patrones de factorización.",
        "Intenta agrupar términos de manera estratégica.",
        "No olvides revisar la aritmética básica al simplificar."
        "Piensa en cómo podrías simplificar términos semejantes."
        "Busca oportunidades para reducir fracciones.",
        "Considera la posibilidad de realizar una sustitución antes de integrar.",
        "No subestimes la utilidad de la simplificación algebraica."
    ]

    pistas_trigonometrico = [
        "Considera las identidades trigonométricas para simplificar la expresión.",
        "Presta atención a las formas estándar de las funciones trigonométricas.",
        "Intenta utilizar sustituciones trigonométricas.",
        "Recuerda las reglas básicas de derivación de funciones trigonométricas.",
        "Piensa en cómo las funciones trigonométricas se relacionan entre sí.",
        "Busca oportunidades para expresar las funciones trigonométricas en términos de otras.",
        "Considera cómo podrías manipular las funciones trigonométricas para facilitar la integración.",
        "No dudes en simplificar expresiones trigonométricas complicadas.",
        "Revisa las identidades trigonométricas básicas antes de comenzar.",
        "Piensa en cómo podrías usar una sustitución trigonométrica para simplificar la integral."
    ]

    pistas_mezclado = [
        "Intenta realizar una sustitución para simplificar la integral.",
        "Verifica si puedes aplicar integración por partes en algún paso.",
        "Considera separar la expresión en partes más simples.",
        "Presta atención a las oportunidades para simplificar términos.",
        "Piensa en cómo podrías combinar técnicas de integración para resolver el problema.",
        "No olvides revisar todas las posibles estrategias antes de comenzar.",
        "Busca patrones o simetrías que puedan facilitar la integración.",
        "Considera cómo podrías manipular la expresión para facilitar la aplicación de fórmulas conocidas.",
        "Revisa las propiedades de las funciones trigonométricas para simplificar expresiones.",
        "No dudes en probar diferentes enfoques antes de elegir uno."
    ]

    if tipo_problema == 'algebraico':
        return random.sample(pistas_algebraico, 2)
    elif tipo_problema == 'trigonometrico':
        return random.sample(pistas_trigonometrico, 2)
    else:  # Problema mezclado
        return random.sample(pistas_mezclado, 2)

# Función para presentar el problema al usuario
def presentar_problema(expr, pregunta, con_pistas=False, tipo_problema=None):
    st.markdown(f"**Pregunta:** {pregunta}")
    st.latex(expr)

    if con_pistas:
        # Proporcionar pistas
        st.markdown("**Pistas:**")
        pistas = generar_pistas(tipo_problema)
        for pista in pistas:
            st.write(f"- {pista}")

# Función principal
def main():
    st.title("Dolores")

    # Configurar opciones
    dificultad = st.sidebar.selectbox("Seleccione la dificultad:", ["Fácil", "Intermedio", "Difícil"])
    cantidad = st.sidebar.slider("Cantidad de problemas:", 1, 10, 5)
    mostrar_pistas = st.sidebar.checkbox("Mostrar pistas")

    # Generar y presentar problemas
    for _ in range(cantidad):
        expr, pregunta, solucion, tipo_problema = generar_problema(dificultad)
        presentar_problema(expr, pregunta, con_pistas=mostrar_pistas, tipo_problema=tipo_problema)
        st.latex(f"\\textbf{{Solución:}} \\quad {solucion}")

if __name__ == "__main__":
    main()








# import requests

# # Tu clave de API de Wolfram Alpha
# app_id = 'TPLJ58-T88JA64PR4'

# # La URL de la API de Wolfram Alpha
# url = 'http://api.wolframalpha.com/v2/query'

# # La entrada del usuario
# input_expr = 'integrate x^2'

# # Los parámetros de la consulta
# params = {
#     'appid': app_id,
#     'input': input_expr,
#     'output': 'json'
# }

# # Enviar la consulta a la API de Wolfram Alpha
# response = requests.get(url, params=params)

# # Analizar la respuesta de la API
# data = response.json()

# # Intentar acceder a 'steps' de manera segura
# pods = data.get('queryresult', {}).get('pods', [])

# # Verificar la existencia de 'IndefiniteIntegral' pod
# indefinite_integral_pod = next((pod for pod in pods if pod.get('id') == 'IndefiniteIntegral'), None)

# if indefinite_integral_pod:
#     subpods = indefinite_integral_pod.get('subpods', [])
#     steps = subpods[0].get('steps', [])

#     # Presentar los pasos detallados al usuario
#     for step in steps:
#         print(step.get('plaintext', 'No hay información de paso'))
# else:
#     print("No se encontró información de la integral indefinida en la respuesta.")
