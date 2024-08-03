import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide',page_title='StartUp Analysis')

df = pd.read_csv('startup_cleaned.csv')
df['date'] = pd.to_datetime(df['date'])
df['month'] = df.date.dt.month
df['year'] = df.date.dt.year

def load_overall_analysis():
    st.title('Overall Analysis')
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        # total invested amount
        total = round(df['amount'].sum())
        st.metric('Total Funding', str(total) + ' Cr')

    with c2:
        # maximum amount infused in a startup
        max_funding = df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
        st.metric('Max Funding', str(max_funding) + ' Cr' )

    with c3:
        # avg ticket size
        avg_funding = df.groupby('startup')['amount'].sum().mean()
        st.metric('Avg', str(round(avg_funding)) + ' Cr')

    with c4:
        # total funded startups
        num_startups = df['startup'].nunique()
        st.metric('Funded Startups',num_startups)

    st.header('MoM Graph')

    selected_option = st.selectbox('Select Type', ['Total', 'Count'], key='options')
    if selected_option == 'Total':
        temp_df = df.groupby(['year', 'month']).amount.sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month']).amount.count().reset_index()

    temp_df['x_axis'] = temp_df['month'].astype(str) + '-' + temp_df['year'].astype(str)

    fig, ax = plt.subplots()
    ax.plot(temp_df['x_axis'], temp_df['amount'])

    st.pyplot(fig)


def load_investor_details(investor):
    st.title(investor)
    # load the recent 5 investments of investor
    last5_df = df[df.investors.str.contains(investor)].head()[
        ['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader('Most recent investments')
    st.dataframe(last5_df)

    c1, c2 = st.columns(2)

    with c1:
        # Top 5 biggest investments
        big_series = df[df.investors.str.contains(investor)].groupby('startup').amount.sum().sort_values(
            ascending=False).head()
        st.subheader('Biggest investments')
        fig, ax = plt.subplots()
        ax.bar(big_series.index, big_series.values)

        st.pyplot(fig)

    with c2:
        vertical_series = df[df.investors.str.contains(investor)].groupby('vertical')['amount'].sum()
        st.subheader('Sectors Invested In')
        fig1, ax1 = plt.subplots()
        ax1.pie(vertical_series,labels=vertical_series.index,autopct='%0.01f%%')

        st.pyplot(fig1)

    c3, c4 = st.columns(2)

    with c3:
        round_series = df[df.investors.str.contains(investor)].groupby('round')['amount'].sum()
        st.subheader('Investor Stages')
        fig2, ax2 = plt.subplots()
        ax2.pie(round_series, labels=round_series.index, autopct='%0.01f%%')

        st.pyplot(fig2)

    with c4:
        city_series = df[df.investors.str.contains(investor)].groupby('city')['amount'].sum()
        st.subheader('Cities Invested In')
        fig3, ax3 = plt.subplots()
        ax3.pie(city_series, labels=city_series.index, autopct='%0.01f%%')

        st.pyplot(fig3)

    c5, c6 = st.columns(2)

    with c5:
        df['year'] = df['date'].dt.year
        year_series = df[df.investors.str.contains(investor)].groupby('year')['amount'].sum()
        st.subheader('YoY Investment')
        fig4, ax4 = plt.subplots()
        ax4.plot(year_series.index, year_series.values)

        st.pyplot(fig4)


st.sidebar.title('Startup Funding Analysis')

st.session_state.option = st.sidebar.selectbox(

    'Select One', ['Overall Analysis', 'StartUp', 'Investor'], key='unique')

option = st.session_state.option

if option == 'Overall Analysis':

    load_overall_analysis()
if option == 'Overall Analysis':
    btn0 = st.sidebar.button('Show Overall Analysis')
    if btn0:
        load_overall_analysis()
elif option == 'StartUp':
    st.sidebar.selectbox('Select StartUp', sorted(df['startup'].unique().tolist()))
    btn1 = st.sidebar.button('Find StartUp Details')
    st.title('StartUp Analysis')
else:
    selected_investor = st.sidebar.selectbox('Select Investor', sorted(set(df['investors'].str.split(',').sum())))
    btn2 = st.sidebar.button('Find Investor Details')
    if btn2:
        load_investor_details(selected_investor)
