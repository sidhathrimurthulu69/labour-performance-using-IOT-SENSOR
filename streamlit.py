#pip install streamlit
import streamlit as st  
import pickle
model = pickle.load(open('C:/Users/sidda/Desktop/assianment/demo/model1.pkl',  'rb'))



def main():
    st.title('labour performance')

    #input variables
    GENDER = st.text_input('GENDER')
    SITE = st.text_input('SITE')
    ROLE = st.text_input('ROLE')
    AGE = st.text_input('AGE')
    EXTRA_HOURS_WORKED = st.text_input('EXTRA HOURS WORKED')
    TOTAL_HOURS = st.text_input('TOTAL HOURS')
    ACTIVE_TIME_OF_WORKER = st.text_input('ACTIVE TIME OF WORKER')
    BODY_TEMP	 = st.text_input('BODY TEMP	')
    HAZARDIOUS = st.text_input('HAZARDIOUS')


    #prediction code
    if st.button('predict'):
        makeprediction = model.predict([[GENDER,SITE,ROLE,AGE,EXTRA_HOURS_WORKED,TOTAL_HOURS,ACTIVE_TIME_OF_WORKER,BODY_TEMP,HAZARDIOUS	]])
        output = round(makeprediction[0],2)
        st.success('labour performance is {}'.format(output))
if __name__ =='__main__':
    main()
