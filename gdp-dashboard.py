import streamlit as st
import pandas as pd
import requests
import io

st.set_page_config(page_title="GDP Dashboard 2026", layout="wide")
st.title("📊 لوحة تحكم الناتج المحلي الإجمالي")

# ضع المعرف (ID) الخاص بجدولك هنا بدقة شديدة
SHEET_ID = "ضع_هنا_المعرف_الذي_استخرجته"

# هذه الصيغة هي الأدق للوصول المباشر
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv"

try:
    response = requests.get(URL)
    if response.status_code == 200:
        # قراءة البيانات مع دعم اللغة العربية
        df = pd.read_csv(io.StringIO(response.text))
        st.success("✅ تم الاتصال بالبيانات بنجاح!")
        
        st.dataframe(df, use_container_width=True)
        
        # التأكد من وجود بيانات للرسم البياني
        if not df.empty:
            st.line_chart(df.set_index(df.columns[0]))
    else:
        st.error(f"فشل الوصول للجدول. كود الخطأ: {response.status_code}")
        st.info("تأكد من أنك نسخت المعرف (ID) بشكل صحيح من رابط المتصفح.")

except Exception as e:
    st.error(f"حدث خطأ تقني: {str(e)}")
