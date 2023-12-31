import numpy as np
import streamlit as st
from st_audiorec import st_audiorec
from tempfile import NamedTemporaryFile
from business_logic import transcribe_video_orchestrator

st.set_page_config(page_title="Streaming Demo")

st.markdown("# Streaming Demo")
st.sidebar.header("Streaming Demo")
st.write(
    """Please speak into the microphone."""
)

st.divider()

model = "small"
wav_audio_data = st_audiorec()

print("\n\n************** TRY 1: STREAMING DEMO *******************")
if wav_audio_data is not None:
    st.audio(wav_audio_data, format='audio/wav', start_time=0)

    st.divider()

    # float_data = np.frombuffer(wav_audio_data, np.int16).flatten().astype(np.float32) / 32768.0
    # transcript = transcribe_video_streaming(float_data, model)

    with NamedTemporaryFile() as temp:
        temp.write(wav_audio_data)
        temp.seek(0)
        transcript = transcribe_video_orchestrator(temp.name, model)

    if transcript or transcript == "":
        st.subheader("Transcription:")
        st.write(transcript)
    else:
        st.error("Error occurred while transcribing.")
        st.write("Please try again.")

    print("MODEL: {}".format(model))
    print("\nTranscript: {}".format(transcript))

st.markdown('<div style="margin-top: 450px;"</div>',
            unsafe_allow_html=True)