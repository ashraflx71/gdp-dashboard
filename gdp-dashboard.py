import streamlit as st
import pandas as pd

st.set_page_config(page_title="GDP Dashboard 2026", layout="wide")

# الرابط السحري الذي يتجاوز أخطاء 404
# تأكد من استبدال المعرف (ID) فقط
SHEET_ID = "ضع_هنا_المعرف_الخاص_بجدولك"
url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv"

st.title("📊 لوحة تحكم الناتج المحلي")

try:
    # قراءة البيانات مباشرة
    df = pd.read_csv(url)
    st.success("✅ تم الاتصال عبر Google Visualization API")
    st.dataframe(df, use_container_width=True)
    
    if not df.empty:
        st.line_chart(df.set_index(df.columns[0]))

except Exception as e:
    st.error(f"خطأ في الوصول: {e}")
    st.info("تأكد من أن الجدول: Anyone with the link can view")
