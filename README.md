# Sentiment Analysis API

This repository contains a **Sentiment Check** that utilizes Google's Gemini AI to classify text as **POSITIVE, NEGATIVE, or NEUTRAL**. The application is built with Flask and can be run locally or inside a Docker container.

## 🚀 Features
- Classifies text sentiment using Gemini AI.
- Provides a REST API endpoint (`/analyze`) to analyze text.
- Dockerized for easy deployment.
- Simple frontend interface using HTML + JavaScript.

---

## 📌 Prompt Chosen
The application was built using Google's **Gemini AI** to classify text sentiment based on user input.

### 📜 Example Prompts:
- "It's so beautiful today!" → **POSITIVE**
- "It's so cold today I can't feel my feet..." → **NEGATIVE**
- "The weather today is perfectly adequate." → **NEUTRAL**

---

## 📂 Setup Instructions

### ✅ 1. Clone the Repository
```sh
 git clone https://github.com/Hitesh203/Backend_task.git
 cd Backend_task
```

### ✅ 2. Install Dependencies
Ensure you have **Python 3.9+** installed, then run:
```sh
pip install -r requirements.txt
```

### ✅ 3. Set Up Environment Variables
Export your **Gemini AI API Key**:
```sh
export GEMINI_API_KEY="your_api_key_here"
```
On Windows (PowerShell):
```sh
$env:GEMINI_API_KEY="your_api_key_here"
```

### ✅ 4. Run the Application Locally
```sh
python sentiment_checker.py
```
The server will start at: **http://127.0.0.1:5000**

### ✅ 5. Test API Endpoint
Use **cURL** to send a test request:
```sh
curl -X POST http://127.0.0.1:5000/analyze -H "Content-Type: application/json" -d '{"text": "I love this!"}'
```
Expected Output:
```json
{"sentiment": "POSITIVE"}
```

---

## 🐳 Running in Docker

### ✅ 1. Build the Docker Image
```sh
docker build -t sentiment-analysis-app .
```

### ✅ 2. Run the Container
```sh
docker run -p 5000:5000 -e GEMINI_API_KEY="your_api_key_here" sentiment-analysis-app
```

### ✅ 3. Access the API in Docker
```sh
curl -X POST http://127.0.0.1:5000/analyze -H "Content-Type: application/json" -d '{"text": "Docker is awesome!"}'
```

If sentiment is **undefined in Docker**, check logs:
```sh
docker logs <container_id>
```

---

## 🌍 Frontend Interface
The frontend is a simple **HTML + JavaScript** page to interact with the API.

### ✅ Open `templates/index.html`
Modify the JavaScript to match your API URL if needed:
```javascript
fetch("http://127.0.0.1:5000/analyze", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text: document.getElementById("inputText").value })
})
```

Then, start Flask and open **http://127.0.0.1:5000** to use the web interface.

---

## 🖼 Screenshot

![API Running Screenshot](screenshot.png)

_Replace with a screenshot of your application running successfully on `http://localhost/`_

---

## 🛠 Troubleshooting
### ❌ Sentiment is Undefined in Docker
- Ensure `GEMINI_API_KEY` is passed when running Docker.
- Debug API response using `docker logs <container_id>`.

### ❌ Flask Shows `TemplateNotFound: index.html`
- Ensure `index.html` is inside a `templates/` folder.
- Restart Flask (`Ctrl+C` and run `python sentiment_checker.py` again).

---

## 🏗 Future Improvements
- ✅ Improve UI design.
- ✅ Add database support for storing sentiment results.
- ✅ Deploy on cloud services (e.g., AWS, Heroku).

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License
This project is licensed under the **MIT License**.

---

### 📬 Contact
For any issues, feel free to reach out via GitHub Issues or email: **hiteshkumarmz16@gmail.com**

