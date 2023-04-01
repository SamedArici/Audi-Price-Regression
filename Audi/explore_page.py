import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

import plotly.express as px

import warnings
warnings.filterwarnings("ignore")

def shorten_models(models,cutoff):
    model_map = {}
    for i in range(len(models)):
        if models.values[i] >= cutoff:
            model_map[models.index[i]] = models.index[i]

        else:
            model_map[models.index[i]] = "Other"
            
    return model_map

@st.cache_data  
def load_data():
    audi = pd.read_csv('audi.csv')
    df = audi.copy()
    df.columns = map(str.lower,df.columns)

    df['model'] = df['model'].apply(str.strip)

    model_map = shorten_models(df['model'].value_counts(),300)
    df['model'] = df['model'].map(model_map)

    df = df[df['fueltype'] != 'Hybrid']

    return df

df = load_data()


def show_explore_page():

    st.title("Explore Audi Car Prices")

    models = df.groupby('model').mean()

    #--------------------------------------------------------------------------

    st.write(
    """
    ##
    #### Heatmap
    """
    )
    fig = px.imshow(df.corr(),text_auto=True,aspect='auto')
    st.plotly_chart(fig, theme="streamlit")

    #--------------------------------------------------------------------------
    
    st.write(
    """
    ##
    #### Distribution of Price
    """
    )
    fig = px.histogram(
    df,
    x="price"
    )
    st.plotly_chart(fig, theme="streamlit")

    #--------------------------------------------------------------------------

    st.write(
    """
    ##
    #### The Average Price of Each Model
    """
    )
    chart_data = models['price']
    st.bar_chart(chart_data)

    #--------------------------------------------------------------------------

    st.write(
    """
    ##
    #### The Average Tax Price of Each Model
    """
    )
    chart_data = models['tax']
    st.bar_chart(chart_data)

    #--------------------------------------------------------------------------
    
    st.write(
    """
    ##
    #### Counts of Cars by Models
    """
    )
    
    chart_data = df['model'].value_counts()
    st.bar_chart(chart_data)

    #--------------------------------------------------------------------------

    st.write(
    """
    ##
    #### Counts of Engine Sizes
    """
    )
    chart_data = df['enginesize'].value_counts()
    st.bar_chart(chart_data)

    #--------------------------------------------------------------------------

    st.write(
    """
    ##
    #### Price v Engine Size
    """
    )
    fig = px.box(df, x="enginesize", y="price")
    st.plotly_chart(fig, theme="streamlit")

    #--------------------------------------------------------------------------

    st.write(
    """
    ##
    #### Price v Year
    """
    )
    fig = px.scatter(
    df,
    x="year",
    y="price",
    color="price",
    color_continuous_scale="blues",
    )
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    #--------------------------------------------------------------------------

    st.write(
    """
    ##
    #### Price v MPG
    """
    )
    fig = px.scatter(
    df,
    x="mpg",
    y="price",
    color="price",
    color_continuous_scale="blues",
    )
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    #--------------------------------------------------------------------------

    st.write(
    """
    ##
    #### Price v Mileage
    """
    )
    fig = px.scatter(
    df,
    x="mileage",
    y="price",
    color="price",
    color_continuous_scale="blues",
    )
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    #--------------------------------------------------------------------------

    st.write(
    """
    ##
    #### Tax v MPG
    """
    )
    fig = px.scatter(
    df,
    x="mpg",
    y="tax",
    color="tax",
    color_continuous_scale="reds",
    )
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    #--------------------------------------------------------------------------

    st.write(
    """
    ##
    #### Tax v Engine Size
    """
    )
    fig = px.scatter(
    df,
    x="enginesize",
    y="tax",
    color="tax",
    color_continuous_scale="reds",
    )
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)


    #--------------------------------------------------------------------------

    st.write(
    """
    ##
    #### Mileage v Year
    """
    )
    fig = px.scatter(
    df,
    x="year",
    y="mileage",
    color="mileage",
    color_continuous_scale="ylgn",
    )
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    #--------------------------------------------------------------------------

    st.write(
    """
    ##
    #### Fueltype V Price
    """
    )
    fig = px.box(df, x="fueltype", y="price")
    st.plotly_chart(fig, theme="streamlit")

    #--------------------------------------------------------------------------

    st.write(
    """
    ##
    #### Fueltype V Tax
    """
    )

    fig = px.box(df, x="fueltype", y="tax")
    st.plotly_chart(fig, theme="streamlit")