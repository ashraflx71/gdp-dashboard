import streamlit as st
import pandas as pd

st.title("📊 لوحة تحكم الناتج المحلي الإجمالي")

# استبدل ID_GOOOGLE_SHEET بالمعرف الخاص بجدولك
# المعرف هو النص الطويل الموجود في رابط الجدول بين /d/ و /edit
sheet_id = "ضع_هنا_رقم_التعريف_الخاص_بجدولك"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

try:
    df = pd.read_csv(url)
    st.success("✅ تم الاتصال بالبيانات بنجاح!")
    st.line_chart(df.set_index(df.columns[0]))
    st.dataframe(df)
except Exception as e:
    st.error(f"خطأ في الوصول: {e}")
    st.info("تأكد أن الجدول متاح للجميع (Anyone with the link can view)")
