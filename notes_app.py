from dependencies import *
from streamlit_option_menu import option_menu


class Notes:

    def __init__(self):
        self.apps = []

    @staticmethod
    def run(): 
        # Move your code for displaying the sidebar content inside this function

        c1, c2, c3 = st.sidebar.columns(3)
        with c1:
            side_title = '<h3 style="font-family:regular; color:black; font-size: 25px;" align="center">Choose Subject</h3><br>'
            st.sidebar.markdown(side_title, unsafe_allow_html=True)
        with c2:
            st.markdown("""
                        <style>
                        .st-emotion-cache-1v0mbdj > img{
                        border-radius: 50%;
                            }
                        </style>
            
                        """, unsafe_allow_html=True)

            

        with st.sidebar:
            option = option_menu(
                menu_title=None,
                options = ["AI", "Mobile Computing", "NLP", "ANN", "Information Security", "Cybersecurity", "DBMS"],
                orientation="vertical",
                icons=["house-door", "robot", "key", "code-slash", "person-fill", "percent", "lightbulb", "database"],
                default_index=0,
            
            # styles={
            # "container": {"padding": "0!important", "background-color": "#fafafa"},
            # "icon": {"color": "orange", "font-size": "25px"}, 
            # "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            # "nav-link-selected": {"background-color": "green"},
            # }
            )

        try:
            if option == "Home":
                Home.app()

            if option == "AI":
                ai = Subject("<br>Artificial Intelligence", option)
                ai.app()

            if option == "Mobile Computing":
                option1="mobile_computing"
                mobile_computing = Subject("Mobile Computing", option1)
                mobile_computing.app()

            if option == "NLP":
                nlp = Subject("NLP", option)
                nlp.app()

            if option == "ANN":
                ann = Subject("ANN", option)
                ann.app()

            if option == "Information Security":
                option1="information_security"
                info_security = Subject("information_security", option1)
                info_security.app()

            if option == "Cybersecurity":
                cybersecurity = Subject("Cybersecurity", option)
                cybersecurity.app()

            if option == "DBMS":
                dbms = Subject("Database Management Systems", option)
                dbms.app()
        except TypeError:
            center_title(50, "red", "server is down .please try again later")

# def run_notes_app():
#     notes_app = Notes()
#     notes_app.run()

# if __name__ == "__main__": 
#     run_notes_app()


