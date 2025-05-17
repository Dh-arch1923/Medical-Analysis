
import streamlit as st
import pickle

# Load the condition model
with open('condetion.pkl', 'rb') as f:
    condetion_model = pickle.load(f)

# Load the drug model
with open('drug.pkl', 'rb') as f:
    drug_model = pickle.load(f)

# Load the preprocessing_text function
with open('preprocessing_text.pkl', 'rb') as f:
    preprocessing_text = pickle.load(f)

st.title("💊 Predict Drug & Condition from Patient Review")

review = st.text_area("📝 Enter a Patient Review:")
if st.button('Predict'):
    if review.strip() != "":
        preprocessed = preprocessing_text(review)
        if isinstance(preprocessed, str):
            preprocessed = [preprocessed]

        predict_condetion = condetion_model.predict(preprocessed)[0]
        predict_drug = drug_model.predict(preprocessed)[0]

        st.success(f"The condition is: **{predict_condetion}**")
        st.success(f"The drug is: **{predict_drug}**")
    else:
        st.warning("Please enter the review to make the prediction")
