import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import pickle


df = pd.read_csv("student_burnout (2).csv")


df = df.drop(columns=['burnout_score'])

le = LabelEncoder()
df['burnout_level'] = le.fit_transform(df['burnout_level'])


X = df.drop(columns=['burnout_level'])
y = df['burnout_level']


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = LogisticRegression(max_iter=1000, random_state=42)
model.fit(X_train, y_train)


accuracy = model.score(X_test, y_test)
print(f"Accuracy: {accuracy * 100:.2f}%")


pickle.dump(model, open('burnout_model.pkl', 'wb'))
pickle.dump(le, open('label_encoder.pkl', 'wb'))

print("✅ Model and encoder saved!")








# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# import pickle

# # load dataset
# df = pd.read_csv("student_burnout (2).csv")

# X = df[["study_hours","sleep_hours","stress_level","assignment_load","attendance"]]
# y = df["burnout_level"]

# # split data
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # train model
# model = RandomForestClassifier()
# model.fit(X_train, y_train)

# # save model
# pickle.dump(model, open("burnout_model.pkl", "wb"))

# print("Model trained and saved!")