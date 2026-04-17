import streamlit as st
import pandas as pd

st.set_page_config(page_title="GDP Dashboard 2026", layout="wide")
st.title("📊 لوحة تحكم الناتج المحلي الإجمالي")

# الصق رابط الجدول كاملاً هنا بين علامتي التنصيص
RAW_URL = "هنا_ضع_رابط_الجدول_كاملاً_من_المتصفح"

try:
    # تحويل الرابط العادي إلى رابط تحميل CSV تلقائياً
    if "/edit" in RAW_URL:
        csv_url = RAW_URL.replace("/edit", "/export?format=csv")
    else:
        csv_url = RAW_URL

    # محاولة قراءة البيانات
    df = pd.read_csv(csv_url)
    
    st.success("✅ تم الاتصال بنجاح! البيانات حية الآن.")
    
    # عرض البيانات
    st.write("### 📋 جدول البيانات")
    st.dataframe(df, use_container_width=True)
    
    # رسم بياني
    if not df.empty:
        st.write("### 📈 التمثيل البياني")
        st.line_chart(df.set_index(df.columns[0]))

except Exception as e:
    st.error("❌ لا يزال هناك عائق.")
    st.write(f"التفاصيل: {e}")
    st.info("💡 تأكد من نسخ الرابط كاملاً من شريط العنوان في المتصفح.")
