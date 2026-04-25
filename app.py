import streamlit as st
import base64

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Taylor Swift Quiz", page_icon="🎵")

# --- MÚSICA DE FONDO PERSISTENTE ---
def autoplay_audio(file_path: str):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f"""
                <audio autoplay="true" loop="true">
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                """
            st.markdown(md, unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"⚠️ No se encontró el archivo de audio: {file_path}")

# Llama a la función (Asegúrate de que el archivo en GitHub se llame 'fondo.mp3')
autoplay_audio("fondo.mp3")

# --- INTERFAZ ---
st.markdown("<h1 style='text-align: center; color: #FF69B4;'>Test Quiz Taylor Swift 🎵✨</h1>", unsafe_allow_html=True)
st.image("https://images.unsplash.com/photo-1598387181032-a3103a2db5b3?q=80&w=1000", use_container_width=True)
st.markdown("---")

# Definición de preguntas
preguntas = [
    {"p": "¿A qué canción pertenece: 'I don't wanna think of anything else now that I thought of you'?", "opciones": ["Daylight", "Wishlist", "So High School"], "correcta": "Daylight"},
    {"p": "¿Cuándo fue el primer show del Eras Tour?", "opciones": ["17 de marzo del 2023", "10 de marzo del 2023", "15 de abril del 2023"], "correcta": "17 de marzo del 2023"},
    {"p": "¿Cuál es la primer canción de la era Evermore en el Eras Tour?", "opciones": ["Willow", "Tolerate It", "Champagne Problems"], "correcta": "Willow"},
    {"p": "¿Cuántas parejas tuvo Taylor Swift?", "opciones": ["11", "10", "13"], "correcta": "11"},
    {"p": "¿Cuál es el álbum más vendido de Taylor Swift?", "opciones": ["1989", "Red", "Midnights"], "correcta": "1989"},
    {"p": "¿De qué canción viene: 'There's just one who could make me stay'?", "opciones": ["You're on your own kid", "Would've, could've, should've", "All you had to do was stay"], "correcta": "You're on your own kid"}
]

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
            st.markdown("
