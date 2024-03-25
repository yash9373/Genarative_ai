# YouTube Toolkit

The YouTube Toolkit is a versatile Python-based application developed with Streamlit, designed to streamline various tasks related to YouTube videos. Whether you need to download video or audio content, extract transcripts, or generate concise summaries, this toolkit has you covered.

## Key Features

### 1. Download Video/Audio
- Seamlessly download video or audio content from any YouTube link.
- Enjoy a hassle-free experience through Streamlit's user-friendly interface.

### 2. Transcript Extraction
- Extract accurate transcripts directly from YouTube videos.
- Leveraging the **YouTubeTranscriptApi**, transcript retrieval is efficient and reliable.

### 3. Summary Generation
- Utilize Google's Generative AI, specifically the Gemini model, to create concise summaries of video content.
- Quickly grasp the essence of any video with autogenerated summaries.

## Implementation Details

- Developed in Python, utilizing Streamlit for web application development.
- Various Python libraries such as pytube, youtube_transcript_api, and dotenv are integrated for specific functionalities.
- Enhanced privacy is ensured through secure management of environmental variables using dotenv.
- The user interface is intentionally designed for simplicity, ensuring smooth navigation and interaction.

**Note**: 
- This toolkit does not support downloading content from private or age-restricted videos.
- Summarization feature requires subtitles to be available for the video. Videos without subtitles cannot be summarized.

## How to Use

1. Simply input the YouTube link of the video you want to work with.
2. Choose whether you want to download the video, audio, extract its transcript, or generate a summary.
3. Enjoy the streamlined experience and make the most out of your YouTube content!
![Screenshot 2024-03-25 195507](https://github.com/yash9373/Genarative_ai/assets/101787484/6b742a93-5748-4f80-b633-83e822818476)
![Screenshot 2024-03-25 195557](https://github.com/yash9373/Genarative_ai/assets/101787484/42be0e92-bbb8-44ac-ad61-5d337a0957ae)
![Screenshot 2024-03-25 195540](https://github.com/yash9373/Genarative_ai/assets/101787484/1c8ff769-7c35-4366-a2a9-55c8c957e091)
![Screenshot 2024-03-25 195519](https://github.com/yash9373/Genarative_ai/assets/101787484/8476a6f2-1de9-4076-8217-1c24a9303857)

## Installation

To install the dependencies, you can use pip:

```bash
pip install -r requirements.txt
