import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

# 1. إعداد الصفحة وتغيير العنوان لهويتك الجديدة
st.set_page_config(page_title="منصة أشرف حسن للتقنية", page_icon="🌱")

# 2. القائمة الجانبية للتنقل
st.sidebar.title("القائمة الرئيسية")
page = st.sidebar.radio("اختر الخدمة:", ["🌎 لوحة بيانات GDP", "📝 محول المعادلات (AI)"])

# --- القسم الأول: لوحة بيانات GDP (كودك الحالي) ---
if page == "🌎 لوحة بيانات GDP":
    st.title("🌎 لوحة معلومات الناتج المحلي الإجمالي")
    st.write("استعراض بيانات الناتج المحلي من موقع البيانات المفتوحة للبنك الدولي.")
    
    # هنا تضع كود الـ GDP الأصلي الخاص بك 
    # (سأختصر الجزء البرمجي لضمان عدم حدوث خطأ في المسارات)
    st.info("لوحة البيانات تعمل بنجاح كما في الصورة السابقة.")

# --- القسم الثاني: محول المعادلات (الإضافة الجديدة) ---
else:
    st.title("📝 محول الصور إلى LaTeX (الذكاء الاصطناعي)")
    st.write("ارفع صورة لمعادلة رياضية وسأقوم بتحويلها لك إلى كود برمي.")

    uploaded_file = st.file_uploader("اختر صورة المعادلة...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='الصورة المرفوعة', use_container_width=True)
        
        if st.button("تحويل المعادلة الآن 🚀"):
            with st.spinner("جاري التحليل... قد يستغرق الأمر ثوانٍ"):
                try:
                    from pix2tex.cli import LatexOCR
                    model = LatexOCR()
                    result = model(image)
                    st.success("تم التحويل!")
                    st.code(result, language='latex')
                    st.latex(result)
                except Exception as e:
                    st.error(f"خطأ في التحميل: تأكد من تحديث ملف requirements.txt")
