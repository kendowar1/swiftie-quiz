import streamlit as st

st.title("Para Ian 🎵✨")
st.markdown("Responde este pequeño cuestionario Swiftie para desbloquear un mensaje especial.")

preguntas = [
    {"p": "¿Cuál es el nombre de tu cantante más escuchada en estos momentos?", "opciones": ["Taylor Swift", "Lana Del Rey", "Olivia Rodrigo"]},
    {"p": "¿Cuál de estas canciones pertenece a '1989'?", "opciones": ["Clean", "Enchanted", "Delicate"]},
    {"p": "¿De qué canción viene esta frase: 'This ultraviolet morning light below'?", "opciones": ["Afterglow", "Daylight", "Cruel Summer"]},
    {"p": "¿Cuál es la canción de Taylor que te hace pensar en un color medio oscuro como el vino?", "opciones": ["Maroon", "Red", "Lavender Haze"]},
    {"p": "¿Cuál es la canción que contiene esta frase: 'When no one is around, my dear'?", "opciones": ["Opalite", "Mirrorball", "Invisible String"]}
]

if "respuestas_dict" not in st.session_state:
    st.session_state.respuestas_dict = {}

# Crear los selectbox con index=None para que empiecen vacíos
for i, pregunta in enumerate(preguntas):
    st.session_state.respuestas_dict[i] = st.selectbox(
        pregunta["p"], 
        options=pregunta["opciones"],
        index=None,
        placeholder="Elige una opción...",
        key=f"q{i}"
    )

st.divider()

st.info("💡 ¡Ya casi! Ahora, toma la primera letra de cada respuesta que seleccionaste arriba y escribe la frase resultante aquí abajo:")

frase_usuario = st.text_input("Escribe la frase secreta:", key="frase_final")

if st.button("Descubrir el mensaje"):
    # Validación: verificar si falta alguna respuesta
    if any(val is None for val in st.session_state.respuestas_dict.values()):
        st.warning("⚠️ ¡Falta completar alguna pregunta! Por favor, responde todo primero.")
    
    # Comprobamos si la frase es "tcamo"
    elif frase_usuario.lower() == "tcamm":
        st.balloons()
        st.success("¡Lo lograste! ✨")
        
        st.markdown("""
        ### Un mensaje para ti:
        Sabía que resolverías la frase secreta, esto es tan solo un proyecto que estoy armando
        del cual fuiste la primera persona en probarlo. Gracias por participar, sos una re conocedora de Taylor
        y sos mi única dúo favorita, con la cual podría jugar mil games y nunca aburrirme.
        No me interesa el resultado si gano o pierdo, mientras sea con vos, siempre voy a estar ganando.
        Y AUNQUE TE CÁGUES DE RISA DE MI MALDITO PROYECTO es solo una prueba de lo que tengo que cambiar de eso.
        """)
    else:
        st.error("Mmm... esa no parece ser la frase correcta. ¡Revisa las iniciales de tus respuestas y vuelve a intentar!")
