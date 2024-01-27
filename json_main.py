import streamlit as st
import json

def main():
    st.title("JSON Beautifier")

    #txt = st.text_input()
    txt = str(st.text_area("Enter the text to beautify"))

    tab_space = int(st.slider('Choose the spacing', 2, 4, 1))
    btn = st.button("Beautify")

    try:
            
            if btn:
                tojson = json.loads(txt)
                result = json.dumps(tojson, indent=tab_space)
                st.code(result, language="json")
    except:
         
         st.caption("Unexpected error |  Reload page ")
        





        
        








if __name__ == "__main__":
    main()
