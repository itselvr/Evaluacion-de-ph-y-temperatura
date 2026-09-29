import streamlit as st

st.title("Evaluación de un lote")

pH = st.number_input(
    "pH",
    value=6.5
)

temperatura = st.number_input(
    "Temperatura (°C)",
    value=23.0
)

if st.button("Evaluar"):

    # Completa aquí la lógica
if revisar ph:
    value= ("ph < 6.0 or ph > 7.0")
elif revisar temperatura:
    value= ("temperatura < 20 or temperatura > 25")
else lote aceptable:
    resultado=("ph=6 or ph=7, temperatura=20 or temperatura=25")

    st.write(f"Resultado: {resultado}")
