import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. الإعدادات الملكية
st.set_page_config(page_title="Optimum 2026 - Repair Service", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #111; color: #D4AF37; }
    .main-button>div>button {
        width: 100%;
        border-radius: 10px;
        height: 4.5em;
        font-size: 20px !important;
        font-weight: bold !important;
        background-color: #28a745 !important; /* لون أخضر */
        color: white !important;
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
    .stSpinner > div > div { border-top-color: #D4AF37 !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚜️ لوحة تحكم الإصلاح الذكي | Optimum 2026 ⚜️")

# 2. خانة البحث (إدخال الرابط) في صدر الصفحة
st.markdown("### 🔍 ابدأ فحص موقعك الآن")
target_url = st.text_input("", placeholder="أدخل رابط موقعك هنا (مثال: www.your-site.com)", key="search_bar")

if target_url:
    # إثبات التحميل لزيادة المصداقية
    with st.spinner('♻️ جاري تحليل بنية الموقع وفحص الأخطاء البرمجية...'):
        time.sleep(3)
    
    st.success(f"✔️ تم تحليل الموقع: {target_url}")

    # 3. عرض النتائج والأزرار
    col1, col2 = st.columns(2)

    with col1:
        # رسم بياني يحاكي الأخطاء
        st.subheader("📊 تقرير الفحص الفني")
        chart_data = pd.DataFrame(np.random.randn(15, 2), columns=['أخطاء الـ SEO', 'سرعة الاستجابة'])
        st.area_chart(chart_data)
        st.metric(label="حالة الموقع الحالية", value="تحتاج تدخل فوري", delta="-15% نقص أداء")

    with col2:
        st.markdown('<div class="main-button">', unsafe_allow_html=True)
        # الزر الأخضر المطلوب
        if st.button("✅ أصلح موقعك هنا (اضغط للبدء)", key="repair_btn"):
            st.markdown(f'''
                <div class="payment-box">
                    <h2 style="color: #28a745;">🚀 جاهزون لإعادة موقعك للقمة</h2>
                    <p style="font-size: 1.2rem; color: #fff;">سعر الخدمة الشاملة (إصلاح + SEO + تسريع):</p>
                    <h1 style="color: #D4AF37;">500 جنيه مصري فقط</h1>
                    <p style="color: #ddd;">ادفع الآن واستلم موقعك في خلال 24 ساعة عمل بأعلى كفاءة</p>
                    <hr style="border-color: #D4AF37;">
                    
                    <a href="https://ipn.eg/S/ashrafhassan567/instapay/9U8f3M" target="_blank" style="text-decoration: none;">
                        <button style="width:100%; background-color:#007bff; color:white; border:none; padding:15px; border-radius:8px; font-weight:bold; cursor:pointer; font-size: 18px; margin-bottom: 10px;">
                            💰 ادفع 500 ج عبر InstaPay واستلم موقعك
                        </button>
                    </a>
                    
                    <a href="https://wa.me/201280208018?text=تم_الدفع_أستاذ_أشرف_وهذا_رابط_موقعي_{target_url}" target="_blank" style="text-decoration: none;">
                        <button style="width:100%; background-color:#25D366; color:white; border:none; padding:12px; border-radius:8px; font-weight:bold; cursor:pointer;">
                            ✅ تأكيد الدفع عبر واتساب
                        </button>
                    </a>
                </div>
            ''', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

else:
    # شاشة الانتظار الاحترافية
    st.info("👋 مرحباً بك في Optimum 2026. من فضلك ضع رابط موقعك في خانة البحث أعلاه لنقوم بفحصه وتقديم الحلول الملكية لك.")
    st.image("https://via.placeholder.com/1000x300/111111/D4AF37?text=REPAIR+YOUR+SITE+NOW+WITH+ASHRAF+HASSAN", use_column_width=True)

st.write("---")
st.markdown("<p style='text-align: center; color: #555;'>حقوق الملكية الفكرية والبرمجية محفوظة للخبير أشرف حسن © 2026</p>", unsafe_allow_html=True)
