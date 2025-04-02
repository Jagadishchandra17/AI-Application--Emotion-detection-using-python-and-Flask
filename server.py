"""
This module provides an application to analyze emotions from user input
using Flask. It provides routes to render an index page, accept user input,
and return the corresponding emotion analysis results.
"""

from flask import Flask, request, render_template

app = Flask(__name__)

def emotion_analyzer(text_to_analyse):
    """
    Analyzes the provided text for emotions and returns the confidence scores 
    along with the dominant emotion.

    Parameters:
    text_to_analyse (str): The text input provided by the user to be analyzed.

    Returns:
    str: A response string containing emotion scores and the dominant emotion, 
    or an error message if input is invalid.
    """
    # Assuming emotion_detector is a function that processes the input text
    emotion_result = emotion_detector(text_to_analyse)

    anger = emotion_result.get('anger')
    disgust = emotion_result.get('disgust')
    fear = emotion_result.get('fear')
    joy = emotion_result.get('joy')
    sadness = emotion_result.get('sadness')
    dominant_emotion = emotion_result.get('dominant_emotion')

    if dominant_emotion is None:
        return "Invalid text! Please try again"

    response_str = f"""For the given statement, the system response is
    'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}.
    The dominant emotion is <strong>{dominant_emotion}</strong>."""
    return response_str

@app.route("/")
def render_index_page():
    """
    Renders the index page, where the user can input a text string to be analyzed.

    Returns:
    str: The HTML content of the index page.
    """
    return render_template('index.html')

@app.route("/analyze", methods=['GET'])
def analyze_text():
    """
    Analyzes the user-provided text and returns the response with emotion scores.

    If no text is provided, an error message is returned.

    Returns:
    str: The analysis result or an error message if no text is provided.
    """
    text_to_analyse = request.args.get('textToAnalyze')
    if text_to_analyse:
        result = emotion_analyzer(text_to_analyse)
        return result
    return "No text provided for analysis."

def emotion_detector(_):
    """
    Detects emotions in the given text and returns emotion scores and dominant emotion.

    Parameters:
    _: The text to analyze (not used in this function).

    Returns:
    dict: A dictionary containing emotion scores and the dominant emotion.
    """
    # Placeholder for actual emotion detection logic
    # Replace this with your real emotion detection API call
    return {
        'anger': 0.1,
        'disgust': 0.05,
        'fear': 0.2,
        'joy': 0.3,
        'sadness': 0.15,
        'dominant_emotion': 'joy'  # Example dominant emotion
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
