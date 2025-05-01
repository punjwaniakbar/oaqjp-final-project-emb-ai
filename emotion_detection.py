import requests

def emotion_detector(text_to_analyze):
    response = requests.post(
        url =
        'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict', # pylint: disable=line-too-long
        headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"},
        json = { "raw_document": { "text": text_to_analyze}, },
        timeout = 20
    )

    return response.text