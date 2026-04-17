import streamlit as st
import pandas as pd
import io
import requests

st.set_page_config(page_title="GDP Dashboard 2026", layout="wide")
st.title("📊 لوحة تحكم الناتج المحلي الإجمالي")

# ضع هنا رقم التعريف الخاص بجدولك (الموجود في الرابط بين /d/ و /edit)
# تأكد أن الجدول متاح للجميع (Anyone with the link can view)
SHEET_ID = "ضع_هنا_رقم_التعريف_الخاص_بجدولك"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"

try:
    # جلب البيانات باستخدام requests مع تحديد الترميز لدعم العربية
    response = requests.get(URL)
    response.encoding = 'utf-8' # هذا السطر هو مفتاح الحل لمشكلة الـ ascii
    
    if response.status_code == 200:
        df = pd.read_csv(io.StringIO(response.text))
        st.success("✅ تم تحديث البيانات بنجاح من المصدر الحي!")
        
        # عرض البيانات والرسوم
        st.dataframe(df, use_container_width=True)
        # تأكد أن العمود الأول يحتوي على السنوات أو الأسماء
        st.line_chart(df.set_index(df.columns[0]))
    else:
        st.error(f"فشل الوصول للجدول. كود الخطأ: {response.status_code}")

except Exception as e:
    st.error(f"حدث خطأ تقني: {str(e)}")
