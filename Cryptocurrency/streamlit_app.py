import streamlit as st
import numpy as np
import pandas as pd

# Assume df_result is the DataFrame containing the prediction results
# It should have columns 'last_original_days_value' and 'next_predicted_days_value'
# You need to replace df_result with your actual DataFrame
df_result = pd.DataFrame({
    'original_days_value': np.random.rand(31),
    'next_predicted_days_value': np.random.rand(31)
})

def main():
    st.title('Prediction App')

    pred_days = st.slider('Select number of days to predict', min_value=1, max_value=30, value=15)

    if st.button('Predict'):
        # Generate random values for both last_original_days_value and next_predicted_days_value
        last_original_values = np.random.rand(pred_days)
        next_predicted_values = last_original_values.copy()  # Use the same values for prediction
        new_pred_plot = pd.DataFrame({
            'Original price': last_original_values,
            'Predicted price': next_predicted_values
        })

        st.write(new_pred_plot)

if __name__ == '__main__':
    main()
