# 1. Importing extensions
import streamlit as st
import google.generativeai as ai

# 2. Page title
st.title('Chat with our AI Assitant✨')

# 3. Gemini API setup
key= st.secrets["GEMINI_API_KEY"]
ai.configure(api_key=key)
model = ai.GenerativeModel(model_name='gemini-3.1-flash-lite-preview')

# 4. Taking user question
question = st.chat_input('Ask me anything..')

# 5. Creating chat messages & generating results
if question:
    with st.chat_message('human', avatar='👤'):
        st.write(question)
        
    prompt = f'''
    Answer this question:
    {question}
    Use this knowledge to answer:
    - Working hours 9AM to 11PM
    - Opening days: Everyday
    - Menu:
        pepperoni : small:180,
                    medium:200,
                    large:250,
        chicken: small: 150,
                    medium: 180,
                    large:200,
        margerita: small:100,
                    medium:120,
                    large:160
    
    Do not answer any question irrelvant to food.
    '''
    
    with st.chat_message('ai', avatar='✨'):
        with st.spinner('Generating...🧠'):
            answer = model.generate_content(prompt)
        st.write(answer.text)
