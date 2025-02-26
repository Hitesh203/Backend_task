import os
from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

# Configure Google Gemini API
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# Create the model
generation_config = {
    "temperature": 2,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
)

# Flask app initialization
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    try:
        data = request.get_json()
        text = data.get("text", "")
        if not text:
            return jsonify({"error": "Text input is required"}), 400

        chat_session = model.start_chat(
            history=[
                {"role": "user", "parts": [f"Analyze the sentiment of the following text: \"{text}\""]},
            ]
        )
        response = chat_session.send_message(text)
        
        return jsonify({"sentiment": response.text.strip()})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
