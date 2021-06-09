import streamlit as st

"""Framework para executar vários aplicativos Streamlit 
   como um único aplicativo."""


class MultiApp:

    def __init__(self):
        self.apps = []

    """
    Framework for combining multiple streamlit applications.
    Usage:
        def foo():
            st.title("Hello Foo")
        def bar():
            st.title("Hello Bar")
        app = MultiApp()
        app.add_app("Foo", foo)
        app.add_app("Bar", bar)
        app.run()
    It is also possible keep each application in a separate file.
        import foo
        import bar
        app = MultiApp()
        app.add_app("Foo", foo.app)
        app.add_app("Bar", bar.app)
        app.run()
    """

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        # COMANDOS DA BARRA LATERAL
        padding = 0
        st.sidebar.markdown(f""" <style> 
        .reportview-container .main .block-container{{
            padding-top: {padding}rem;
            padding-bottom: {padding}rem;
        }} </style> """, unsafe_allow_html=True)

        st.sidebar.title("🚀 Veritas")
        #st.sidebar.title("Menu")
        st.sidebar.markdown("---")

        app = st.sidebar.radio(
            '',
            self.apps,
            format_func=lambda veritas: veritas['title'])

        app['function']()

        st.sidebar.markdown("---")

        if st.sidebar.button("Fale com a gente!", key="5"):
            st.sidebar.markdown('''
                Grupo Tera
                
               moxú - dairenkonmajime@gmail.com

               felipe - fmonteirogabriel@gmail.com

               lauro - lauro.namiki@gmail.com

               mel - meliza.caug@gmail.com

               rodolpho - rodolphoya@gmail.com

                ''')
            pass
