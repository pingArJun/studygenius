import streamlit as st
import datetime
import time
import openai
import sqlite3
from notes_app import Notes
from testzone import Test
from PIL import Image
from streamlit_option_menu import option_menu
from  streamlit_lottie import  st_lottie

# Set your OpenAI API key
openai.api_key = "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"


def progress_bar(progress):
    st.progress(progress)
st.set_page_config(page_title="Interactive Study Planner and Resource Aggregator", page_icon="📚", layout="wide")
def localcss(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
localcss("style.css")
pg_bg_img = f"""
<style>
[data-testid="stApp"] {{
background-image: url("https://i.imgur.com/3cuoReB.png");
background-size: cover;
background-repeat: no-repeat;
background-attachment: local;
background-position: top left;
}}
[data-testid="stHeader"]{{
background-color: rgba(0,0,0,0);
}}

[data-testid="stSidebar"]{{
# background-color: rgba(255,255,243,50);
background-image : url("https://i.imgur.com/mrWHjUb.png")
}}

</style>
"""

st.markdown(pg_bg_img, unsafe_allow_html=True)
c1,c2 = st.sidebar.columns(2)
with c1:
    st.markdown("""
                        <style>
                        .st-emotion-cache-1v0mbdj > img{
                        border-radius: 40%;
                            }
                        </style>
            
                        """, unsafe_allow_html=True)

    st.image("audlogo.png")

with c2:
    st.empty()
     


# Sidebar for navigation
st.sidebar.title("Interactive Study Planner")

study_option = st.sidebar.selectbox("What would you like to do?", ["Menu","Create a study plan", "Access resources",  "Test Zone", "Join a study group", "Code Questions"])
# Main content area
if study_option == "Menu":
    st.title("Interactive Study Planner and Resource Aggregator")
    
    st.header("Welcome! Buddy")
    st.write("""
            Welcome to the Interactive Study Planner and Resource Aggregator! This app is your personal study buddy.
            Input your subjects, topics, and deadlines, and get a personalized study plan. Let's make studying efficient and fun!
            """)
        
        

    
    st.header("Features:")
    st.write("""
        - **Create a Study Plan:** Input your subjects, topics, and deadlines, and generate a personalized study plan.
        - **Access Resources:** Explore various study materials including notes, assignments, and video tutorials.
        - **Test Zone:** Test your knowledge with quizzes and practice questions.
        - **Join a Study Group:** Collaborate with peers and join study groups for effective learning.
        - **Review Notes:** Review your notes and study materials easily within the app.
        - **Code Questions:** Get question on programming language and tips to stay focused on your studies.
        """)

    # Footer for additional information
    st.markdown("""
    <div style="text-align: center; padding: 20px; background-color: #f0f0f0; border-radius: 5px;">
        <p>Made with ❤️ by Your Team Name</p>
        <p>Contact us at sdearjunkumar@gmail.com</p>
    </div>
    """, unsafe_allow_html=True)





elif study_option == "Create a study plan":
    st.header("Create a Study Plan")

    # User inputs for the study planner
    st.write("### Select a subject:")
    subject_options = ["Mathematics", "Physics", "Chemistry"]
    selected_subject = st.selectbox("", subject_options + ["Other"], key="subject")

    if selected_subject == "Other":
        other_subject = st.text_input("Enter your own subject:")
        selected_subject = other_subject.strip()

    st.write("### Choose a topic:")
    if selected_subject in subject_options:
        topic_options = {
            "Mathematics": ["Algebra", "Geometry", "Calculus"],
            "Physics": ["Classical Mechanics", "Electromagnetism", "Quantum Mechanics"],
            "Chemistry": ["Inorganic", "Organic", "Physical"]
        }
        selected_topic = st.selectbox("", topic_options[selected_subject], key="topic")

    else:
        selected_topic = st.text_input("Enter your own topic:")

    st.write("### Enter deadline:")
    deadline_text = st.date_input("Input deadline as yyyy-mm-dd", key="deadline")

    st.write("### Study plan:")

    if st.button("Generate Study Plan", key="plan_btn"):
        # Get current date

        current_date = datetime.date.today()
        st.markdown(f'<p style="color: blue;">Generating study plan for {selected_subject} {selected_topic}...</p>', unsafe_allow_html=True)
        
        progress_placeholder = st.empty()
        with progress_placeholder:
            st.write("Generating study plan...")
            progress_bar(0)
            for progress in range(1, 101):
                time.sleep(20/100)
                progress_bar(progress)

        # Send a POST request to OpenAI's API using chat/completions endpoint
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Using the specified model
            messages=[
                {
                    "role": "system",
                     "content":f"""

        Subject: {selected_subject}

        Topic: {selected_topic}

        Deadline: {deadline_text}

        Current Date: {current_date}


        Generate a personalized study plan for the given subject and topic, considering the current date and the specified deadline. The study plan should include a breakdown of the topic into smaller sub-topics, a time allocation for each sub-topic based on its complexity, scheduled breaks and review days, and a daily study schedule. The plan should be flexible and adjustable based on the learners progress and understanding of the topic.in last  Provide links to relevant textbooks, articles, videos, and online resources for further study."""
                }
            ]
        )

        study_plan = response.choices[0].message["content"].strip()
        st.success("Study plan generated successfully:")

        # Display the study plan in an expander
        with st.expander("Study Plan", expanded=True):
            st.markdown(expander_css, unsafe_allow_html=True) 
             # Apply custom CSS
            st.write(study_plan)  # Display the study plan text
            
            

