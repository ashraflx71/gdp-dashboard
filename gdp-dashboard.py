import streamlit as st
import pandas as pd
import requests
import io

# إعداد الصفحة بلمسة فخمة تناسب مشروعك
st.set_page_config(page_title="GDP Dashboard 2026", layout="wide")

st.markdown("""
    <style>
    .main {
        background-color: #000000;
    }
    .stTitle {
        color: #FFD700;
    }
    </style>
    """, unsafe_allow_input=True)

st.title("📊 لوحة تحكم الناتج المحلي الإجمالي - تحديث حي")

# استبدل المعرف أدناه بالمعرف الخاص بجدولك (ID فقط)
SHEET_ID = "ضع_هنا_المعرف_الخاص_بجدولك"

# الرابط بصيغة التصدير المباشر
url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"

try:
    # جلب البيانات مع فرض ترميز UTF-8 لدعم العربية
    response = requests.get(url)
    response.encoding = 'utf-8'
    
    if response.status_code == 200:
        # قراءة البيانات من النص المستلم
        df = pd.read_csv(io.StringIO(response.text))
        
        st.success("✅ تم الاتصال بنجاح! البيانات محدثة الآن.")
        
        # عرض الجدول بشكل احترافي
        st.write("### 📋 جدول البيانات")
        st.dataframe(df, use_container_width=True)
        
        # رسم بياني تفاعلي
        if not df.empty:
            st.write("### 📈 التمثيل البياني للنمو")
            # تعيين العمود الأول كمؤشر للرسم
            st.line_chart(df.set_index(df.columns[0]))
    else:
        st.error(f"خطأ 404: لم يتم العثور على الجدول. تأكد من الـ ID ومن أنك فعلت 'Share' للجميع.")

except Exception as e:
    st.error("❌ حدث خطأ غير متوقع.")
    st.write(f"التفاصيل: {str(e)}")
