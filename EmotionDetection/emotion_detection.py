'''Using the Emotion Predict function of the Watson NLP Library 
to create the emotion detector function.
'''
import json
import requests

def emotion_detector(text_to_analyze):
    '''the emotion detector function
    '''
    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    newobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = newobj, headers = headers)
    formatted_response = json.loads(response.text)

    emotions = formatted_response['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotions, key=emotions.get)
    emotions['dominant emotion'] = dominant_emotion
    return emotions
