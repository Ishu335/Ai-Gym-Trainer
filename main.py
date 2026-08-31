import streamlit as st
from services.auth.login_wall import render_login_wall

def main():
    st.set_page_config(page_icon=r'static\icons\dumbbell.png',page_title='AI Gym Trainer',
                       initial_sidebar_state="expanded",
                       layout='centered')
    if not render_login_wall():
        return
    st.write('welcome')
if __name__ =="__main__":
    main()