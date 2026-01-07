import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import pandas as pd

st.text('In Progress....')

# conn = st.connection("postgresql", type="sql")
# df = conn.query("SELECT * FROM dbt.delays_by_time WHERE delay_percentage > 0")
# 
# df['average_delay_duration'] = df['average_delay_duration'].apply(lambda t: t.strftime("%H:%M:%S"))
# 
# average_delay = round(df['average_delay_duration_seconds'].mean())
# delay_min, delay_sec = divmod(average_delay, 60)
#  
# st.set_page_config(
#     page_title="Airport Delays by Hour",
#     layout="wide"
# )
# 
# st.title("Airline Delay Analysis - by Hour")
# st.text("data collected from 4th Nov 2025")
# 
# # KPIs at top
# col1, col2, col3, col4 = st.columns(4)
# col1.metric("Total Flights", df['total_flights'].sum())
# col2.metric("Avg Delay Rate", f"{df['delay_percentage'].mean():.0f}%")
# col3.metric("Avg Delay Duration", f"{delay_min:02d}:{delay_sec:02d}")
# col4.metric("Worst Hour", f"{df.nlargest(1, 'delay_percentage')['flight_hour'].values[0]:.0f}:00")
# 
# # Main chart: Delay percentage (sorted)
# st.subheader("Delay Rate by Flight hour")
# fig1 = px.bar(
#     df.sort_values('delay_percentage'),
#     x='delay_percentage',
#     y='flight_hour',
#     orientation='h',
#     color='delay_percentage',
#     color_continuous_scale='Reds',
#     text='delay_percentage'
# )
# fig1.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
# st.plotly_chart(fig1, use_container_width=True)
# 
# # Graph 2
# st.subheader("Average delay duration by Flight hour")
# fig1 = px.bar(
#     df.sort_values('average_delay_duration_seconds'),
#     x='average_delay_duration_seconds',
#     y='flight_hour',
#     orientation='h',
#     color='average_delay_duration_seconds',
#     color_continuous_scale='Reds',
#     text='average_delay_duration'
# )
# fig1.update_traces(texttemplate='%{text}', textposition='outside')
# st.plotly_chart(fig1, use_container_width=True)
# 
# 
# # Data table
# st.subheader("Detailed Breakdown")
# st.dataframe(
#     df.sort_values('flight_hour'),
#     use_container_width=True,
#     hide_index=True
# )