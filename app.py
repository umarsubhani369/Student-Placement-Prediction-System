from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open('placement_model_tuned.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get input values
            cgpa = float(request.form['cgpa'])
            internships = int(request.form['internships'])
            projects = int(request.form['projects'])
            workshops = int(request.form['workshops'])
            aptitude = float(request.form['aptitude'])
            skill_test = float(request.form['skill_test'])
            extracurricular = int(request.form['extracurricular'])
            training = int(request.form['training'])
            ssc = float(request.form['ssc'])
            hsc = float(request.form['hsc'])

            # Feature array
            features = np.array([[cgpa, internships, projects, workshops, aptitude, skill_test,
                                  extracurricular, training, ssc, hsc]])
            features_scaled = scaler.transform(features)

            # Prediction
            prediction = model.predict(features_scaled)[0]
            status = "Placed" if prediction == 1 else "Not Placed"

            # Weakness detection
            weak_points = []
            feedback = ""

            # Custom threshold messages if near threshold
            if cgpa < 2.5:
                weak_points.append("Low CGPA")
            elif 2.4 <= cgpa < 2.5:
                weak_points.append("Your CGPA is close to the threshold. Focus on improving it.")
            if internships == 0:
                weak_points.append("No Internships")
            if projects < 1:
                weak_points.append("Fewer Projects")
            elif projects == 1:
                weak_points.append("You have one project. Adding more projects would help.")
            if workshops < 1:
                weak_points.append("No Certifications/Workshops")
            elif workshops == 1:
                weak_points.append("Consider attending workshops to enhance your profile.")
            if aptitude < 60:
                weak_points.append("Low Aptitude Score")
            elif 55 <= aptitude < 60:
                weak_points.append("Your aptitude score is close. A little more focus can improve it.")
            if skill_test < 5:
                weak_points.append("Skill Test Score could be better")
            elif 4.5 <= skill_test < 5:
                weak_points.append("You're close! Try improving your skill test score.")
            if extracurricular == 0:
                weak_points.append("No Extracurricular Activities")
            if training == 0:
                weak_points.append("No Placement Training")
            if ssc < 60:
                weak_points.append("Low SSC Marks")
            if hsc < 60:
                weak_points.append("Low HSC Marks")
            

            # Feedback message
            if status == "Placed":
                if weak_points:
                    feedback = "You're placed, great job! However, here's what you can still improve:"
                else:
                    feedback = "Keep it up! You're all set for placement!"
            else:
                feedback = "You are not placed. Focus on the following areas to improve:"

            return render_template('result.html', status=status, weak_points=weak_points, feedback=feedback)

        except ValueError:
            return "Invalid input values. Please enter valid numbers."
        except Exception as e:
            return f"Error: {str(e)}"

@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
