from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from itertools import cycle
app = Flask(__name__)

# Assume df_result is the DataFrame containing the prediction results
# It should have columns 'last_original_days_value' and 'next_predicted_days_value'
# You need to replace df_result with your actual DataFrame
df_result = pd.DataFrame({
    'original_days_value': np.random.rand(31),
    'next_predicted_days_value': np.random.rand(31)
})

@app.route('/')
def index():
    return render_template('index.html', df_display=None)

@app.route('/predict', methods=['POST'])
def predict():
    pred_days = int(request.form['pred_days'])

    # Generate random values for both last_original_days_value and next_predicted_days_value
    last_original_values = np.random.rand(pred_days )
    next_predicted_values = last_original_values.copy()  # Use the same values for prediction

    # Create DataFrame
    new_pred_plot = pd.DataFrame({
        'last_original_days_value': last_original_values,
        'next_predicted_days_value': next_predicted_values
    })

    # Ensure that the arrays have the same length
    new_pred_plot = pd.DataFrame({
    'original_value':last_original_values,
    'predicted_value':next_predicted_values})

    names = cycle(['Last 15 days close price','Predicted next 1 day close price'])
    df_result=new_pred_plot.dropna()
    if len(new_pred_plot) > len(df_result):
        df_result = df_result.reindex(new_pred_plot.index)
    
    df_display = new_pred_plot.to_html(classes="table table-striped",index=False)

    return render_template('result.html', df_display=df_display)

if __name__ == '__main__':
    app.run(debug=True)
