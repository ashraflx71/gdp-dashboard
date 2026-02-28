import streamlit as st
import pandas as pd
from pathlib import Path
import google.generativeai as genai
from PIL import Image

# 1. إعداد واجهة المنصة
st.set_page_config(
    page_title="منصة أشرف حسن للتقنية",
    page_icon="🌱",
    layout="wide"
)

# 2. إعداد مفتاح الذكاء الاصطناعي (ضع مفتاحك هنا)
# للحصول عليه مجاناً: https://aistudio.google.com/
API_KEY = "ضـع_مفتاح_الـ_API_الخـاص_بـك_هنـا"

try:
    genai.configure(api_key=API_KEY)
except:
    st.sidebar.error("يرجى إضافة مفتاح API صحيح")

# 3. القائمة الجانبية الاحترافية
st.sidebar.title("💎 قائمة التحكم")
st.sidebar.markdown(f"**المطور:** أشرف حسن")
page = st.sidebar.radio("انتقل إلى:", ["🌎 لوحة بيانات GDP", "📝 محول المعادلات الذكي"])

# --- القسم الأول: لوحة بيانات GDP ---
if page == "🌎 لوحة بيانات GDP":
    st.title("🌱 منصة أشرف حسن: لوحة بيانات GDP")
    st.markdown("---")
    
    @st.cache_data
    def load_data():
        # التأكد من مسار الملف في Streamlit Cloud
        data_path = Path(__file__).parent/'data/gdp_data.csv'
        if not data_path.exists():
            return None
        df = pd.read_csv(data_path)
        return df.melt(id_vars=['Country Code'], var_name='Year', value_name='GDP')

    data = load_data()
    
    if data is not None:
        data['Year'] = pd.to_numeric(data['Year'], errors='coerce')
        countries = st.multiselect("اختر الدول:", data['Country Code'].unique(), default=['BRA', 'MEX', 'FRA'])
        years = st.slider("اختر الفترة الزمنية:", int(data['Year'].min()), int(data['Year'].max()), (2000, 2022))
        
        filtered = data[(data['Country Code'].isin(countries)) & (data['Year'].between(years[0], years[1]))]
        st.line_chart(filtered, x='Year', y='GDP', color='Country Code')
        st.success("تم تحديث البيانات بنجاح!")
    else:
        st.info("لوحة البيانات جاهزة، سيتم عرض الرسوم عند رفع ملف gdp_data.csv")

# --- القسم الثاني: محول المعادلات الذ
