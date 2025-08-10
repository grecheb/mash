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
    .icono-redondo {
        border-radius: 50%;
        width: 120px;
        height: 120px;
        object-fit: cover;
    }
    </style>
""", unsafe_allow_html=True)

# --- Variables ---
PASSWORDS_VALIDOS = ["mash mash", "mashmash", "mash  mash", "mash  mash "]  # Variantes
mensajes_error = [
    "💌 Si te lo sabes, tú puedes",
    "💖 Te lo digo apretando tu manito...",
    "🐱 También se lo puedes decir a Ringuito"
]

# Estado de sesión
if "fase" not in st.session_state:
    st.session_state.fase = "advertencia"
if "intentos" not in st.session_state:
    st.session_state.intentos = 0
if "acceso" not in st.session_state:
    st.session_state.acceso = False

# --- FASE 1: Advertencia inicial ---
if st.session_state.fase == "advertencia":
    st.image("https://raw.githubusercontent.com/grecheb/mash/refs/heads/main/images/ringuito%20alerta.png")
    st.markdown("<h1 style='text-align:center;'>ADVERTASAO</h1>", unsafe_allow_html=True)
    st.write("Abre esta página en tu compu para visualizarla mejor")

    st.write("¿Estás viendo esto desde tu compu?")
    col1, col2 = st.columns(2)
    if col1.button("Chi"):
        st.session_state.fase = "prueba_humano"
        st.rerun()
    if col2.button("No"):
        st.write("Miau Miau Miau Miau")

# --- FASE 2: Prueba para humanos ---
elif st.session_state.fase == "prueba_humano":
    st.image("https://raw.githubusercontent.com/grecheb/mash/refs/heads/main/images/ringuito%20de%20hecho%20.png")
    st.write("Resuelve para demostrar que eres humano:")

    # Guardar a y b en la sesión si aún no existen
    if "num_a" not in st.session_state or "num_b" not in st.session_state:
        st.session_state.num_a = random.randint(1, 10)
        st.session_state.num_b = random.randint(1, 10)

    # Mostrar la suma siempre igual hasta que se acierte
    respuesta = st.number_input(
        f"¿Cuánto es {st.session_state.num_a} + {st.session_state.num_b}?",
        step=1
    )

    if st.button("Verificar"):
        if respuesta == st.session_state.num_a + st.session_state.num_b:
            st.session_state.fase = "login"
            del st.session_state["num_a"]
            del st.session_state["num_b"]
            st.rerun()
        else:
            st.error("Respuesta incorrecta. Intenta de nuevo.") 

# --- FASE 3: Pantalla de login ---
elif st.session_state.fase == "login":
    st.image("https://raw.githubusercontent.com/grecheb/mash/refs/heads/main/images/ringuito%20brillante.png")
    st.title("🔒 Ingresa la contraseña secreta")
    password_input = st.text_input("Contraseña:", type="password")
    if st.button("Entrar"):
        if password_input.strip().lower() in PASSWORDS_VALIDOS:
            st.session_state.acceso = True
            st.session_state.fase = "principal"
            st.success("¡Correcto! :3")
            st.rerun()
        else:
            st.session_state.intentos += 1
            st.error("Contraseña incorrecta...")
            if st.session_state.intentos <= len(mensajes_error):
                st.info(mensajes_error[st.session_state.intentos - 1])

# --- FASE 4: Página principal ---
elif st.session_state.fase == "principal" and st.session_state.acceso:
    st.title("✨ Felices 3 meses mi amor ✨")
    st.image("https://raw.githubusercontent.com/grecheb/mash/refs/heads/main/images/ringuito%20enamordo.png")
    st.write("Te amo")
    st.write("de Grechi para Mena")

    # Pestañas
    tab1, tab2 = st.tabs(["Para ti", "Álbum de recuerdos"])

    # --- Tab 1: Para ti ---
    with tab1:
        st.header("Para ti")
        st.write("""Me gustaría iniciar agradeciéndote por estos increíbles tres meses mi amor. Me siento muy feliz por haberte encontrado y por haber iniciado una relación muy bonita contigo :3. Se que somos chavas y nos queda mucho por vivir y aprender, pero yo estoy segura de que mi futuro es a tu lado. Te veo en todos lados y te pienso en todo momento. Mi corazón es completamente tuyo. Estoy bien enamorada, así como dice Mon en nuestra canción jeje. Te amo muchísimo mi mujer hermosa, espero te guste esta pagina estoy en mi era programadora JADJADJ""")
        st.image("https://raw.githubusercontent.com/grecheb/mash/refs/heads/main/images/dibujito%20de%20las%20dos.jpg")
        st.image([
            "https://raw.githubusercontent.com/grecheb/mash/refs/heads/main/images/chiquita%201.JPG",
            "https://raw.githubusercontent.com/grecheb/mash/refs/heads/main/images/chiquita%202.HEIC"
        ], caption=["Estas dos niñas están completamente enamoradas", ""], width=300)

    # --- Tab 2: Álbum de recuerdos ---
    with tab2:
        st.header("Álbum de recuerdos")
        st.write("Aquí algunos recuerdos bonitos juntitas y por muchísimos más")

        album_recuerdos = [
            {"titulo": "Ellas dos se van a enamorar", "desc": "Creo que todavía no lo saben, aunque las dos tienen un crush gigante en la otra, pero ahora se aman :3 que buena clase de antro", "fotos": ["https://raw.githubusercontent.com/grecheb/mash/refs/heads/main/images/ellas%20dos%20se%20van%20a%20enamorar.jpg"]},
            {"titulo": "Que rico beso", "desc": "Esta es de las primeras fotos que nos tomamos ya juntitas. Amo mucho cuando me besas especialmente con labial y me dejas marcadita :P lléname de besos siempre", "fotos": ["https://raw.githubusercontent.com/grecheb/mash/refs/heads/main/images/primera%20fotito%20beso.JPG"]},
            {"titulo": "Esta fotitooo", "desc": "Nuestra primera fotito en el espejo, en el baño de sociales donde una vez me estampaste contra la pared :3 (como me gusta), amo mucho capturar momento bonitos contigo, creo que te gusto", "fotos": ["https://raw.githubusercontent.com/grecheb/mash/refs/heads/main/images/primer%20fotito%20en%20el%20espejo.JPG"]},
            {"titulo": "En el ascensor del stella maris", "desc": "Me encanta tener citas contigo y que me acompañes a lugares random, como también amo acompañarte. Por más besitos en ascensores :333", "fotos": ["https://raw.githubusercontent.com/grecheb/mash/refs/heads/main/images/ascensor%20stella.JPG"]},
            {"titulo": "Unas hamburguestitas", "desc": "QUE RICOOOO comer contigo :3333 esto fue después de mi cita en el stella, que bonitos son los full days contigo, los quiero para toda la vida", "fotos": ["https://raw.githubusercontent.com/grecheb/mash/refs/heads/main/images/cita%20comiendo%20hamburgesas.JPG"]},
            {"titulo": "Ahora usas mi inicial", "desc": "La primera vez que te la pusiste casi se me sale mi corazoncito, te queda muy bien la g, y yo me siento completamente tuya", "fotos": ["https://raw.githubusercontent.com/grecheb/mash/refs/heads/main/images/usas%20mi%20inicial.JPG"]},
            {"titulo": "Somos kbros", "desc": "Ojo creo que somos gays DAJDJADJAJ por muchos más pride juntitas VIVAN LAS LESBIANAS", "fotos": ["https://raw.githubusercontent.com/grecheb/mash/refs/heads/main/images/nuestros%20nombres%20pride.HEIC"]},
            {"titulo": "Tan pero tan linda", "desc": "QUE BONITA CON NUESTRA MANTITA MIMIMIMIMI citas casuales como la que tuvimos ese día, o simplemente estar en cato contigo es perfecto", "fotos": ["https://raw.githubusercontent.com/grecheb/mash/refs/heads/main/images/IMG_1171.HEIC"]},
            {"titulo": "Bien cansaditas", "desc": "Porque estaremos tan cansaditas a amor? Jejejeje que buen día, creo que chi te acuerdas como olvidarlo, comimos bien rico (no almorzamos), que ganas de siempre comer rico contigo :3", "fotos": ["https://raw.githubusercontent.com/grecheb/mash/refs/heads/main/images/ese%20jueves%20en%20mi%20casita.HEIC"]},
            {"titulo": "Serving cunt", "desc": "Este día servimos concha, fotito juntitas cuando estabas por quedarte dormida encima de mío, siempre voy a estar aquí para ti", "fotos": ["https://raw.githubusercontent.com/grecheb/mash/refs/heads/main/images/fiesta%20de%20ana.JPG"]},
            {"titulo": "Full queso", "desc": "Aquí quería pizza y fuimos a comer una jeje, gracias por cumplir mis caprichos y engreírme siempre mi amor, a mí también me gusta hacerlo contigo :3", "fotos": ["https://raw.githubusercontent.com/grecheb/mash/refs/heads/main/images/cita%20comiendo%20pizza.HEIC"]},
            {"titulo": "Dímelo de frente", "desc": "Amo demasiado esta foto en la que parece que me quieres consumir, yo también quiero hacerlo la verdad. Te como te como a besos", "fotos": ["https://raw.githubusercontent.com/grecheb/mash/refs/heads/main/images/beshito.JPG"]},
            {"titulo": "Mi amor con un quesito", "desc": "Estoy completamente enamorada", "fotos": ["https://raw.githubusercontent.com/grecheb/mash/refs/heads/main/images/tu%20con%20un%20quesito.HEIC"]},
            {"titulo": "Aventuras en el centro", "desc": "Este día la pase increíble, me divertí mucho contigo amor paseando y comprando. Sin duda me haces muy feliz :3333", "fotos": ["https://raw.githubusercontent.com/grecheb/mash/refs/heads/main/images/besito%20en%20el%20centro.JPG"]},
            {"titulo": "Ahora las dos usamos nuestras iniciales", "desc": "Yo soy tuya como tu eres mía y se siente muy bien :3", "fotos": ["https://raw.githubusercontent.com/grecheb/mash/refs/heads/main/images/usando%20tu%20inicial.JPG", "https://raw.githubusercontent.com/grecheb/mash/refs/heads/main/images/mi%20amor%20con%20la%20g.JPG"]},
            {"titulo": "Mi amor con sus flores", "desc": "Quiero darte flores siempre y verte sonreir todos los días, mi mujer hermosa", "fotos": ["https://raw.githubusercontent.com/grecheb/mash/refs/heads/main/images/mi%20amor%20con%20sus%20flores.HEIC"]},
            {"titulo": "FULL LECHE", "desc": "Soy la mujer más suertuda del mundo por tenerte a mi lado, y tu eres la mejor enamorada del mundo, alimentándome con arroz con leche VIVAAAA", "fotos": ["https://raw.githubusercontent.com/grecheb/mash/refs/heads/main/images/arroz%20con%20leche%201.HEIC", "https://raw.githubusercontent.com/grecheb/mash/refs/heads/main/images/arroz%20con%20leche%202.JPG"]},
            {"titulo": "Que tal salchipapa", "desc": "Otra aventura loca loca junto a ti, JAAA tenemos una suerte, igual me he dado cuenta que los días son mejores a tu lado", "fotos": ["https://raw.githubusercontent.com/grecheb/mash/refs/heads/main/images/esta%20salchipapa.HEIC"]},
            {"titulo": "Juguemos como locas?", "desc": "JADJADJAJDAJDJADJAJDJA mi mujer competitiva :3 amo jugar como loca contigo mi amor", "fotos": ["https://raw.githubusercontent.com/grecheb/mash/refs/heads/main/images/juguemos%20como%20locas%3F.HEIC"]},
            {"titulo": "Amor de mi vida", "desc": "Esta es una de mis fotos favoritas, que me gustaría tener así en un polo cof cof, nunca me canso de decirte que eres preciosa hermosa, te amo con todo mi ser", "fotos": ["https://raw.githubusercontent.com/grecheb/mash/refs/heads/main/images/mi%20amor%20en%20el%20fil%20esta%20foto%20para%20polo.HEIC"]}
        ]

        seleccion = st.selectbox("Elige un recuerdo:", [r["titulo"] for r in album_recuerdos])
        recuerdo = next(r for r in album_recuerdos if r["titulo"] == seleccion)
        st.write(recuerdo["desc"])
        for foto in recuerdo["fotos"]:
            st.image(foto)
