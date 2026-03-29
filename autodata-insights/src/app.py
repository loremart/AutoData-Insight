import streamlit as st
from components.sidebar import render_sidebar
from utils.data_cleaner import load_and_clean_data
from components.charts import render_data_visualization

st.set_page_config(
    page_title="AutoData Insights",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


def main():
    st.title("📊 AutoData Insights UI")
    st.markdown("### The automated data analyst in your browser")

    uploaded_file = render_sidebar()

    if uploaded_file is None:
        st.info("👈 Start by uploading a CSV file from the left sidebar.")
    else:
        st.write("---")
        st.write("### 🔍 Data Exploration")

        with st.spinner("Processing dataset..."):
            df = load_and_clean_data(uploaded_file)

        if df is not None:
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Rows", df.shape[0])
            col2.metric("Total Columns", df.shape[1])
            col3.metric("Missing Values (Null)", df.isna().sum().sum())

            st.markdown("#### Dataset Preview")
            st.dataframe(df.head(100), use_container_width=True)

            render_data_visualization(df)


if __name__ == "__main__":
    main()