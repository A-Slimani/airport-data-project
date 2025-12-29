import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import pandas as pd

conn = st.connection("postgresql", type="sql")
df = conn.query("SELECT * FROM dbt.delays_by_airline")

df['average_delay_duration'] = df['average_delay_duration'].apply(lambda t: t.strftime("%H:%M:%S"))

average_delay = round(df['average_delay_duration_seconds'].mean())
delay_min, delay_sec = divmod(average_delay, 60)

st.set_page_config(
    page_title="Airport Delays by Airlines",
    layout="wide"
)

st.title("Airline Delay Analysis - By Airline")
st.text("data collected from 4th Nov 2025")

# Options
# locality_option = st.radio(
#     "Locality: ",
#     ("All", "International", "Domestic"),
#     index=1
# )

# KPIs at top
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Airlines", len(df))
col2.metric("Avg Delay Rate", f"{df['delay_percentage'].mean():.2f}%")
col3.metric("Avg Delay Duration", f"{delay_min:02d}:{delay_sec:02d}")
col4.metric("Worst Performer", df.nlargest(1, 'delay_percentage')['airline'].values[0])

# Main chart: Delay percentage (sorted)
st.subheader("Delay Rate by Airline")
fig1 = px.bar(
    df.sort_values('delay_percentage'),
    x='delay_percentage',
    y='airline',
    orientation='h',
    color='delay_percentage',
    color_continuous_scale='Reds',
    text='delay_percentage'
)
fig1.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
st.plotly_chart(fig1, use_container_width=True)

# Graph 2
st.subheader("Average delay duration by Airline")
fig1 = px.bar(
    df.sort_values('average_delay_duration_seconds'),
    x='average_delay_duration_seconds',
    y='airline',
    orientation='h',
    color='average_delay_duration_seconds',
    color_continuous_scale='Reds',
    text='average_delay_duration'
)
fig1.update_traces(texttemplate='%{text}', textposition='outside')
st.plotly_chart(fig1, use_container_width=True)


# Data table
st.subheader("Detailed Breakdown")
st.dataframe(
    df.sort_values('delay_percentage', ascending=False),
    use_container_width=True
)