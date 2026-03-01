import streamlit as st
import requests

st.title("Pinterest Email checking")
st.write("---------------------------------------------")

def fetch_pinterest(email):
    session=requests.Session() # for cookies

    header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.pinterest.com/signup/",
    "X-Requested-With": "XMLHttpRequest",
    "X-Pinterest-AppState": "active",
}
   



    try:
        session.get("https://www.pinterest.com/", headers=header, timeout=10)
        URL="https://www.pinterest.com/_ng_common/accounts/get_email_status/?email="+email
        response=session.get(URL,headers=header,timeout=10)
        if response.status_code!=200:
            st.error("Pinterest fobidden")
            return None
        
        if "application/json" in response.headers.get("Content-Type", ""):
            data = response.json()
            resource = data.get("resource_response", {})
            data_inner = resource.get("data", {})
            return data_inner.get("exists")
        else:
            st.error("Received an HTML page instead of data. (Likely a Bot Challenge/Captcha)")
            return None

      
        # data=response.json()
        # resourse=data.get("resource_response",{})
        # data1=resourse.get("data",{})
        # return data1.get("exists")
        
    
    except Exception as e:
        st.error("Processs Failed. Due to"+str(e))
        return None

email=st.text_input("Enter your email: ")
if st.button("Fetch pineterest"):
    result=fetch_pinterest(email)

    if result is True:
        st.success("The "+email+" is registered in pinterest.")
    elif result is False:
        st.error("The email '"+email+"' is not registered.")
    else:
        st.error("Error Occured. Try again.")

