import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
import pickle
import json

# Load task data
with open('../data/tasks.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
if df.empty:
    print("No data to train on.")
    exit()

# Preprocessing
le_day = LabelEncoder()
le_time = LabelEncoder()
le_task = LabelEncoder()

df['day_enc'] = le_day.fit_transform(df['day'])
df['time_enc'] = le_time.fit_transform(df['time'])
df['task_enc'] = le_task.fit_transform(df['task'])

X = df[['day_enc', 'time_enc']]
y = df['task_enc']

# Train model
model = MultinomialNB()
model.fit(X, y)

# Save model and encoders
with open('task_predictor.pkl', 'wb') as f:
    pickle.dump((model, le_day, le_time, le_task), f)

print("Model trained and saved.")
