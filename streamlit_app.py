import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="Spam Detector",
    page_icon="🛡️",
    layout="centered"
)


st.title("🛡️ Spam Detector")
st.caption("Powered by Multinomial Naive Bayes")

st.divider()


message = st.text_area(
    "Type or paste your message:",
    placeholder="e.g. Congratulations! You won a free prize. Click here now!",
    height=150
)


col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    check = st.button(
        "🔍 Check Message",
        use_container_width=True
    )


if check:

    if not message.strip():
        st.warning("Please enter a message first!")

    else:

        # Data that will be sent to FastAPI
        data = {
            "Text": message
        }

        try:

            # Send request to FastAPI
            response = requests.post(
                f"{API_URL}/predict",
                json=data
            )

            # If API request was successful
            if response.status_code == 200:

                result = response.json()

                target = result["Target"]
                probability = result["Probability"]

                if target == "spam":

                    st.error("🚨 SPAM detected!")

                    st.metric(
                        "Spam probability",
                        f"{probability * 100:.1f}%"
                    )

                else:

                    st.success("✅ Legitimate message (Ham)")

                    st.metric(
                        "Ham probability",
                        f"{probability * 100:.1f}%"
                    )

            else:

                st.error(
                    f"API request failed: {response.status_code}"
                )

        except requests.exceptions.ConnectionError:

            st.error(
                "Could not connect to FastAPI. "
                "Make sure the API server is running."
            )


st.divider()


with st.expander("ℹ️ Model info"):

    st.write("**Model:** Multinomial Naive Bayes (sklearn)")
    st.write("**Vectorizer:** CountVectorizer")
    st.write("**Classes:** spam / ham")
