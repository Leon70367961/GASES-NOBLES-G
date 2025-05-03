import streamlit as st

st.set_page_config(page_title="Calculadora Gases Ideales", layout="centered")

st.title("Calculadora de la Ecuación General de Gases Ideales")
st.write("**Fórmula:** (P₁ × V₁) / T₁ = (P₂ × V₂) / T₂")
st.caption("Unidades: Presión en atm, Volumen en litros, Temperatura en Kelvin")

# Selector principal
variable_objetivo = st.radio(
    "¿Qué variable deseas calcular?",
    ("P1", "V1", "T1", "P2", "V2", "T2")
)

# Diccionario con campos requeridos para cada variable
variables_requeridas = {
    "P1": ["V1", "T1", "P2", "V2", "T2"],
    "V1": ["P1", "T1", "P2", "V2", "T2"],
    "T1": ["P1", "V1", "P2", "V2", "T2"],
    "P2": ["P1", "V1", "T1", "V2", "T2"],
    "V2": ["P1", "V1", "T1", "P2", "T2"],
    "T2": ["P1", "V1", "T1", "P2", "V2"]
}

# Crear inputs dinámicamente
datos = {}
for var in variables_requeridas[variable_objetivo]:
    datos[var] = st.number_input(f"Ingrese {var}:", min_value=0.01, format="%.3f")

# Lógica de cálculo
def calcular(variable, valores):
    try:
        if variable == "P1":
            return valores["P2"] * valores["V2"] * valores["T1"] / (valores["T2"] * valores["V1"])
        elif variable == "V1":
            return valores["P2"] * valores["V2"] * valores["T1"] / (valores["T2"] * valores["P1"])
        elif variable == "T1":
            return valores["T2"] * valores["P1"] * valores["V1"] / (valores["P2"] * valores["V2"])
        elif variable == "P2":
            return valores["P1"] * valores["V1"] * valores["T2"] / (valores["T1"] * valores["V2"])
        elif variable == "V2":
            return valores["P1"] * valores["V1"] * valores["T2"] / (valores["T1"] * valores["P2"])
        elif variable == "T2":
            return valores["T1"] * valores["P2"] * valores["V2"] / (valores["P1"] * valores["V1"])
    except ZeroDivisionError:
        return "Error: división por cero"

# Botón para calcular
if st.button("Calcular"):
    resultado = calcular(variable_objetivo, datos)
    st.success(f"El valor de {variable_objetivo} es: {resultado:.3f}")
