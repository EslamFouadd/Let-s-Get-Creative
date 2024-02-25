# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Step 1: Data Loading
# Assuming you have a CSV file 'student_data.csv' with columns representing student features and the target variable 'solution'
data = pd.read_csv('student_data.csv')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(data.head())

# Step 2: Data Preprocessing
# Separate features and target variable
X = data.drop('solution', axis=1)  # Features
y = data['solution']  # Target variable

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features by removing the mean and scaling to unit variance
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 3: Model Training (Using Logistic Regression as an example)
model = LogisticRegression(random_state=42)
model.fit(X_train_scaled, y_train)

# Step 4: Model Evaluation
# Predict on the test set
y_pred = model.predict(X_test_scaled)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy:", accuracy)

# Generate classification report and confusion matrix
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
