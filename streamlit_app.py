st.title("🌱 منصة أشرف حسن للتقنية والذكاء الاصطناعي")
st.write("مرحباً بك! هذه اللوحة تجمع بين بيانات الاقتصاد العالمي وأدوات الذكاء الاصطناعي.")
# إضافة قائمة جانبية للتنقل
page = st.sidebar.selectbox("اختر الخدمة", ["لوحة بيانات GDP", "محول المعادلات (قريباً)"])

if page == "لوحة بيانات GDP":
    # هنا نترك كود الـ GDP الحالي كما هو
    st.header("📊 لوحة معلومات الناتج المحلي الإجمالي")
else:
    st.header("📝 محول الصور إلى LaTeX")
    st.write("ارفع صورة معادلة مكتوبة بخط اليد أو مطبوعة لتحويلها إلى كود LaTeX.")
    
    # اختيار ملف الصورة
    uploaded_file = st.file_uploader("اختر صورة المعادلة...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # عرض الصورة المرفوعة
        from PIL import Image
        image = Image.open(uploaded_file)
        st.image(image, caption='الصورة المرفوعة', use_container_width=True)
        
        if st.button("تحويل الآن 🚀"):
            with st.spinner("جاري تحليل المعادلة بالذكاء الاصطناعي..."):
                # هنا سيقوم التطبيق باستدعاء مكتبة pix2tex التي وضعناها في requirements
                try:
                    from pix2tex.cli import LatexOCR
                    model = LatexOCR()
                    result = model(image)
                    st.success("تم التحويل بنجاح!")
                    st.code(result, language='latex')
                    st.latex(result)
                except Exception as e:
                    st.error(f"حدث خطأ: تأكد من تثبيت المكتبات المطلوبة. {e}")
