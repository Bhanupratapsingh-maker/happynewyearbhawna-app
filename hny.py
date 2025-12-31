import streamlit as st
import requests

# Set page title and icon
st.set_page_config(page_title="Happy New Year Bhawna", page_icon="🐱")

# --- CUSTOM CSS FOR THE VIBE ---
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .letter-box {
        background-color: white;
        padding: 30px;
        border-radius: 15px;
        border-left: 5px solid #ff4b4b;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    .special-text {
        color: #ff4b4b;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.title("🎉 Happy New Year, Bhawna Singh!")
st.subheader("A small effort from your friend (and some cats)")

# --- CAT IMAGE SECTION ---
# Fetches a random cat image from a free API
def get_cat():
    try:
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        return response.json()[0]['url']
    except:
        return "https://placekitten.com/400/400" # Fallback cat

cat_url = get_cat()
st.image(cat_url, caption="Here's a random cute cat for you!", width=400)

# --- THE LETTER SECTION ---
st.markdown('<div class="letter-box">', unsafe_allow_html=True)
st.write("""
Hey Bhawna,

This is my effort to wishing you **HAPPY NEW YEAR**. 

The passed year i found you, you are my really good friend this what mutual but what is one sided you know what it is. 
This is not to impress you it just what i feel and what i like to do and i dont care if you are impressed or not. 

Everyone talk shit about you but i found you a nice human being except late replies. 
I hope that next year too we will remain good friends and our friendship will become even better. 

Last thing just letting you that i killed my expectation so i would't get hurt. 

**AGAIN Happy new year my <span class="special-text">special 1</span>.**
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.divider()
st.info("Note: Every time you refresh this page, a new cat appears just for you. 🤖🐾")
