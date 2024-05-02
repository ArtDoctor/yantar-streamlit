import streamlit as st
import requests
import json

# Set up the page configuration
st.set_page_config(page_title="Yantar Demo App", layout="wide")

# Title of the application
st.title("Ads retrieval demo app")

# Input field for the URL
url = "https://backend.yantar.yazero.io/api/get-ads"

# Input field for the user to enter text
user_input = st.text_area("Enter your text here - you will get ads relevant to this text:")


def display_ads_data(ads_data):
    # Check if the data contains success key and it's true
    if ads_data.get("success", False):
        # Display each ad in a well-structured format
        for ad in ads_data["data"]:
            st.write("#### ID:", ad["id"])
            st.write("**One-liner:**", ad["one_liner"])
            st.markdown("**Link:** [{}]({})".format(ad["cta"], ad["link"]), unsafe_allow_html=True)
            # st.write("**Call to Action:**", ad["cta"])
            st.write("**Similarity Score:** {:.3f}".format(ad["similarity"]))
            st.write("---")  # Adding a line for separation between entries
    else:
        st.error("Failed to retrieve ads data.")

# Submit button
if st.button("Get Ads"):
    if url and user_input:
        try:
            # Convert user input to JSON format (assuming JSON is expected by the API)
            payload = {
                "text": user_input,
                "api_key": "uSTaNAOa67",
                "amount_of_ads": 4
            }
            # Send POST request
            response = requests.post(url, json=payload)
            
            # Check if the request was successful
            if response.status_code == 200:
                # Try to parse JSON response
                response_data = response.json()
                st.success("POST request successful!")
                
                # Display the custom structure
                # st.write("### Response Data", response_data)
                display_ads_data(response_data)


                # Example of accessing structured data
                # st.write("#### Details")
                # st.write("Status Code:", response.status_code)
                # st.write("Response Body:", response.text)
                
            else:
                st.error(f"Failed to send POST request. Status code: {response.status_code}")
        
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please provide a valid URL and input data.")
