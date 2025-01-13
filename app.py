from flask import Flask, render_template

app = Flask(__name__)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    return "Message sent successfully!"

@app.route('/weather')
def weather_case_study():
    return render_template('weather_case_study.html')

@app.route('/case_study/telemedicine')
def telemedicine_case_study():
    return render_template('telemedicine_case_study.html')

@app.route('/case_study/opportunity_portal')
def opportunity_portal_case_study():
    return render_template('opportunity_portal_case_study.html')

@app.route('/case_study/school_web_design')
def school_web_design_case_study():
    return render_template('school_web_design_case_study.html')



if __name__ == "__main__":
    # Bind to 0.0.0.0 and use the environment variable for the port
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))