# 1. Importing extensions
import streamlit as st

# 2. Converting files to pages
home_page = st.Page(
    page='pages/home.py',
    title='Home page',
    icon='🏠',
    default=True
)
signin_page = st.Page(
    page='pages/signin.py', 
    title='Sign In', 
    icon='🔑'
)
signup_page = st.Page(
    page='pages/signup.py', 
    title='Sign Up', 
    icon='📝'
)
menu_page = st.Page(
    page='pages/menu.py', 
    title='Explore Menu', 
    icon='🍽️'
)
chatbot_page = st.Page(
    page='pages/chatbot.py', 
    title='Talk with AI', 
    icon='✨'
)

# 3. Creating the navbar
all_pages = st.navigation(
    pages=[
        home_page, signup_page, signin_page,
        menu_page, chatbot_page
    ], 
    position='top'
)
all_pages.run()