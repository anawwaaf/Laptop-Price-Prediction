import streamlit as st
import pandas as pd
import pickle

st.title("--Laptop Price Prediction--")

# Step 1 - import saved model
model = pickle.load(open("price_pred.pkl", "rb"))

st.write('Insert feature to predict')

# Step 2 - prepare input data for user
Inch = st.slider(label='Inch', min_value=10.3, max_value=17.3, value=13.0, step=0.1)
Rs_X = st.slider(label='Resolution X', min_value=1366, max_value=2880, value=1800, step=1)
Rs_Y = st.slider(label='Resolution Y', min_value=768, max_value=1800, value=900, step=1)
PPI = (Rs_X**2+Rs_Y**2)**0.5/Inch
CPU_GHz = st.slider(label='CPU GHz', min_value=1.0, max_value=3.4, value=2.4, step=0.1)
RAM_GB = st.selectbox(label='RAM GB', options=[2,4,6,8,12,16,32], key=1)
HDD = st.selectbox(label='HDD GB', options=[0, 32,128,500,1000,2000])
SSD = st.selectbox(label='SSD GB', options=[0, 8,16,32,128,256,512,1024])
Total_Storage_GB = RAM_GB+HDD+SSD
Flash = st.selectbox(label='Flash Storage GB', options=[0,16,32,64,128,256,512])
Laptop_Brand = st.selectbox(label='Laptop', options=['Lenovo', 'HP', 'Dell', 'Asus', 'Acer', 'Toshiba', 'MSI'])
Laptop_Type = st.selectbox(label='Laptop Type', options=['Notebook', 'Ultrabook', 'Gaming', '2 in 1 Convertible'])
OS_Laptop = st.selectbox(label='Laptop Type', options=['Windows', 'Linux', 'DOS'])
CPU_Model = st.selectbox(label='Laptop Type', options=['Intel Celeron Dual', 'Intel Core i3', 'Intel Core i5', 'Intel Core i7', 'AMD Ryzen 1700', 'AMD A9-Series 9420', 'AMD A10-Series 9600P','AMD A12-Series 9720P'])
GPU = st.selectbox(label='GPU', options=['Intel HD Graphics 520', 'Intel HD Graphics 620', 'Intel Iris Plus Graphics 640', 'Intel UHD Graphics 620', 'Nvidia GeForce MX150', 'Nvidia GeForce 920MX', 'Nvidia GeForce 930MX', 'Nvidia GeForce GTX 1050', 'Nvidia GeForce GTX 1050 Ti', 'Nvidia GeForce GTX 1080', 'AMD Radeon RX 580', 'AMD Radeon RX 560', 'AMD Radeon R9 M385', 'AMD Radeon R7 M445', 'AMD Radeon R5 M430', 'AMD Radeon R5', 'AMD Radeon 530'])
TouchScreen = st.selectbox(label='Touch Screen 0_No 1_Yes', options=[0, 1])

# convert into dataframe
data = pd.DataFrame({'PPI':[PPI],
 'CPU_GHz':[CPU_GHz],
 'RAM_GB':[RAM_GB],
 'Total_Storage_GB': [Total_Storage_GB],
 'Laptop_Brand':[Laptop_Brand],
 'Laptop_Type':[Laptop_Type],
 'OpSys':[OS_Laptop],
 'CPU_Model':[CPU_Model],
 'GPU':[GPU],
 'TouchScreen':[TouchScreen]
                })
st.write(data)
# model predict
clas = model.predict(data).tolist()[0]

# interpretation
st.write('Price Prediction Result: ', round(clas,2), 'Euro')


