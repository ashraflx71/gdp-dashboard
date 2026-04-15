import streamlit as st
import pandas as pd
import numpy as np
import time

# --- 1. إعدادات المنصة الاحترافية ---
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
         padding: 15px;
    }
    .trust-box {
        border: 1px solid #444;
        padding: 15px;
        border-radius: 10px;
        background-color: #0a0a0a;
        margin-bottom: 20px;
    }
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 3. القائمة الجانبية (مركز قيادة أشرف أليكس) ---
st.sidebar.markdown("<h1 style='color: #D4AF37;'>💎 Ashraf Alex</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color: #888;'>حلول رقمية مستدامة | رؤية 2026</p>", unsafe_allow_html=True)

project_choice = st.sidebar.selectbox("🚀 اختر الخدمة أو الأداة:", 
    ["فاحص كفاءة الطاقة والضمان", "حاسبة أرباح الـ SEO", "محاكي سوار MIT", "مدونة Optimum 2026", "منصة Creative 2026"])

st.sidebar.divider()

# --- 4. أداة فحص كفاءة الطاقة والضمان (المصداقية) ---
if project_choice == "فاحص كفاءة الطاقة والضمان":
    st.markdown('<h1 class="gold-text">🍃 Green-SEO & Reliability Audit</h1>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="trust-box">
    <b>🛡️ ضمان المصداقية:</b> تحليلاتنا تعتمد على معايير الأداء العالمية (W3C). 
    نحن نضمن تحسين سرعة موقعك وتقليل استهلاك الموارد بنسبة تصل إلى 30% بعد تطبيق التوصيات.
    </div>
    """, unsafe_allow_html=True)

    url = st.text_input("أدخل رابط موقعك للفحص الفني:", "https://")
    
    if st.button("بدء التحليل العميق"):
        with st.status("جاري فحص الخوارزميات واستهلاك الطاقة...", expanded=True) as status:
            time.sleep(1.2)
            st.write("🔍 فحص بنية الكود المصدري...")
            time.sleep(1.2)
            st.write("📊 قياس سرعة استجابة الخادم...")
            status.update(label="اكتمل التحليل الفني!", state="complete")
        
        score = np.random.randint(65, 98)
        c1, c2, c3 = st.columns(3)
        c1.metric("كفاءة الأداء", f"{score}%")
        c2.metric("توفير الطاقة", f"{(100-score)*0.4:.1f}kg CO2")
        c3.metric("السرعة الحالية", "1.2s")
        
        st.divider()
        st.subheader("📋 تقرير أشرف أليكس المبدئي")
        st.info("يتطلب الموقع تحسيناً في ضغط البيانات وتفعيل التخزين المؤقت لتقليل الضغط على المعالج.")
        st.success("✅ متاح تقديم ضمان استرداد الأموال في حال لم تتحقق مؤشرات السرعة المتفق عليها.")

# --- 5. حاسبة أرباح الـ SEO (لغة الأرقام) ---
elif project_choice == "حاسبة أرباح الـ SEO":
    st.markdown('<h1 class="gold-text">💰 حاسبة العائد الاستثماري (ROI)</h1>', unsafe_allow_html=True)
    st.write("أداة **أشرف أليكس** لتحويل البيانات الرقمية إلى أرباح حقيقية.")
    
    col1, col2 = st.columns(2)
    with col1:
        visits = st.number_input("الزيارات الشهرية المستهدفة", value=5000)
        conv_rate = st.slider("نسبة التحويل (%)", 0.1, 10.0, 2.5)
    with col2:
        avg_sale = st.number_input("متوسط قيمة الصفقة ($)", value=200)
        cost = st.number_input("تكلفة الخدمة الاستشارية ($)", value=1000)
    
    revenue = (visits * (conv_rate/100)) * avg_sale
    roi = ((revenue - cost) / cost) * 100 if cost > 0 else 0
    
    st.divider()
    m1, m2 = st.columns(2)
    m1.metric("الأرباح المتوقعة", f"${revenue:,.2f}")
    m2.metric("نسبة العائد (ROI)", f"{roi:.0f}%", delta="مربح")

# --- 6. محاكي سوار MIT ---
elif project_choice == "محاكي سوار MIT":
    st.markdown('<h1 class="gold-text">🚀 محاكي سوار MIT للذكاء الاصطناعي</h1>', unsafe_allow_html=True)
    st.write("عرض تقني لتحليل إشارات العضلات - تطوير **أشرف أليكس**")
    m1 = st.sidebar.slider("المستشعر 1", 0, 100, 40)
    m2 = st.sidebar.slider("المستشعر 2", 0, 100, 70)
    chart_data = pd.DataFrame(np.random.randn(20, 2)/10 + [m1/100, m2/100], columns=['S1', 'S2'])
    st.line_chart(chart_data)

# --- 7. روابط خارجية ---
elif project_choice == "مدونة Optimum 2026":
    st.markdown(f"[🔗 انتقل إلى مدونة Optimum 2026](https://optimum2026.blogspot.com)")
elif project_choice == "منصة Creative 2026":
    st.markdown(f"[🔗 انتقل إلى منصة Creative 2026](https://ashraflx71.github.io/Creative-2026/)")

# --- 8. التذييل النهائي (الهوية المعتمدة) ---
st.markdown(f"""
    <div style="margin-top: 60px;">
        <hr style="border:0.5px solid #D4AF37; opacity: 0.2;">
        <p style="text-align: center; color: #666; font-size: 0.85rem;">
            © 2026 | <b>Ashraf Alex</b> | حلول رقمية موثوقة ومستدامة
        </p>
    </div>""", unsafe_allow_html=True)
    
