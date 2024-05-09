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
    # r, c = df.shape 
    # listt = []
    # for i in range(0,r):
    #   listt.append(f"{st.button('Show Details', key=f'button_{i}')}")
    # # df["Details"] = listt
    # df["Show Details"] = df["Name"].apply(lambda name: st.button("Show Details", key=name))
    st.table(df)

    if(selected_option != "All"):
      anss = log.main_search_user_time(selected_option, number)
      list_dicts = []
      for string in anss:
        parts = string.split(", ")
        d = {}
        for part in parts:
            key, value = part.split(": ")
            d[key.strip()] = value.strip()
        list_dicts.append(d)
      df = pd.DataFrame(list_dicts)
      st.table(df)
      # st.write(anss)




      
def Query():
    st.title("Query Latency")
    selected_option2 = st.selectbox("Select an option", ["7 days", "30 days", "14 days"])
    st.markdown("---")
    numbers = re.findall(r'\d+', selected_option2)
    number = numbers.pop(0)
    ans = {}
    que = query()
    ans = que.main_query(number)
    list_dicts = []
    for string in ans:
      parts = string.split(", ")
      d = {}
      for part in parts:
          key, value = part.split(": ")
          d[key.strip()] = value.strip()
      list_dicts.append(d)
    df = pd.DataFrame(list_dicts)
    st.table(df)

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
    list_dicts = []
    for string in most_ans:
      parts = string.split(", ")
      d = {}
      for part in parts:
          key, value = part.split(": ")
          d[key.strip()] = value.strip()
      list_dicts.append(d)
    df = pd.DataFrame(list_dicts)
    st.table(df)
    st.markdown("## Actions performed")
    ans = user_action.main_user_action(selected_option, number, selected_option2)

    data_list = []
    for line in ans:
      parts = line.split(", ")
      entry_dict = {}
      for part in parts:
          key_value = part.split(":", 1)
          key, value = key_value
          key = key.strip()
          value = value.strip()
          entry_dict[key] = value
          data_list.append(entry_dict)
    df = pd.DataFrame(data_list)
    st.table(df)

def Resources():
    st.title("Resource Utilization")
    st.markdown("## CPU Threshold")
    col1, col2 = st.columns(2)
    with col1:
      user_input = st.text_input("Enter some text", "80")
    with col2:
      selected_option1 = st.selectbox("Select an option", ["30 days", "7 days", "14 days"])
    st.markdown("---")
    numbers = re.findall(r'\d+', selected_option1)
    number = numbers.pop(0)
    cpu = cpuUtilization()
    ans = cpu.main_cpuUtilization(number, int(user_input))
    list_dicts = []
    for string in ans:
      parts = string.split(", ")
      d = {}
      for part in parts:
          key, value = part.split(": ")
          d[key.strip()] = value.strip()
      list_dicts.append(d)
    df = pd.DataFrame(list_dicts)
    st.table(df)

    st.markdown("## Memory Threshold")
    col3, col4 = st.columns(2)
    with col3:
      user_input1 = st.text_input("Enter the free memory threshold", "90")
    with col4:
      selected_option2 = st.selectbox("Select a range", ["30 days", "7 days", "14 days"])
    st.markdown("---")
    numberss = re.findall(r'\d+', selected_option2)
    numberr = numberss.pop(0)
    mem = memUtilzation()
    anss = mem.main_memUtilization(numberr, int(user_input1))
    list_dicts = []
    for string in anss:
      parts = string.split(", ")
      d = {}
      for part in parts:
          key, value = part.split(": ")
          d[key.strip()] = value.strip()
      list_dicts.append(d)
    df = pd.DataFrame(list_dicts)
    st.table(df)

def Services():
    st.title("Services status")
    st.markdown("## GSE Status")
    selected_option1 = st.selectbox("Select an option", ["30 days", "7 days", "14 days"])
    st.markdown("---")
    numbers = re.findall(r'\d+', selected_option1)
    number = numbers.pop(0)
    gse = gseStatus()
    ans = gse.main_gseStatus(number)
    list_dicts = []
    for string in ans:
      parts = string.split(", ")
      d = {}
      for part in parts:
          key, value = part.split(": ")
          d[key.strip()] = value.strip()
      list_dicts.append(d)
    df = pd.DataFrame(list_dicts)
    st.table(df)
    # st.write(ans)

def main():
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

    pages = ["Login", "Query", "User", "Resources", "Services"]
    selected_page = st.sidebar.radio("Go to", pages, index=0)

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
