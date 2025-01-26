import streamlit as st
import matplotlib.pyplot as plt

# Initialize session state for game progress
if 'game_started' not in st.session_state:
    st.session_state.game_started = False
if 'round' not in st.session_state:
    st.session_state.round = 1
if 'game_completed' not in st.session_state:
    st.session_state.game_completed = False
if 'user_responses' not in st.session_state:
    st.session_state.user_responses = {}

# Define the function to calculate spiritual gifts
def calculate_spiritual_gifts(user_responses):
    # Define the weights for each spiritual gift
    gifts = {
        "Mercy": 0,
        "Leadership": 0,
        "Teaching": 0,
        "Serving": 0,
        "Encouragement": 0
    }
    
    # Round 1
    if "q1" in user_responses:
        if user_responses["q1"] == "Pray for them":
            gifts["Mercy"] += 2
        elif user_responses["q1"] == "Help practically":
            gifts["Serving"] += 2
        elif user_responses["q1"] == "Offer wisdom":
            gifts["Teaching"] += 2
        elif user_responses["q1"] == "Gather others to assist":
            gifts["Leadership"] += 2
        elif user_responses["q1"] == "Encourage them":
            gifts["Encouragement"] += 2
    
    if "q2" in user_responses:
        gifts["Serving"] += user_responses["q2"]  # assuming user response is a slider value (0-5)
    
    # Round 2
    if "q1_round_2" in user_responses:
        if user_responses["q1_round_2"] == "By praying for guidance":
            gifts["Mercy"] += 2
        elif user_responses["q1_round_2"] == "By leading others to act":
            gifts["Leadership"] += 2
        elif user_responses["q1_round_2"] == "By teaching others how to handle it":
            gifts["Teaching"] += 2
        elif user_responses["q1_round_2"] == "By organizing support":
            gifts["Leadership"] += 2
        elif user_responses["q1_round_2"] == "By offering emotional support":
            gifts["Encouragement"] += 2
    
    if "q2_round_2" in user_responses:
        gifts["Teaching"] += user_responses["q2_round_2"]  # Slider for frequency of helping
    
    # Round 3
    if "q1_round_3" in user_responses:
        if user_responses["q1_round_3"] == "Mercy":
            gifts["Mercy"] += 3
        elif user_responses["q1_round_3"] == "Leadership":
            gifts["Leadership"] += 3
        elif user_responses["q1_round_3"] == "Teaching":
            gifts["Teaching"] += 3
        elif user_responses["q1_round_3"] == "Serving":
            gifts["Serving"] += 3
        elif user_responses["q1_round_3"] == "Encouragement":
            gifts["Encouragement"] += 3
    
    if "q2_round_3" in user_responses:
        gifts["Encouragement"] += user_responses["q2_round_3"]  # Slider for frequency of helping
    
    # Calculate the results by sorting the gifts based on their scores
    sorted_gifts = sorted(gifts.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_gifts

# Function to restart the game
def restart_game():
    st.session_state.game_started = False
    st.session_state.game_completed = False
    st.session_state.round = 1
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

# Game rounds
if st.session_state.game_started and not st.session_state.game_completed:
    
    if st.session_state.round == 1:
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
            st.session_state.round = 2  # Proceed to Round 2
    
    elif st.session_state.round == 2:
        st.title("Round 2: Deep Dive")
        st.write("Based on your previous answers, let's dive deeper!")

        with st.form("round_2"):
            q1 = st.radio("Which of the following best describes how you respond to challenges?", 
                        ["By praying for guidance", "By leading others to act", "By teaching others how to handle it", "By organizing support", "By offering emotional support"])
            q2 = st.slider("On a scale of 0-5, how often do you see yourself helping others?", 0, 5, 3)
            q3 = st.text_input("Describe a time when you felt especially motivated to help others:")

            submitted = st.form_submit_button("Submit Round 2")
        
        if submitted:
            st.session_state.user_responses.update({"q1_round_2": q1, "q2_round_2": q2, "q3_round_2": q3})
            st.session_state.round = 3  # Proceed to Round 3
    
    elif st.session_state.round == 3:
        st.title("Round 3: Gift Identification")
        st.write("Based on your answers, let's explore your spiritual gifts!")

        with st.form("round_3"):
            q1 = st.radio("Which gift do you feel called to develop the most?", 
                        ["Mercy", "Leadership", "Teaching", "Serving", "Encouragement"])
            q2 = st.slider("On a scale of 0-5, how often do you feel energized when helping others?", 0, 5, 3)
            q3 = st.text_input("Describe how you believe God is calling you to serve with your gifts:")

            submitted = st.form_submit_button("Submit Round 3")
        
        if submitted:
            st.session_state.user_responses.update({"q1_round_3": q1, "q2_round_3": q2, "q3_round_3": q3})
            st.session_state.game_completed = True  # Mark the game as complete

# Show results after completion
if st.session_state.game_completed:
    st.title("Your Spiritual Gifts")
    
    # Calculate and display results (mock logic here)
    results = calculate_spiritual_gifts(st.session_state.user_responses)  # Now this function exists
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

    # Restart button
if st.button('Restart Game'):
    st.session_state.clear()  # Clear all session state (optional, if you want to reset everything)
    st.rerun()  # Reload the app to restart the game
