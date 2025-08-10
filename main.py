import streamlit as st
import random

# --- Configuración de la página ---
st.set_page_config(page_title="Felices 3 meses ❤️", layout="wide")

# CSS para personalizar diseño
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #ffe6e6, #fff0f5);
    }
    .stTabs [role="tablist"] button {
        font-size: 18px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- Variables ---
PASSWORDS_VALIDOS = ["mash mash", "mashmash"]  # en minúscula
mensajes_error = [
    "💌 Si te lo sabes, tú puedes",
    "💖 Te lo digo apretando tu manito...",
    "🐱 También se lo puedes decir a Ringuito"
]

# Álbum de recuerdos
album_recuerdos = [
    {"titulo": "Parque Kennedy", "descripcion": "Nuestra primera cita 💕", 
     "foto": "https://upload.wikimedia.org/wikipedia/commons/7/77/Parque_Kennedy.jpg"},
    {"titulo": "Playa Miraflores", "descripcion": "Paseo al atardecer 🌅", 
     "foto": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Miraflores_Peru_Beach.jpg"}
]

# Lista de capítulos Pataclaun con categorías
pataclaun_episodes = [
    {"title": "Piloto (Wendy está embarazada)", "url": "https://www.youtube.com/watch?v=49ZNrmBvyr0", "category": "🎭 Clásico imperdible"},
    {"title": "La genio loca", "url": "https://www.youtube.com/watch?v=XXXXXXX", "category": "😂 Para reírte a carcajadas"},
    {"title": "Capítulo Random Ejemplo", "url": "https://www.youtube.com/watch?v=YYYYYYY", "category": "😜 Absurdo y loco"}
]

# --- Estado de sesión ---
if "intentos" not in st.session_state:
    st.session_state.intentos = 0
if "acceso" not in st.session_state:
    st.session_state.acceso = False

# --- Pantalla de login ---
if not st.session_state.acceso:
    st.title("🔒 Ingresa la contraseña secreta")
    password_input = st.text_input("Contraseña:", type="password")

    if st.button("Entrar"):
        if password_input.strip().lower() in PASSWORDS_VALIDOS:
            st.session_state.acceso = True
            st.success("¡Correcto! :3")
        else:
            st.session_state.intentos += 1
            st.error("Contraseña incorrecta...")
            if st.session_state.intentos <= len(mensajes_error):
                st.info(mensajes_error[st.session_state.intentos - 1])

else:
    # --- Pantalla principal ---
    st.title("✨ ¡Felices 3 meses mi amor! ✨")
    st.write("Te amo 💌")

    # Pestañas
    tab1, tab2, tab3 = st.tabs(["📜 Mensaje lindo", "📸 Álbum de recuerdos", "🎭 Sorpresa Pataclaun"])

    # Tab 1: Mensaje lindo
    with tab1:
        st.header("💖 Para ti...")
        st.write("""
        Desde aquel primer beso hace tres meses, cada día contigo ha sido un capítulo nuevo de mi serie favorita.
        Gracias por ser mi mejor amiga, mi cómplice y mi gran amor.  
        Te amo más que Machín a Wendy, más que Tony a su cama, más que cualquier final feliz que haya visto en la tele. 💕
        """)
        st.image("https://i.imgur.com/XhYIu4J.jpeg", caption="Nosotros 💞", use_container_width=True)

    # Tab 2: Álbum de recuerdos
    with tab2:
        st.header("📸 Nuestros recuerdos")
        seleccion = st.selectbox("Elige un momento especial:", [r["titulo"] for r in album_recuerdos])
        recuerdo = next(r for r in album_recuerdos if r["titulo"] == seleccion)
        st.image(recuerdo["foto"], caption=recuerdo["descripcion"], use_container_width=True)

    # Tab 3: Pataclaun con categorías
    with tab3:
        st.header("🎭 Sorpresa Pataclaun")
        categorias = list(set(ep["category"] for ep in pataclaun_episodes))
        categoria_sel = st.selectbox("Elige el tipo de capítulo:", categorias)
        filtrados = [ep for ep in pataclaun_episodes if ep["category"] == categoria_sel]

        opciones = [ep["title"] for ep in filtrados]
        seleccion = st.selectbox("Elige un capítulo:", opciones)
        episodio = next(ep for ep in filtrados if ep["title"] == seleccion)

        if st.button("Ver capítulo seleccionado"):
            st.markdown(f"[Ver en YouTube]({episodio['url']})")

        if st.button("🎲 Dame uno al azar de esta categoría"):
            random_ep = random.choice(filtrados)
            st.markdown(f"Capítulo: **{random_ep['title']}**\n\n[Ver en YouTube]({random_ep['url']})")

        # Huevo de pascua
        buscador = st.text_input("🔍 Busca algo especial...")
        if buscador.strip().lower() == "te amo":
            st.success("💖 Yo también te amo, mi amor 🥹💌")


