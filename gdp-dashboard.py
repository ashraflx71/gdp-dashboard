import streamlit as st
import pandas as pd
import numpy as np
import time
import requests

# 1. الإعدادات الملكية (Black & Gold)
st.set_page_config(page_title="Optimum 2026 - Real Analysis", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #111; color: #D4AF37; }
    .analyze-btn>div>button {
        width: 100%;
        background-color: #D4AF37 !important;
        color: #111 !important;
        font-weight: bold !important;
        height: 3em;
        border-radius: 10px;
    }
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

st.title("⚜️ منظومة Optimum 2026 للتحليل الحقيقي ⚜️")

# 2. خانة إدخال الرابط
target_url = st.text_input("🔍 أدخل رابط الموقع (مثال: https://www.google.com):", placeholder="https://")

st.markdown('<div class="analyze-btn">', unsafe_allow_html=True)
analyze_clicked = st.button("📊 ابدأ التحليل الحقيقي")
st.markdown('</div>', unsafe_allow_html=True)

if analyze_clicked:
    if target_url:
        try:
            with st.spinner(f'🌐 جاري الاتصال بـ {target_url} وتحليل سرعة السيرفر...'):
                start_time = time.time()
                # محاولة طلب الموقع مع مهلة 10 ثواني
                response = requests.get(target_url, timeout=10)
                end_time = time.time()
                
                response_speed = end_time - start_time
                
                # تصنيف النتائج بناءً على السرعة الحقيقية
                if response_speed < 0.6:
                    rating = "ممتاز"
                    score_color = "green"
                    msg = "موقعك في القمة! يمكننا تعزيز الـ SEO أكثر."
                elif response_speed < 1.8:
                    rating = "جيد"
                    score_color = "orange"
                    msg = "أداء جيد، ولكن هناك مساحة للتحسين لزيادة سرعة التحميل."
                else:
                    rating = "ضعيف"
                    score_color = "red"
                    msg = "تم اكتشاف بطء شديد في استجابة السيرفر، الموقع يحتاج تدخل فوري."

                # عرض النتائج
                st.success(f"✔️ تم تحليل الموقع بنجاح")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("سرعة الاستجابة", f"{response_speed:.2f} ثانية")
                    st.subheader(f"التقييم العام: :{score_color}[{rating}]")
                    st.line_chart([0.2, 0.4, response_speed, response_speed * 0.9])
                
                with col2:
                    st.markdown(f"### 🛠️ حالة الموقع: {rating}")
                    st.write(msg)
                    
                    st.markdown('<div class="repair-btn">', unsafe_allow_html=True)
                    if st.button("✅ أصلح موقعك الآن (500 ج)"):
                        st.markdown(f'''
                            <div class="payment-box">
                                <h2 style="color: #D4AF37;">تأكيد الإصلاح الملكي</h2>
                                <p style="color: #fff;">سعر الخدمة: 500 جنيه مصري</p>
                                <a href="https://ipn.eg/S/ashrafhassan567/instapay/9U8f3M" target="_blank" style="text-decoration: none;">
                                    <button style="width:100%; background-color:#007bff; color:white; border:none; padding:15px; border-radius:8px; font-weight:bold; cursor:pointer; font-size: 18px;">💰 ادفع الآن عبر InstaPay</button>
                                </a>
                                <br><br>
                                <a href="https://wa.me/201280208018?text=تم_الدفع_لموقع_{target_url}" target="_blank" style="text-decoration: none;">
                                    <button style="width:100%; background-color:#25D366; color:white; border:none; padding:12px; border-radius:8px; font-weight:bold; cursor:pointer;">✅ تأكيد عبر واتساب</button>
                                </a>
                            </div>
                        ''', unsafe_allow_html=True)
                    st.markdown('</div>', unsafe_allow_html=True)

        except:
            st.error("❌ تعذر الوصول للموقع. تأكد من كتابة الرابط بشكل صحيح (يجب أن يبدأ بـ https://)")
    else:
        st.warning("⚠️ يرجى إدخال الرابط أولاً قبل الضغط على تحليل.")

st.write("---")
st.markdown("<p style='text-align: center; color: #555;'>جميع الحقوق محفوظة للخبير أشرف حسن © 2026</p>", unsafe_allow_html=True)
