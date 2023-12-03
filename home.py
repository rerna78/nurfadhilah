import streamlit as st
st.set_page_config(
    page_title="Portfolio |Aisyah",
    page_icon="👨‍🎓",
    layout="wide"
)

st.title("SELAMAT DATANG DI PORTFOLIO SAYA")
st.sidebar.success("SILAHKAN PILIH MENU DI ATAS")

col1, col2 = st.columns(2)

with col1:
   st.header("About Me")
   st.image("me.jpg", width= 390)

with col2:
   st.header("My Biodata")
   st.subheader("NAMA : RU'YATUN AISA")
   st.caption("NIM : 0402201093")
   st.write(
            """
            - Tempat Tanggal Lahir : Brebes 13 Juni 2002 
            - Alamat               : Pengabean Losari Brebes
            - Hobi                 : Healing
            - Cita-cita            : Pengusaha
            - Hal yang disukai     : Mayoran
            - Status               : Jomblo
            """
        )

st.header("*Call Me If You Want*")
