import streamlit as st
import sqlite3
import pandas as pd

# CONNECTING DATABASE
def get_data(query, params=None):
    conn = sqlite3.connect("uberbase.db")
    if params:
        df = pd.read_sql_query(query, conn, params=params)
    else:
        df = pd.read_sql_query(query, conn)
    conn.close()
    return df

st.set_page_config(page_title="Restaurant Data Analysis ", layout="wide")
# Sidebar for navigation
page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Restaurant Data Q&A", "Order data Q&A"]
)

#   PAGE 1

if page == "Dashboard":

    st.title("🍽️ Uber Eats Bangalore Restaurant Dashboard Page")
    st.write("#### Dynamic Restaurant Filtering Dashboard")
    st.sidebar.header("Filters")
    
    locations = get_data(
    "SELECT DISTINCT location FROM Restaurant"
     )["location"].tolist()

    selected_location = st.sidebar.selectbox("Location", [None] + locations)

    if selected_location is not None:
        restaurant_query = """
         SELECT DISTINCT restaurant_name
        FROM Restaurant
        WHERE location = ?
        """
        restaurants = get_data(restaurant_query, (selected_location,))["restaurant_name"].tolist()
    else:
        restaurants = get_data("SELECT DISTINCT restaurant_name FROM Restaurant")["restaurant_name"].tolist()

    selected_restaurant = st.sidebar.selectbox("Restaurant Name", [None] + restaurants)

    if selected_restaurant is not None :
        cuisine_query = "SELECT DISTINCT cuisines FROM Restaurant WHERE restaurant_name = ?"
        
        cuisine = get_data(cuisine_query, (selected_restaurant,))["cuisines"].tolist()
    else:
        cuisine = get_data("SELECT DISTINCT cuisines FROM Restaurant")["cuisines"].tolist()

    selected_cuisine=st.sidebar.selectbox("Cuisines",[None]+ cuisine)
    rate = st.sidebar.slider("Minimum Rating", 0.0, 5.0, 0.0)
    cost = st.sidebar.slider("Maximum Cost(for two)", 40, 6000, 6000)
    online_ordered = st.sidebar.selectbox("Online_order",[None,"Yes","No"])
    Table_booking = st.sidebar.selectbox("Book_table",[None,"Yes","No"])
    
    query = """
    SELECT * FROM Restaurant
    WHERE (location = ? OR ? IS NULL )
    AND (restaurant_name = ? OR ? IS NULL)
    AND (cuisines = ? OR ? IS NULL)
    AND rating>= ? 
    AND approx_cost_for_two_people <= ? 
    AND (online_order = ? OR ? IS NULL)
    AND (book_table = ? OR ? IS NULL)
    """

    params = [
    selected_location, selected_location,
    selected_restaurant, selected_restaurant,
    selected_cuisine,selected_cuisine,
    rate,
    cost,
    online_ordered,online_ordered,
    Table_booking,Table_booking
    ]
    df = get_data(query, params)
    st.success(f"{len(df)} results found")
    if df.empty:
        st.warning("No data found")
    else:
        df.index+=1
        st.dataframe(df)
  # PAGE 2
        
