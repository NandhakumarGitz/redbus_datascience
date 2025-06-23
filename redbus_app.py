import streamlit as st
import pandas as pd
import pymysql

# Function to connect to MySQL database
def get_connection():
    return pymysql.connect(host='localhost', user='root', passwd='1234', database='redbuses')

# Function to fetch distinct locations
def fetch_locations(connection):
    query = "SELECT DISTINCT Location FROM bus_routes ORDER BY Location"
    return pd.read_sql(query, connection)['Location'].tolist()

# Function to fetch routes based on selected location
def fetch_route_names(connection, location):
    query = "SELECT DISTINCT Route_Name FROM bus_routes WHERE Location = %s ORDER BY Route_Name"
    return pd.read_sql(query, connection, params=[location])['Route_Name'].tolist()

# Function to fetch data based on selected Route_Name
def fetch_data(connection, route_name):
    query = "SELECT * FROM bus_routes WHERE Route_Name = %s ORDER BY Star_Rating DESC, Price ASC"
    df = pd.read_sql(query, connection, params=[route_name])

    # Convert "Price" column to numeric
    df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

    return df

# Function to filter data based on Star Rating, Bus Type, and Price Range
def filter_data(df, star_ratings, bus_types, price_range):
    if star_ratings:
        df = df[df['Star_Rating'].isin(star_ratings)]
    if bus_types:
        df = df[df['Bus_Type'].isin(bus_types)]
    if price_range != "All":
        if price_range == "Low (Below 500)":
            df = df[df['Price'] < 500]
        elif price_range == "Medium (500 - 1000)":
            df = df[(df['Price'] >= 500) & (df['Price'] <= 1000)]
        elif price_range == "High (Above 1000)":
            df = df[df['Price'] > 1000]
    return df

# Streamlit UI
st.title("Red Bus Okk - Bus Search")

# Get MySQL connection
conn = get_connection()

# Fetch all unique locations
location_options = fetch_locations(conn)

# Select Location
selected_location = st.sidebar.selectbox("Select Location", location_options)

# Fetch available routes for selected location
if selected_location:
    route_names = fetch_route_names(conn, selected_location)
    selected_route = st.sidebar.selectbox("Select Route Name", route_names)

    # Fetch data for selected route
    if selected_route:
        df = fetch_data(conn, selected_route)

        # Filters for Star Rating & Bus Type
        star_ratings = st.sidebar.multiselect("Select Star Rating", sorted(df['Star_Rating'].unique()))
        bus_types = st.sidebar.multiselect("Select Bus Type", sorted(df['Bus_Type'].unique()))

        # Price Filter Selectbox
        price_options = ["All", "Low (Below 500)", "Medium (500 - 1000)", "High (Above 1000)"]
        selected_price_range = st.sidebar.selectbox("Select Price Range", price_options)

        # Apply filters
        df = filter_data(df, star_ratings, bus_types, selected_price_range)

        # Display results
        st.write(f"Showing results for **{selected_route}** from **{selected_location}**")
        st.dataframe(df)

# Close connection
conn.close()
