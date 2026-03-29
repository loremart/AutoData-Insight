import plotly.express as px
import streamlit as st


def render_data_visualization(df):
    """
    Crea la sezione di visualizzazione dati con grafici interattivi Plotly.
    Permette all'utente di selezionare assi e tipi di grafico.
    """
    st.markdown("---")
    st.markdown("### 📊 Generazione Grafici Automatica")

    if df is None or df.empty:
        st.warning("Carica un dataset per generare grafici.")
        return

    # 1. Identifichiamo i tipi di colonne
    # Ci servono numeri per l'asse Y e statistiche, categorie per l'asse X o i colori
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object', 'category', 'bool']).columns.tolist()

    if not numeric_cols:
        st.warning("⚠️ Questo dataset non contiene colonne numeriche sufficienti per creare grafici.")
        return

    # 2. Layout a colonne per i controlli del grafico
    ctrl_col1, ctrl_col2 = st.columns(2)

    with ctrl_col1:
        # Scegliamo il tipo di grafico
        chart_type = st.selectbox(
            "Seleziona il tipo di visualizzazione:",
            ["Scatter Plot (Dispersione)", "Bar Chart (Istogramma/Barre)"]
        )

    # 3. Logica condizionale e rendering basato sulla scelta

    if chart_type == "Scatter Plot (Dispersione)":
        st.markdown("#### Configura Scatter Plot")
        if len(numeric_cols) < 2:
            st.error("⚠️ Servono almeno due colonne numeriche per uno Scatter Plot.")
            return

        c1, c2, c3 = st.columns(3)
        with c1:
            x_axis = st.selectbox("Asse X (Numerico)", numeric_cols, key="scatter_x")
        with c2:
            y_axis = st.selectbox("Asse Y (Numerico)", numeric_cols, index=1, key="scatter_y")
        with c3:
            # Opzionale: Colore basato su una categoria (es. Segmento di mercato, Genere)
            color_axis = st.selectbox("Colore (Opzionale)", [None] + categorical_cols, key="scatter_color")

        # Generazione grafico con Plotly Express
        with st.spinner("Generazione grafico..."):
            fig = px.scatter(df, x=x_axis, y=y_axis, color=color_axis,
                             title=f"Analisi Dispersione: {y_axis} vs {x_axis}",
                             template="plotly_white",  # Tema pulito
                             trendline="ols" if not color_axis else None  # Aggiunge linea di tendenza se non c'è colore
                             )
            # Mostriamo il grafico in Streamlit
            st.plotly_chart(fig, use_container_width=True)


    elif chart_type == "Bar Chart (Istogramma/Barre)":
        st.markdown("#### Configura Grafico a Barre")

        # Per un grafico a barre tipico, usiamo una categoria su X e sommiamo un numero su Y
        x_candidates = categorical_cols if categorical_cols else numeric_cols

        c1, c2, c3 = st.columns(3)
        with c1:
            x_axis = st.selectbox("Asse X (Categorie)", x_candidates, key="bar_x")
        with c2:
            y_axis = st.selectbox("Asse Y (Valore da Sommare)", numeric_cols, key="bar_y")
        with c3:
            # Opzionale: Orientamento
            orientation = st.radio("Orientamento", ["Verticale", "Orizzontale"], horizontal=True)

        with st.spinner("Generazione grafico..."):
            is_horizontal = orientation == "Orizzontale"

            # Creiamo una copia per non sporcare il DF originale, aggregando i dati
            # (Plotly lo fa internamente ma aggregare a mano con Pandas è più 'Senior' per le performance)
            df_grouped = df.groupby(x_axis)[y_axis].sum().reset_index()
            df_grouped = df_grouped.sort_values(by=y_axis, ascending=False).head(20)  # Top 20 per non intasare

            if is_horizontal:
                fig = px.bar(df_grouped, x=y_axis, y=x_axis,
                             orientation='h',
                             title=f"Somma di {y_axis} per Top 20 {x_axis}",
                             template="plotly_white",
                             color=y_axis,  # Colore sfumato in base al valore
                             color_continuous_scale=px.colors.sequential.Viridis)
            else:
                fig = px.bar(df_grouped, x=x_axis, y=y_axis,
                             title=f"Somma di {y_axis} per Top 20 {x_axis}",
                             template="plotly_white",
                             color=y_axis,
                             color_continuous_scale=px.colors.sequential.Plasma)

            st.plotly_chart(fig, use_container_width=True)