# 1. Importing Streamlit
import streamlit as st

# 2. Initializing session state variables
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'name' not in st.session_state:
    st.session_state['name'] = None
if 'phone' not in st.session_state:
    st.session_state['phone'] = None

# 3. Creating page title and intro text
st.title("Create Account 📝")
st.write("Join PizzaHub today!")

# 4. Creating signup form
with st.form("signup"):
    
    # 5. Personal information section
    st.write("Personal Information")
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Full Name")
        email = st.text_input("Email")
    
    with col2:
        phone = st.text_input("Phone Number")
        password = st.text_input("Password", type="password")
    
    # 6. Delivery details section
    st.write("Delivery Details")
    col3, col4 = st.columns([3, 1])
    
    with col3:
        address = st.text_input("Street Address")
    
    with col4:
        apt = st.text_input("Apartment No.")
        
    # 7. Submit button
    submit = st.form_submit_button("Sign Up", use_container_width=True)
    
    # 8. Form validation and account creation
    if submit:
        if name and email and password and address:
            st.session_state['name'] = name
            st.session_state['phone'] = phone
            st.session_state['email'] = email
            st.session_state['address'] = f"{address}, Apt {apt}"
            
            st.success(f"Account created successfully for {name}! Please sign in.")
            
            # 9. Redirecting to sign-in page
            st.switch_page("pages/signin.py")
        else:
            st.error("Please fill in all required fields (Name, Email, Password, Address).")

# 10. Divider and sign-in redirect option
st.divider()
st.write("Already have an account?")

# 11. Sign-in button
if st.button("Sign In Here", use_container_width=True):
    st.switch_page("pages/signin.py")
    