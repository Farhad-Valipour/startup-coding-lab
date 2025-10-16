import streamlit as st
import pandas as pd
from PIL import Image


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


elif Menu == "CSV Uploader":
    st.title("CSV Uploader & Interactive Table")
    csv_uploaded = st.file_uploader(label="Upload CSV", type='CSV', help="open a csv file!")

    def search_in_df(df, keyword):
        keyword = str(keyword).lower().strip()
        if not keyword:
            return df  # اگر جستجو خالی بود، دیتافریم اصلی را برگردان
        matched_rows = []
        for i, row in df.iterrows():
            for col in df.columns:
                cell_value = str(row[col]).lower()
                if keyword in cell_value:
                    matched_rows.append(i)
                    break
        return df.loc[matched_rows]

    def show_df_result(df):
        row_count = df.shape[0]
        page_count = max(1, (row_count - 1) // 10 + 1)  # حداقل یک صفحه وجود دارد
        page_number = st.slider(label="Select Page", min_value=1, max_value=page_count, value=1)
        df_row_start, df_row_end = (page_number - 1) * 10, page_number * 10
        st.dataframe(df.iloc[df_row_start:df_row_end], selection_mode="single-row")

    if csv_uploaded:
        df = pd.read_csv(csv_uploaded)
        st.write("Data Table")

        search_item = st.text_input(label="Search")
        sort_by_column = st.selectbox(label="Sort by Column:", options=df.columns)
        df_sorted = df.sort_values(by=sort_by_column)

        # اگر چیزی در سرچ نوشته شده بود، دیتافریم فیلترشده را بگیر
        df_to_show = search_in_df(df_sorted, search_item)
        show_df_result(df_to_show)

        
elif Menu == "Image Gallery":
    st.title("Image Galley")

    image_files = st.file_uploader(label="open an image",type=["jpg", "jpeg", "ong"],accept_multiple_files=True)

    if image_files:

        cols = st.columns(len(image_files))
        
        for i , file in enumerate(image_files):
            img = Image.open(file)
            img.thumbnail((150,150))

            with cols[i]:
                st.image(img)






    


