import streamlit as st
import requests

st.title("Currency Converter")

# Input fields
amount = st.number_input("Enter amount:", min_value=0.01, format="%.2f")
from_currency = st.text_input("From currency (e.g., USD)").upper()
to_currency = st.text_input("To currency (e.g., INR)").upper()

# Conversion function
def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
    response = requests.get(url)

    if response.status_code != 200:
        return None, "❌ Error: Check your currency codes or internet connection."

    data = response.json()
    try:
        result = data['rates'][to_currency]
        return result, None
    except KeyError:
        return None, "❌ Error: Invalid currency code."

#Button to convert
if st.button("Convert"):
    if not from_currency or not to_currency:
        st.warning("Please enter both currency codes.")
    else:
        result, error = convert_currency(amount, from_currency, to_currency)
        if error:
            st.error(error)
        else:
            st.success(f"{amount} {from_currency} = {result:.2f} {to_currency}")
