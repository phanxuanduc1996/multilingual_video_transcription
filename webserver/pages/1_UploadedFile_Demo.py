import streamlit as st
from utils import write_json
from datetime import datetime
from tempfile import NamedTemporaryFile
from business_logic import transcribe_video_orchestrator

st.set_page_config(page_title="Uploaded File Demo", page_icon="🤖")

st.markdown("# Uploaded File Demo")
st.sidebar.header("Uploaded File Demo")
st.write(
    """Please upload an audio file."""
)

st.divider()

print("\n\n************** TRY 2: UPLOADED FILE *******************")

models = ["tiny", "base", "small", "medium",
          "large", "large-v2"]  # , "large-v3"
uploaded_file = st.file_uploader("Upload your file here:", type=[
    "wav", "flac", "m4a", "mp3", "wma", "aiff", "aac", "alac"], accept_multiple_files=False)

if (uploaded_file is not None):
    st.audio(uploaded_file, format="audio/wav", start_time=0)

st.divider()

model = st.selectbox("Select Model:", models)
print("MODEL: {}".format(model))
st.caption(
    "If you take a smaller model it is faster but not as accurate, whereas a larger model is slower but more accurate.")

st.divider()

if st.button("Transcribe"):
    if (uploaded_file is not None):
        time_now = datetime.now().strftime(r"%Y%m%d_%H_%M_%S")

        with NamedTemporaryFile(suffix=".wav") as temp:
            temp.write(uploaded_file.getvalue())

            temp.seek(0)
            trans_output = transcribe_video_orchestrator(
                temp.name, model, time_now)

            print("\n\n\n--------------------------")
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
                              "\t UPLOADED_FILE - \t Model: {}".format(model))
    log_transcript_text.write(transcript + "\n")
    log_transcript_text.close()

    write_json(time_now, trans_output)

st.markdown('<div style="margin-top: 450px;"</div>',
            unsafe_allow_html=True)
