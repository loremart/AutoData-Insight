import streamlit as st
from components.sidebar import render_sidebar
from utils.data_cleaner import load_and_clean_data
# --- NUOVO IMPORT ---
from components.charts import render_data_visualization

st.set_page_config(
    page_title="AutoData Insights",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


def main():
    st.title("📊 AutoData Insights UI")
    st.markdown("### L'analista dati automatico nel tuo browser")

    uploaded_file = render_sidebar()

    if uploaded_file is None:
        st.info("👈 Inizia caricando un file CSV dalla barra laterale sinistra.")
    else:
        # --- LOGICA DATI ---
        st.write("---")
        st.write("### 🔍 Esplorazione Dati")

        with st.spinner("Elaborazione del dataset in corso..."):
            df = load_and_clean_data(uploaded_file)

        if df is not None:
            # Metriche chiave
            col1, col2, col3 = st.columns(3)
            col1.metric("Righe Totali", df.shape[0])
            col2.metric("Colonne Totali", df.shape[1])
            col3.metric("Valori Mancanti (Null)", df.isna().sum().sum())

            st.markdown("#### Anteprima del Dataset")
            st.dataframe(df.head(100), use_container_width=True)

            # --- NUOVA SEZIONE: VISUALIZZAZIONE ---
            # Passiamo il dataframe alla funzione dei grafici
            render_data_visualization(df)


if __name__ == "__main__":
    main()