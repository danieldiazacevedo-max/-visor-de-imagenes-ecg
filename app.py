import streamlit as st
from pathlib import Path
from PIL import Image

carpeta = Path("imagenes")
fotos = sorted(
    p for p in carpeta.glob("*")
    if p.suffix.lower() in (".jpg", ".jpeg")
)

@st.cache_data
def cargar(ruta):
    img = Image.open(ruta)
    img.thumbnail((1600, 1600))
    return img

st.title("Visor de imágenes")

if not fotos:
    st.warning("No se encontraron imágenes en la carpeta 'imagenes'.")
    st.stop()

if "i" not in st.session_state:
    st.session_state.i = 0

def anterior():
    st.session_state.i = (st.session_state.i - 1) % len(fotos)

def siguiente():
    st.session_state.i = (st.session_state.i + 1) % len(fotos)

foto = fotos[st.session_state.i]
st.image(cargar(str(foto)), width="stretch")
st.caption(f"{foto.stem} ({st.session_state.i + 1} de {len(fotos)})")

c1, c2 = st.columns(2)
c1.button("⬅ Anterior", on_click=anterior)
c2.button("Siguiente ➡", on_click=siguiente)
