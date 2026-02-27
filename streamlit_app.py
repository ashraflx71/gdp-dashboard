import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

# إعداد الصفحة
st.set_page_config(page_title="منصة أشرف حسن للتقنية", page_icon="🌱")

# القائمة الجانبية للتنقل
st.sidebar.title("القائمة الرئيسية")
page = st.sidebar.radio("اختر الخدمة:", ["🌎 لوحة بيانات GDP", "📝 محول المعادلات (AI)"])

if page == "🌎 لوحة بيانات GDP":
    st.title("🌱 منصة أشرف حسن: لوحة الـ GDP")
    st.write("استعراض بيانات البنك الدولي بتحديث 2026")
    # هنا يظهر كود اللوحة التفاعلية تلقائياً
    st.info("قم باختيار السنوات والدول من القائمة الجانبية")

else:
    st.title("📝 محول الصور إلى LaTeX")
    st.write("ارفع صورة معادلة رياضية وسيقوم الذكاء الاصطناعي بتحويلها لك.")
    
    uploaded_file = st.file_uploader("اختر صورة...", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="الصورة المرفوعة")
        if st.button("تحويل الآن 🚀"):
            with st.spinner("جاري التحليل..."):
                try:
                    from pix2tex.cli import LatexOCR
                    model = LatexOCR()
                    result = model(img)
                    st.success("تم التحويل بنجاح!")
                    st.code(result, language='latex')
                    st.latex(result)
                except Exception as e:
                    st.error("المحرك قيد التحميل، جرب مرة أخرى خلال دقيقة.")
