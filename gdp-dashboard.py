import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# إعداد الصفحة بلمسة ملكية
st.set_page_config(page_title="GDP Dashboard 2026", layout="wide")

st.title("📊 لوحة تحكم الناتج المحلي الإجمالي - تحديث حي")

# الاتصال بـ Google Sheets
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    df = conn.read()
    
    # عرض البيانات في واجهة تفاعلية
    st.success("تم تحديث البيانات بنجاح من المصدر الحي!")
    
    # هنا يمكنك إضافة الرسوم البيانية الخاصة بك
    st.line_chart(df.set_index(df.columns[0]))
    
    st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error(f"حدث خطأ في الاتصال بالبيانات: {e}")
    st.info("تأكد من وضع رابط الجدول في إعدادات Secrets على Streamlit Cloud.")
