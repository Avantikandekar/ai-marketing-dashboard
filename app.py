import streamlit as st

st.title("🚀 AI Marketing Dashboard")

st.markdown("Generate marketing ideas based on your brand and niche")

# Inputs
brand = st.text_input("🏢 Enter Brand Name")
niche = st.text_input("🎯 Enter Niche")

# Dummy AI function (no API needed)
def generate_ideas(brand, niche):
    return [
        f"{brand} launches a viral Instagram challenge in {niche}",
        f"Behind-the-scenes reel showing {brand}'s journey in {niche}",
        f"Influencer collaboration campaign targeting {niche} audience",
        f"User-generated content contest for {brand}",
        f"Story-based ad campaign highlighting {brand}'s impact in {niche}"
    ]

# Button logic
if st.button("✨ Generate Ideas"):
    if brand and niche:
        with st.spinner("Generating ideas..."):
            ideas = generate_ideas(brand, niche)

        st.success("Ideas Generated!")

        for idea in ideas:
            st.write("👉", idea)
    else:
        st.warning("Please enter both Brand Name and Niche")