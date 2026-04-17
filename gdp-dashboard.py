import streamlit as st
import pandas as pd
import requests
import io

# إعداد الصفحة لتعمل بشكل ممتاز على الموبايل
st.set_page_config(page_title="GDP Dashboard 2026", layout="wide")

st.title("📊 لوحة تحكم الناتج المحلي الإجمالي - تحديث حي")

# ضع المعرف (ID) الخاص بجدولك هنا (النص بين /d/ و /edit)
SHEET_ID = "ضع_هنا_المعرف_الخاص_بجدولك"
url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"

try:
    # طلب البيانات مع فرض الترميز العالمي UTF-8
    response = requests.get(url)
    response.encoding = 'utf-8'
    
    if response.status_code == 200:
        df = pd.read_csv(io.StringIO(response.text))
        st.success("✅ تم الاتصال بنجاح! البيئة الآن مستقرة (3.11).")
        
        # عرض البيانات
        st.dataframe(df, use_container_width=True)
        
        # رسم بياني للنمو
        if not df.empty:
            st.line_chart(df.set_index(df.columns[0]))
    else:
        st.error(f"خطأ 404: تأكد من 'صلاحية المشاركة' في جوجل شيت.")

except Exception as e:
    st.error(f"تنبيه: {str(e)}")
