import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
st.set_page_config(page_title="Plotting Demo")
st.title('Analytics')

new_df = pd.read_csv('datasets/data_viz1.csv')
feature_text = pickle.load(open('datasets/feature_text.pkl', 'rb'))

cols = ['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']
for col in cols:
    new_df[col] = pd.to_numeric(new_df[col], errors='coerce')

group_df = new_df.groupby('sector')[cols].mean()

st.header('sector price per Sqft Geomap')
fig = px.scatter_mapbox(
    group_df,
    lat="latitude",
    lon="longitude",
    color="price_per_sqft",
    size="built_up_area",
    color_continuous_scale=px.colors.cyclical.IceFire,
    zoom=10,
    mapbox_style="open-street-map",
    width=1200,
    height=700,
    hover_name=group_df.index
)
st.plotly_chart(fig, use_container_width=True)

st.header('Features wordcloud')
wordcloud = WordCloud(
    width=800, height=800, background_color='white',
    stopwords=set(['S']), min_font_size=10
).generate(feature_text)

fig_wc, ax = plt.subplots(figsize=(8, 8))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
plt.tight_layout(pad=0)
st.pyplot(fig_wc)

st.header('Area vs Price')

property_type = st.selectbox('Select Property Type', ['Flat', 'House'])

if property_type == 'House':
    fig1 = px.scatter(
        new_df[new_df['property_type'] == 'house'],
        x="built_up_area",
        y="price",
        color="bedRoom",
        title="Area Vs Price"
    )
    st.plotly_chart(fig1, use_container_width=True)
else:
    fig1 = px.scatter(
        new_df[new_df['property_type'] == 'flat'],
        x="built_up_area",
        y="price",
        color="bedRoom",
        title="Area Vs Price"
    )
    st.plotly_chart(fig1, use_container_width=True)

st.header('BHK Pie Chart')
sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0, 'Overall')
selected_sector = st.selectbox('Select Sector', sector_options)

if selected_sector == 'Overall':
    fig2 = px.pie(new_df, names='bedRoom')
    st.plotly_chart(fig2, use_container_width=True)
else:
    fig2 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom')
    st.plotly_chart(fig2, use_container_width=True)


st.header('Side By Side BHK Price Comparison')
fig3 = px.box(new_df[new_df['bedRoom']<=4] , x='bedRoom',y='price',title='BHK Price Range')
st.plotly_chart(fig3, use_container_width=True)

st.header('Side By Side Distplot  For property Type')

fig4 = plt.figure(figsize=(10, 4))
sns.distplot(new_df[new_df['property_type'] == 'house']['price'], label='House')
sns.distplot(new_df[new_df['property_type'] == 'flat']['price'], label='Flat')
plt.legend()

st.pyplot(fig4)
