import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def getLinkSource(period):
    return 'https://www.kaggle.com/datasets/unsdsn/world-happiness?select=%s.csv' % period


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
st.title("Korelasi antara tingkat kebebasan (Freedom to make life choice) di suatu negara dengan tingkat pendapatan serta kesejahteraan masyarakatnya pada tahun 2015-2019".title())
st.markdown('Kebebasan telah menjadi komponen hidup yang sangat penting terutama bagi kebanyakan _milenial_ dan _gen z_. Namun apakah keinginan manusiawi untuk meraih kebebasan (_Freedom to make life choice_) tersebut memiliki dampak terhadap ekonomi serta kesejahteraan masyarakat secara umum dan selalu memiliki korelasi yang selaras?')

st.markdown('Mari kita lihat dalam diagram berikut:')

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

cf1, cf2 = st.columns(2)

with cf1:
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    st.header(
        'Korelasi antara kebebasan dan kesejahteraan masyarakat pada %s' % selectPeriod)
    plt.scatter(df['freedom'], df['happiness_score'])
    plt.xlabel("Freedom")
    plt.ylabel("Happiness Score")
    st.write(fig)
    st.info('Sumber: %s' % getLinkSource(selectPeriod))

with cf2:
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    st.header(
        'Korelasi antara kebebasan dan GDP (PDB) pada %s' % selectPeriod)
    plt.scatter(df['freedom'], df['economy_gdp'])
    plt.xlabel("Freedom")
    plt.ylabel("GDP")
    st.write(fig)
    st.info('Sumber: %s' % getLinkSource(selectPeriod))

st.markdown('Menurut kedua diagram di atas, memang cenderung selaras antara tingkat kebebasan (_freedom_) dengan tingkat _GDP_ serta kesejahteraan (_happiness score_), namun ada beberapa anomali terutama yang terlihat jelas tedapat dalam beberapa data terakhir dengan tingkat _freedom_ yang tinggi namun memiliki _GDP_ serta _happiness score_ yang rendah. Mengapa hal tersebut dapat terjadi?')

st.markdown(
    '''Kebebasan memang diinginkan semua orang, namun ketika sesuatu yang diinginkan itu diberikan secara berlebihan, maka akan berakibat buruk. Seperti dalam segi ekonomi suatu negara yang terlalu bebas (_liberalis_) maka akan berakibat buruk terhadap perekonomian negara itu sendiri.  
    Seperti mengutip dari [kompas.com](https://nasional.kompas.com/read/2018/01/26/08294921/apakah-demokrasi-liberal-sungguh-menyejahterakan-masyarakat), **_Joseph Stiglitz_** pada kuliah umum di Central Europe University, Budapest, Hungaria, awal November 2014 pernah berpendapat bahwa dengan membiarkan pasar bergerak dalam logika self regulating market (pasar bebas), maka pemerintah juga telah melebarkan kesempatan (_opportunity_) bagi kelompok-kelompok masyarakat kaya untuk terus memperkaya diri bahkan sampai mengeksploitasi kekayaan masyarakat menengah ke bawah.''')

st.markdown('Untuk lebih jelasnya, kita dapat melihat tabel berikut:')

c1, c2 = st.columns(2)
df2019freedom = df2019.sort_values(by='freedom', ascending=False)[['happiness_rank', 'country',
                                                                   'freedom', 'happiness_score', 'economy_gdp']]
with c1:
    st.header("10 Negara Dengan Freedom Score Paling Tinggi Pada Tahun 2019")
    st.table(df2019freedom.head(10).assign(
        number=[i for i in range(1, 11)]).set_index('number'))
    st.info('Sumber: %s' % getLinkSource(2019))

with c2:
    st.header("10 Negara Dengan Freedom Score Paling Rendah Pada Tahun 2019")
    st.table(df2019freedom.head(10).assign(
        number=[i for i in range(1, 11)]).set_index('number'))
    st.info('Sumber: %s' % getLinkSource(2019))

st.markdown('''Dapat kita lihat contohnya pada data tahun 2019 di atas, Uzbekistan merupakan negara dengan tingkat _freedom_ tertinggi namun dalam hal kesejahteraan rakyatnya berada di posisi ke-41. Mengapa hal tersebut dapat terjadi? Apakah berarti tidak ada korelasi antara kebebasan, kesejahteraan, serta ekonomi?  
            Perlu diketahui bahwa Uzbekistan merupakan negara paling korup ke-153 dari 180 negara hal ini [Sumber](https://www.transparency.org/en/cpi/2019/index/uzb), sedangkan negara Sweden yang merupakan perinkat ke-10 dalam _freedom score_ menempati posisi ke-4 dalam negara paling anti korup [Sumber](https://www.transparency.org/en/cpi/2019/index/swe). Itu berarti apa yang dikatakan oleh Joseph Stiglitz di atas tentang semakin bebas suatu negara maka semakin besar kesempatan orang kaya untuk mengeksploitasi masyarakat menengah ke bawah adalah benar menurut data pada 2019 tersebut.''')


st.header('Kesimpulan')
st.markdown('''Berdasarkan data di atas dapat disimpulkan bahwa peningkatan _Freedom Score_ tidak selalu beriringan dengan peningkatan _GDP_ atau _Happiness Score_. Bahkan Semakin bebas suatu negara maka akan semakin rentan untuk terjadi apa yang dikhawatirkan oleh Joseph Stiglitz di atas sehingga alih-alih membuat pertumbuhan _GDP_ dan _happiness score_ terus naik malah membuatnya stagnan atau bahkan cenderung menurun. Namun semakin tidak bebas juga suatu negara maka tingkat kesejahteraan serta GDP negara tersebut akan sangat sulit untuk bertumbuh.''')
# Footer
st.markdown(
    "<p style='text-align: center; color: grey; margin-top: 100px;'>&copy; 2022  by <a href='https://github.com/rojsiroj' target='_blank'>Muhamad Sirojudin</a> TETRIS PROA CAPSTONE PROJECT</p>", unsafe_allow_html=True)
