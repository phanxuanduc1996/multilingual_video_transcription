import streamlit as st
# import noisereduce as nr
from datetime import datetime
from st_audiorec import st_audiorec
from tempfile import NamedTemporaryFile
from business_logic import transcribe_video_orchestrator

st.set_page_config(page_title="Streaming Demo", page_icon="🏠")

st.markdown("# Streaming Demo")
st.sidebar.header("Streaming Demo")
st.write(
    """Please speak into the microphone."""
)

st.divider()

print("\n\n************** TRY 1: STREAMING DEMO *******************")

models = ["tiny", "base", "small", "medium", "large"]

wav_audio_data = st_audiorec()
if wav_audio_data is not None:
    time_now = datetime.now().strftime(r"%Y%m%d_%H_%M_%S")

    # st.audio(wav_audio_data, format='audio/wav', start_time=0)

    st.divider()

    # model = st.selectbox("Select Model:", models)
    # print("MODEL: {}".format(model))
    # st.caption(
    #     "If you take a smaller model it is faster but not as accurate, whereas a larger model is slower but more accurate.")
    # st.divider()

    model = "large"
    with NamedTemporaryFile(suffix=".wav") as temp:  # , delete=False
        temp.write(wav_audio_data)
        temp.seek(0)
        print("\n\ntemp.name: ", temp.name)
        transcript = transcribe_video_orchestrator(temp.name, model, time_now)

    if transcript or transcript == "":
        st.subheader("Transcription:")
        st.write(transcript)
    else:
        st.error("Error occurred while transcribing.")
        st.write("Please try again.")

    print("MODEL: {}".format(model))
    print("\nTranscript: {}".format(transcript))

    log_file = open("logs/log_file.txt", "a")
    log_file.write("\n" + time_now +
                   "\t STREAMING - \t Model: {}".format(model))
    log_file.write(transcript + "\n")
    log_file.close()

st.markdown('<div style="margin-top: 450px;"</div>',
            unsafe_allow_html=True)
