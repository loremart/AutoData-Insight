import pandas as pd
import streamlit as st


@st.cache_data
def load_and_clean_data(uploaded_file):
    """
    Legge il CSV caricato, esegue una pulizia di base e lo salva in cache.
    Ritorna un DataFrame Pandas pulito o None in caso di errore.
    """
    try:
        # Leggiamo il CSV. Pandas fa già un ottimo lavoro a dedurre i tipi di dato.
        df = pd.read_csv(uploaded_file)

        # Pulizia base: eliminiamo righe o colonne che sono COMPLETAMENTE vuote
        df = df.dropna(how='all', axis=0).dropna(how='all', axis=1)

        # Qui in futuro potremmo aggiungere logica complessa, tipo:
        # - Riconoscere automaticamente le colonne data e fare il parsing
        # - Riempire i valori nulli (imputation)

        return df

    except Exception as e:
        # Se l'utente carica un file corrotto o non formattato bene, lo catturiamo qui
        st.error(f"Errore durante l'elaborazione del file: {str(e)}")
        return None