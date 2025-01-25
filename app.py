import streamlit as st
from src.api import robinhood

st.markdown(
    """
    <style>
    .stApp {
      background: linear-gradient(-45deg, #d6e97a, #f8f9fa, #d6e97a, #e0e0e0);
      background-size: 400% 400%;
      animation: gradientBG 15s ease infinite;
    }
    @keyframes gradientBG {
      0% {background-position: 0% 50%;}
      50% {background-position: 100% 50%;}
      100% {background-position: 0% 50%;}
    }
    h1, h2, h3, h4, h5, h6 {
      color: #FFC107 !important;
      text-shadow: 1px 1px 4px #44444422;
    }
    /* Amber buttons */
    button[kind="primary"], .stButton>button {
      background-color: #FFC107 !important;
      color: #222 !important;
      border: none !important;
      font-weight: bold;
    }
    .stButton>button:hover {
      background-color: #ffb300 !important;
      color: #111 !important;
    }
    input[type="text"], input[type="number"] {
  background-color: #FFF8E1 !important;  /* light amber background */
  color: #FFC107 !important;             /* amber text */
  border: 2px solid #FFC107 !important;  /* amber border */
  font-weight: bold;
}
    </style>
    """,
    unsafe_allow_html=True
)
st.title("Robinhood Trading Bot")

if st.button("Login"):
    robinhood.login_to_robinhood()
    st.success("Logged in successfully!")

if st.button("Show Account Info"):
    st.write(robinhood.get_account_info())

if st.button("Show Portfolio"):
    st.write(robinhood.get_portfolio_stocks())

st.header("Trade")
symbol = st.text_input("Symbol", "AAPL")
quantity = st.number_input("Quantity", min_value=1, value=1)

col1, col2 = st.columns(2)
with col1:
    if st.button("Buy"):
        st.write(robinhood.buy_stock(symbol, quantity))
with col2:
    if st.button("Sell"):
        st.write(robinhood.sell_stock(symbol, quantity))

if st.button("Show Watchlist"):
    st.write(robinhood.get_watchlist_stocks("My Watchlist"))

if st.button("Show Ratings"):
    st.write(robinhood.get_ratings(symbol))

if st.button("Show Historical Data"):
    st.write(robinhood.get_historical_data(symbol))