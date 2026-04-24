import streamlit as st

st.title("Para Ian 🎵✨")
st.markdown("Responde este pequeño cuestionario Swiftie para desbloquear un mensaje especial.")

# Definición de las preguntas
preguntas = [
    {"p": "¿Cuál es el nombre de tu cantante más escuchada en estos momentos?", "r": "Taylor Swift"},
    {"p": "¿Cual de estas canciones pertenece a 'Speak Now'? (Enchanted / Clean)", "r": "Enchanted"},
    {"p": "¿De qué canción viene esta frase: 'This ultraviolet morning light below'?", "r": "Afterglow"},
    {"p": "¿Cuál es la canción de Taylor que te hace pensar en un color medio oscuro como el vino?", "r": "Maroon"},
    {"p": "¿Cuál es la canción que contiene esta frase: 'You had to make your own sunshine'?", "r": "Opalite"}
]

# Cambiamos el nombre a 'respuestas_dict' para evitar conflictos con el estado anterior
if "respuestas_dict" not in st.session_state:
    st.session_state.respuestas_dict = {}

# Crear los campos de entrada
for i, pregunta in enumerate(preguntas):
    # Usamos la nueva variable y la forma de obtener datos de forma segura
    if i not in st.session_state.respuestas_dict:
        st.session_state.respuestas_dict[i] = ""
    
    st.session_state.respuestas_dict[i] = st.text_input(
        pregunta["p"], 
        value=st.session_state.respuestas_dict[i], 
        key=f"q{i}"
    )

st.divider()

st.info("💡 ¡Ya casi! Ahora, toma la primera letra de cada respuesta que diste arriba y escribe la frase resultante aquí abajo:")

frase_usuario = st.text_input("Escribe la frase secreta:", key="frase_final")

if st.button("Descubrir el mensaje"):
    if frase_usuario.lower() == "teamo":
        st.balloons()
        st.success("¡Lo lograste! ✨")
        
        st.markdown("""
        ### Un mensaje para ti:
       Sabia que resolverias la frase secreta, esto es tan solo un proyecto que estoy armando
       lo cual fuiste la primera en probarlo, gracias por participar, sos una re conocedora de taylor
       y que sos mi unica duo y favorita, con la cual podria jugar mil games y nunca aburrime
       y no me interesa el resultado si gano o pierdo mientras sea con vos, siempre voy a estar ganando,
        Y AUNQUE TE CAGUES DE RISA DE MI MALDITO PROYECTO es solo una prueba de lo que intentaba hacer      
        para crear mini juegos de CUANTO SABES DE TAYLOR WACHINA
        """)
    else:
        st.error("Mmm... esa no parece ser la frase correcta. ¡Revisa las iniciales de tus respuestas y vuelve a intentar!")
