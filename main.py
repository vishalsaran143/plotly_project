import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
df = pd.read_csv("project_plotly1.csv")
df.columns = df.columns.str.replace("_"," ")
list_of_state = list(df['State'].unique())
list_of_state.insert(0,"Overall India")
st.sidebar.title("India DataBase")
select_state = st.sidebar.selectbox("Select a State",list_of_state)
Primary = st.sidebar.selectbox("Select Primary Perameter",sorted(df.columns[5:]))
Secondary = st.sidebar.selectbox("Select Secondary Perameter",sorted(df.columns[5:]))
plot = st.sidebar.button("Plot Graph")
st.text("Primary Represent Size")
st.text("Secondary Represent Color")
if plot:
    if select_state == "Overall India":
        fig = px.scatter_mapbox(df,lat="Latitude", lon="Longitude",size=Primary,color=Secondary,
                                zoom=3,mapbox_style="carto-positron",width=1200,height=800,size_max=30,hover_name="District")
        st.plotly_chart(fig,use_container_width=True)
    else:
        state_df = df[df['State'] == select_state]
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=Primary, color=Secondary,
                                zoom=6, mapbox_style="carto-positron", width=1200, height=800, size_max=30,hover_name="District")
        st.plotly_chart(fig, use_container_width=True)