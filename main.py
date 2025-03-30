import streamlit as st
from streamlit_lottie import st_lottie
import requests
from datetime import datetime

# Custom CSS for modern UI
def apply_custom_css():
    st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .css-1d391kg {
        padding-top: 2rem;
    }
    .stTitle {
        font-weight: 800 !important;
        color: #1e3a8a !important;
        margin-bottom: 1.5rem !important;
    }
    .info-card {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }
    .feature-card {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
        border-left: 4px solid #4338ca;
    }
    .feature-icon {
        font-size: 24px;
        margin-right: 10px;
        color: #4338ca;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1.5rem 0;
        font-size: 0.8rem;
        color: #6b7280;
    }
    .sidebar .sidebar-content {
        background-color: #f1f5f9;
    }
    </style>
    """, unsafe_allow_html=True)

# Load Lottie animation
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Function to create a feature card
def feature_card(icon, title, description):
    st.markdown(f"""
    <div class="feature-card">
        <h3><span class="feature-icon">{icon}</span> {title}</h3>
        <p>{description}</p>
    </div>
    """, unsafe_allow_html=True)

# Function to display a counter card
def stat_counter(label, value, icon):
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown(f'<div style="font-size: 2rem; text-align: center; color: #4338ca;">{icon}</div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div style="font-size: 1.5rem; font-weight: bold;">{value}</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="color: #6b7280;">{label}</div>', unsafe_allow_html=True)

# Set the page configuration
st.set_page_config(
    page_title="Voice RAG Agent",
    page_icon="🎙️",
    layout="wide"
)

# Apply custom CSS
apply_custom_css()

# Sidebar content
with st.sidebar:
    st.image("https://your-logo-url.com/logo.png", width=200)  # Replace with your logo URL
    st.title("Navigation")
    
    selected_page = st.radio(
        "Go to:",
        ["Home", "Upload Documents", "Query Interface", "Settings"]
    )
    
    st.markdown("---")
    st.markdown("### About")
    st.info("Voice RAG Agent combines document retrieval with voice interface for a seamless experience.")
    
    # User profile section in sidebar
    st.markdown("---")
    st.markdown("### Profile")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("👤")
    with col2:
        st.markdown("**Guest User**")
        st.markdown("*Free Plan*")

# Main content based on selected page
if selected_page == "Home":
    # Main page header
    st.title("🎙️ Voice RAG Agent")
    
    # Two columns layout for animation and intro
    col1, col2 = st.columns([2, 3])
    
    with col1:
        lottie_animation = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_touohxv0.json")
        st_lottie(lottie_animation, height=300, key="welcome")
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <h2>Welcome to the Voice RAG Agent!</h2>
            <p>This advanced tool combines the power of Retrieval-Augmented Generation (RAG) with a natural voice interface, allowing you to interact with your documents in a more intuitive way.</p>
            <p>Upload your documents, ask questions, and receive accurate answers - all through a seamless voice experience.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Statistics row
    st.markdown("### System Stats")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        stat_counter("Documents Processed", "532", "📄")
    
    with col2:
        stat_counter("Queries Answered", "1,248", "❓")
    
    with col3:
        stat_counter("Users Served", "86", "👥")
    
    # Feature highlights
    st.markdown("### Key Features")
    col1, col2 = st.columns(2)
    
    with col1:
        feature_card("📚", "Document Processing", "Upload and process multiple document formats including PDFs, Word docs, and more.")
        feature_card("🔍", "Semantic Search", "Find information across your documents using natural language queries.")
    
    with col2:
        feature_card("🎤", "Voice Interface", "Interact with your documents using voice commands and receive spoken responses.")
        feature_card("🧠", "AI-Powered Answers", "Get comprehensive answers generated by advanced language models.")
    
    # Recent activity
    st.markdown("### Recent Activity")
    activity_data = [
        {"action": "Document Upload", "details": "financial_report_2023.pdf", "time": "2 hours ago"},
        {"action": "Query", "details": "What were the Q3 earnings?", "time": "1 hour ago"},
        {"action": "System Update", "details": "Voice recognition engine updated", "time": "30 minutes ago"}
    ]
    
    for item in activity_data:
        st.markdown(f"""
        <div style="display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #e5e7eb;">
            <div>
                <strong>{item['action']}</strong><br>
                {item['details']}
            </div>
            <div style="color: #6b7280; font-size: 0.9rem;">
                {item['time']}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
