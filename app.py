import pickle
import datetime

def get_time_slot(hour):
    if 5 <= hour < 9:
        return "Morning"
    elif 9 <= hour < 17:
        return "Afternoon"
    elif 17 <= hour < 22:
        return "Evening"
    else:
        return "Night"

def suggest_task():
    with open('../model/task_predictor.pkl', 'rb') as f:
        model, le_day, le_time, le_task = pickle.load(f)

    now = datetime.datetime.now()
    day = now.strftime('%A')
    time_slot = get_time_slot(now.hour)

    X_pred = [[le_day.transform([day])[0], le_time.transform([time_slot])[0]]]
    y_pred = model.predict(X_pred)
    task = le_task.inverse_transform(y_pred)[0]

    return task
