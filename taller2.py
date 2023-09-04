import re
from collections import Counter
from youtube_transcript_api import YouTubeTranscriptApi

# Función para obtener la transcripción de un video de YouTubE 
def get_youtube_transcription(video_url, language='es'):
    
    video_id = video_url.split('https://youtu.be/')[1]
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    transcript = transcript_list.find_transcript([language])
    transcript_text = ' '.join([d['text'] for d in transcript.fetch()])
    return transcript_text

def preprocess_transcription(transcript_text):
    transcript_text = re.sub(r'[^\w\s]', '', transcript_text)
    transcript_text = transcript_text.lower()
    stopwords = ['el', 'la', 'de', 'en', 'y', 'que', 'para']
    transcript_words = transcript_text.split()
    transcript_words = [word for word in transcript_words if word not in stopwords]
    
    tokens = transcript_words
    
    return tokens

def count_words(tokens):
    word_counts = Counter(tokens)
    return word_counts

def analyze_sentiments(tokens):
    positive_words = ['bueno', 'feliz', 'positivo']
    negative_words = ['mal', 'triste', 'negativo']
    
    positive_count = sum(1 for word in tokens if word in positive_words)
    negative_count = sum(1 for word in tokens if word in negative_words)
    
    if positive_count > negative_count:
        return "Positivo"
    elif negative_count > positive_count:
        return "Negativo"
    else:
        return "Neutral"

video_url = 'https://youtu.be/_wngl0OLmBY?si=ZumKix0rntw6DIHE'  # URL del video que quieres analizar

transcript_text = get_youtube_transcription(video_url)
tokens = preprocess_transcription(transcript_text)
word_counts = count_words(tokens)
sentiment = analyze_sentiments(tokens)

print("Frecuencia de palabras:")
print(word_counts)
print("Análisis de sentimientos:", sentiment)