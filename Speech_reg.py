import streamlit as st
import speech_recognition as sr
import pyttsx3
import time
import pandas as pd

# Create a function for Speech Trancription
def transcribe_speech():
    # Initialize recognizer class
    r = sr.Recognizer()

    # Reading Microphone as source
    with sr.Microphone() as source:

        # create a streamlit spinner that shows progress
        with st.spinner(text='Silence pls, Caliberating background noise.....'):
            time.sleep(2)

        r.adjust_for_ambient_noise(source, duration = 1) # ..... Adjust the sorround noise
        st.info("Speak now...")

        audio_text = r.listen(source) #........................ listen for speech and store in audio_text variable
        with st.spinner(text='Transcribing your voice to text'):
            time.sleep(2)

        try:
            # using Google speech recognition to recognise the audio
            text = r.recognize_google(audio_text)
            # print(f' Did you say {text} ?')
            return text
        except:
            return "Sorry, I did not get that."

# # Create a function for text Talkback
# def Text_Speaker(your_command):
#     speaker_engine = pyttsx3.init() #................ initiate the talkback engine
#     speaker_engine.say(your_command) #............... Speak the command
#     speaker_engine.runAndWait() #.................... Run the engine



def main():
    st.title("Speech Recognition App")
    st.write("Click on the microphone to start speaking:")

    # add a button to trigger speech recognition
    if st.button("Start Recording"):
        your_words_in_text = transcribe_speech()
        st.write("Transcription: ", your_words_in_text)
if _name_ == "_main_":
    main()