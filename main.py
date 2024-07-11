from util import *
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

# Initialize streamlit app
page_title = "Algerian Forest Fire Prediction"
page_icon = "👨‍💼"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout="centered")

# Streamlit app title and description
st.title(page_title)
st.write(':blue[***Predict Forest Fire Risks with Precision***]')
st.write('*Leverage advanced machine learning to accurately predict the Forest Fire Weather Index. '
         'Input key meteorological and environmental parameters to assess fire danger levels and '
         'enhance forest fire management and prevention strategies.*')
st.info('🛈 Select the parameters from sidebar ⬅️')

# Parameter Configuration
df = configure_sidebar_parameters()

# Display the parameters in tabular format
st.subheader('Selected Parameters')
st.dataframe(df, hide_index=True)

# Encode the Region and Fire Status parameters
df['Region'] = np.where(df['Region'].str.contains('Sidi-Bel'), 1, 0)
# df['Region'] = df['Region'].replace({'Sidi-Bel': 1, 'Bejaia': 0})
df['Fire Status'] = np.where(df['Fire Status'].str.contains('Not Fire'), 0, 1)
# df['Fire Status'] = df['Fire Status'].replace({'Fire': 1, 'Not Fire': 0})

# Rename the column "Fire Status" to "Classes"
df = df.rename(columns={'Fire Status': 'Classes'})

# Import Ridge Regressor and Standard Scaler Pickle files
ridge_model = pickle.load(open('ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('scaler.pkl', 'rb'))

# Button for prediction
predict_button = st.button('Predict', type='primary')

if predict_button:
    st.subheader('Fire Weather Index Prediction:')

    # Transform the input parameters using Standard Scaler
    df_scaled = standard_scaler.transform(df)

    result = ridge_model.predict(df_scaled)
    result = round(result[0], 2)
    st.subheader(result)


