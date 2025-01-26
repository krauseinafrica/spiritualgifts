import streamlit as st

st.title("Discover Your Spiritual Gifts")
st.subheader("Uncover how God has uniquely gifted you to serve!")
st.write("""
Take this fun and interactive assessment to find out your spiritual gifts and how you can use them to glorify God and serve others. 
""")
if st.button("Start the Game"):
    st.session_state.start_game = True
