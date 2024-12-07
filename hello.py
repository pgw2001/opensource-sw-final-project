import streamlit as st
import streamlit.components.v1 as components
import streamlit_authenticator as stauth
import yaml
with open('config.yaml') as file:
        config = yaml.load(file, Loader=stauth.SafeLoader)

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

## yaml 파일 데이터로 객체 생성
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
## 로그인 위젯 렌더링
## log(in/out)(로그인 위젯 문구, 버튼 위치)
## 버튼 위치 = "main" or "sidebar"
name, authentication_status, username = authenticator.login('main')

# authentication_status : 인증 상태 (실패=>False, 값없음=>None, 성공=>True)
if st.session_state["authentication_status"] == False:
    st.error("Username/password is incorrect")

if st.session_state["authentication_status"] == None:
    st.warning("Please enter your username and password")

if st.session_state["authentication_status"]:
    authenticator.logout('Logout',"sidebar")
    st.sidebar.title(f"Welcome {name}")
    ## 로그인 후 기능들 작성 ##