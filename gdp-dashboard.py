import streamlit as st
import pandas as pd

st.set_page_config(page_title="GDP Dashboard 2026", layout="wide")
st.title("📊 لوحة تحكم الناتج المحلي الإجمالي")

# الصق رابط جدولك الفعلي هنا بين علامتي التنصيص
# مثال: RAW_URL = "https://docs.google.com/spreadsheets/d/1XyZ/edit"
RAW_URL = "ضع_رابط_جدولك_هنا_يا_أشرف"

try:
    # تحويل الرابط تلقائياً لصيغة البيانات
    if "docs.google.com" in RAW_URL:
        if "/edit" in RAW_URL:
            csv_url = RAW_URL.split("/edit")[0] + "/export?format=csv"
        elif "/gviz" in RAW_URL:
            csv_url = RAW_URL
        else:
            csv_url = RAW_URL + "/export?format=csv"
    else:
        csv_url = RAW_URL

    # قراءة البيانات
    df = pd.read_csv(csv_url)
    
    st.success("✅ تم الاتصال بنجاح! البيانات حية الآن.")
    
    # عرض الجدول
    st.write("### 📋 جدول البيانات")
    st.dataframe(df, use_container_width=True)
    
    # الرسم البياني
    if not df.empty:
        st.write("### 📈 التمثيل البياني")
        # نستخدم العمود الأول كسنوات والثاني كقيم
        st.line_chart(df.set_index(df.columns[0]))

except Exception as e:
    st.error("❌ عائق في الوصول")
    st.write(f"التفاصيل: {e}")
    st.info("💡 تأكد من لصق رابط الجدول كاملاً بشكل صحيح داخل علامات التنصيص.")
