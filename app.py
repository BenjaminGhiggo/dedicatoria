import streamlit as st
from PIL import Image
import base64
import random
import io  # Asegúrate de importar el módulo io

# Función para agregar un fondo personalizado usando CSS
def agregar_fondo(imagen):
    try:
        with open(imagen, "rb") as f:
            data = f.read()
        encoded = base64.b64encode(data).decode()
        css = f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            /* background-attachment: fixed; Eliminado para mejor compatibilidad móvil */
        }}
        </style>
        """
        st.markdown(css, unsafe_allow_html=True)
    except FileNotFoundError:
        st.write("Imagen de fondo no encontrada. Asegúrate de tener 'fondo.jpg' en la carpeta del proyecto.")

# Función para agregar fuentes personalizadas y estilos
def agregar_fuentes_y_estilos():
    css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Montserrat:wght@400;700&display=swap');

    /* Ocultar el menú principal, el encabezado y el pie de página de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Estilos para el título */
    .titulo-principal {
        font-family: 'Great Vibes', cursive;
        color: #ff69b4;
        font-size: 60px; /* Tamaño aumentado para destacar */
        text-align: center;
        margin-bottom: 20px;
        text-shadow: 3px 3px 6px #000000; /* Sombra más pronunciada para mejor legibilidad */
    }

    /* Estilos para el subtítulo */
    .subtitulo {
        font-family: 'Great Vibes', cursive;
        color: #ffffff;
        font-size: 30px; /* Tamaño aumentado */
        text-align: center;
        margin-bottom: 40px;
        text-shadow: 2px 2px 4px #000000;
    }

    /* Estilos para los poemas */
    .poema {
        background: rgba(0, 0, 0, 0.6);
        padding: 25px; /* Aumentar padding para mayor legibilidad */
        border-radius: 10px;
        margin-bottom: 20px;
    }

    .poema h2 {
        font-family: 'Great Vibes', cursive;
        color: #ff69b4;
        font-size: 36px; /* Tamaño aumentado */
        text-shadow: 1px 1px 2px #000000;
    }

    .poema p {
        font-family: 'Montserrat', sans-serif;
        color: #ffffff;
        font-size: 20px; /* Tamaño aumentado */
    }

    /* Estilos para el mensaje final */
    .footer {
        font-family: 'Great Vibes', cursive;
        font-size: 28px; /* Tamaño aumentado */
        color: #ff69b4;
        text-align: center;
        margin-top: 40px;
        text-shadow: 3px 3px 6px #000000;
    }

    /* Estilos para los corazones animados */
    @keyframes corazones-fall {
        0% { top: -10%; }
        100% { top: 100%; }
    }
    @keyframes corazones-shake {
        0%, 100% { transform: translateX(0); }
        50% { transform: translateX(80px); }
    }
    .corazon {
        position: fixed;
        top: 0;
        z-index: 9999;
        user-select: none;
        pointer-events: none;
        animation-name: corazones-fall, corazones-shake;
        animation-duration: 10s, 3s;
        animation-timing-function: linear, ease-in-out;
        animation-iteration-count: infinite, infinite;
        opacity: 0.8;
    }

    /* Estilos para la imagen con marco */
    .imagen-princesa {
        border: 5px solid #ff69b4; /* Borde rosa */
        border-radius: 15px; /* Bordes redondeados */
        box-shadow: 0px 0px 15px rgba(0,0,0,0.5); /* Sombra para dar profundidad */
        max-width: 100%;
        height: auto;
    }

    /* Media Queries para dispositivos móviles */
    @media (max-width: 768px) {
        .stApp {
            background-size: contain; /* Ajustar el tamaño de la imagen para mostrar ambos gatos */
            background-position: center;
        }

        .titulo-principal {
            font-size: 40px; /* Reducir tamaño en móviles si es necesario */
        }

        .subtitulo {
            font-size: 24px;
        }

        .poema h2 {
            font-size: 28px;
        }

        .poema p {
            font-size: 16px;
        }

        .footer {
            font-size: 20px;
        }
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Configuración de la página
st.set_page_config(
    page_title="Benjamín y Araceli",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Agregar fondo y estilos personalizados
agregar_fondo("fondo.jpg")  # Asegúrate de tener 'fondo.jpg' en la carpeta del proyecto
agregar_fuentes_y_estilos()

# Título principal
st.markdown("""
    <div class='titulo-principal'>Benjamín y Araceli ❤️</div>
    """, unsafe_allow_html=True)

# Subtítulo con emojis
st.markdown("""
    <div class='subtitulo'>Un amor que crece cada día 🌹✨</div>
    """, unsafe_allow_html=True)

# Mostrar una imagen con estilo y marco
try:
    image = Image.open("princesa.jpg")
    # Convertir la imagen a base64 para incrustarla en HTML
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    st.markdown(f"""
        <div style="display: flex; justify-content: center;">
            <img src="data:image/png;base64,{img_str}" alt="Mi Princesa Araceli" class="imagen-princesa" />
        </div>
        """, unsafe_allow_html=True)
except FileNotFoundError:
    st.markdown("<p class='contenido'>Imagen no encontrada. Asegúrate de tener 'princesa.jpg' en la carpeta del proyecto.</p>", unsafe_allow_html=True)

# Poemas con estilos
poemas = [
    {
        "titulo": "Eres mi inspiración",
        "contenido": """
