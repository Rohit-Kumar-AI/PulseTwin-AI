"""PulseTwin AI: synthetic, non-clinical digital twin demonstration."""
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

st.set_page_config(page_title='PulseTwin AI', page_icon='💓', layout='wide')
st.title('💓 PulseTwin AI | Synthetic Wellness Digital Twin')
st.error('EDUCATIONAL DEMO ONLY — synthetic inputs and labels. Not clinically validated; never use for diagnosis, treatment, or medical decisions.')

FEATURES = ['Age', 'Systolic BP', 'BMI', 'Resting HR', 'HRV', 'Sleep hours', 'Daily steps', 'SpO2']

@st.cache_data
def generate_data(n=2400):
    rng = np.random.default_rng(42)
    data = pd.DataFrame({
        'Age': rng.integers(18, 86, n),
        'Systolic BP': rng.integers(95, 181, n),
        'BMI': rng.uniform(18, 39, n).round(1),
        'Resting HR': rng.integers(48, 111, n),
        'HRV': rng.integers(12, 101, n),
        'Sleep hours': rng.uniform(4, 10, n).round(1),
        'Daily steps': rng.integers(500, 16001, n),
        'SpO2': rng.integers(92, 101, n),
    })
    score = (0.015*(data['Age']-45) + 0.025*(data['Systolic BP']-120)
             + 0.07*(data['BMI']-25) + 0.018*(data['Resting HR']-70)
             - 0.012*(data['HRV']-50) - 0.20*(data['Sleep hours']-7)
             - 0.00007*(data['Daily steps']-7000) - 0.15*(data['SpO2']-97))
    data['Synthetic label'] = (score > 0.35).astype(int)
    return data

@st.cache_resource
def train():
    data = generate_data()
    x_train, x_test, y_train, y_test = train_test_split(data[FEATURES], data['Synthetic label'], test_size=0.25, random_state=42, stratify=data['Synthetic label'])
    model = RandomForestClassifier(n_estimators=120, random_state=42, min_samples_leaf=3)
    model.fit(x_train, y_train)
    return model, accuracy_score(y_test, model.predict(x_test))

model, agreement = train()
st.sidebar.header('Fictional patient inputs')
values = {
    'Age': st.sidebar.slider('Age', 18, 85, 42),
    'Systolic BP': st.sidebar.slider('Systolic BP (mmHg)', 95, 180, 124),
    'BMI': st.sidebar.slider('BMI', 18.0, 39.0, 25.5, 0.1),
    'Resting HR': st.sidebar.slider('Resting heart rate (bpm)', 48, 110, 72),
    'HRV': st.sidebar.slider('HRV (ms)', 12, 100, 48),
    'Sleep hours': st.sidebar.slider('Sleep (hours)', 4.0, 10.0, 7.0, 0.1),
    'Daily steps': st.sidebar.slider('Daily steps', 500, 16000, 7500, 100),
    'SpO2': st.sidebar.slider('SpO₂ (%)', 92, 100, 98),
}
patient = pd.DataFrame([values])[FEATURES]
probability = float(model.predict_proba(patient)[0, list(model.classes_).index(1)])
left, right = st.columns(2)
left.metric('Illustrative model score', f'{probability:.0%}')
right.metric('Agreement with synthetic labels (holdout)', f'{agreement:.1%}')
st.caption('Scores reflect patterns in a fabricated mathematical label, NOT a probability of disease. Holdout agreement is NOT clinical accuracy.')
st.progress(probability)
st.subheader('Rule-based demo observations (not medical advice)')
notes = []
if values['Sleep hours'] < 7: notes.append('The simulated sleep duration is below the demo reference of 7 hours.')
if values['Daily steps'] < 5000: notes.append('The simulated daily steps are below the demo reference of 5,000.')
if values['HRV'] < 30: notes.append('The simulated HRV is below an arbitrary demo reference of 30 ms.')
if not notes: notes.append('No demo reference flags were triggered by these fictional inputs.')
for note in notes: st.info(note)

st.subheader('Seven-day synthetic wearable timeline')
rng = np.random.default_rng(101)
dates = pd.date_range(end=pd.Timestamp('2026-10-20'), periods=7)
timeline = pd.DataFrame({'Date': dates, 'Resting HR': np.clip(values['Resting HR'] + rng.normal(0, 4, 7), 45, 120), 'HRV': np.clip(values['HRV'] + rng.normal(0, 7, 7), 5, 120), 'Sleep hours': np.clip(values['Sleep hours'] + rng.normal(0, .7, 7), 3, 11), 'Daily steps': np.clip(values['Daily steps'] + rng.normal(0, 1200, 7), 0, 20000).astype(int)}).set_index('Date')
st.line_chart(timeline[['Resting HR', 'HRV']])
st.line_chart(timeline[['Sleep hours']])
st.bar_chart(timeline[['Daily steps']])
st.download_button('Download synthetic timeline CSV', timeline.to_csv().encode(), 'synthetic_timeline.csv', 'text/csv')
st.subheader('Model feature importance (synthetic label only)')
importance = pd.Series(model.feature_importances_, index=FEATURES).sort_values(ascending=False)
st.bar_chart(importance)
with st.expander('Inspect synthetic training data'):
    st.dataframe(generate_data().head(30), use_container_width=True)
st.caption('All profiles, training records, wearable signals and observations are fictional. No real wearable, EHR, cloud, or clinical integration exists.')
