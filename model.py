import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import pickle

# Load the dataset
df = pd.read_csv('D:/MLProject/data/placementdatav2.csv ') # replace with your actual CSV file name

# Clean column names (optional but recommended)
df.columns = df.columns.str.strip()

# Convert categorical 'Yes'/'No' to 1/0
df['ExtracurricularActivities'] = df['ExtracurricularActivities'].map({'Yes': 1, 'No': 0})
df['PlacementTraining'] = df['PlacementTraining'].map({'Yes': 1, 'No': 0})
df['PlacementStatus'] = df['PlacementStatus'].map({'Placed': 1, 'NotPlaced': 0})

# Select features and target
X = df[['CGPA', 'Internships', 'Projects', 'Workshops/Certification',
        'AptitudeTestScore', 'Skill Test Score', 'ExtracurricularActivities',
        'PlacementTraining', 'SSC_Marks', 'HSC_Marks']]
y = df['PlacementStatus']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train the model
model = RandomForestClassifier()
model.fit(X_scaled, y)

# Save model and scaler
pickle.dump(model, open('placement_model_tuned.pkl', 'wb'))
pickle.dump(scaler, open('scaler.pkl', 'wb'))
print("Model accuracy:", model.score(scaler.transform(X), y))
print("Model and scaler saved successfully.")
