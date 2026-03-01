import streamlit as st
import pyperclip

# heading information
st.title("Text Format Tool")
st.caption("created by Arin S for the Alabama Regional Tech Fair")

col1, col2 = st.columns(2, gap="small")
# text column
with col1:
    st.markdown("This tool will help you format text in a varity of ways. Please type or paste your text inside of the box, and choose how to format it using the options below!")
# text box
with col2:
    original_text = st.text_area(":grey[Place your text here]", value="The quick brown fox jumped over the lazy dog.")

st.divider()

# keeping the final text for each session
if 'final' not in st.session_state:
    st.session_state['final'] = original_text

# formattiang functions
def copy_text():
    pyperclip.copy(st.session_state.final)

def upper_text():
    return st.session_state.final.upper()

def lower_text():
    return st.session_state.final.lower()

def find_and_replace(find, replace):
    return st.session_state.final.replace(find, replace)

# buttons and output
buttons, output = st.columns(2, gap="small")

with buttons:
    st.caption("Modifcation Options")

    with st.popover("Casing"):
        upper = st.button("Uppercase")
        if (upper):
            st.session_state.final = upper_text()
        lower = st.button("Lowercase")
        if (lower):
            st.session_state.final = lower_text()
    
    with st.popover("Find and Replace"):
        find_text = st.text_input("Find")
        replace_text = st.text_input("Replace")
        far = st.button("Find and Replace")
        if (far):
            st.session_state.final = find_and_replace(find_text, replace_text)

    copy = st.button("Copy to clipboard")
    if (copy) :
        copy_text()

    reset = st.button("Reset changes")
    if (reset):
        st.session_state.final = original_text

with output:
    st.text_area(":grey[Output text]", value=st.session_state.final)


