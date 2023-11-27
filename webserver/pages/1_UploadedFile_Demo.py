import streamlit as st
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

models = ["tiny", "base", "small", "medium", "large"]
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
            transcript = transcribe_video_orchestrator(
                temp.name, model, time_now)

    if transcript:
        st.subheader("Transcription:")
        st.write(transcript)
    else:
        st.error("Error occurred while transcribing.")
        st.write("Please try again.")

    print("\nTranscript: {}".format(transcript))

    log_file = open("logs/log_file.txt", "a")
    log_file.write("\n" + time_now +
                   "\t UPLOADED_FILE - \t Model: {}".format(model))
    log_file.write(transcript + "\n")
    log_file.close()

st.markdown('<div style="margin-top: 450px;"</div>',
            unsafe_allow_html=True)
