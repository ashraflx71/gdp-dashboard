import streamlit as st
import pandas as pd

st.set_page_config(page_title="GDP Dashboard 2026", layout="wide")
st.title("📊 لوحة تحكم الناتج المحلي الإجمالي")

# ضع المعرف الخاص بجدولك هنا (ID فقط)
SHEET_ID = "ضع_هنا_المعرف_الخاص_بجدولك"

# الرابط المباشر بصيغة التصدير
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"

try:
    # محاولة قراءة البيانات
    df = pd.read_csv(URL)
    
    st.success("✅ تم الاتصال بنجاح! البيانات حية الآن.")
    
    # عرض البيانات
    st.dataframe(df, use_container_width=True)
    
    # رسم بياني
    if not df.empty:
        st.subheader("التمثيل البياني للنمو")
        st.line_chart(df.set_index(df.columns[0]))

except Exception as e:
    st.error("❌ لا يزال هناك عائق في الوصول.")
    st.write(f"نوع الخطأ: {e}")
    st.info("💡 تأكد من أنك ضغطت على 'Share' ثم جعلت الوصول 'Anyone with the link can view'.")
