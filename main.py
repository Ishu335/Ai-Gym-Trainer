import streamlit as st
from services.auth.login_wall import render_login_wall
from services.state.session_defaults import initial_session_defaults
from services.components.style_side_bar import style_side_bar
from services.components.side_bar import render_sidebar

def main():
    st.set_page_config(page_icon=r'static\icons\dumbbell.png',page_title='AI Gym Trainer',
                       initial_sidebar_state="expanded",
                       layout='centered')
    if not render_login_wall():
        return

    initial_session_defaults()

    style_side_bar()
    render_sidebar()
if __name__ =="__main__":
    main()