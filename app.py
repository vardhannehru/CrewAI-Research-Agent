import os
import re
import subprocess
import sys
import streamlit as st
import streamlit.components.v1 as components


def clean_ansi(text: str) -> str:
    """Removes terminal color codes like [33m from the text."""
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
    return ansi_escape.sub("", text)


# Streamlit Page Setup
st.set_page_config(
    page_title="AI Daily Newsletter Dashboard", page_icon="📰", layout="wide"
)

st.title("📰 AI Daily Newsletter Dashboard")
st.write("Watch your CrewAI team research, verify, and write in real-time.")

# Sidebar Controls
with st.sidebar:
    st.header("⚡ Agent Controls")
    st.info("Brain: Claude Haiku 5.5\n\nFramework: CrewAI")
    start_btn = st.button("🚀 Run Newsletter Crew", type="primary")

if start_btn:
    with st.status(
        "🤖 AI Agents are actively researching...", expanded=True
    ) as status:
        st.write("### 📡 Live Agent Activity Log:")
        log_placeholder = st.empty()
        logs = []

        # Tell the child process to strictly use UTF-8
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"

        process = subprocess.Popen(
            [sys.executable, "-u", "main.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
            env=env,  # <--- Pass the UTF-8 environment here
        )

        # Stream output line-by-line to the webpage
        for line in iter(process.stdout.readline, ""):
            cleaned_line = clean_ansi(line)
            if cleaned_line.strip():
                logs.append(cleaned_line)
                log_placeholder.code("".join(logs[-20:]), language="plaintext")

        process.stdout.close()
        return_code = process.wait()

        if return_code == 0:
            status.update(
                label="✅ Newsletter Generated Successfully!",
                state="complete",
                expanded=False,
            )
        else:
            status.update(label="❌ Agent process failed", state="error")

    # Display the final styled HTML newsletter inside the dashboard
    html_file_path = os.path.join("output", "newsletter.html")
    if os.path.exists(html_file_path):
        st.subheader("📰 Today's AI Newsletter")
        with open(html_file_path, "r", encoding="utf-8") as f:
            html_content = f.read()

        components.html(html_content, height=800, scrolling=True)
    else:
        st.warning("No newsletter file was found in output/.")