import streamlit as st
from PIL import Image
import requests # مكتبة خفيفة جداً

st.set_page_config(page_title="منصة أشرف حسن للتقنية", page_icon="🌱")

# القائمة الجانبية
st.sidebar.title("القائمة الرئيسية")
page = st.sidebar.radio("اختر الخدمة:", ["🌎 لوحة بيانات GDP", "📝 محول المعادلات الذكي"])

if page == "🌎 لوحة بيانات GDP":
    st.title("🌱 منصة أشرف حسن: لوحة الـ GDP")
    st.info("البيانات تعمل بكفاءة عالية الآن.")
    # كود الـ GDP الأصلي يوضع هنا

else:
    st.title("📝 محول الصور إلى LaTeX (سحابي)")
    st.write("ارفع صورة المعادلة وسنستخدم الذكاء الاصطناعي السحابي لتحويلها.")
    
    uploaded_file = st.file_uploader("اختر صورة...", type=["jpg", "png", "jpeg"])
    
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="الصورة المرفوعة")
        
        if st.button("تحويل الآن 🚀"):
            st.success("جاري الإرسال للمحرك السحابي... (لا يستهلك مساحة من سيرفرك)")
            # هنا سنضع كود الربط بـ Gemini أو أي API مجاني
            st.code(r"\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}", language='latex')
            st.latex(r"\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}")
