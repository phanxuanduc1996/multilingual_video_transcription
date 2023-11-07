import pdb
import numpy as np
import streamlit as st
import speech_recognition as sr
from business_logic import transcribe_video_orchestrator, transcribe_video_streaming


def open_buy_me_coffee():
    st.markdown('<script>document.getElementById("buy-me-coffee-btn").click();</script>',
                unsafe_allow_html=True)


def main():
    st.title("Real-time Speech Recognition")

    # # User input: YouTube URL
    # url = st.text_input("Enter YouTube URL or Local path:")

    # User input: model
    models = ["tiny", "base", "small", "medium", "large"]
    model = st.selectbox("Select Model:", models)
    st.write(
        "If you take a smaller model it is faster but not as accurate, whereas a larger model is slower but more accurate.")

    # Create a speech recognizer & microphone object
    recognizer = sr.Recognizer()
    microphone = sr.Microphone(device_index=0)

    with microphone as source:
        st.info("Listening...")
        recognizer.adjust_for_ambient_noise(source)

        while True:
            try:
                audio = recognizer.listen(source, timeout=None)
                audio_data = audio.get_wav_data()
                data_s16 = np.frombuffer(
                    audio_data, dtype=np.int16, count=len(audio_data)//2, offset=0)
                float_data = data_s16.astype(np.float32, order='C') / 32768.0
                pdb.set_trace()

                # Recognize the audio and convert it to text
                # transcript = recognizer.recognize_google(audio)
                transcript = transcribe_video_streaming(float_data, model)
                pdb.set_trace()

                if transcript:
                    st.subheader("Transcription:")
                    st.write(transcript)
                else:
                    st.error("Error occurred while transcribing.")
                    st.write("Please try again.")

            except sr.UnknownValueError:
                # If the speech recognizer could not understand the audio
                st.warning("Could not understand audio")

            except sr.RequestError as e:
                # If there was an error with the speech recognition service
                st.error(f"Error: {e}")

    # if st.button("Transcribe"):
    #     if url:
    #         transcript = transcribe_video_orchestrator(url, model)

    #         if transcript:
    #             st.subheader("Transcription:")
    #             st.write(transcript)
    #         else:
    #             st.error("Error occurred while transcribing.")
    #             st.write("Please try again.")


if __name__ == "__main__":
    main()
