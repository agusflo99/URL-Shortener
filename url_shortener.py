import pyshorteners 
import streamlit as st

#Creamos una funcion shorten_url
def shorten_url(url):
    #nombramos al objeto el cual llama a la libreria pyshorteners 
    s = pyshorteners.Shortener()
    #nombramos una variable la cual aplica los metodos para acortar la url
    shortened_url = s.tinyurl.short(url)
    #llamamos a la funcion que nos devuelve la url acortada
    return shortened_url

#Creamos app web con streamlit:

#configuramos la pagina colocando el titulo y centrando el contenido 
st.set_page_config(page_title = 'URL Shortener' ,layout = 'centered')
#colocamos una imagen a la pagina 
st.image("images\LOGO PNG sin fondo.png",use_column_width=True)
#Colocamos un titulo a la parte superior del input
st.title('URL SHORTENER WITH RF SERVICIOS INDUSTRIALES SA')
#creamos un input para ingresar el valor de la url 
url = st.text_input("Enter the url please:")
#creamos el condicional donde ejecutamos la funcion
if st.button("Generate new URL"):
    st.write("URL shortened: ", shorten_url(url))