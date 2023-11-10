import pdb
import numpy as np
import streamlit as st
from st_audiorec import st_audiorec
from tempfile import NamedTemporaryFile
from business_logic import transcribe_video_streaming, transcribe_video_orchestrator


def main():
    st.title("Automation Speech Recognition")
    st.code(
        'Please speak into the microphone.')

    model = "small"
    wav_audio_data = st_audiorec()

    print("\n\n\n************** TRY *******************")
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


if __name__ == "__main__":
    main()


# cmd = [
#     "ffmpeg",
#     "-nostdin",
#     "-threads", "0",
#     "-i", file,
#     "-f", "s16le",
#     "-ac", "1",
#     "-acodec", "pcm_s16le",
#     "-ar", str(sr),
#     "-"
# ]
# # fmt: on
# try:
#     out = run(cmd, capture_output=True, check=True).stdout
# except CalledProcessError as e:
#     raise RuntimeError(f"Failed to load audio: {e.stderr.decode()}") from e

# return np.frombuffer(out, np.int16).flatten().astype(np.float32) / 32768.0
