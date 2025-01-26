import streamlit as st

st.title("Discover Your Spiritual Gifts")
st.subheader("Uncover how God has uniquely gifted you to serve!")
st.write("""
Take this fun and interactive assessment to find out your spiritual gifts and how you can use them to glorify God and serve others. 
""")
if st.button("Start the Game"):
    st.session_state.start_game = True

if "start_game" in st.session_state and st.session_state.start_game:
    st.title("Round 1: Passion Finder")
    
    st.write("Answer the following questions to uncover your interests:")
    
    with st.form("round_1"):
        q1 = st.radio("When I see someone struggling, my first instinct is to:", 
                      ["Pray for them", "Help practically", "Offer wisdom", "Gather others to assist", "Encourage them"])
        q2 = st.slider("How often do you volunteer for church-related activities?", 0, 5, 3)
        q3 = st.text_input("Describe a time you felt most fulfilled serving others:")
        
        submitted = st.form_submit_button("Submit Round 1")
    
    if submitted:
        st.session_state.round_1_responses = {"q1": q1, "q2": q2, "q3": q3}
        st.success("Round 1 Complete!")

def calculate_spiritual_gifts(responses):
    # Simplified scoring example
    scores = {
        "Mercy": 0,
        "Leadership": 0,
        "Teaching": 0,
        "Serving": 0,
        "Encouragement": 0,
    }
    if "Pray" in responses.get("q1", ""):
        scores["Mercy"] += 2
    if "Help practically" in responses.get("q1", ""):
        scores["Serving"] += 2
    # Add more scoring logic...

    return sorted(scores.items(), key=lambda x: x[1], reverse=True)

import matplotlib.pyplot as plt

if "round_1_responses" in st.session_state:
    st.title("Your Spiritual Gifts")
    
    results = calculate_spiritual_gifts(st.session_state.round_1_responses)
    top_gifts = [f"{gift[0]}: {gift[1]}" for gift in results[:3]]
    st.write("Your Top Gifts:")
    st.write("\n".join(top_gifts))
    
    # Radar Chart
    gifts = [r[0] for r in results]
    scores = [r[1] for r in results]

    fig, ax = plt.subplots()
    ax.bar(gifts, scores)
    st.pyplot(fig)

st.write("**Suggestions for using your gifts:**")
st.markdown("""
- **Mercy**: Volunteer at a local hospital or prison ministry.
- **Leadership**: Organize a church outreach event.
- **Teaching**: Lead a Bible study or mentor younger Christians.
- **Serving**: Help with setup, cleanup, or community projects.
- **Encouragement**: Write letters or messages of encouragement to others.
""")

import pandas as pd

if st.button("Save Results"):
    user_data = pd.DataFrame.from_dict([st.session_state.round_1_responses])
    user_data.to_csv("spiritual_gifts_results.csv", mode="a", index=False, header=False)
    st.success("Results saved!")
