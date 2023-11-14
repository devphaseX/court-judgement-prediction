import joblib
import streamlit as st

model = joblib.load('./RF_model.pkl')

def predict(facts):
    input = facts
    prediction = model.predict(input)

def main():
    st.title('Court Facts')

    facts= st.text_input('Enter your facts',)

    if st.button('Predict facts'):
        output = predict(facts)
        if (output== 0):
            st.write('False')
        else:
            st.write('True')
if __name__=='__main__':
    main()
