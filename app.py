import streamlit as st # type: ignore
import streamlit.components.v1 as components # type: ignore

st.set_page_config(page_title="Healthy Living Guide Bot", layout="wide")
st.title("Healthy Living Guide Chatbot")

iframe_code = """
<!DOCTYPE html>
<html>
  <body style="margin:0;padding:0;">
    <iframe 
      src="https://copilotstudio.microsoft.com/environments/Default-24f213d4-aa1c-4f84-ad54-7f26dbd4545a/bots/cr444_healthyLivingGuide/webchat?__version__=2" 
      frameborder="0" 
      style="width: 100%; height: 800px;">
    </iframe>
  </body>
</html>
"""

components.html(iframe_code, height=820, scrolling=True)
