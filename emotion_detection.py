import requests
import json

def emotion_detector(text_to_analyze):
    """
    Run emotion detection on the input text using the Watson NLP Library.

    Args:
        text_to_analyze (str): The text to be analyzed for emotions.

    Returns:
        dict: A dictionary containing the scores for anger, disgust, fear, joy, and sadness, along with the dominant emotion.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, headers=headers, json=input_json)

    if response.status_code == 200:
        response_json = response.json()
        print("Response JSON:", response_json)
        try:
            return response_json['emotion']['document']['emotion']['targets'][0]['target']
        except KeyError as e:
            print("KeyError:", e)
            return None

        # Initialize emotion scores
        anger_score = 0
        disgust_score = 0
        fear_score = 0
        joy_score = 0
        sadness_score = 0

        # Extract scores for each emotion
        for emotion in emotions:
            if emotion['type'] == 'anger':
                anger_score = emotion['score']
            elif emotion['type'] == 'disgust':
                disgust_score = emotion['score']
            elif emotion['type'] == 'fear':
                fear_score = emotion['score']
            elif emotion['type'] == 'joy':
                joy_score = emotion['score']
            elif emotion['type'] == 'sadness':
                sadness_score = emotion['score']

        # Find the dominant emotion
        dominant_emotion = max([(anger_score, 'anger'), (disgust_score, 'disgust'), (fear_score, 'fear'), (joy_score, 'joy'), (sadness_score, 'sadness')])[1]

        # Return the desired output format
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    else:
        return None

# Example usage:
text_to_analyze=input("Enter")
result = emotion_detector(text_to_analyze)
print(result)