elif selected_page == "Upload Documents":
    st.title("📤 Upload Documents")
    
    upload_col, preview_col = st.columns([1, 1])
    
    with upload_col:
        st.markdown("""
        <div class="info-card">
            <h3>Upload your documents</h3>
            <p>Supported formats: PDF, DOCX, TXT, CSV</p>
        </div>
        """, unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader("Choose files", accept_multiple_files=True, type=['pdf', 'docx', 'txt', 'csv'])
        
        if uploaded_file:
            st.success(f"{len(uploaded_file)} file(s) uploaded successfully!")
            
            # Processing options
            st.markdown("### Processing Options")
            col1, col2 = st.columns(2)
            with col1:
                chunk_size = st.slider("Chunk Size", 100, 1000, 500)
            with col2:
                overlap = st.slider("Overlap", 0, 200, 50)
            
            embeddings_model = st.selectbox(
                "Embedding Model",
                ["OpenAI Embeddings", "HuggingFace Embeddings", "Custom Embeddings"]
            )
            
            if st.button("Process Documents", type="primary"):
                with st.spinner("Processing your documents..."):
                    # Simulate processing
                    import time
                    time.sleep(2)
                    st.success("Documents processed and indexed successfully!")
    
    with preview_col:
        st.markdown("""
        <div class="info-card">
            <h3>Document Preview</h3>
            <p>Upload a document to see preview and extraction results.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Placeholder for document preview
        st.image("https://via.placeholder.com/400x500?text=Document+Preview", use_column_width=True)

elif selected_page == "Query Interface":
    st.title("💬 Query Interface")
    
    # Query interface
    query_col, results_col = st.columns([1, 1])
    
    with query_col:
        st.markdown("""
        <div class="info-card">
            <h3>Ask a Question</h3>
            <p>Type your question or use the microphone button to speak.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Text query input
        query = st.text_input("Enter your question", placeholder="e.g., What was the revenue in Q2?")
        
        col1, col2 = st.columns([1, 3])
        with col1:
            st.button("🎤", help="Click to speak your question")
        with col2:
            st.button("Send Query", type="primary")
        
        # Advanced options
        with st.expander("Advanced Options"):
            st.slider("Response Detail Level", 1, 5, 3)
            st.checkbox("Include source citations")
            st.checkbox("Use voice response")
            st.select_slider("Voice Speed", options=["Slow", "Normal", "Fast"], value="Normal")
    
    with results_col:
        if not query:
            st.markdown("""
            <div class="info-card">
                <h3>Results will appear here</h3>
                <p>Ask a question to see AI-generated answers based on your documents.</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Placeholder animation
            lottie_waiting = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_bujdzzfn.json")  # Replace with a suitable waiting animation
            st_lottie(lottie_waiting, height=200, key="waiting")
        else:
            # Simulate response (replace with actual RAG response logic)
            st.markdown("""
            <div class="feature-card">
                <h3>Response</h3>
                <p>Based on the financial reports, the revenue for Q2 2023 was $24.5 million, representing a 12.3% increase compared to the same period last year.</p>
                <p><small>Sources: financial_report_2023.pdf (page 12), quarterly_summary.pdf (page 3)</small></p>
            </div>
            """, unsafe_allow_html=True)
            
            # Related questions
            st.markdown("### Related Questions")
            for question in ["How does this compare to Q1?", "What were the main revenue drivers?", "What is the forecast for Q3?"]:
                st.markdown(f"""
                <div style="padding: 10px; background-color: #f3f4f6; border-radius: 5px; margin-bottom: 8px; cursor: pointer;">{question}</div>
                """, unsafe_allow_html=True)

elif selected_page == "Settings":
    st.title("⚙️ Settings")
    
    tabs = st.tabs(["General", "Voice", "API Keys", "Theme"])
    
    with tabs[0]:
        st.markdown("### General Settings")
        st.toggle("Dark Mode", value=False)
        st.toggle("Save Chat History", value=True)
        st.selectbox("Default Page", ["Home", "Upload Documents", "Query Interface"])
        
    with tabs[1]:
        st.markdown("### Voice Settings")
        st.selectbox("Voice Type", ["Female (Default)", "Male", "Neutral"])
        st.select_slider("Voice Speed", options=["Very Slow", "Slow", "Normal", "Fast", "Very Fast"], value="Normal")
        st.slider("Voice Volume", 0, 100, 75)
        
    with tabs[2]:
        st.markdown("### API Keys")
        st.text_input("OpenAI API Key", type="password")
        st.text_input("HuggingFace API Key", type="password")
        st.button("Save Keys", type="primary")
        
    with tabs[3]:
        st.markdown("### Theme Settings")
        st.color_picker("Primary Color", "#4338ca")
        st.color_picker("Secondary Color", "#1e3a8a")
        st.selectbox("Font Family", ["Inter", "Roboto", "Open Sans", "Lato"])

# Footer
st.markdown("""
<div class="footer">
    <p>Voice RAG Agent v1.0.2 | Last updated: March 2025<br>
    © 2025 Your Company Name. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)