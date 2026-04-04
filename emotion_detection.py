import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    tempobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=tempobj, headers=header)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key = emotions.get)
        result = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }
        return result
    else:
        return {'error': 'Failed to retrieve emotions'}