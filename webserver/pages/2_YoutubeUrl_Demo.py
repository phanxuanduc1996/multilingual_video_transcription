import os
import streamlit as st
from utils import is_youtube_url
from business_logic import transcribe_video_orchestrator

st.set_page_config(
    page_title="Youtube URL or Server local path Demo", page_icon="🔥")

st.markdown("# Youtube URL or Server local path Demo")
st.sidebar.header("Youtube URL or Server local path Demo")
st.write(
    """Please pass Youtube URL or Server local path."""
)

st.divider()

print("\n\n************** TRY 3: YOUTUBE YRL + SERVER LOCAL PATH *******************")

models = ["tiny", "base", "small", "medium", "large"]
url = st.text_input("Enter YouTube URL or Server local path:",
                    key="url")
if url:
    if os.path.exists(url) and os.path.isfile(url):
        print("LOCAL PATH: {}".format(url))
        url = os.path.abspath(url)
        st.audio(url, format="audio/wav", start_time=0)
    elif is_youtube_url(url):
        print("YOUTUBE URL: {}".format(url))
        st.video(url, format="video/mp4", start_time=0)

st.divider()

model = st.selectbox("Select Model:", models)
print("MODEL: {}".format(model))
st.caption(
    "If you take a smaller model it is faster but not as accurate, whereas a larger model is slower but more accurate.")

st.divider()

if st.button("Transcribe"):
    if url:
        transcript = transcribe_video_orchestrator(url, model)

    if transcript:
        st.subheader("Transcription:")
        st.write(transcript)
    else:
        st.error("Error occurred while transcribing.")
        st.write("Please try again.")

    print("\nTranscript: {}".format(transcript))

st.markdown('<div style="margin-top: 450px;"</div>',
            unsafe_allow_html=True)
