import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="University Dashboard", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv('university_student_data.csv')
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df

df = load_data()

st.title("🎓 University Student Data Dashboard")

st.sidebar.header("Filtros")

years = st.sidebar.multiselect("Seleccionar Año:", sorted(df['year'].unique()), default=sorted(df['year'].unique()))
terms = st.sidebar.multiselect("Seleccionar Periodo (Term):", sorted(df['term'].unique()), default=sorted(df['term'].unique()))

filtered = df[(df['year'].isin(years)) & (df['term'].isin(terms))]

col1, col2 = st.columns(2)
col1.metric("📈 Promedio Retención (%)", f"{filtered['retention_rate_(%)'].mean():.2f}")
col2.metric("😊 Promedio Satisfacción (%)", f"{filtered['student_satisfaction_(%)'].mean():.2f}")

st.subheader("Evolución de la Tasa de Retención (%) por Año")
fig1, ax1 = plt.subplots()
sns.lineplot(data=filtered, x='year', y='retention_rate_(%)', marker='o', ax=ax1)
st.pyplot(fig1)

st.subheader("Satisfacción Promedio (%) por Año")
fig2, ax2 = plt.subplots()
sns.barplot(data=filtered, x='year', y='student_satisfaction_(%)', ax=ax2)
st.pyplot(fig2)

st.subheader("Comparación de Satisfacción (%) entre Spring y Fall")
fig3, ax3 = plt.subplots()
sns.boxplot(data=filtered, x='term', y='student_satisfaction_(%)', ax=ax3)
st.pyplot(fig3)

st.markdown("---")
st.markdown("📘 *Dashboard interactivo creado con Streamlit Cloud*")
