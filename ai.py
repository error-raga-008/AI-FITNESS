from flask import Flask, render_template, request, redirect
import os
import google.generativeai as genai

# Initialize Flask app
app = Flask(__name__)

# Configure the Gemini API key
genai.configure(api_key="AIzaSyBh8h_vMfbism7OTejfRoFuVtkimo_1Gq8")

@app.route('/generated_page')
def generated_page():
    """ Serves the generated HTML page. """
    if os.path.exists("generated_page.html"):
        with open("generated_page.html", "r", encoding="utf-8") as file:
            content = file.read()
        return content
    else:
        return "Generated page not found.", 404

@app.route('/submit', methods=['POST'])
def submit_form():
    """ Handles form submission and generates AI-based recommendations. """
    try:
        # Get form data
        lifestyle = request.form['lifestyle']
        current_health = request.form['current_health']
        current_diet = request.form['current_diet']
        recommendation = request.form['recommendation']

        # Define the model
        model = genai.GenerativeModel("gemini-1.5-pro")  # Updated to latest model

        # Generate AI response
        prompt = (
            f"act as my fitness coach and make a personlised time table for me with and make it as detaield as possilbe including each smallest details and i want you to make the table coloriesed and make it more user engaging as possbile and use symbols as possible and this as my data from the promt {lifestyle} as my lifestyle and {current_health} as current health and {current_diet} as my current diet and {recommendation} as my recomendation and wishes that i would like to see in my daily routine and put all the output you have generated in a html web page code with clean and material ui inspired ui and all the data which are needed to be in a tables and charts etcs and only give the html code as the output and you can also use css and js and i want you give response staring from <html> and ending with </html>"
        )
        
        response = model.generate_content(prompt)
        
        # Save the generated HTML to a file
        html_output = response.text if response and response.text else "<h1>Error generating content</h1>"
        
        with open("generated_page.html", "w", encoding="utf-8") as new_file:
            new_file.write(html_output)

        return redirect('/generated_page')

    except Exception as e:
        return f"An error occurred: {str(e)}", 500

@app.route('/')
def index():
    """ Renders the homepage with the input form. """
    return render_template('web.html')

if __name__ == '__main__':
    app.run(debug=True)
