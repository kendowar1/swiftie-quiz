import streamlit as st

# Configuración de página
st.set_page_config(page_title="Taylor Swift Quiz", page_icon="🎵")

# Título colorido
st.markdown("<h1 style='text-align: center; color: #FF69B4;'>Test Quiz Taylor Swift 🎵✨</h1>", unsafe_allow_html=True)

# Imagen de cabecera
st.image("https://images.unsplash.com/photo-1598387181032-a3103a2db5b3?q=80&w=1000", use_container_width=True)

# Definición de preguntas
preguntas = [
    {"p": "¿A qué canción pertenece: 'I don't wanna think of anything else now that I thought of you'?", "opciones": ["Daylight", "Wishlist", "So High School"], "correcta": "Daylight", "audio": "daylight.mp3"},
    {"p": "¿Cuándo fue el primer show del Eras Tour?", "opciones": ["17 de marzo del 2023", "10 de marzo del 2023", "15 de abril del 2023"], "correcta": "17 de marzo del 2023", "audio": "eras_tour.mp3"},
    {"p": "¿Cuál es la primer canción de la era Evermore en el Eras Tour?", "opciones": ["Willow", "Tolerate It", "Champagne Problems"], "correcta": "Willow", "audio": "willow.mp3"},
    {"p": "¿Cuántas parejas tuvo Taylor Swift?", "opciones": ["11", "10", "13"], "correcta": "11", "audio": "swiftie.mp3"},
    {"p": "¿Cuál es el álbum más vendido de Taylor Swift?", "opciones": ["1989", "Red", "Midnights"], "correcta": "1989", "audio": "1989.mp3"},
    {"p": "¿De qué canción viene: 'There's just one who could make me stay'?", "opciones": ["You're on your own kid", "Would've, could've, should've", "All you had to do was stay"], "correcta": "You're on your own kid", "audio": "yoyok.mp3"}
]

# Estado de respuestas
if "respuestas_usuario" not in st.session_state:
    st.session_state.respuestas_usuario = [None] * len(preguntas)

# Renderizado de preguntas
for i, pregunta in enumerate(preguntas):
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        respuesta = st.selectbox(pregunta["p"], options=pregunta["opciones"], index=None, key=f"q{i}")
        st.session_state.respuestas_usuario[i] = respuesta
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        if respuesta == pregunta["correcta"]:
            st.markdown("### ✅")
            with st.expander("Escuchar audio 🎵"):
                st.audio(pregunta["audio"], format="audio/mp3")
        elif respuesta is not None:
            st.markdown("### ❌")
    st.divider()

# Adivinanza final
st.subheader("🕵️‍♀️ El desafío final (Adivinanza)")
st.info("""
No hablo de una danza, sino de una fecha que marca el fin de la calidez. 
Fui la primera en romper el pacto del orgullo, entregando una confesión que no buscaba el triunfo, 
sino la redención ante un hombre de piel tan clara como la honestidad que yo perdí. 
En el mapa de mi discografía, soy el punto exacto donde el invierno se vuelve una disculpa, 
y el 'te extraño' es el eco más amargo de un error cometido bajo la luz de una estación que juré cambiar.
¿Qué canción soy?
""")

frase_usuario = st.text_input("Escribe tu respuesta aquí:")

if st.button("¡Descubrir mensaje final!"):
    # Limpiamos el texto para que no importe mayúsculas, espacios o guiones
    respuesta_limpia = frase_usuario.lower().replace(" ", "").replace("-", "")
    objetivo = "backtodecember"
    
    if None in st.session_state.respuestas_usuario:
        st.warning("¡Completa todas las preguntas primero!")
    elif respuesta_limpia == objetivo:
        st.balloons()
        st.success("¡Lo lograste✨")
        st.markdown("### Un mensaje para ti:")
        st.write("Bien reina, aunque esto parezca muy pete, espero haberte divertido aunque sea un ratazo dea, y si te gusto, puedo hacer mas como estos con diferentes artistas o cosas, espero que la hayas pasado bien y que no te haya costado tanto")
    else:
        st.error("Mmm... esa no es la canción de la adivinanza. ¡Reinténtalo!")
