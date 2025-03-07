# AI Diet and Health Planner

## Overview
The **AI Diet and Health Planner** is a web-based application that generates a personalized fitness and diet plan using AI. Users can input their lifestyle, current health conditions, dietary habits, and recommendations to receive a structured daily schedule in the form of an HTML webpage.

## Features
- **User Input Form:** Allows users to enter details about their lifestyle, health, diet, exercise, sleep, and recommendations.
- **AI-Powered Plan Generation:** Uses Google's Generative AI to create a structured fitness and diet plan.
- **Material UI Design:** The generated page follows a clean and modern UI inspired by Material Design.
- **Flask Backend:** A lightweight backend that processes user inputs and generates the HTML response.

## Technologies Used
- **Python (Flask)** - For handling web requests and AI processing.
- **Google Generative AI API** - For generating personalized fitness and diet plans.
- **HTML, CSS, JavaScript** - For frontend rendering.
- **Materialize CSS** - For a clean and responsive UI.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/ai-diet-health-planner.git
   cd ai-diet-health-planner
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up the API key for Google Generative AI in `ai.py`:
   ```python
   import google.generativeai as genai
   genai.configure(api_key="YOUR_API_KEY")
   ```
5. Run the application:
   ```sh
   python ai.py
   ```
6. Open the application in a browser:
   ```
   http://127.0.0.1:5000
   ```

## Usage
1. Enter your details in the form (lifestyle, health, diet, exercise, sleep, recommendations).
2. Click **Submit** to generate a personalized plan.
3. The AI-generated HTML page will be displayed with structured data in tables and charts.

## Project Structure
```
├── ai.py                 # Main Flask application
├── templates
│   ├── web.html          # Main user input form
├── generated_page.html   # AI-generated HTML output
├── requirements.txt      # Dependencies
├── README.md             # Documentation
```

## Issues and Contributions
If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on GitHub.

## License
This project is licensed under the MIT License.

---
### Author
*Rishi* – [GitHub Profile](https://github.com/error-raga-008)

