import streamlit as st
import matplotlib.pyplot as plt

# Initialize session state for game progress
if 'game_started' not in st.session_state:
    st.session_state.game_started = False
if 'game_completed' not in st.session_state:
    st.session_state.game_completed = False
if 'user_responses' not in st.session_state:
    st.session_state.user_responses = {}

# Welcome screen
if not st.session_state.game_started:
    st.title("Discover Your Spiritual Gifts")
    st.subheader("Uncover how God has uniquely gifted you to serve!")
    st.write("""
    Take this fun and interactive assessment to find out your spiritual gifts and how you can use them to glorify God and serve others.
    """)
    
    if st.button("Start the Game"):
        st.session_state.game_started = True

# Game questions and responses
if st.session_state.game_started and not st.session_state.game_completed:
    st.title("Round 1: Passion Finder")
    
    st.write("Answer the following questions to uncover your interests:")

    with st.form("round_1"):
        q1 = st.radio("When I see someone struggling, my first instinct is:", 
                     ["Pray for them", "Help practically", "Offer wisdom", "Gather others to assist", "Encourage them"])
        q2 = st.slider("How often do you volunteer for church-related activities?", 0, 5, 3)
        q3 = st.text_input("Describe a time you felt most fulfilled serving others:")
        
        submitted = st.form_submit_button("Submit Round 1")
    
    if submitted:
        st.session_state.user_responses = {"q1": q1, "q2": q2, "q3": q3}
        st.session_state.game_completed = True  # Mark the game as complete

# Show results after completion
if st.session_state.game_completed:
    st.title("Your Spiritual Gifts")
    
    # Calculate and display results (mock logic here)
    results = calculate_spiritual_gifts(st.session_state.user_responses)  # Define this function to calculate gifts
    top_gifts = [f"{gift[0]}: {gift[1]}" for gift in results[:3]]
    st.write("Your Top Gifts:")
    st.write("\n".join(top_gifts))
    
    # Radar Chart (matplotlib example)
    gifts = [r[0] for r in results]
    scores = [r[1] for r in results]
    fig, ax = plt.subplots()
    ax.bar(gifts, scores)
    st.pyplot(fig)

    # Show suggestions based on top gifts
    st.write("**Suggestions for using your gifts:**")
    st.markdown("""
    - **Mercy**: Volunteer at a local hospital or prison ministry.
    - **Leadership**: Organize a church outreach event.
    - **Teaching**: Lead a Bible study or mentor younger Christians.
    - **Serving**: Help with setup, cleanup, or community projects.
    - **Encouragement**: Write letters or messages of encouragement to others.
    """)

    # Option to save results or email
    if st.button("Save Results"):
        st.write("Results have been saved successfully!")
