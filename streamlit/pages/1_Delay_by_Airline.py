import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Airport Delays by Airlines",
    layout="wide"
)

st.title("Delay Analysis by Airline - Dec 2025")
st.text("Delays for Sydney Airport for the period of 1 Dec to 31 Dec 2025")

# Options
flight_direction = st.radio(
    "Flight Direction: ",
    ("All", "Departure", "Arrival"),
    index=0
)

# DATA HANDLING
conn = st.connection("postgresql", type="sql")
if flight_direction == "All":
    df = conn.query("SELECT * FROM mart_delays_by_airline_month WHERE flight_month='2025-12'")
elif flight_direction == "Arrival":
    df = conn.query("""
        SELECT * FROM mart_delays_by_airline_month 
        WHERE flight_month='2025-12'
        AND flight_direction='arrival'
    """)
elif flight_direction == "Departure":
    df = conn.query("""
        SELECT * FROM mart_delays_by_airline_month 
        WHERE flight_month='2025-12'
        AND flight_direction='departure'
    """)

average_delay = round(df['average_delay_duration_seconds'].mean())
delay_min, delay_sec = divmod(average_delay, 60)

overall = df.groupby('airline').agg({
    'total_flights': 'sum',
    'delayed_flights': 'sum',
    'delay_percentage': 'mean',
    'average_delay_duration_seconds': 'mean',
}).reset_index()
overall['minutes'], overall['seconds'] = divmod(overall['average_delay_duration_seconds'].round(), 60)
overall['avg_delay_time'] = overall.apply(lambda row: f"{int(row['minutes'])}:{int(row['seconds']):02d}", axis=1) 

# KPIs at top
col1, col2, col3, col4 = st.columns(4)
col1.metric("Toal Flights", sum(df['total_flights']))
col2.metric("Avg Delay Rate", f"{df['delay_percentage'].mean():.2f}%")
col3.metric("Avg Delay Duration", f"{delay_min:02d}:{delay_sec:02d}")
col4.metric("Worst Performer", overall.nlargest(1, 'delay_percentage')['airline'].values[0])

# Main chart: Delay percentage (sorted)
st.subheader("Delay Rate by Airline Overall")
left_col, right_col = st.columns([3, 1])
with left_col:
    fig1 = px.bar(
        overall.sort_values('delay_percentage'),
        x='delay_percentage',
        y='airline',
        orientation='h',
        color='delay_percentage',
        color_continuous_scale='RdYlGn_r',
        text='delay_percentage'
    )
    fig1.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
    st.plotly_chart(fig1, use_container_width=True)
with right_col:
    st.text("Top 5 most delayed airlines")
    st.table(
        overall.sort_values('delay_percentage', ascending=False)
            .head(5)
            .set_index('airline')
            [['delay_percentage']]
            .style.format("{:.2f}")
    )

    st.text("Top 5 least delayed airlines")
    st.table(
        overall.sort_values('delay_percentage', ascending=True)
            .head(5)
            .set_index('airline')
            [['delay_percentage']]
            .style.format("{:.2f}")
    )

# Graph 2
st.subheader("Average delay duration by Airline Overall")
left_col, right_col = st.columns([3, 1])
with left_col:
    fig1 = px.bar(
        overall.sort_values('average_delay_duration_seconds'),
        x='average_delay_duration_seconds',
        y='airline',
        orientation='h',
        color='average_delay_duration_seconds',
        color_continuous_scale='RdYlGn_r',
        text='avg_delay_time'
    )
    fig1.update_traces(texttemplate='%{text}', textposition='outside')
    st.plotly_chart(fig1, use_container_width=True)
with right_col:
    st.text("Top 5 highest average delay duration")
    st.table(
        overall.sort_values('average_delay_duration_seconds', ascending=False)
            [['airline', 'avg_delay_time']]
            .head(5)
            .set_index('airline')
    )

    st.text("Top 5 lowest delay duration")
    st.table(
        overall.sort_values('average_delay_duration_seconds', ascending=True)
            [['airline', 'avg_delay_time']]
            .head(5)
            .set_index('airline')
    )



# Data table
st.subheader("Full Table")
st.dataframe(
    overall.sort_values('delay_percentage', ascending=False),
    use_container_width=True,
    hide_index=True,
    column_config={
       "minutes": None,
       "seconds": None 
    }
)