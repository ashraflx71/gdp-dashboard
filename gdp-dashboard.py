import streamlit as st
import pandas as pd
import requests
import io

# إعداد الصفحة
st.set_page_config(page_title="GDP Dashboard 2026", layout="wide")
st.title("📊 لوحة تحكم الناتج المحلي الإجمالي")

# 1. استبدل المعرف أدناه بالرقم فقط (تأكد أنه بين علامتي التنصيص وبدون مسافات)
SHEET_ID = "ضع_هنا_المعرف_الخاص_بجدولك"

# 2. بناء الرابط بطريقة تضمن عدم وجود حروف غريبة
url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv"

try:
    # جلب البيانات يدويًا لفرض الترميز الصحيح
    response = requests.get(url)
    
    # فرض ترميز UTF-8 لحل مشكلة الـ ascii نهائيًا
    response.encoding = 'utf-8' 
    
    if response.status_code == 200:
        # قراءة البيانات من النص المشفر بـ utf-8
        df = pd.read_csv(io.StringIO(response.text))
        
        if not df.empty:
            st.success("✅ تم الاتصال بنجاح وتجاوز خطأ الترميز!")
            
            # عرض الجدول
            st.write("### البيانات الحالية")
            st.dataframe(df, use_container_width=True)
            
            # رسم بياني
            st.write("### تحليل النمو")
            st.line_chart(df.set_index(df.columns[0]))
        else:
            st.warning("الجدول متصل ولكنه فارغ.")
    else:
        st.error(f"خطأ في الوصول للملف (404). تأكد من الـ ID ومن أن المشاركة Anyone with link.")

except Exception as e:
    # إظهار الخطأ بشكل مبسط
    st.error("حدث عائق تقني في قراءة البيانات.")
    st.info("تأكد أن نسخة بايثون في الإعدادات هي 3.11")
