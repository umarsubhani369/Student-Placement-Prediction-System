:

🎓 Student Placement Prediction System
The Student Placement Prediction System is a web-based application designed to help assess whether a student is likely to get placed in a job based on their academic and extracurricular profile. Built using Flask and a trained machine learning model, the system provides real-time predictions along with actionable feedback.

🚀 Key Features
📥 Student Input Form
Users can fill out a detailed form that captures important attributes such as:

CGPA
Internships
Projects
Workshops/Certification
AptitudeTestScore
Skill Test Score
ExtracurricularActivities
PlacementTraining	
SSC_Marks
HSC_Marks	

📊 Prediction Output
Once submitted, the system uses a trained Random Forest Classifier to predict whether the student is likely to be Placed or Not Placed.

💡 Smart Feedback
If the prediction is negative, the system doesn’t stop there. It provides personalized suggestions on what factors might have lowered the placement chances (e.g., low CGPA, lack of internships) so users know where to improve.

📱 Responsive UI
The front end is designed to be clean, responsive, and mobile-friendly — ensuring accessibility from both laptops and smartphones.

🧠 Tech Stack
Python & Flask – Handles the server-side logic and routing

Scikit-learn (Random Forest) – For building and deploying the ML model

HTML + CSS – Simple and responsive UI

Pandas & NumPy – For data preprocessing

CSV Dataset – Historical student data used to train the model

📈 Goal of the Project
This tool is aimed at helping students understand how their current academic profile influences their chances of getting placed. It's especially useful for training & placement cells, college counselors, or students preparing for campus recruitment.

