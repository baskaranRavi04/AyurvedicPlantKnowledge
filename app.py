
import streamlit as st

st.set_page_config(
    page_title="Ayurvedic Plant Knowledge System",
    page_icon="🌿",
    layout="wide"
)

plants = {
    "Tulsi": {
        "scientific": "Ocimum tenuiflorum",
        "category": "Herb",
        "description": "Tulsi is a sacred plant widely grown in Indian households.",
        "uses": "Traditionally used in Indian household remedies and valued in Ayurveda.",
        "precaution": "May interact with medicines. Consult a healthcare professional before medicinal use."
    },
    "Neem": {
        "scientific": "Azadirachta indica",
        "category": "Tree",
        "description": "Neem is a tree known for its importance in traditional Indian practices.",
        "uses": "Traditionally used in skin-care preparations and personal hygiene.",
        "precaution": "Neem oil can be toxic if swallowed. Avoid self-medication."
    },
    "Turmeric": {
        "scientific": "Curcuma longa",
        "category": "Spice",
        "description": "Turmeric is a golden-yellow rhizome used in Indian cooking and traditions.",
        "uses": "Traditionally used as a culinary spice and in skin-care preparations.",
        "precaution": "Concentrated supplements may interact with medicines and may not suit everyone."
    },
    "Aloe Vera": {
        "scientific": "Aloe vera",
        "category": "Succulent",
        "description": "Aloe vera is a succulent plant with thick, water-storing leaves.",
        "uses": "The clear inner gel is commonly used in topical skin-care products.",
        "precaution": "Topical products may irritate some skin. Do not ingest aloe latex."
    },
    "Amla": {
        "scientific": "Phyllanthus emblica",
        "category": "Fruit",
        "description": "Amla is an Indian fruit known for its sour taste.",
        "uses": "Traditionally valued as food and used in Ayurvedic preparations.",
        "precaution": "Concentrated preparations may interact with medicines; seek professional advice."
    },
    "Ginger": {
        "scientific": "Zingiber officinale",
        "category": "Spice",
        "description": "Ginger is an aromatic rhizome used in Indian food and traditional practices.",
        "uses": "Traditionally used in food and household preparations for digestive comfort.",
        "precaution": "Large amounts may cause discomfort or interact with certain medicines."
    },
    "Ashwagandha": {
        "scientific": "Withania somnifera",
        "category": "Herb",
        "description": "Ashwagandha is a plant used in several Ayurvedic traditions.",
        "uses": "Traditionally described in Ayurveda as a rejuvenating herb.",
        "precaution": "It may affect the liver, thyroid, and medicines. Avoid during pregnancy and seek medical advice."
    },
    "Brahmi": {
        "scientific": "Bacopa monnieri",
        "category": "Herb",
        "description": "Brahmi is a creeping herb associated with traditional Indian knowledge.",
        "uses": "Traditionally used in preparations associated with learning and memory.",
        "precaution": "Evidence and safety vary by preparation. Consult a healthcare professional."
    }
}

st.title("🌿 Ayurvedic Plant Knowledge System")
st.write("Discover India's Traditional Medicinal Plant Knowledge")

st.sidebar.title("🌱 Navigation")
page = st.sidebar.radio(
    "Choose a page",
    ["Home", "Plant Explorer", "Plant Search", "About IKS"]
)

if page == "Home":
    st.header("Welcome!")
    st.write(
        "Explore traditional Indian knowledge about plants, "
        "their cultural importance, and their traditional uses."
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Plants in Database", len(plants))
    col2.metric("Plant Categories", len(set(p["category"] for p in plants.values())))
    col3.metric("Knowledge Tradition", "Ayurveda")

    st.info("Select Plant Explorer or Plant Search from the sidebar.")

elif page == "Plant Explorer":
    st.header("🌱 Plant Explorer")

    category = st.selectbox(
        "Filter by category",
        ["All"] + sorted(set(p["category"] for p in plants.values()))
    )

    for name, details in plants.items():
        if category == "All" or details["category"] == category:
            with st.expander(name):
                st.write("**Scientific name:**", details["scientific"])
                st.write("**Category:**", details["category"])
                st.write("**Description:**", details["description"])
                st.write("**Traditional uses:**", details["uses"])
                st.warning("Safety: " + details["precaution"])

elif page == "Plant Search":
    st.header("🔍 Search for a Plant")
    query = st.text_input("Enter a plant name")

    if query:
        matches = [
            (name, details)
            for name, details in plants.items()
            if query.lower() in name.lower()
            or query.lower() in details["scientific"].lower()
        ]

        if matches:
            for name, details in matches:
                st.subheader(name)
                st.write("**Scientific name:**", details["scientific"])
                st.write(details["description"])
                st.write("**Traditional uses:**", details["uses"])
                st.warning("Safety: " + details["precaution"])
        else:
            st.info("No matching plant found. Try another name.")

elif page == "About IKS":
    st.header("🇮🇳 Indian Knowledge Systems")
    st.write(
        "Indian Knowledge Systems include knowledge developed "
        "and passed down through India's diverse intellectual, "
        "cultural, and practical traditions."
    )
    st.write(
        "Ayurveda is one such traditional knowledge system. "
        "This project introduces selected plants and their "
        "traditional context for educational purposes."
    )

st.markdown("---")
st.caption("Indian Knowledge Systems (IKS) Project")
st.caption(
    "Educational information only. Traditional uses do not "
    "establish medical effectiveness. Not medical advice."
)
