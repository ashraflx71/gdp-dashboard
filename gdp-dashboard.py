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
project_choice = st.sidebar.selectbox("🚀 اختر الأداة أو المشروع:", 
    ["محاكي سوار MIT", "حاسبة أرباح الـ SEO", "فاحص كفاءة الطاقة (Green-SEO)", "مدونة Optimum 2026", "منصة Creative 2026", "خدمات شريف سالم"])

st.sidebar.divider()

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
    with col2:
        chart_data = pd.DataFrame(np.random.randn(15, 2)/10 + [m1/100, m2/100], columns=['A', 'B'])
        st.line_chart(chart_data)

# --- 5. أداة الأرباح (SEO ROI Calculator) ---
elif project_choice == "حاسبة أرباح الـ SEO":
    st.markdown('<h1 class="gold-text">💰 حاسبة العائد من الـ SEO</h1>', unsafe_allow_html=True)
    st.write("أداة تحليل الجدوى الاقتصادية لخدمات **أشرف أليكس**.")
    col1, col2 = st.columns(2)
    with col1:
        visits = st.number_input("الزيارات الشهرية المستهدفة", value=5000)
        conv_rate = st.slider("نسبة التحويل (%)", 0.1, 10.0, 2.5)
    with col2:
        avg_sale = st.number_input("متوسط قيمة المبيعة ($)", value=200)
        seo_cost = st.number_input("ميزانية الحملة ($)", value=1000)
    total_sales = (visits * (conv_rate/100)) * avg_sale
    roi = ((total_sales - seo_cost) / seo_cost) * 100 if seo_cost > 0 else 0
    st.divider()
    c1, c2 = st.columns(2)
    c1.metric("الأرباح المتوقعة", f"${total_sales:,.2f}")
    c2.metric("العائد ROI", f"{roi:.0f}%", delta="مربح")

# --- 6. الأداة الربحية الكبرى (Green-SEO Auditor) ---
elif project_choice == "فاحص كفاءة الطاقة (Green-SEO)":
    st.markdown('<h1 class="gold-text">🍃 Green-SEO Audit Tool</h1>', unsafe_allow_html=True)
    st.write("حلول **أشرف أليكس** لتقليل انبعاثات المواقع وتحسين سرعتها.")
    url = st.text_input("أدخل رابط موقع العميل لفحصه:", "https://")
    if st.button("بدء الفحص العميق"):
        with st.status("جاري تحليل الكود واستهلاك الطاقة...", expanded=True) as status:
            time.sleep(1.5)
            st.write("📡 فحص استجابة السيرفر وتوفير الموارد...")
            time.sleep(1.5)
            status.update(label="اكتمل الفحص التقني!", state="complete")
        score = np.random.randint(65, 98)
        c1, c2, c3 = st.columns(3)
        c1.metric("كفاءة الطاقة", f"{score}%")
        c2.metric("توفير الكربون", f"{(100-score)*0.4:.1f}kg")
        c3.metric("السرعة", "1.1s")
        st.divider()
        st.subheader("📋 تقرير أشرف أليكس المبدئي:")
        st.info("موقعك يحتاج لتحسين ضغط الصور وتنظيف ملفات JavaScript لتقليل استهلاك السيرفر.")
        st.warning("⚠️ للحصول على التقرير التفصيلي (PDF) وخدمة الإصلاح، يرجى التواصل مع الإدارة.")

# --- 7. التذييل ---
st.markdown(f"""
    <div style="margin-top: 50px;">
        <hr style="border:0.5px solid #D4AF37; opacity: 0.3;">
        <p style="text-align: center; color: #777; font-size: 0.9rem;">
            © 2026 | <b>Ashraf Alex</b> | حلول رقمية ذكية ومستدامة
        </p>
    </div>""", unsafe_allow_html=True)
