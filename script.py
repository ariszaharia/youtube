from youtube_transcript_api import YouTubeTranscriptApi
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

model = OllamaLLM(model="qwen2.5:7b")

def get_yt_text(video_id):
    try:
        api = YouTubeTranscriptApi()
        text = api.fetch(video_id)
        return text
    except Exception as e:
        print(f"Error: {e}")
        return None


template = """Make a short summary of the following video transcript : {text}"""
prompt = PromptTemplate.from_template(template)

chain = prompt | model

if __name__ == "__main__":
    video_id = "ZzrHfxwDcBg"
    video_text = get_yt_text(video_id)
    
    result = chain.run(text=video_text)
    print(result)

