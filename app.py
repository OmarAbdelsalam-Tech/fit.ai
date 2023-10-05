import streamlit as st
import openai

openai.api_key = st.secrets["openai"]["api_key"]


# Replace the path with your own Islamic-related background image
background_image_path = "vaugn.jpg"

def main():
    st.set_page_config(page_title="Fit.ai", page_icon=":guardsman:", layout="wide")
    st.title("Fit.ai")
    st.subheader(" Contributions: Omar , Vaughn, Robert, Seth, Will")

    # Set up the layout
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image(background_image_path, width=500, use_column_width=False)

        # Wrap the chat history label in a ScrollView widget
        scroll_view = st.empty()
        chat_history = scroll_view.markdown("", unsafe_allow_html=True)

        user_input = st.text_input("Type your message", key="user_input")

        if st.button("Send"):
            send_message(user_input, chat_history)

    with col2:
         st.subheader("About Fit.ai")
         st.write("Struggling to maintain a balanced diet or looking for the right workout routine?")
                
         st.write("Ever too embarrassed to ask your gym instructor or nutritionist about something personal?")
        
         st.write("Fit.ai is an AI-powered health app designed to guide you on diet and workouts tailored to your specific needs.")
        
         st.subheader("Example Questions for Fit.ai:")
         st.write("- What's a balanced meal plan for weight loss?")
         st.write("- How many calories should I consume daily?")
         st.write("- What exercises can help strengthen my core?")
         st.write("- Is a keto diet right for me?")
         st.write("- How can I improve my running stamina?")
         st.write("- Are there any effective home workouts?")
         st.write("- What foods can help boost my metabolism?")
         st.write("- How often should I change my workout routine for optimal results?")



def send_message(user_input, chat_history):
    message = user_input.strip()
    if message:
        chat_history.write(f"<p style='font-weight:bold'>User: {message}</p>", unsafe_allow_html=True)

        response_text = get_chatbot_response(message)
        response = f"<p style='color:blue;font-weight:bold'>Fit.ai: {response_text}</p>"
        chat_history.write(response, unsafe_allow_html=True)

        # Clear the user input after sending the message
        user_input = ""




def get_chatbot_response(message):
    openai_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a Personal Coach that gives advice on Workouts and gives recipies with macros. "},
                {"role": "user", "content": message},
            ],
        )
    
    
    
    

    assistant_message = openai_response.choices[0]["message"]["content"]
    return assistant_message.strip()


if __name__ == "__main__":
    main()
