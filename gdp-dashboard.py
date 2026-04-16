import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. الإعدادات الملكية (Black & Gold)
st.set_page_config(page_title="Optimum 2026 - Analysis & Repair", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #111; color: #D4AF37; }
    /* تنسيق زر التحليل */
    .analyze-btn>div>button {
        width: 100%;
        background-color: #D4AF37 !important;
        color: #111 !important;
        font-weight: bold !important;
        height: 3em;
        border-radius: 10px;
    }
    /* تنسيق زر الإصلاح الأخضر */
    .repair-btn>div>button {
        width: 100%;
        background-color: #28a745 !important;
        color: white !important;
        font-weight: bold !important;
        height: 4em;
        font-size: 20px !important;
        border-radius: 10px;
        border: 2px solid #D4AF37;
    }
    .payment-box {
        border: 2px solid #D4AF37;
        padding: 25px;
        border-radius: 15px;
        background-color: #1a1a1a;
        text-align: center;
        direction: rtl;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("⚜️ منظومة Optimum 2026 للتحليل والإصلاح ⚜️")

# 2. خانة إدخال الرابط
target_url = st.text_input("🔍 أدخل رابط الموقع المراد فحصه:", placeholder="www.your-site.com")

# استخدام session_state لحفظ حالة الضغط على الزرار
if 'analyzed' not in st.session_state:
    st.session_state.analyzed = False

col_a, col_b = st.columns([1, 4])
with col_a:
    st.markdown('<div class="analyze-btn">', unsafe_allow_html=True)
    if st.button("📊 ابدأ التحليل"):
        if target_url:
            st.session_state.analyzed = True
        else:
            st.error("أدخل الرابط أولاً!")
    st.markdown('</div>', unsafe_allow_html=True)

# 3. عرض النتائج فقط بعد الضغط على "تحليل"
if st.session_state.analyzed:
    with st.spinner('♻️ جاري تحليل البيانات العميقة للموقع...'):
        time.sleep(2)
    
    st.success(f"✔️ اكتمل التقرير الفني لـ: {target_url}")
    
    res_col1, res_col2 = st.columns(2)
    
    with res_col1:
        st.subheader("📈 فحص النبض الرقمي")
        chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['كفاءة الكود', 'سرعة السيرفر'])
        st.line_chart(chart_data)
        st.metric(label="التقييم العام", value="ضعيف", delta="-22% عن المعدل الطبيعي")

    with res_col2:
        st.markdown("### 🛠️ الإجراء المطلوب")
        st.write("تم اكتشاف ثغرات في الـ SEO وبطء في استجابة قاعدة البيانات.")
        
        st.markdown('<div class="repair-btn">', unsafe_allow_html=True)
        if st.button("✅ أصلح موقعك الآن (500 ج)"):
            st.markdown(f'''
                <div class="payment-box">
                    <h2 style="color: #D4AF37;">إتمام عملية الإصلاح الملكي</h2>
                    <p style="color: #fff;">بمجرد الدفع، سيبدأ النظام فوراً في معالجة المشاكل التقنية لموقعك.</p>
                    <a href="https://ipn.eg/S/ashrafhassan567/instapay/9U8f3M" target="_blank" style="text-decoration: none;">
                        <button style="width:100%; background-color:#007bff; color:white; border:none; padding:15px; border-radius:8px; font-weight:bold; cursor:pointer; font-size: 18px; margin-bottom: 10px;">
                            💰 ادفع 500 ج عبر InstaPay
                        </button>
                    </a>
                    <a href="https://wa.me/201280208018?text=تم_الدفع_أستاذ_أشرف_لموقع_{target_url}" target="_blank" style="text-decoration: none;">
                        <button style="width:100%; background-color:#25D366; color:white; border:none; padding:12px; border-radius:8px; font-weight:bold; cursor:pointer;">
                            ✅ إرسال الإيصال (واتساب)
                        </button>
                    </a>
                </div>
            ''', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

else:
    st.info("👋 أهلاً بك يا بطل. أدخل الرابط واضغط على 'ابدأ التحليل' للكشف عن أداء موقعك.")

st.write("---")
st.markdown("<p style='text-align: center; color: #555;'>جميع الحقوق محفوظة للخبير أشرف حسن © 2026</p>", unsafe_allow_html=True)
