import streamlit as st


def render_sidebar():
    """
    Renders the sidebar and handles CSV file upload.
    Returns the uploaded file (or None if empty).
    """
    with st.sidebar:
        st.title("⚙️ Configuration")
        st.markdown("Upload your dataset to start the automated exploration.")

        uploaded_file = st.file_uploader(
            "Drag and drop your CSV here",
            type=["csv"],
            help="Only .csv files are supported"
        )

        if uploaded_file is not None:
            st.success("File uploaded successfully! 🎉")

        st.markdown("---")
        st.caption("AutoData Insights UI v0.1")

        return uploaded_file