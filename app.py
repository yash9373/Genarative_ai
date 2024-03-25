import streamlit as st
from dotenv import load_dotenv
import os 
from pytube import YouTube
load_dotenv() #load all the enviorment

import google.generativeai as genai

from youtube_transcript_api import YouTubeTranscriptApi
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def download_video(url, filename):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    file_path = stream.download(filename=filename)
    st.success("Video downloaded successfully!")
    return file_path

def download_audio(url, filename):
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    file_path = stream.download(filename=filename)
    st.success("Audio downloaded successfully!")
    return file_path

prompt="you are the youtube sumerrizer you will be tacking the transivript and provideing dhort report on the video of the project like what they are implimentting steps and what technology they used "
#prompt="you are the youtube sumerrizer you will be tacking the transivript and provideing the important sumer in the 250 words the transcript text is following  plz provide hte summery:"
def genarate_gemini_content(transcript_text,prompt):
    model=genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt+transcript_text)
    return response.text

st.title("YT transcrpt creator")
yt_link = st.text_input("enter the link:")
video_url = yt_link

if yt_link:
    video_id = yt_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg",use_column_width=True)

if st.button("Download video"):
        video_path = download_video(video_url, "video")
        st.subheader("Downloaded Video")
        st.video(video_path)  # Display the downloaded video

if st.button("Download Audio"):
        audio_path = download_audio(video_url, "audio")
        st.subheader("Downloaded Audio")
        st.audio(audio_path)  # Display the downloaded audio

def extract_transcript(url):
    try:
        video_id = url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript =""
        for i in transcript_text:
            transcript += " " + i["text"]
        return transcript

    except Exception as e:
        raise e

if st.button("get details"):
    trans_text = extract_transcript(yt_link)

    if trans_text :
        summary = genarate_gemini_content(trans_text,prompt)
        st.markdown("## DEtailed notes :")
        st.write(summary)
        
def extract_video_id_audio(url):
    video_id = None
    if "youtube.com" in url:
        video_id = url.split("v=")[1]
        ampersand_pos = video_id.find("&")
        if ampersand_pos != -1:
            video_id = video_id[:ampersand_pos]
    elif "youtu.be" in url:
        video_id = url.split("/")[-1]
    return video_id


