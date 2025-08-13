import numpy as np
from sklearn.linear_model import LinearRegression

def predict_next_rate(df):
    """
    Прогнозирует курс на следующий день на основе линейной регрессии
    """
    x = np.arange(len(df)).reshape(-1, 1)
    y = df["rate"].values

    model = LinearRegression()
    model.fit(x, y)

    next_day_index = len(df)
    predicted_rate = model.predict([next_day_index])[0]
    return predicted_rate