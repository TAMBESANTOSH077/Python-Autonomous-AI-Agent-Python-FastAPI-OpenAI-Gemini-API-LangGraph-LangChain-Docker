import streamlit as st
import requests
import os

st.set_page_config(
    page_title="Autonomous AI Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Autonomous AI Agent")
st.markdown(
    "Generate professional business documents using **Autonomous AI Planning, Execution, Reflection, and Word Generation**."
)

request = st.text_area(
    "Enter your request",
    height=180,
    placeholder="Example: Create a professional business proposal for an AI-powered hospital chatbot."
)

if st.button("🚀 Generate Document", use_container_width=True):

    if not request.strip():
        st.warning("Please enter a request.")
        st.stop()

    with st.spinner("🤖 AI Agent is thinking..."):

        try:
            response = requests.post(
                "http://127.0.0.1:8000/agent",
                json={"request": request},
                timeout=180
            )

            if response.status_code != 200:
                st.error(response.text)
                st.stop()

            data = response.json()

        except requests.exceptions.ConnectionError:
            st.error("❌ FastAPI server is not running.")
            st.info("Start it using:\n\n`uvicorn app:app --reload`")
            st.stop()

        except requests.exceptions.Timeout:
            st.error("⏳ Request timed out.")
            st.stop()

        except Exception as e:
            st.error(f"Unexpected Error:\n\n{e}")
            st.stop()

    st.success("✅ Document Generated Successfully!")

    st.subheader("📋 Execution Plan")

    for i, task in enumerate(data["plan"], start=1):
        st.write(f"**{i}.** {task}")

    st.divider()

    with st.expander("📄 Generated Document", expanded=True):
        st.write(data["output"])

    st.divider()

    st.success(f"📁 Word Document Saved")

    st.code(data["document"])

    if os.path.exists(data["document"]):
        with open(data["document"], "rb") as file:
            st.download_button(
                label="⬇ Download Word Document",
                data=file,
                file_name="report.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                use_container_width=True
            )



















            