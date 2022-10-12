import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(layout='wide')

# Cleansing Data
df2015 = pd.read_csv('dataset/2015.csv')
df2015 = df2015.drop(df2015.columns[[1, 4, 6, 10, 11]], axis=1)
df2015 = df2015.rename(columns={'Country': 'country', 'Happiness Rank': 'happiness_rank', 'Happiness Score': 'happiness_score',
                       'Health (Life Expectancy)': 'life_expextancy', 'Economy (GDP per Capita)': 'economy_gdp', 'Freedom': 'freedom', 'Trust (Government Corruption)': 'trust_goverment'})


df2016 = pd.read_csv('dataset/2016.csv')
df2016 = df2016.drop(df2016.columns[[1, 4, 5, 7, 11, 12]], axis=1)
df2016 = df2016.rename(columns={'Country': 'country', 'Happiness Rank': 'happiness_rank', 'Happiness Score': 'happiness_score',
                       'Health (Life Expectancy)': 'life_expextancy', 'Economy (GDP per Capita)': 'economy_gdp', 'Freedom': 'freedom', 'Trust (Government Corruption)': 'trust_goverment'})

df2017 = pd.read_csv('dataset/2017.csv')
df2017 = df2017.drop(df2017.columns[[3, 4, 6, 9, 11]], axis=1)
df2017 = df2017.rename(columns={'Country': 'country', 'Happiness.Rank': 'happiness_rank', 'Happiness.Score': 'happiness_score',
                       'Health..Life.Expectancy.': 'life_expextancy', 'Economy..GDP.per.Capita.': 'economy_gdp', 'Freedom': 'freedom', 'Trust..Government.Corruption.': 'trust_goverment'})

df2018 = pd.read_csv('dataset/2018.csv')
df2018 = df2018.drop(df2018.columns[[4, 7]], axis=1)
df2018 = df2018.rename(columns={'Country or region': 'country', 'Overall rank': 'happiness_rank', 'Score': 'happiness_score', 'Healthy life expectancy': 'life_expextancy',
                       'GDP per capita': 'economy_gdp', 'Freedom to make life choices': 'freedom', 'Perceptions of corruption': 'trust_goverment'})

df2019 = pd.read_csv('dataset/2019.csv')
df2019 = df2019.drop(df2019.columns[[4, 7]], axis=1)
df2019 = df2019.rename(columns={'Country or region': 'country', 'Overall rank': 'happiness_rank', 'Score': 'happiness_score', 'Healthy life expectancy': 'life_expextancy',
                       'GDP per capita': 'economy_gdp', 'Freedom to make life choices': 'freedom', 'Perceptions of corruption': 'trust_goverment'})


# Streamlit
with st.sidebar:
    selectPeriod = st.select_slider(
        "Tahun", ["2015", "2016", "2017", "2018", "2019"])
st.title("Korelasi antara tingkat kebebasan (Freedom to make life choice) di suatu negara dengan tingkat pendapatan serta kesejahteraan masyarakatnya pada tahun 2015-2019")

if (selectPeriod == '2015'):
    df = df2015
elif (selectPeriod == '2016'):
    df = df2016
elif (selectPeriod == '2017'):
    df = df2017
elif (selectPeriod == '2018'):
    df = df2018
elif (selectPeriod == '2019'):
    df = df2019
else:
    df = df2019

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
st.header(
    'Korelasi antara kebebasan dan kesejahteraan masyarakat pada %s' % selectPeriod)
plt.scatter(df['freedom'], df['happiness_score'])
plt.xlabel("Freedom")
plt.ylabel("Happiness Score")
st.write(fig)
st.info('Sumber: %s' %
        'https://www.kaggle.com/datasets/unsdsn/world-happiness?select=2015.csv')


fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
st.header(
    'Korelasi antara kebebasan dan GDP pada %s' % selectPeriod)
plt.scatter(df['freedom'], df['economy_gdp'])
plt.xlabel("Freedom")
plt.ylabel("GDP")
st.write(fig)
st.info('Sumber: %s' %
        'https://www.kaggle.com/datasets/unsdsn/world-happiness?select=2015.csv')
