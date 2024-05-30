import streamlit as st
import gspread
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

cred_1 ={}

# Authenticate with Google Sheets
# gc = gspread.service_account(filename=cred_1)
gc = gspread.service_account_from_dict(cred_1)

# Function to get data from Google Sheets
def get_data(sheet_name, worksheet_name):
    sh = gc.open(sheet_name).worksheet(worksheet_name)
    data = sh.get_all_values()
    headers = data.pop(0)
    df = pd.DataFrame(data, columns=headers)
    return df

# Function to create interactive chart
def create_chart(df):
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=df['Date'], y=df['SELL (MMK)'], name='Price'), secondary_y=False)
    fig.update_layout(title='Historical Price Chart', xaxis_title='Date', yaxis_title='Price')
    return fig

# Main function to run the Streamlit app
def main():
    st.title('Historical Price Chart')
    
    # Get data from Google Sheets
    sheet_name = 'Binance USDT-MMK tracker'
    worksheet_name = 'sheet1'
    df = get_data(sheet_name, worksheet_name)
    
    # Display raw data if needed
    st.subheader('Raw Data')
    st.write(df)
    
    # Create interactive chart
    st.subheader('Interactive Chart')
    fig = create_chart(df)
    st.plotly_chart(fig)

if __name__ == '__main__':
    main()
