import streamlit as st
from pathlib import Path

fotos = sorted(Path("imagenes").glob("*.jpg"))
if "i" not in st.session_state:
    st.session_state.i = 0

st.title("Visor de imágenes")
st.image(str(fotos[st.session_state.i]), width="stretch")

c1, c2 = st.columns(2)
if c1.button("⬅ Anterior"):
    st.session_state.i = (st.session_state.i - 1) % len(fotos)
    st.rerun()
if c2.button("Siguiente ➡"):
    st.session_state.i = (st.session_state.i + 1) % len(fotos)
    st.rerun()
