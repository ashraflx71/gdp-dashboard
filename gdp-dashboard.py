import streamlit as st
import pandas as pd
import numpy as np
import time

# --- 1. إعدادات الصفحة الاحترافية ---
st.set_page_config(page_title="Ashraf Alex Empire", layout="centered")

# --- 2. الهوية البصرية الملكية (Black & Gold) ---
st.markdown("""
    <style>
    .main { background-color: #000000; color: #D4AF37; }
    .stSelectbox label { color: #D4AF37 !important; font-weight: bold; }
    .gold-text {
        background: linear-gradient(45deg, #D4AF37, #F9E27E);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
    }
    .stMetric { 
         background-color: #111; 
         border: 1px solid #D4AF37; 
         border-radius: 10px; 
         padding: 10px;
    }
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. القائمة الجانبية (The Hub) ---
st.sidebar.markdown("<h1 style='color: #D4AF37;'>💎 Ashraf Alex</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color: #888;'>العودة للصفر - رؤية 2026</p>", unsafe_allow_html=True)
project_choice = st.sidebar.selectbox("🚀 انتقل بين مشاريعك الموحدة:", 
    ["محاكي سوار MIT", "مدونة Optimum 2026", "منصة Creative 2026", "خدمات شريف سالم"])

st.sidebar.divider()

# روابط التنقل السريع
if project_choice == "مدونة Optimum 2026":
    st.sidebar.success("🔗 تم توجيهك إلى Optimum")
    st.sidebar.markdown("[افتح المدونة الآن](https://optimum2026.blogspot.com)")
elif project_choice == "منصة Creative 2026":
    st.sidebar.warning("🛠️ منصة التطوير نشطة")
    st.sidebar.markdown("[زيارة Creative 2026](https://ashraflx71.github.io/Creative-2026/)")
elif project_choice == "خدمات شريف سالم":
    st.sidebar.info("🚗 قسم السيارات الكلاسيكية")
    st.sidebar.write("إدارة محتوى SEO وخدمات الموقع.")

# --- 4. محتوى مشروع محاكي MIT ---
if project_choice == "محاكي سوار MIT":
    st.markdown('<h1 class="gold-text">🚀 محاكي سوار MIT الذكي</h1>', unsafe_allow_html=True)
    st.write("نظام تحليل إشارات العضلات القائم على الذكاء الاصطناعي - بتوقيع **أشرف أليكس**")
    
    # مدخلات المحاكي في القائمة الجانبية
    st.sidebar.header("🕹️ مستشعرات EMG")
    m1 = st.sidebar.slider("العضلة القابضة", 0, 100, 30)
    m2 = st.sidebar.slider("وتر الإبهام", 0, 100, 60)
    
    if st.sidebar.checkbox("🍃 نمط توفير الطاقة"):
        time.sleep(0.4)
        st.sidebar.success("وضع الاستدامة نشط")
        
    # تحليل النتائج
    col1, col2 = st.columns(2)
    
    with col1:
        accuracy = 95 + (m1/300) + (m2/300)
        st.metric(label="دقة التنبؤ بالحركة", value=f"{min(accuracy, 99.9):.2f}%")
        
        # منطق التصنيف
        if m1 > 70 and m2 > 70: res, ico, clr = "قبضة كاملة", "✊", "#28a745"
        elif m1 > 70: res, ico, clr = "إشارة سبابة", "☝️", "#17a2b8"
        else: res, ico, clr = "وضع الاستعداد", "✋", "#6c757d"
        
        st.markdown(f"""
            <div style='border:1px solid #D4AF37; padding:20px; border-radius:10px; text-align:center; background-color: #111;'>
                <h1 style='margin:0;'>{ico}</h1>
                <h3 style='color:{clr};'>{res}</h3>
            </div>""", unsafe_allow_html=True)

    with col2:
        st.subheader("📊 موجات الـ Ultrasound")
        chart_data = pd.DataFrame(np.random.randn(15, 2)/10 + [m1/100, m2/100], columns=['A', 'B'])
        st.line_chart(chart_data)

# --- 5. التذييل الموحد (The Final Touch) ---
st.markdown(f"""
    <div style="margin-top: 50px;">
        <hr style="border:0.5px solid #D4AF37; opacity: 0.3;">
        <p style="text-align: center; color: #777; font-size: 0.9rem;">
            © 2026 | <b>Ashraf Alex</b> | Developed with Green Software Principles
        </p>
    </div>""", unsafe_allow_html=True)
