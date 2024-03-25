import streamlit as st
from pytube import YouTube
import os

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

st.title("YouTube Downloader")

video_url = st.text_input("Enter YouTube Video URL:")
if video_url:
    if st.button("Download video"):
        video_path = download_video(video_url, "video")
        st.subheader("Downloaded Video")
        st.video(video_path)  # Display the downloaded video

    if st.button("Download Audio"):
        audio_path = download_audio(video_url, "audio")
        st.subheader("Downloaded Audio")
        st.audio(audio_path)  # Display the downloaded audio
