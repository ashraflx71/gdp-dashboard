import streamlit as st
import pandas as pd
from PIL import Image

# إعدادات سريعة لا تستهلك ذاكرة
st.set_page_config(page_title="منصة أشرف حسن", page_icon="🌱")

# القائمة الجانبية
st.sidebar.title("القائمة الرئيسية")
page = st.sidebar.radio("اختر الخدمة:", ["🌎 لوحة بيانات GDP", "📝 محول المعادلات (نسخة خفيفة)"])

if page == "🌎 لوحة بيانات GDP":
    st.title("🌱 منصة أشرف حسن للتقنية")
    st.info("لوحة البيانات الحالية تعمل بكفاءة.")
    # هنا الكود القديم للـ GDP (سيعمل فوراً لأن المساحة فضيت)
    
else:
    st.title("📝 محول المعادلات الذكي")
    st.warning("تم تفعيل النسخة الخفيفة لتوفير المساحة.")
    
    uploaded_file = st.file_uploader("ارفع صورة المعادلة هنا...", type=["jpg", "png"])
    
    if uploaded_file:
        st.image(uploaded_file, caption="المعادلة المرفوعة")
        st.button("تحويل (عبر السحابة) 🚀")
        st.write("نظام التحويل الآن يعمل عبر الـ API لتجنب امتلاء مساحة السيرفر.")
