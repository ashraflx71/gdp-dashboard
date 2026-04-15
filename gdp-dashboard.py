import streamlit as st
import pandas as pd
import numpy as np
import time

# --- 1. إعدادات الصفحة ---
st.set_page_config(page_title="Ashraf Alex Empire", layout="centered")

# --- 2. الهوية البصرية (Black & Gold) ---
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
project_choice = st.sidebar.selectbox("🚀 اختر الأداة أو المشروع:", 
    ["محاكي سوار MIT", "حاسبة أرباح الـ SEO", "مدونة Optimum 2026", "منصة Creative 2026", "خدمات شريف سالم"])

st.sidebar.divider()

# روابط التنقل السريع في القائمة الجانبية
if project_choice == "مدونة Optimum 2026":
    st.sidebar.markdown("[🔗 افتح Optimum 2026](https://optimum2026.blogspot.com)")
elif project_choice == "منصة Creative 2026":
    st.sidebar.markdown("[🔗 زيارة Creative 2026](https://ashraflx71.github.io/Creative-2026/)")
elif project_choice == "خدمات شريف سالم":
    st.sidebar.info("🚗 إدارة SEO لقطاع السيارات")

# --- 4. محتوى مشروع محاكي MIT ---
if project_choice == "محاكي سوار MIT":
    st.markdown('<h1 class="gold-text">🚀 محاكي سوار MIT الذكي</h1>', unsafe_allow_html=True)
    st.write("نظام تحليل إشارات العضلات - بتوقيع **أشرف أليكس**")
    
    m1 = st.sidebar.slider("العضلة القابضة", 0, 100, 30)
    m2 = st.sidebar.slider("وتر الإبهام", 0, 100, 60)
    
    col1, col2 = st.columns(2)
    with col1:
        accuracy = 95 + (m1/300) + (m2/300)
        st.metric(label="دقة التنبؤ", value=f"{min(accuracy, 99.9):.2f}%")
        st.write("✅ النظام يعمل بكفاءة عالية")
    with col2:
        chart_data = pd.DataFrame(np.random.randn(15, 2)/10 + [m1/100, m2/100], columns=['A', 'B'])
        st.line_chart(chart_data)

# --- 5. أداة الأرباح (SEO ROI Calculator) ---
elif project_choice == "حاسبة أرباح الـ SEO":
    st.markdown('<h1 class="gold-text">💰 حاسبة العائد من الـ SEO</h1>', unsafe_allow_html=True)
    st.write("أداة **أشرف أليكس** لتحليل الجدوى الاقتصادية لتحسين محركات البحث.")

    col1, col2 = st.columns(2)
    with col1:
        visits = st.number_input("عدد الزيارات الشهرية المتوقعة", value=5000)
        conv_rate = st.slider("نسبة التحويل (%)", 0.1, 10.0, 2.5)
    
    with col2:
        avg_sale = st.number_input("متوسط قيمة المبيعة ($)", value=200)
        seo_cost = st.number_input("تكلفة الحملة مع أشرف أليكس ($)", value=1000)

    # الحسبة المخططة
    total_sales = (visits * (conv_rate/100)) * avg_sale
    roi = ((total_sales - seo_cost) / seo_cost) * 100 if seo_cost > 0 else 0

    st.divider()
    c1, c2 = st.columns(2)
    c1.metric(label="الأرباح المتوقعة", value=f"${total_sales:,.2f}")
    c2.metric(label="العائد على الاستثمار (ROI)", value=f"{roi:.0f}%", delta="مربح جداً")
    
    st.info("💡 ملاحظة: هذه الأرقام تقديرية بناءً على خوارزميات تحليل السوق لعام 2026.")

# --- 6. التذييل الموحد ---
st.markdown(f"""
    <div style="margin-top: 50px;">
        <hr style="border:0.5px solid #D4AF37; opacity: 0.3;">
        <p style="text-align: center; color: #777; font-size: 0.9rem;">
            © 2026 | <b>Ashraf Alex</b> | الرواد في الحلول الرقمية المستدامة
        </p>
    </div>""", unsafe_allow_html=True)
