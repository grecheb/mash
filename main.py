import streamlit as st
import folium
from streamlit_folium import st_folium
import random

# --- Configuración de la página ---
st.set_page_config(page_title="Felices 3 meses ❤️", layout="wide")

# --- Variables ---
PASSWORDS_VALIDOS = ["mash mash", "mashmash"]  # en minúscula para comparar
mensajes_error = [
    "Si te lo sabes, tú puedes",
    "Te lo digo apretando tu manito...",
    "También se lo puedes decir a Ringuito"
]

# Recuerdos para el mapa
recuerdos = [
    {
        "nombre": "Parque Kennedy",
        "lat": -12.1225,
        "lon": -77.0290,
        "foto": "https://upload.wikimedia.org/wikipedia/commons/7/77/Parque_Kennedy.jpg",
        "descripcion": "Nuestra primera cita 💕"
    },
    {
        "nombre": "Playa Miraflores",
        "lat": -12.1303,
        "lon": -77.0326,
        "foto": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Miraflores_Peru_Beach.jpg",
        "descripcion": "Paseo al atardecer 🌅"
    }
]

# Lista de capítulos Pataclaun
pataclaun_episodes = [
    {"title": "Piloto (Wendy está embarazada)", "url": "https://www.youtube.com/watch?v=49ZNrmBvyr0"},
    {"title": "La genio loca (Wendy la intelectual)", "url": "https://www.youtube.com/watch?v=XXXXXXX"},
    {"title": "Capítulo Random Ejemplo", "url": "https://www.youtube.com/watch?v=YYYYYYY"}
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
    tab1, tab2, tab3 = st.tabs(["📜 Mensaje lindo", "🗺 Mapa de recuerdos", "🎭 Sorpresa Pataclaun"])

    # Tab 1: Mensaje lindo
    with tab1:
        st.header("💖 Para ti...")
        st.write("""
        Desde aquel primer beso hace tres meses, cada día contigo ha sido un capítulo nuevo de mi serie favorita.
        Gracias por ser mi mejor amiga, mi cómplice y mi gran amor.  
        Te amo más que Machín a Wendy, más que Tony a su cama, más que cualquier final feliz que haya visto en la tele. 💕
        """)
        st.image("https://i.imgur.com/XhYIu4J.jpeg", caption="Nosotros 💞", use_container_width=True)

    # Tab 2: Mapa de recuerdos
    with tab2:
        st.header("🌍 Nuestros lugares especiales")
        m = folium.Map(location=[-12.0464, -77.0428], zoom_start=13)
        for r in recuerdos:
            popup_html = f"<b>{r['nombre']}</b><br><img src='{r['foto']}' width='150'><br>{r['descripcion']}"
            folium.Marker(location=[r['lat'], r['lon']], popup=popup_html).add_to(m)
        st_folium(m, width=700, height=500)

    # Tab 3: Pataclaun
    with tab3:
        st.header("🎭 Sorpresa Pataclaun")
        opciones = [ep["title"] for ep in pataclaun_episodes]
        seleccion = st.selectbox("Elige un capítulo:", opciones)
        episodio = next(ep for ep in pataclaun_episodes if ep["title"] == seleccion)
        if st.button("Ver capítulo seleccionado"):
            st.markdown(f"[Ver en YouTube]({episodio['url']})")

        if st.button("🎲 Dame uno al azar"):
            random_ep = random.choice(pataclaun_episodes)
            st.markdown(f"Capítulo: **{random_ep['title']}**\n\n[Ver en YouTube]({random_ep['url']})")

