"""Flask Server for Web Deployment"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detection")

@app.route('/')
def render_homepage():
    """ Render homepage """
    return render_template("index.html")

@app.route('/emotionDetector', methods=["GET"])
def emotion_detection():
    """ Analyze text and return emotion detection result """
    text_to_analyze = request.args["textToAnalyze"]
    analysis_result = emotion_detector(text_to_analyze)

    if analysis_result["dominant_emotion"] is None:
        response = "Invalid text! Please try again!"
    else:
        response = "For the given statement, the system response is "

        for key, value in analysis_result.items():
            if key != "dominant_emotion":
                response += f" '{key}': {value},"

        last_comma_index = response.rfind(",")
        if last_comma_index != -1:
            response = response[:last_comma_index] + '.' + response[last_comma_index + 1:]

        response += f" The dominant emotion is <b>{analysis_result['dominant_emotion']}</b>."

    return response

if __name__ == "__main__":
    app.run(debug = True)
    