from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detection")

@app.route('/')
def render_homepage():
    return render_template("index.html")

@app.route('/emotionDetector', methods=["GET"])
def emotion_detection():
    text_to_analyze = request.args["textToAnalyze"]
    analysis_result = emotion_detector(text_to_analyze)

    if analysis_result["dominant_emotion"] is None:
        response = "Could not detect emotions! Please try again!"
    else:
        response = "For the given statement, the system response is "

        for key, value in analysis_result.items():
            if key != "dominant_emotion":
                response += f" '{key}': {value},"

        last_comma_index = response.rfind(",")
        if last_comma_index != -1:
            response = response[:last_comma_index] + '.' + response[last_comma_index + 1:]

        response += f" The dominant emotion is {analysis_result['dominant_emotion']}."

    return response

if __name__ == "__main__":
    app.run(debug = True)