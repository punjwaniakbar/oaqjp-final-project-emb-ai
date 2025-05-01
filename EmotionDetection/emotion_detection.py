import requests
import json

def emotion_detector(text_to_analyze):
    response = requests.post(
        url =
        'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict', 
        headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"},
        json = { "raw_document": { "text": text_to_analyze}, },
        timeout = 20
    )
    if response.status_code == 400:
        emotionpredict_reponse = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        # Convert JSON to Dictionary
        emotionpredict_json = json.loads(response.text)
        # Extract set of emotions
        emotions = emotionpredict_json["emotionPredictions"][0]["emotion"]
        # Get Emotion-Key with highest score
        key_max_score = max(emotions, key = emotions.get)

        emotionpredict_reponse = {
            'anger': emotions["anger"],
            'disgust': emotions["disgust"],
            'fear': emotions["fear"],
            'joy': emotions["joy"],
            'sadness': emotions["sadness"],
            'dominant_emotion': key_max_score
        }
    return emotionpredict_reponse