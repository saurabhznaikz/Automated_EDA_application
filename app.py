import numpy as np
import pandas as pd
import streamlit as st
import wget
import os
from pandas_profiling import ProfileReport
from autoviz.AutoViz_Class import AutoViz_Class
from autoviz import data_cleaning_suggestions
# from streamlit_pandas_profiling import st_profile_report
from pathlib import Path
from dataprep.eda import create_report


# Web App Title
st.markdown('''
# **The AUTOML EDA App**
**Credit:** App built by [Saurabh Naik](https://www.linkedin.com/in/saurabh-naik-981b611a3/)
---
''')


# Upload CSV data
with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)
""")

if uploaded_file is not None:
    if "df" not in st.session_state:
        st.session_state['df'] = pd.read_csv(uploaded_file)

    st.markdown('### 1.1. Glimpse of dataset')
    st.dataframe(st.session_state['df'].head(5))

    st.markdown('### 1.2. Basic Analysis on the data')
    st.dataframe(st.session_state['df'].describe(include='all'))

    if "dft" not in st.session_state:
        AV = AutoViz_Class()
        st.session_state['dft'] = AV.AutoViz(
            filename="",
            sep=",",
            depVar="",
            dfte=st.session_state['df'],
            header=0,
            verbose=0,
            lowess=False,
            chart_format="html",
            max_rows_analyzed=150000,
            max_cols_analyzed=30,
            save_plot_dir=None,
        )

    if "pandas_report" not in st.session_state:
        st.session_state['pandas_report'] = ProfileReport(st.session_state['df'],
                                                                  title='Detailed Analysis Report',
                                                                  explorative=True).to_file("Detailed Analysis Report.html")
        # st.session_state['report']=create_report(st.session_state['df'])
        # st.session_state['report'].save(filename='Detailed Analysis Report')

    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

    with col1:
        with open("./AutoViz_Plots/AutoViz/distplots_nums.html", "rb") as file:
            btn = st.download_button(
                label="Download DistilPlot report",
                data=file,
                file_name="DistilPlot.html",
                key='download_distilplot')
    with col2:
        with open("./AutoViz_Plots/AutoViz/heatmaps.html", "rb") as file:
            btn = st.download_button(
                label="Download Heatmap report",
                data=file,
                file_name="Heatmaps.html",
                key='download_heatmap')
    with col3:
        with open("./AutoViz_Plots/AutoViz/pair_scatters.html", "rb") as file:
            btn = st.download_button(
                label="Download Pair Scatter report",
                data=file,
                file_name="PairScatter.html",
                key='download_pairscatter')
    with col4:
        with open("./AutoViz_Plots/AutoViz/violinplots.html", "rb") as file:
            btn = st.download_button(
                label="Download Violin Plots report",
                data=file,
                file_name="ViolinPlots.html",
                key='download_ViolinPlots')
    # pandas_report = ProfileReport(st.session_state['df'], title='Detailed Analysis Report', explorative=True)
    # st.session_state['pandas_report'].to_file("Detailed Analysis Report.html")
    with open("Detailed Analysis Report.html", "rb") as file:
        btn = st.download_button(
            label="Download Detailed report",
            data=file,
            file_name="Detailed Analysis Report.html",
            key='download_detailed_report')

else:
    # --- Initialising SessionState ---
    if "example_dataset_button" not in st.session_state:
        st.session_state['example_dataset_button'] = False

    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset') or st.session_state['example_dataset_button']:
        st.session_state['example_dataset_button'] = True
        if "df_example" not in st.session_state:
                st.session_state['df_example'] = pd.DataFrame(
                np.random.rand(100, 5),
                columns=['a', 'b', 'c', 'd', 'e'])

        st.markdown('### 1.1. Glimpse of dataset')
        st.dataframe(st.session_state['df_example'].head(5))

        st.markdown('### 1.2. Basic Analysis on the data')
        st.dataframe(st.session_state['df_example'].describe(include='all'))

        if "dft_example" not in st.session_state:
            AV = AutoViz_Class()
            st.session_state['dft_example'] = AV.AutoViz(
                filename="",
                sep=",",
                depVar="",
                dfte=st.session_state['df_example'],
                header=0,
                verbose=0,
                lowess=False,
                chart_format="html",
                max_rows_analyzed=150000,
                max_cols_analyzed=30,
                save_plot_dir=None,
            )

        if "pandas_report_example" not in st.session_state:
            st.session_state['pandas_report_example'] = ProfileReport(st.session_state['df_example'],
                                                                      title='Detailed Analysis Report',
                                                                      explorative=True).to_file("Detailed Analysis Report.html")
            # st.session_state['report_example'] = create_report(st.session_state['df_example'],title='Detailed Analysis Report')
            # st.session_state['report_example'].save(filename='Detailed Analysis Report')

        col1, col2, col3,col4 = st.columns([1, 1, 1,1])

        with col1:
            with open("./AutoViz_Plots/AutoViz/distplots_nums.html", "rb") as file:
                btn = st.download_button(
                label="Download DistilPlot report",
                data=file,
                file_name="DistilPlot.html",
                key='download_distilplot_example')
        with col2:
            with open("./AutoViz_Plots/AutoViz/heatmaps.html", "rb") as file:
                btn = st.download_button(
                    label="Download Heatmap report",
                    data=file,
                    file_name="Heatmaps.html",
                    key='download_heatmap_example')
        with col3:
            with open("./AutoViz_Plots/AutoViz/pair_scatters.html", "rb") as file:
                btn = st.download_button(
                    label="Download Pair Scatter report",
                    data=file,
                    file_name="PairScatter.html",
                    key='download_pairscatter_example')
        with col4:
            with open("./AutoViz_Plots/AutoViz/violinplots.html", "rb") as file:
                btn = st.download_button(
                    label="Download Violin Plots report",
                    data=file,
                    file_name="ViolinPlots.html",
                    key='download_ViolinPlots_example')
        # pandas_report = ProfileReport(st.session_state['df'], title='Detailed Analysis Report', explorative=True)
        # st.session_state['pandas_report'].to_file("Detailed Analysis Report.html")
        with open("Detailed Analysis Report.html", "rb") as file:
            btn = st.download_button(
                label="Download Detailed report",
                data=file,
                file_name="Detailed Analysis Report.html",
                key='download_detailed_report_example')
