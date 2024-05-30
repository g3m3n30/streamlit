import streamlit as st
import gspread
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

cred_1 ={
  "type": "service_account",
  "project_id": "vivid-osprey-374312",
  "private_key_id": "3ad4ee4a8f1b14ef26ee1c5a5ad3ddb84089d37b",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDPFsUumNJ0Um8g\nDVueXB5fi8nf80xn8qC2+NIuV4YG32dh7TTwWeC8vwVALdjIr3+Xo2aksWrRYp6D\nFm5MlPePKZYaEbH8/59J+6E+fcCR49grdvXcPSOo+oHSMre1k7+ka6ZtULDnesuK\ngIncv1HQPK/0R+3kI/7k+kmyAGXIjHrT/C0j5+L2ejmv7iHnryLDI3ntCopD7XRG\nmwfbJFwDS0ti+d+4tlLQpZSVoam05GQn7/PQ/TixfA8oLpxhjm6LWL68YmU0iX1+\n7aCRxlZiadtT5Iml446quamuyC9Y8v8Bcasq30/c0v0h80Y9ofvOJOWQrcw+B/o7\nuMyJCiW3AgMBAAECggEAA5P6I4b3w+i/YMdk+NnQmzKtcerLPCngsFNLll9kF8RO\nY05s5ruMJYFgvtjL8RO52aM0x82vnHSJa+xm9Xhxb+N2Y3breK/rTvpDsUe3nGMF\nE3iCYPlxdJ73apapE+sR7u5T5CRLxNlwoNuoW3cMG9P176Y6gaxENYKZjrNxDsOj\n+reTilcy2ev8J6orUXgrJPGwT2r8M1YzjWOfYoRyu08BC5jsZBL/7qjYpTG6p1Xv\nBKQoIzu6GKJzdHIGdH9dcUTfUFcrXRrCAs77eZMZbF0A6QToWi/WAM1umujlQpKT\nw8sNKoGLs4IA3OJ/8P/ecI8j7yIRnk7uNbuIlhaxgQKBgQDoGWqgBmZX4oFrLD4Z\n0k+i+xYcTo2BnpA/7Aa9vjOpHREyp+JkQtaCWlQdC4U2iB7TbaSXBF4wVHm9QyVk\nvx4zcgh8P+s3KJJU3dUxrJXtvYwsz1YatX7jNUczG2nFegimvDmfjag6zngn1Tgd\nGJkd9amjqt6dYBY2qKa++IG7wQKBgQDkagh8x+FIgeJ7i9QiFth3A5/1v4FDzn7X\nJmPiPAbMbRtYRkoz3k+l4pYNMk6GE2Sln5PCOMtYdxxf3Bw7DuxJuelCvVEwjA0Q\nAk/o7c0VffVvDxxA31G2F0x281cj+yMXJoNqSq9i5Dg791dFl+1WBj606VnAh3UA\nFwJ05N+fdwKBgCde8FxW2ZN847E3Xw1oRIQEDZsdpBlhuVxugDI9imvcd2ddXSTe\nxZ51DiGjK6S1cG0zAyFu5z9RhRkaw8QUO15EsLXK7e58Xl4xBxIXEZOzfIy5WwTK\n1sxZ5EsCEm4iJkeKVEgBcpEPJwiyvYMKAic33d/ag0q02u/IqghpBTDBAoGBAKIf\n1NhkszXY4x2YGUD9ADYxf3dZr3GmfwdNO3ZX7udoxhD5CzAXqmbvFlxVicDGwRiB\n1Mn1r/ehy6UKwYr1w6ds6vExGRChR6BGU9vb9kY7+loS2pX9LK1XijGf9QkX90c2\nUe6/Bg/mNzfxDqPZ+16k3htgyhDK1LP0oQzBayxvAoGAFqD6oBZClUPvJSuQCW/g\nQzIPTb+BKWizobzqxrkzIBRlljvUDKMn5puizsP1mpQji7e/24Na8yklTYAIhMB+\n49ANsICSHbOJSfYfPZ62GtagLgECmtOYKeigvvByGQh8CzsNotzzuhnbx1Hm4sZt\n9rQjcSTw8mTXnb4ezNmXkO8=\n-----END PRIVATE KEY-----\n",
  "client_email": "binancedatascrape@vivid-osprey-374312.iam.gserviceaccount.com",
  "client_id": "115884127362060148149",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/binancedatascrape%40vivid-osprey-374312.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

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
