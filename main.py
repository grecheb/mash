import streamlit as st

# --- Configuración de la página ---
st.set_page_config(page_title="Felices 3 meses ❤️", layout="centered")

# --- Variables ---
PASSWORD = "Mash Mash"
mensajes_error = [
    "Si te lo sabes, tú puedes",
    "Te lo digo apretando tu manito...",
    "También se lo puedes decir a Ringuito"
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
        if password_input.strip() == PASSWORD:
            st.session_state.acceso = True
            st.success("¡Correcto! :3")
        else:
            st.session_state.intentos += 1
            st.error("Contraseña incorrecta...")
            if st.session_state.intentos <= len(mensajes_error):
                st.info(mensajes_error[st.session_state.intentos - 1])

else:
    # --- Aquí irá la pantalla principal ---
    st.title("✨ ¡Felices 3 meses mi amor! ✨")
    st.write("Te amo 💌")
    # Luego aquí pondremos las tabs con mensaje, mapa y Pataclaun

