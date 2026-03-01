import requests
import streamlit as st  

st.title("Github Profile Fetcher")

def fetch_github(username):
    url="https://api.github.com/users/"+username

    try:
        header={"User-Agent":"Ilyan321"}
        response=requests.get(url,headers=header)

        if response.status_code==200:
            data=response.json()

            avatar_url=data.get("avatar_url","N/A")
            if avatar_url:
                st.image(avatar_url,width=150)


            st.subheader(data.get("name","N/A"))
            st.write(data.get("bio","N/A"))

            col1,col2,col3=st.columns(3)
            with col1:
                st.metric("Public Repos",data.get("public_repos","N/A"))
            with col2:
                st.metric("Followers",data.get("followers","N/A"))
            with col3:
                    st.metric("Following",data.get("following","N/A"))

            st.write("ID: ",data.get("id","N/A"))
            st.markdown("Profile URL:"+data.get("html_url","#"))
            email=data.get("email") or "Not provided"
            st.markdown("Email: "+email)
            st.write("Location: ",data.get("location","N/A"))
            st.write("Company: ",data.get("company","N/A"))

        elif response.status_code==404:
            st.error("User Not Found.")
        else:
           st.error("Failed to fetch data.")
    except Exception as e:
        st.error("An error occured. Response code: "+str(e))


st.write("----------------------------------------")
username=st.text_input("Enter Github Username: ")

if st.button("Fetch Profile"):
    if username:
        fetch_github(username)
    else:
        st.warning("Please eneter a username.")

