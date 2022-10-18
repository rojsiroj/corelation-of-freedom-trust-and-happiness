import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
import streamlit as st


def getLinkSource(period):
    return 'https://www.kaggle.com/datasets/unsdsn/world-happiness?select=%s.csv' % period


def spaces(count=1):
    for i in range(count):
        st.write('\n')


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


st.markdown("""
<style>
.text-font {
    font-size:14pt !important;
}
.font-bold{
    font-weight: bold !important;
}
.text-center{
    text-align: center !important;
}
.text-justify{
    text-align: justify !important;
}
</style>
""", unsafe_allow_html=True)

# Streamlit
with st.sidebar:
    selectPeriod = st.select_slider(
        "Tahun", ["2015", "2016", "2017", "2018", "2019"])
st.title("Korelasi antara tingkat kebebasan dengan tingkat kesejahteraan dan Ekonomi masyarakat".title())
st.markdown('<p class="text-font text-justify">Kebebasan telah menjadi komponen hidup yang sangat penting terutama bagi kebanyakan <i>milenial</i> dan <i>gen z</i>. Namun apakah keinginan manusiawi untuk meraih kebebasan (<i>Freedom to make life choice</i>) tersebut memiliki dampak terhadap ekonomi serta kesejahteraan masyarakat secara umum dan selalu memiliki korelasi yang selaras?</p>', unsafe_allow_html=True)

st.markdown('<p class="text-font">Mari kita lihat dalam diagram berikut:</p>',
            unsafe_allow_html=True)

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
    st.markdown('<p class="text-font font-bold text-center">Korelasi antara kebebasan dan kesejahteraan masyarakat pada %s</p>' %
                selectPeriod, unsafe_allow_html=True)
    plt.scatter(df['freedom'], df['happiness_score'])
    plt.xlabel("Freedom")
    plt.ylabel("Happiness Score")
    st.write(fig)

with cf2:
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    st.markdown('<p class="text-font font-bold text-center">Korelasi antara kebebasan dengan GDP (PDB) pada %s</p>' %
                selectPeriod, unsafe_allow_html=True)
    plt.scatter(df['freedom'], df['economy_gdp'])
    plt.xlabel("Freedom")
    plt.ylabel("GDP")
    st.write(fig)
st.info('Sumber: %s' % getLinkSource(selectPeriod))


spaces(2)
st.markdown('<p class="text-font text-justify">Menurut kedua diagram di atas, memang cenderung selaras antara tingkat kebebasan (<i>freedom</i>) dengan tingkat <i>GDP</i> serta kesejahteraan (<i>happiness score</i>), namun ada beberapa anomali terutama yang terlihat jelas tedapat dalam beberapa data terakhir dengan tingkat <i>freedom</i> yang tinggi namun memiliki <i>GDP</i> serta <i>happiness score</i> yang rendah. Mengapa hal tersebut dapat terjadi?</p>', unsafe_allow_html=True)
spaces(1)
st.markdown(
    '''<p class="text-font text-justify">Kebebasan memang diinginkan semua orang, namun ketika sesuatu yang diinginkan itu diberikan secara berlebihan, maka akan berakibat buruk. Seperti dalam segi ekonomi suatu negara yang terlalu bebas (<i>liberalis</i>) maka akan berakibat buruk terhadap perekonomian negara itu sendiri.  
    Seperti mengutip dari <a href="https://nasional.kompas.com/read/2018/01/26/08294921/apakah-demokrasi-liberal-sungguh-menyejahterakan-masyarakat" target="_blank">kompas.com</a>, <b><i>Joseph Stiglitz</i></b> pada kuliah umum di Central Europe University, Budapest, Hungaria, awal November 2014 pernah berpendapat bahwa dengan membiarkan pasar bergerak dalam logika self regulating market (pasar bebas), maka pemerintah juga telah melebarkan kesempatan (<i>opportunity</i>) bagi kelompok-kelompok masyarakat kaya untuk terus memperkaya diri bahkan sampai mengeksploitasi kekayaan masyarakat menengah ke bawah.</p>''', unsafe_allow_html=True)

st.markdown(
    '<p class="text-font text-justify">Untuk lebih jelasnya, kita dapat melihat geoheatmap berikut:</p>', unsafe_allow_html=True)

spaces(2)
st.markdown('<p class="text-font text-center font-bold">Negara Berdasarkan <i>Freedom Score</i> Pada Tahun 2019',
            unsafe_allow_html=True)
st.image('images/freedom.png')

spaces(3)
st.markdown('<p class="text-font text-center font-bold">Negara Berdasarkan <i>GDP</i> (PDB) Pada Tahun 2019',
            unsafe_allow_html=True)
st.image('images/gdp.png')

spaces(3)
st.markdown('<p class="text-font text-center font-bold">Negara Berdasarkan <i>Happiness Score</i> Pada Tahun 2019',
            unsafe_allow_html=True)
st.image('images/happiness.png')

spaces(3)
st.markdown('<p class="text-font text-center font-bold">Negara Berdasarkan <i>Happiness Rank</i> Pada Tahun 2019',
            unsafe_allow_html=True)
st.image('images/happiness_rank.png')


st.info('Sumber: %s' % getLinkSource(2019))


st.markdown('''<p class="text-font text-justify">Dapat kita lihat contohnya pada data tahun 2019 di atas, Uzbekistan merupakan negara dengan tingkat <i>freedom</i> tertinggi namun dalam hal kesejahteraan rakyatnya berada di posisi ke-41. Mengapa hal tersebut dapat terjadi? Apakah berarti tidak ada korelasi antara kebebasan, kesejahteraan, serta ekonomi?  
            Perlu diketahui bahwa Uzbekistan merupakan negara paling korup ke-153 dari 180 negara (<a href="https://www.transparency.org/en/cpi/2019/index/uzb" target="_blank">lihat sumber</a>), sedangkan negara Sweden yang merupakan perinkat ke-10 dalam <i>freedom score</i> menempati posisi ke-4 dalam negara paling anti korup (<a href="https://www.transparency.org/en/cpi/2019/index/swe" target="_blank">lihat sumber</a>). Itu berarti apa yang dikatakan oleh Joseph Stiglitz di atas tentang semakin bebas suatu negara maka semakin besar kesempatan orang kaya untuk mengeksploitasi masyarakat menengah ke bawah adalah benar menurut data pada 2019 tersebut.</p>''', unsafe_allow_html=True)

spaces(2)
st.markdown('<p class="text-font font-bold">Kesimpulan</p>',
            unsafe_allow_html=True)
st.markdown('''<p class="text-font text-justify">Berdasarkan data di atas dapat disimpulkan bahwa peningkatan <i>Freedom Score</i> tidak selalu beriringan dengan peningkatan <i>GDP</i> atau <i>Happiness Score</i>. Bahkan Semakin bebas suatu negara maka akan semakin rentan untuk terjadi apa yang dikhawatirkan oleh Joseph Stiglitz di atas sehingga alih-alih membuat pertumbuhan <i>GDP<i> dan <i>happiness score<i> terus naik malah membuatnya stagnan atau bahkan cenderung menurun. Namun semakin tidak bebas juga suatu negara maka tingkat kesejahteraan serta GDP negara tersebut akan sangat sulit untuk bertumbuh.</p>''', unsafe_allow_html=True)
# Footer
st.markdown(
    "<p style='text-align: center; color: grey; margin-top: 100px;'>&copy; 2022  by <a href='https://github.com/rojsiroj' target='_blank'>Muhamad Sirojudin</a> TETRIS PROA CAPSTONE PROJECT</p>", unsafe_allow_html=True)
