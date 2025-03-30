import streamlit as st
from main import process_pdf, store_embeddings, setup_qdrant

st.title("📄 Upload Documents")

uploaded_file = st.file_uploader("Upload a PDF document", type=["pdf"])

if uploaded_file:
    with st.spinner("Processing your document..."):
        try:
            # Setup Qdrant if not already done
            if not st.session_state.get("client"):
                client, embedding_model = setup_qdrant()
                st.session_state["client"] = client
                st.session_state["embedding_model"] = embedding_model

            # Process and store document
            documents = process_pdf(uploaded_file)
            if documents:
                store_embeddings(
                    st.session_state["client"],
                    st.session_state["embedding_model"],
                    documents,
                    "voice-rag-agent"
                )
                st.success("✅ Document processed and stored successfully!")
        except Exception as e:
            st.error(f"Error processing document: {str(e)}")