import streamlit as st
import re
from Function import *
import pandas as pd

st.markdown(
    """
    <style>
    .stSelectbox {
        width: 200px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def Login():
    st.title("User Login Frequency")
    col1, col2 = st.columns(2)
    with col1:
      selected_option = st.selectbox("Select an option", ["All", "Varun", "tigergraph", "ashraf", "nikhil", "swasthik", "surajbangera"])
    with col2:
      selected_option1 = st.selectbox("Select an option", ["30 days", "7 days", "14 days"])
    st.markdown("---")
    numbers = re.findall(r'\d+', selected_option1)
    number = numbers.pop(0)
    log = login()
    st.markdown("### Frequency")
    ans = {}
    ans = log.main_user_login(number)
    df = pd.DataFrame(list(ans.items()), columns=["Name", "Count"])
    r, c = df.shape 
    listt = []
    for i in range(0,r):
      listt.append("Details")
    df["Details"] = listt
    df["Details"] = df["Details"].apply(details_click)
    st.table(df)
def show_popup(name):
    st.write(f"Hi, {name}!")

def details_click(detail):
  return "hi"
  # st.write("Clicked")
  # return st.button("Details" + detail)


      
def Query():
    st.title("Query Latency")
    selected_option2 = st.selectbox("Select an option", ["7 days", "30 days", "14 days"])
    st.markdown("---")
    numbers = re.findall(r'\d+', selected_option2)
    number = numbers.pop(0)
    ans = {}
    que = query()
    ans = que.main_query(number)
    st.write(ans)

def User():
    st.title("User Actions")
    col1, col2, col3 = st.columns(3)
    with col1:
      selected_option = st.selectbox("Select an option", ["All", "Varun", "tigergraph", "ashraf", "nikhil", "swasthik", "surajbangera"])
    with col2:
      selected_option1 = st.selectbox("Select an option", ["30 days", "7 days", "14 days"])
    with col3:
      selected_option2 = st.selectbox("Select an option", ["All", "login",  "showCatalog", "showQuery", "createQuery", "installQuery",
       "interpretQuery", "createGraph", "runLocalSchemaChangeJob", "dropSecret", "createSecret", "createLoadingJob", "requestToken"])
    st.markdown("---")
    numbers = re.findall(r'\d+', selected_option1)
    number = numbers.pop(0)
    user_action = UserAction()

    matching_results = user_action.most_search_text(number)
    most_ans = user_action.most_user_actions(matching_results)
    st.markdown("## Most performed Actions")
    st.write(most_ans)
    st.markdown("## Actions performed")
    ans = user_action.main_user_action(selected_option, number, selected_option2)
    st.write(ans)
    

def Resources():
    st.title("Resource Utilization")
    st.markdown("## CPU Threshold")
    col1, col2 = st.columns(2)
    with col1:
      user_input = st.text_input("Enter some text", "80")
      # st.write("You entered:", user_input)  
    with col2:
      selected_option1 = st.selectbox("Select an option", ["30 days", "7 days", "14 days"])
    st.markdown("---")
    numbers = re.findall(r'\d+', selected_option1)
    number = numbers.pop(0)
    cpu = cpuUtilization()
    ans = cpu.main_cpuUtilization(number, int(user_input))
    st.write(ans)

    st.markdown("## Memory Threshold")
    col3, col4 = st.columns(2)
    with col3:
      user_input1 = st.text_input("Enter the free memory threshold", "90")
      # st.write("You entered:", user_input)  
    with col4:
      selected_option2 = st.selectbox("Select a range", ["30 days", "7 days", "14 days"])
    st.markdown("---")
    numberss = re.findall(r'\d+', selected_option2)
    numberr = numberss.pop(0)
    mem = memUtilzation()
    anss = mem.main_memUtilization(numberr, int(user_input1))
    st.write(anss)

def Services():
    st.title("Services status")
    st.markdown("## GSE Status")
    selected_option1 = st.selectbox("Select an option", ["30 days", "7 days", "14 days"])
    st.markdown("---")
    numbers = re.findall(r'\d+', selected_option1)
    number = numbers.pop(0)
    gse = gseStatus()
    ans = gse.main_gseStatus(number)
    st.write(ans)

    # st.markdown("## GPE Status")
    # selected_option11 = st.selectbox("Select an date", ["30 days", "7 days", "14 days"])
    # st.markdown("---")
    # numbers = re.findall(r'\d+', selected_option11)
    # number = numbers.pop(0)
    # gpe = gpeStatus()
    # ans = gpe.main_gpeStatus(number)
    # st.write(ans)

def main():
    # Custom CSS styles for sidebar
    sidebar_style = """
        <style>
            .sidebar-content {
                background-color: red;
                padding: 50px;
            }
            .sidebar-content a {
                color: white;
                display: block;
                padding: 30px 0;
            }
            .sidebar-content a:hover {
                color: blue;
            }
        </style>
    """
    st.markdown(sidebar_style, unsafe_allow_html=True)

    # Create sidebar with text list for navigation
    pages = ["Login", "Query", "User", "Resources", "Services"]
    selected_page = st.sidebar.radio("Go to", pages, index=0)

    # Display the selected page
    if selected_page == "Login":
        Login()
    elif selected_page == "Query":
        Query()
    elif selected_page == "User":
        User()
    elif selected_page == "Resources":
        Resources()
    elif selected_page == "Services":
        Services()

if __name__ == "__main__":
    main()