Araceli, tu sonrisa ilumina mi día,<br>
como el sol que brilla en la mañana fría.<br>
Cada momento a tu lado es un regalo,<br>
mi corazón late por ti, sin fallo.
        """
    },
    {
        "titulo": "Nuestro amor",
        "contenido": """
En tus ojos encuentro mi hogar,<br>
tu amor es el sueño que quiero alcanzar.<br>
Juntos caminamos por la vida,<br>
mi amor por ti nunca tendrá medida.
        """
    },
    {
        "titulo": "Para siempre",
        "contenido": """
Quiero escribir nuestra historia en estrellas,<br>
cada capítulo lleno de dulces centellas.<br>
Araceli, mi amor por ti es eterno,<br>
juntos seremos felices, sin invierno.
        """
    }
]

# Mostrar los poemas con estilos
for poema in poemas:
    st.markdown(f"""
    <div class='poema'>
        <h2>{poema['titulo']}</h2>
        <p>{poema['contenido']}</p>
    </div>
    """, unsafe_allow_html=True)

# Mensaje final con iconos
st.markdown("""
    <div class='footer'>
        Gracias por ser mi compañera, mi amiga y mi amor.<br>
        Te amo con todo mi corazón, Araceli.<br>
        - Benjamín ❤️
    </div>
    """, unsafe_allow_html=True)

# Agregar corazones animados
st.markdown("""
    <style>
    /* Asegurarse de que los corazones estén por encima de otros elementos */
    .corazon {
        position: fixed;
        top: 0;
        z-index: 9999;
        user-select: none;
        pointer-events: none;
        animation-name: corazones-fall, corazones-shake;
        animation-duration: 10s, 3s;
        animation-timing-function: linear, ease-in-out;
        animation-iteration-count: infinite, infinite;
        opacity: 0.8;
    }
    </style>
    """, unsafe_allow_html=True)

# Añadir múltiples corazones
for i in range(30):  # Puedes ajustar el número de corazones aquí
    left = random.randint(0, 100)
    size = random.randint(20, 40)
    duration = random.uniform(5, 15)
    shake = random.uniform(1, 3)
    st.markdown(f"""
        <div class='corazon' style='left: {left}%; font-size: {size}px; animation-duration: {duration}s, {shake}s;'>❤️</div>
    """, unsafe_allow_html=True)

# Nota: Los efectos adicionales pueden afectar el rendimiento. Si notas que la aplicación es lenta, puedes reducir el número de corazones.
