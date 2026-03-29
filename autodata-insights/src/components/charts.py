import plotly.express as px
import streamlit as st


def render_data_visualization(df):
    """
    Creates the data visualization section with interactive Plotly charts.
    """
    st.markdown("---")
    st.markdown("### 📊 Automatic Chart Generation")

    if df is None or df.empty:
        st.warning("Upload a dataset to generate charts.")
        return

    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object', 'category', 'bool']).columns.tolist()

    if not numeric_cols:
        st.warning("⚠️ This dataset lacks sufficient numeric columns to create charts.")
        return

    ctrl_col1, ctrl_col2 = st.columns(2)

    with ctrl_col1:
        chart_type = st.selectbox(
            "Select visualization type:",
            ["Scatter Plot", "Bar Chart"]
        )

    if chart_type == "Scatter Plot":
        st.markdown("#### Configure Scatter Plot")
        if len(numeric_cols) < 2:
            st.error("⚠️ At least two numeric columns are required for a Scatter Plot.")
            return

        c1, c2, c3 = st.columns(3)
        with c1:
            x_axis = st.selectbox("X-Axis (Numeric)", numeric_cols, key="scatter_x")
        with c2:
            y_axis = st.selectbox("Y-Axis (Numeric)", numeric_cols, index=1, key="scatter_y")
        with c3:
            color_axis = st.selectbox("Color (Optional)", [None] + categorical_cols, key="scatter_color")

        with st.spinner("Generating chart..."):
            fig = px.scatter(df, x=x_axis, y=y_axis, color=color_axis,
                             title=f"Scatter Analysis: {y_axis} vs {x_axis}",
                             template="plotly_white",
                             trendline="ols" if not color_axis else None
                             )
            st.plotly_chart(fig, use_container_width=True)

    elif chart_type == "Bar Chart":
        st.markdown("#### Configure Bar Chart")

        x_candidates = categorical_cols if categorical_cols else numeric_cols

        c1, c2, c3 = st.columns(3)
        with c1:
            x_axis = st.selectbox("X-Axis (Categories)", x_candidates, key="bar_x")
        with c2:
            y_axis = st.selectbox("Y-Axis (Value to Sum)", numeric_cols, key="bar_y")
        with c3:
            orientation = st.radio("Orientation", ["Vertical", "Horizontal"], horizontal=True)

        with st.spinner("Generating chart..."):
            is_horizontal = orientation == "Horizontal"

            df_grouped = df.groupby(x_axis)[y_axis].sum().reset_index()
            df_grouped = df_grouped.sort_values(by=y_axis, ascending=False).head(20)

            if is_horizontal:
                fig = px.bar(df_grouped, x=y_axis, y=x_axis,
                             orientation='h',
                             title=f"Sum of {y_axis} by Top 20 {x_axis}",
                             template="plotly_white",
                             color=y_axis,
                             color_continuous_scale=px.colors.sequential.Viridis)
            else:
                fig = px.bar(df_grouped, x=x_axis, y=y_axis,
                             title=f"Sum of {y_axis} by Top 20 {x_axis}",
                             template="plotly_white",
                             color=y_axis,
                             color_continuous_scale=px.colors.sequential.Plasma)

            st.plotly_chart(fig, use_container_width=True)