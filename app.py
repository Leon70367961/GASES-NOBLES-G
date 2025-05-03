import streamlit as st

st.title("Calculadora de la Ecuación General de los Gases Ideales")
st.write("Unidades: Presión en atm, Volumen en litros, Temperatura en Kelvin")

# Opciones disponibles
variable_a_calcular = st.selectbox(
    "Selecciona la variable que deseas calcular:",
    ("Presión 1 (P1)", "Volumen 1 (V1)", "Temperatura 1 (T1)",
     "Presión 2 (P2)", "Volumen 2 (V2)", "Temperatura 2 (T2)")
)

# Diccionario de campos a mostrar según la selección
campos = {
    "Presión 1 (P1)": ["V1", "T1", "P2", "V2", "T2"],
    "Volumen 1 (V1)": ["P1", "T1", "P2", "V2", "T2"],
    "Temperatura 1 (T1)": ["P1", "V1", "P2", "V2", "T2"],
    "Presión 2 (P2)": ["P1", "V1", "T1", "V2", "T2"],
    "Volumen 2 (V2)": ["P1", "V1", "T1", "P2", "T2"],
    "Temperatura 2 (T2)": ["P1", "V1", "T1", "P2", "V2"]
}

# Solicita los datos faltantes
inputs = {}
for campo in campos[variable_a_calcular]:
    inputs[campo] = st.number_input(f"Ingrese {campo}:", step=0.01, format="%.2f")

# Cálculo
def calcular(variable, datos):
    try:
        if variable == "Presión 1 (P1)":
            return datos["P2"] * datos["V2"] * datos["T1"] / (datos["T2"] * datos["V1"])
        elif variable == "Volumen 1 (V1)":
            return datos["P2"] * datos["V2"] * datos["T1"] / (datos["T2"] * datos["P1"])
        elif variable == "Temperatura 1 (T1)":
            return datos["T2"] * datos["P1"] * datos["V1"] / (datos["P2"] * datos["V2"])
        elif variable == "Presión 2 (P2)":
            return datos["P1"] * datos["V1"] * datos["T2"] / (datos["T1"] * datos["V2"])
        elif variable == "Volumen 2 (V2)":
            return datos["P1"] * datos["V1"] * datos["T2"] / (datos["T1"] * datos["P2"])
        elif variable == "Temperatura 2 (T2)":
            return datos["T1"] * datos["P2"] * datos["V2"] / (datos["P
