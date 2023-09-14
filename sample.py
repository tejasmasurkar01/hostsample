import streamlit as st
st.title("Movie Ticket Booking System")

# User Input Fields
name = st.text_input("Name")
email = st.text_input("Email")
phone = st.text_input("Phone")

# Movie and Showtime Selection
movie_choice = st.selectbox("Select Movie", ["Movie A", "Movie B", "Movie C"])
showtime_choice = st.selectbox("Select Showtime", ["10:00 AM", "2:00 PM", "7:00 PM"])

# Seat Selection
available_seats = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
selected_seats = st.multiselect("Select Seats", available_seats)

# Payment Options
payment_option = st.radio("Payment Option", ["Credit Card", "PayPal", "Cash"])
agree_terms = st.checkbox("I agree to the terms and conditions")

if st.button("Book Tickets"):
    if not name:
        st.error("Please enter your name")
    elif not email:
        st.error("Please enter your email")
    elif not phone:
        st.error("Please enter your phone number")
    elif not selected_seats:
        st.error("Please select at least one seat")
    elif not agree_terms:
        st.error("Please agree to the terms and conditions")