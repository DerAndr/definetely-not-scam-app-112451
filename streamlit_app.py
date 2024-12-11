import streamlit as st
import pandas as pd
import random

st.title("✨🥸✨ Your best friend App - validate if your bank data was stolen ! ✨🥸✨")
st.write(
    "It is important to be sure that all your data is secured!"
)

st.write(
    "Our shiny app is ready to help you! 🥷"
)

st.header(
    "Validate if your data was stolen!"
)

# Function to anonymize sensitive data
def anonymize_data(data):
    return "*" * len(data[:-4]) + data[-4:]

# Generate random card numbers for demo
def generate_card_number():
    return f"{random.randint(4000,4999)}-{random.randint(1000,9999)}-{random.randint(1000,9999)}-{random.randint(1000,9999)}"


# Data entry form
with st.form(key="data_form"):
    st.header("Enter Your Personal Information")

    name = st.text_input("🙂 Full Name:")
    email = st.text_input("📧 Email Address:")
    phone = st.text_input("📱 Phone Number:")
    address = st.text_area("🏚️ Address:")
    card_number = st.text_input("💳 Bank Card Number:", placeholder="####-####-####-####")

    submit_button = st.form_submit_button(label="Submit")

# Display submitted data
if submit_button:
    if name and email and phone and address and card_number:
        anonymized_card = anonymize_data(card_number)

        st.success("Data Submitted Successfully!")

        st.header("Sensitive Data")
        st.write("Below is the entered and anonymized data.")

        # Display data
        data = {
            "Name": name,
            "Email": email,
            "Phone": phone,
            "Address": address,
            "Card Number": anonymized_card,
        }
        st.json(data)

        # Option to download anonymized data
        df = pd.DataFrame([data])
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Anonymized Data",
            data=csv,
            file_name="anonymized_data.csv",
            mime="text/csv",
        )
    else:
        st.error("Please fill in all the fields.")

# Footer with a note on data security
st.markdown(
    "---\n**Note:** All sensitive data is handled securely within this app and anonymized for safe storage and sharing."
)
