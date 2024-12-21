import streamlit as st

# Uma classe para definir e manipular todos os componentes de ui do streamlit em um unico arquivo

class StreamlitManipulationUi():
    def __init__(self):
        pass
    
    def navegation(self, end_point, page_file, page_title):
        pages = {
            end_point: [
                st.Page(page=page_file, title=page_title),
            ],
        }

        st.navigation(pages).run()