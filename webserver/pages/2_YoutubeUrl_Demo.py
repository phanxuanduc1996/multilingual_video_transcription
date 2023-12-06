import os
import streamlit as st
from datetime import datetime
from utils import is_youtube_url, write_json
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
        time_now = datetime.now().strftime(r"%Y%m%d_%H_%M_%S")
        trans_output = transcribe_video_orchestrator(url, model, time_now)
        transcript = trans_output["text"]

    if transcript:
        st.subheader("Transcription:")
        st.write(transcript)
    else:
        st.error("Error occurred while transcribing.")
        st.write("Please try again.")

    print("\nTranscript: {}".format(transcript))

    log_transcript_text = open("logs/log_transcript_text.txt", "a")
    log_transcript_text.write("\n" + time_now +
                              "\t YOUTUBE_URL - \t Model: {}".format(model))
    log_transcript_text.write(transcript + "\n")
    log_transcript_text.close()

    write_json(time_now, trans_output)

st.markdown('<div style="margin-top: 450px;"</div>',
            unsafe_allow_html=True)
