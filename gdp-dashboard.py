import streamlit as st
import pandas as pd

# إعداد الصفحة
st.set_page_config(page_title="GDP Dashboard 2026", layout="wide")
st.title("📊 لوحة تحكم الناتج المحلي الإجمالي")

# ⚠️ التعديل هنا فقط يا هندسة ⚠️
# امسح الرابط التجريبي اللي تحت ده وحط رابط جدولك الحقيقي مكانه
RAW_URL = "https://docs.google.com/spreadsheets/d/1XyZ_ضع_رابط_جدولك_هنا/edit"

try:
    # تحويل الرابط تلقائياً لصيغة البيانات
    csv_url = RAW_URL.replace("/edit", "/export?format=csv") if "/edit" in RAW_URL else RAW_URL
    
    # قراءة البيانات
    df = pd.read_csv(csv_url)
    
    st.success("✅ الله المستعان.. تم الاتصال بنجاح!")
    
    # عرض البيانات
    st.subheader("📋 جدول البيانات")
    st.dataframe(df, use_container_width=True)
    
    # رسم بياني
    st.subheader("📈 التحليل البياني")
    st.line_chart(df.set_index(df.columns[0]))

except Exception as e:
    st.error("لم يتم العثور على الرابط الصحيح بعد.")
    st.info("تأكد أن الرابط يبدأ بـ https وينتهي بـ /edit")
