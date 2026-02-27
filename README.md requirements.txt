import streamlit as st
from pix2tex.cli import LatexOCR
from PIL import Image

# إعداد الصفحة لتناسب شاشة الهاتف
st.set_page_config(page_title="محول المعادلات", layout="centered")

st.title("📝 محول الصور إلى LaTeX")

# تحميل النموذج مع الذاكرة المؤقتة
@st.cache_resource
def load_model():
    return LatexOCR()

try:
    model = load_model()
    
    # اختيار الملف
    img_file = st.file_uploader("ارفع صورة المعادلة", type=['png', 'jpg', 'jpeg'])

    if img_file:
        img = Image.open(img_file)
        st.image(img, caption="الصورة المرفوعة")
        
        if st.button("تحويل"):
            with st.spinner("جاري التحليل..."):
                result = model(img)
                st.success("تم!")
                st.code(result)
                st.latex(result)
except Exception as e:
    st.error(f"خطأ: {e}")
<div style="text-align: center; padding: 20px;">
    <div style="font-size: 50px;">🌱</div>
    <h1 style="margin: 0; color: #2ecc71;">دليل البرمجيات الخضراء</h1>
    <p style="color: #888; font-style: italic;">نحو مستقبل تقني مستدام</p>
</div>
streamlit
pix2tex
Pillow
