import os
import pdb
import streamlit as st
from utils import is_youtube_url
from tempfile import NamedTemporaryFile
from business_logic import transcribe_video_orchestrator


def main():
    st.title("Automation Speech Recognition")

    models = ["tiny", "base", "small", "medium", "large"]

    st.code(
        'Please use URL / Local path or Uploaded file.')
    st.caption("If both are passed in, we will prioritize the **uploaded file**.")
    st.divider()

    url = st.text_input("Enter YouTube URL or Local path:",
                        key="url")

    uploaded_file = st.file_uploader("OR - Upload your file here:", type=[
                                     "wav", "flac", "m4a", "mp3", "wma", "aiff", "aac", "alac"], accept_multiple_files=False, key="upload")

    print("\n\n\n************** TRY *******************")
    if (uploaded_file is not None):
        st.audio(uploaded_file, format="audio/wav", start_time=0)
    elif url:
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
        if (uploaded_file is not None):
            with NamedTemporaryFile() as temp:
                temp.write(uploaded_file.getvalue())
                pdb.set_trace()

                temp.seek(0)
                transcript = transcribe_video_orchestrator(temp.name, model)
        elif url:
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


if __name__ == "__main__":
    main()
