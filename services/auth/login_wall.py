import streamlit as st 
from services.auth.login_style import load_login_css
def render_login_wall():
    if st.session_state.get("username") is not None:
        return True
    
    load_login_css()
    # st.image(
    #     "static/assets/body builder.png",
    #     use_container_width=True
    # )
    st.title("🏋️ RepVision AI")

    st.markdown("""
    ### 🤖 Your Real-Time AI Fitness Coach

    **RepVision AI** uses computer vision to track your movements,
    count repetitions, analyze exercise form, and provide
    real-time workout feedback.

    🎯 **Track Reps** &nbsp;&nbsp; 💪 **Analyze Form** &nbsp;&nbsp; 🧠 **AI Feedback**
    """)
    with st.form('login_from',clear_on_submit=True):
        username=st.text_input('Name (unique)',placeholder='eg. Akshay Kumer')
        submit_button=st.form_submit_button("Start Session",width='stretch')
    if submit_button:
        if not username:
            st.error("Pls Enter the User-Name")
            return False
        st.session_state['username']=username
        st.session_state['user_id']='i'
        st.rerun()
    return False
    