import streamlit as st


def render_sidebar():
    """
    Renderizza la barra laterale e gestisce l'upload del file CSV.
    Ritorna il file caricato (o None se non c'è).
    """
    with st.sidebar:
        st.title("⚙️ Configurazione")
        st.markdown("Carica il tuo dataset per iniziare l'esplorazione automatica.")

        # Il widget magico di Streamlit per l'upload
        uploaded_file = st.file_uploader(
            "Trascina qui il tuo CSV",
            type=["csv"],
            help="Sono supportati solo file in formato .csv"
        )

        if uploaded_file is not None:
            st.success("File caricato con successo! 🎉")

        st.markdown("---")
        st.caption("AutoData Insights UI v0.1")

        return uploaded_file