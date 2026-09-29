import streamlit as st
st.sidebar.title("evaluacion de temperatura y ph")
st.sidebar.write("es una aplicacion de un lote liquido que evalua dos variables: ph y temperatura, itsel guadalupe vazquez reyes, grupo 3l, facultad de ciencias quimicas.")

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
  if ph < 6.0 or ph > 7.0:
      st.error("revisar el ph")
  elif temperatura < 20 or temperatura > 25:
      st.warning("revisar la temperatura")
  else:
      st.success("el lote es aceptable")
    
concentracion= st.number_imput( "concentracion (%), value=10.0")
    st.write(f"Resultado: {resultado}")