# Main code for the "Access Resources" section
elif study_option == "Access resources":
    st.title("Access Resources")
    def main():
        # Add a sidebar menu option for accessing the notes app
        
        notes_app = Notes()  # Instantiate the Notes class
        notes_app.run()      # Run the Notes application
        

        # Add other sections of your Streamlit app (e.g., Home) based on user selection
        

    # Run the main function to start the Streamlit app
    if __name__ == "__main__":
        main()

    
elif study_option == "Join a study group":
    st.title("Join a Study Group")
    # Add your code for joining a study group here
elif study_option == "Test Zone":
    def main():
        # Add a sidebar menu option for accessing the notes app
        
        test_app = Test()  # Instantiate the Notes class
        test_app.run()      # Run the Notes application
        

        # Add other sections of your Streamlit app (e.g., Home) based on user selection
        

    # Run the main function to start the Streamlit app
    if __name__ == "__main__":
        main()
               

    # Add your code for taking a quiz here
elif study_option == "Review notes":
    st.title("Review Notes")
    # Add your code for reviewing notes here
elif study_option == "Code Questions":
    

# Set your OpenAI API key
    programming_language = st.selectbox("Select a programming language:", ["Python", "C", "JavaScript"])

    # Dictionary mapping programming languages to available topics
    language_topics = {
        "Python": ["String Manipulation", "Data Structures", "File Handling", "Web Scraping"],
        "C": ["Pointer Operations", "Memory Management", "File Handling", "Data Structures"],
        "JavaScript": ["DOM Manipulation", "Asynchronous Programming", "Events Handling", "AJAX Requests"]
    }

    # Select a topic based on the chosen programming language
    selected_topic = st.selectbox(f"Select a topic for {programming_language}:", language_topics[programming_language])

    # Generate code example when button is clicked
    if st.button("Generate Code"):
        # Display a loading message while generating code
        with st.spinner("Generating code example..."):
            # Generate code example using OpenAI based on the selected topic
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": f"Generate a code example in {programming_language} for {selected_topic}"
                    }
                ]
            )
            code_example = response.choices[0].message["content"].strip()
        
        # Display the generated code example
        st.subheader(f"Code Example for {selected_topic}")
        st.code(code_example, language=programming_language.lower())
        
        # Add a button to copy the code to the clipboard
        if st.button("Copy Code"):
            st.write("Code copied to clipboard:", code_example)

    # Add your code for the Code Questions here

# section1 =st.sidebar.columns(1)
# with section1:
# Add icons and hover effects to the "Made by" section


st.sidebar.markdown("<br><br>", unsafe_allow_html=True)
st.sidebar.markdown("<br><br>", unsafe_allow_html=True)


st.sidebar.markdown("""
<style>
.made-by {
    font-family: monospace;
    color: #0C2637;
    font-size: 30px;
    text-align: center;
}
.made-by-links {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    margin: 10px 0;
}
.made-by-link {
    margin: 5px;
    text-decoration: none;
    color: #0C2637;
    font-size: 18px;
    transition: color 0.3s ease;
}
.made-by-link:hover {
    color: #0077B5;
}
.made-by-link img {
    width: 24px;
    height: 24px;
    margin-right: 5px;
}
</style>
<div class="made-by">💙 Made by : </div>
<div class="made-by-links">
    <a href="https://github.com/pingArJun" target="_blank" class="made-by-link">
        <img src="https://img.icons8.com/ios-glyphs/30/000000/github.png"/> GitHub
    </a>
    <a href="https://www.linkedin.com/in/arjunkumar7/" target="_blank" class="made-by-link">
        <img src="https://img.icons8.com/ios-glyphs/30/000000/linkedin.png"/> LinkedIn
    </a>
    <a href="https://twitter.com/pingarjun" target="_blank" class="made-by-link">
        <img src="https://img.icons8.com/ios-glyphs/30/000000/twitter.png"/> Twitter
    </a>
</div>
""", unsafe_allow_html=True)

# Add icons and hover effects to the "Follow me on" section

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<style>
.follow-me {
    font-family: monospace;
    color: #0C2637;
    font-size: 30px;
    text-align: center;
}
.follow-me-icons {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    margin: 10px 0;
}
.follow-me-icon {
    margin: 5px;
    transition: transform 0.3s ease;
}
.follow-me-icon:hover {
    transform: scale(1.2);
}
</style>


<div class="follow-me">🚀  Follow me  : </div>
<div class="follow-me-icons">
    <a href="https://www.linkedin.com/in/arjunkumar7/" target="_blank" class="follow-me-icon">
        <img src="https://img.icons8.com/ios-glyphs/30/000000/linkedin.png"/>
    </a>
    <a href="https://twitter.com/pingarjun" target="_blank" class="follow-me-icon">
        <img src="https://img.icons8.com/ios-glyphs/30/000000/twitter.png"/>
    </a>
    <a href="https://github.com/pingArJun" target="_blank" class="follow-me-icon">
        <img src="https://img.icons8.com/ios-glyphs/30/000000/github.png"/>
    </a>
</div>
""", unsafe_allow_html=True)




