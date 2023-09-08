import streamlit as st
import pickle

st.title("TITANIC SURVIVAL PREDICTION")

pclass= st.number_input('Enter pclass(1,2,3)',min_value=1, max_value=3) 

sex= st.radio('FEMALE/MALE',[0,1])   #female is 0 ,male is 1

age=st.number_input('Enter age')

sibsp= st.number_input('Sibsp (0,1,2,3)',min_value=0, max_value=3) #no. of siblings

parch= st.number_input('Parch (0,1,2)',min_value=0, max_value=2) #no. of parents

fare = st.number_input('Enter Fare') 

uploaded_file = st.file_uploader(
    "Choose your database", accept_multiple_files=False)
if uploaded_file is not None:
    file_name = uploaded_file
else:
    file_name = "titanic.csv"
 
clicked=st.button('Get prediction')
print(clicked)   

#LOADING THE MODEL
with open('model.pkl', 'rb') as f:
    model= pickle.load(f)     
    
if clicked==True:  
    #take the data and predict survived/dead.
     data=[pclass,sex,age,sibsp,parch,fare]  
     print(data)        

     pred = model.predict([data])[0] 
     if (pred==0):
        st.header("NOT SURVIVED")
     else:
        st.header("SURVIVED")






