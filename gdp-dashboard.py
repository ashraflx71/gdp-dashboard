import streamlit as st
import pandas as pd
import requests
import io

# 1. إعداد الصفحة بلمسة احترافية
st.set_page_config(page_title="GDP Dashboard 2026", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #000000; }
    h1 { color: #FFD700; text-align: center; font-size: 32px; }
    .stDataFrame { border: 1px solid #FFD700; }
    </style>
    """, unsafe_allow_html=True)

st.title("📊 لوحة تحكم الناتج المحلي الإجمالي")

# 2. ضع رابط جدولك بالكامل هنا (تأكد من وجود علامات التنصيص)
# يجب أن يكون الرابط مثل: "https://docs.google.com/spreadsheets/d/xxx/edit"
RAW_URL = "ضع_رابط_جدولك_هنا_من_المتصفح"

def load_data(url):
    try:
        # تحويل الرابط لصيغة CSV تلقائياً
        if "docs.google.com" in url:
            if "/edit" in url:
                csv_url = url.split("/edit")[0] + "/export?format=csv"
            elif "/gviz" in url:
                csv_url = url
            else:
                csv_url = url.rstrip('/') + "/export?format=csv"
        else:
            csv_url = url
            
        # جلب البيانات مع فرض ترميز UTF-8 لدعم العربية
        response = requests.get(csv_url)
        response.encoding = 'utf-8'
        
        if response.status_code == 200:
            return pd.read_csv(io.StringIO(response.text))
        else:
            st.error(f"خطأ في الوصول للملف (كود: {response.status_code})")
            return None
    except Exception as e:
        st.error(f"حدث خطأ أثناء تحميل البيانات: {e}")
        return None

# 3. تنفيذ جلب البيانات وعرضها
if RAW_URL == "ضع_رابط_جدولك_هنا_من_المتصفح":
    st.warning("⚠️ من فضلك ضع رابط الجدول الخاص بك في الكود بدلاً من الجملة العربية.")
else:
    df = load_data(RAW_URL)
    
    if df is not None:
        st.success("✅ تم الاتصال بالبيانات بنجاح!")
        
        # تقسيم الشاشة لعرض البيانات والرسوم
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("📋 جدول البيانات الحية")
            st.dataframe(df, use_container_width=True)
            
        with col2:
            st.subheader("📈 التحليل البياني")
            if not df.empty:
                # نفترض أن العمود الأول هو السنوات/الدول والثاني هو القيمة
                st.line_chart(df.set_index(df.columns[0]))
    else:
        st.info("💡 تأكد من أنك فعلت خيار Share -> Anyone with the link can view في ملف Google Sheets.")