elif page == "Restaurant Data Q&A":
    st.title("📋 Restaurant Data Insights")
    queries={
        "1. Which Bangalore locations have the highest average restaurant ratings?":"""
                SELECT location, ROUND(AVG(rating),1) AS average_rating, COUNT(*) AS total_restaurants
                FROM Restaurant
                GROUP BY location
                ORDER BY average_rating DESC
                LIMIT 5;""",
        "2. Which locations are over-saturated with restaurants?":"""
                SELECT location,
                COUNT(*) AS total_restaurants
                FROM Restaurant
                GROUP BY location
                ORDER BY total_restaurants DESC
                LIMIT 10;""",
        "3. Does online ordering improve restaurant ratings?":"""
                SELECT online_order,
                ROUND(AVG(rating), 2) AS average_rating
                FROM Restaurant
                GROUP BY online_order;""",
        "4. Does table booking correlate with higher customer ratings?":"""  
                SELECT
                book_table,
                ROUND(AVG(rating), 2) AS average_rating
                FROM Restaurant
                GROUP BY book_table
                ORDER BY average_rating DESC;""",
        "5. What price range delivers the best customer satisfaction?":"""
                SELECT
                       CASE
                           WHEN approx_cost_for_two_people<=500 THEN "LOW"
                           WHEN approx_cost_for_two_people<=1000 THEN "MEDIUM"
                           WHEN approx_cost_for_two_people<=2000 THEN "HIGH"
                           ELSE "PREMIUM"
                        END AS price_range,    
                ROUND(AVG(rating),2) as average_rating,
                COUNT(*) AS total_restaurants
                FROM Restaurant
                GROUP BY price_range
                ORDER BY average_rating DESC;""",
        "6. How do low, mid, and premium-priced restaurants perform in terms of ratings?":"""
                SELECT
                    CASE
                          WHEN approx_cost_for_two_people<=500 THEN "LOW"
                          WHEN approx_cost_for_two_people<=1000 THEN "MEDIUM"
                          WHEN approx_cost_for_two_people<=2000 THEN "HIGH"
                          ELSE "PREMIUM"
                    END AS price_range,    
                ROUND(AVG(rating),2) as average_rating,
                COUNT(*) AS total_restaurants
                FROM Restaurant
                GROUP BY price_range
                ORDER BY average_rating DESC;""",
        "7. Which cuisines are most common in Bangalore?":"""
                SELECT cuisines, COUNT(*) AS total_restaurants
                FROM Restaurant
                GROUP BY cuisines
                ORDER BY total_restaurants DESC
                LIMIT 5;""",
        "8. Which cuisines receive the highest average ratings?":"""
                SELECT cuisines, AVG(rating) as average_rating
                FROM Restaurant
                GROUP BY cuisines
                ORDER BY average_rating DESC
                Limit 5;""",
        "9. Which cuisines perform well despite having fewer restaurants?":"""
                SELECT cuisines,
                ROUND(AVG(rating),2) AS average_rating,
                COUNT(*) AS total_restaurants
                FROM Restaurant
                GROUP BY cuisines
                HAVING COUNT(*) < 50
                ORDER BY average_rating DESC
                limit 10;""",
        "10. What is the relationship between restaurant cost and rating?":"""
                SELECT
                    CASE
                        WHEN approx_cost_for_two_people<=500 THEN "LOW"
                        WHEN approx_cost_for_two_people<=1000 THEN "MEDIUM"
                        WHEN approx_cost_for_two_people<=2000 THEN "HIGH"
                        ELSE "PREMIUM"
                    END AS price_range,    
                ROUND(AVG(rating),2) as average_rating,
                COUNT(*) AS total_restaurants
                FROM Restaurant
                GROUP BY price_range
                ORDER BY average_rating DESC;""",
        "11. Which locations are ideal for premium restaurant onboarding?":"""
                SELECT location,AVG(rating) AS avg_rating,
                AVG(approx_cost_for_two_people) AS avg_cost,
                COUNT(*) AS total_restaurants
                FROM Restaurant
                WHERE approx_cost_for_two_people >= 1000
                GROUP BY location
                HAVING avg_rating>=4
                ORDER BY avg_rating DESC ,avg_cost DESC
                LIMIT 10;""",
        "12. Which locations show high demand but lower average ratings?":"""
                SELECT location,ROUND(AVG(rating),2) AS avg_rating,COUNT(*) AS Total_restaurants
                FROM Restaurant
                GROUP BY location
                HAVING COUNT(*) > 50
                ORDER BY avg_rating ASC,Total_restaurants DESC;""",
        "13. Do restaurants offering both online ordering and table booking perform better?":"""
                SELECT online_order,book_table,
                ROUND(AVG(rating),2) AS avg_rating
                FROM Restaurant
                GROUP BY online_order,book_table
                ORDER BY avg_rating desc
                LIMIT 5;"""}
    selected_query = st.selectbox("**Choose a Query**",list(queries.keys()))
    query_result = get_data(queries[selected_query])
    query_result.index = query_result.index + 1
    st.write("**Query Result**")
    st.dataframe(query_result)
# PAGE 3            
elif page == "Order data Q&A":
    st.title("📋 Order Data Insights")
    queries={
        "1. Which restaurants have the highest number of orders?":"""
                SELECT restaurant_name,count(order_id) as no_of_orders
                from orders
                GROUP BY restaurant_name
                ORDER BY  no_of_orders DESC
                limit 10;""",
        "2. How does discount usage affect total order value?":"""
                SELECT discount_used,
                COUNT(order_id) AS total_orders,
                ROUND(AVG(order_value),2) AS avg_order_value,
                ROUND(SUM(order_value),2) AS total_revenue FROM orders
                GROUP BY discount_used;""",
        "3. Which payment methods are most commonly used?":"""
                SELECT payment_method,
                COUNT(order_id) AS total_orders FROM orders
                GROUP BY payment_method
                ORDER BY total_orders DESC;""",
        "4. Does payment method influence order value?":"""
                SELECT payment_method,
                COUNT(order_id) AS total_orders,
                ROUND(AVG(order_value),2) AS avg_order_value,
                ROUND(SUM(order_value)) AS total_revenue FROM orders
                GROUP BY payment_method
                ORDER BY total_revenue DESC;""",
        "5.What is the most common order value range (low, medium, high)?":"""
                SELECT
                CASE
                WHEN order_value < 600 THEN 'Low'
                WHEN order_value <= 1300 THEN 'Medium'
                ELSE 'High'
                END AS order_range,
                COUNT(*) AS total_orders
                FROM Orders
                GROUP BY order_range
                ORDER BY total_orders DESC;""",
        }
    selected_query = st.selectbox("**Choose a Query**", list(queries.keys()))
    query_result = get_data(queries[selected_query])
    query_result.index = query_result.index + 1
    st.write("**Query Result**")
    st.dataframe(query_result)         
