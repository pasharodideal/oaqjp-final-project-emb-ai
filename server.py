'''
    handling the response from the emotion detection function
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route('/emotionDetector')
def emo_detect():
    '''
    handling the response from the emotion detection function
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant emotion'] is None:
        return "<b>Invalid text! Please try again!</b>"

    dominant_emotion = response['dominant emotion']
    response.popitem()
    response_string = str(response)
    response_string = response_string.strip('{}')
    return (f"For the given statement, the system response is {response_string}."
            f"The dominant emotion is <b>{dominant_emotion}</b>.")

@app.route('/')
def render_index_page():
    '''render the html template
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5008)
