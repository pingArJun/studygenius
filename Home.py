import streamlit as st
import datetime
import time
import openai
import sqlite3
from notes_app import Notes
from PIL import Image
from streamlit_option_menu import option_menu
import pyperclip 

# Set your OpenAI API key
openai.api_key = "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"

def progress_bar(progress):
    st.progress(progress)
st.set_page_config(page_title="Interactive Study Planner and Resource Aggregator", page_icon="📚", layout="wide")

pg_bg_img = f"""
<style>
[data-testid="stApp"] {{
background-image: url("https://t3.ftcdn.net/jpg/05/77/27/02/240_F_577270209_zkEudjWqdnCF3CidEF83gP1KqmTZGy4l.jpg");
background-size: cover;
background-repeat: no-repeat;
background-attachment: local;
background-position: top left;
}}
[data-testid="stHeader"]{{
background-color: rgba(0,0,0,0);
}}

[data-testid="stSidebar"]{{
background-color: rgba(255,255,243,0.50);
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

study_option = st.sidebar.selectbox("What would you like to do?", ["Menu","Create a study plan", "Access resources",  "Test Zone", "Join a study group", "Motivation booster"])

# Custom CSS for the expander
expander_css = """
<style>
.st-expander {
    border-radius: 5px;
    border: 1px solid #ccc;
    padding: 10px;
    margin-bottom: 10px;
}
.stExpander > div:first-child {
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.copy-btn {
    background-color: white;
    border: none;
    cursor: pointer;
    font-size: 16px;
    padding: 5px;
}
.copy-btn:hover {
    background-color: #f0f0f0;
}
.copy-icon {
    fill: currentColor;
    margin-right: 5px; 
}
</style>
"""

# Main content area
if study_option =="Menu":
    st.title("Interactive Study Planner and Resource Aggregator")
   

    st.header("Welcome! Buddy")
    st.write("""
    Welcome to the Interactive Study Planner and Resource Aggregator! This app is your personal study buddy.
    Input your subjects, topics, and deadlines, and get a personalized study plan. Let's make studying efficient and fun!
    """)
    # Footer for additional information
    st.markdown("""
<div style="text-align: center; padding: 20px; background-color: #f0f0f0; border-radius: 5px;">
    <p>Made with ❤️ by Your Team Name</p>
    <p>Contact us at yourteam@email.com</p>
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
    st.title("Test Zone")
    st.write("Enter subject for test")
    test_topic=st.text_input("")
    if st.button("Generate Test Questions", key="plan_btn"):
        st.markdown(f'<p style="color: blue;">Generating Test Question for {test_topic}...</p>', unsafe_allow_html=True)
        
        progress_placeholder = st.empty()
        with progress_placeholder:
            st.write("Generating study plan...")
            progress_bar(0)
            for progress in range(1, 101):
                time.sleep(20/100)
                progress_bar(progress)
        response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Using the specified model
                messages=[
                    {
                        "role": "system",
                        "content":f"""

            Subject: {test_topic}



            create a 30 test question + 30 objective question on this subject. """
                    }
                ]
            )

        test_question = response.choices[0].message["content"].strip()
        st.success("Test Question generated successfully:") 
            # Display the study plan in an expander
        with st.expander("Test_question", expanded=True):
            st.markdown(expander_css, unsafe_allow_html=True)
            st.write(test_question)

    # Add your code for taking a quiz here
elif study_option == "Review notes":
    st.title("Review Notes")
    # Add your code for reviewing notes here
elif study_option == "Motivation booster":
    st.title("Motivation Booster")
    
    
    # Display a brief description of the available resources
    st.write("Welcome to the Resources section! Here, you can access various study materials and resources.")
    
    # Provide options for different types of resources
    resource_options = ["Notes", "Assignments", "Test Questions", "Study Guides", "Video Tutorials"]
    selected_resource = st.radio("Select a resource type:", resource_options)
    
    # Display the code for accessing the selected resource type
    if selected_resource == "Notes":
        st.subheader("Code for Accessing Notes")
        with st.expander("View Code"):
            st.code("""
            # Insert code here to access notes
            # For example:
            # notes = Database().get_notes(subject)
            # Display notes using st.write(notes)
            """, language="python")
    
    elif selected_resource == "Assignments":
        st.subheader("Code for Accessing Assignments")
        with st.expander("View Code"):
            st.code("""
            # Insert code here to access assignments
            # For example:
            # assignments = Database().get_assignments(subject)
            # Display assignments using st.write(assignments)
            """, language="python")
    
    elif selected_resource == "Test Questions":
        st.subheader("Code for Generating Test Questions")
        subject="python"
        with st.expander("View Code"):
            # Generate test questions using OpenAI
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": f"Generate 30 test questions on {subject}"
                    }
                ]
            )
            test_questions = response.choices[0].message["content"]
            # Split the test_questions string into individual questions
            questions_list = test_questions.split("\n\n")

            # Display each question separately
            for i, question in enumerate(questions_list, start=1):
                st.write(f"**Question {i}:**")
                st.write(question)

            
            # Display code for generating test questions
            st.code(f"""
            # Code to generate test questions for {selected_resource}
            # Replace this with your actual implementation
            
            test_questions = {repr(test_questions)}
            st.write(test_questions)
            """,)
    
    elif selected_resource == "Study Guides":
        st.subheader("Code for Accessing Study Guides")
        with st.expander("View Code"):
            st.code("""
            # Insert code here to access study guides
            # For example:
            # guides = Database().get_study_guides(subject)
            # Display guides using st.write(guides)
            """, language="python")
    
    elif selected_resource == "Video Tutorials":
        st.subheader("Code for Accessing Video Tutorials")
        with st.expander("View Code"):
            st.code("""
            # Insert code here to access video tutorials
            # For example:
            # tutorials = Database().get_video_tutorials(subject)
            # Display tutorials using st.write(tutorials)
            """, language="python")
    # Add your code for the motivation booster here

# section1 =st.sidebar.columns(1)
# with section1:
with st.sidebar:
    side_title = '<h1 style="font-family:monospace; color:#0C2637; font-size: 30px;" align="center">👨‍💻Made by : </h1><br>'
    st.sidebar.markdown(side_title, unsafe_allow_html=True)

    st.sidebar.link_button("About Me", url="https://github.com/pingArJun",
                        use_container_width=True)
    st.sidebar.link_button("Contact Me", url="https://github.com/pingArJun",
                        use_container_width=True)  # Made by section

    # Follow me on section
    side_title = '<br><h1 style="font-family:monospace; color:#0C2637; font-size: 30px;" align="center">📲Follow me on : </h1><br>'
    st.sidebar.markdown(side_title, unsafe_allow_html=True)
    st.link_button("Linked-In",
                    url="https://www.linkedin.com/in/arjunkumar7/",
                    use_container_width=True,
                    type="secondary",
                    help="Linked-In Profile")

    st.link_button("Twitter",
                    url="https://twitter.com/pingarjun",
                    use_container_width=True,
                    type="secondary",
                    help="My Twitter")
    st.link_button("GitHub",
                    url="https://github.com/pingarjun",
                    use_container_width=True,
                    type="secondary",
                    help="My GitHub")
