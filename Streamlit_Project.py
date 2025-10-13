import streamlit as st


Menu = st.sidebar.radio("Menu",["Form","CSV Uploader","Image Gallery"])


if Menu == "Form":
    st.title("User Information Form")
    
    with st.form("my_form"):

        f_name = st.text_input(label="Enter Your Name:",value="")
        f_age = st.number_input(label="Enter Your Age:",step=1,min_value=1,max_value=110)
        st.write("age is",f_age)

        f_feedback = st.text_area(label="Your feedback")
        f_agreement = st.checkbox(label="I Accept the Terms and Conditions")

        f_gender = st.radio(label="Gender",options=["Male","Female","Other"])

        f_workdays = st.slider(label="how many days do you work per week?",min_value=1,max_value=7,step=1)

        f_submit = st.form_submit_button(label="Submit")
        if f_submit:
            if f_agreement:

                st.markdown(f" <span style='color:green; background-color: honeydew;padding: 3px 6px; border-radius: 4px;'>Thank You for Submitting,{f_name}!</span>", unsafe_allow_html=True)
                st.write("Age:",f_age)
                st.write("Feedback:",f_feedback)
                st.write("Gender:",f_gender)
                st.write("Days Active per Week:",f_workdays)
                st.write("You have Accepted the Terms and Condition.")

            elif not f_agreement:

                st.markdown(":red[please accept the Terms and Condition...]")


if Menu == "CSV Uploader":
    form = st.form("my_form2")
    form.slider("Inside the form")
    st.slider("Outside the form")

    # Now add a submit button to the form:
    form.form_submit_button("Submit")