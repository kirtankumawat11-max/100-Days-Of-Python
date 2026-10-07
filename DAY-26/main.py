import pandas as pd
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="NATO Phonetic Alphabet",
    page_icon="🔤"
)

# Custom styling
st.markdown("""
<style>
    .stApp {
        background-color: #F7F1E3;
        color: #000000;
    }

    h1, h2, h3, p, label {
        color: #000000 !important;
    }

    .stTextInput label {
        color: #000000 !important;
    }

    .stTextInput input {
        background-color: #FFFDF7;
        color: #000000;
        border: 1px solid #000000;
    }

    .stTextInput input::placeholder {
        color: #555555;
    }
</style>
""", unsafe_allow_html=True)

# Load NATO phonetic alphabet
data = pd.read_csv("nato_phonetic_alphabet.csv")

# Create phonetic dictionary
phonetic_dict = {
    row.letter: row.code
    for _, row in data.iterrows()
}

# App
st.title("🔤 NATO Phonetic Alphabet")
st.write("Convert any word into its NATO phonetic alphabet.")

word = st.text_input("Enter a word:")

if word:
    try:
        output_list = [phonetic_dict[letter] for letter in word.upper()]

        st.subheader("Phonetic Code")
        st.write(" → ".join(output_list))

    except KeyError:
        st.error("Please enter letters from A-Z only.")