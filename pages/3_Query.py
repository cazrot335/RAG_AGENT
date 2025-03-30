import streamlit as st
from main import process_query
import asyncio

st.title("🔍 Query Interface")

query = st.text_input("Ask a question about the uploaded documents:")

if query:
    with st.spinner("Processing your query..."):
        try:
            result = asyncio.run(process_query(
                query,
                st.session_state["client"],
                st.session_state["embedding_model"],
                "voice-rag-agent",
                st.session_state.get("openai_api_key", ""),
                st.session_state.get("selected_voice", "coral")
            ))

            if result["status"] == "success":
                st.markdown("### Response:")
                st.write(result["text_response"])

                if "audio_path" in result:
                    st.markdown("### 🔊 Audio Response")
                    st.audio(result["audio_path"], format="audio/mp3")
            else:
                st.error(f"Error: {result.get('error', 'Unknown error occurred')}")
        except Exception as e:
            st.error(f"Error processing query: {str(e)}")