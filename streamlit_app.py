
streamlit_app.py
import streamlit as st
import pandas as pd

st.title("📊 لوحة تحليل الناتج المحلي (GDP)")
st.success("تم تشغيل التطبيق بنجاح بعد إضافة الكود!")

# بيانات تجريبية
data = {'السنة': [2020, 2021, 2022, 2023], 'GDP': [350, 410, 480, 520]}
df = pd.DataFrame(data)

st.line_chart(df.set_index('السنة'))
st.write("هذه لوحة بيانات تفاعلية بسيطة.")
requirements.txt