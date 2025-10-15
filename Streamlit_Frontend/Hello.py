import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Diet Recommendation System",
    page_icon="🥗",
    layout="wide"
)

# Custom CSS styling for a cleaner look
st.markdown("""
    <style>
        .main {
            background-color: #f4f6f8;
            padding: 2rem;
        }
        h1 {
            color: #2c3e50;
        }
        .sidebar .sidebar-content {
            background-color: #dff0ea;
        }
        .st-emotion-cache-1v0mbdj {
            padding-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Title section
st.markdown("<h1 style='text-align: center;'>🥗 Welcome to the Diet Recommendation System! 👋</h1>", unsafe_allow_html=True)

# Sidebar message
st.sidebar.title("Navigation")
st.sidebar.success("Select a recommendation app.")

# App description
st.markdown("---")
st.markdown("""
### 🌟 About the Project  
This web app provides personalized **diet recommendations** based on user preferences and nutritional needs.

Built with:
- `Scikit-Learn` for machine learning
- `FastAPI` for backend API
- `Streamlit` for frontend

> Our goal is to make healthy eating easier and more accessible!
""")

# Optional call-to-action or start button
if st.button("Get Started"):
    st.success("Navigate from the sidebar to try out the recommendations!")

