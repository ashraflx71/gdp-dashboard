# --- قسم خطط النمو الاستراتيجي ---
st.markdown('<h1 class="gold-text">💎 عروض النمو الرقمي 2026</h1>', unsafe_allow_html=True)
st.write("اختر مسار النمو الذي يناسب طموح مؤسستك مع ضمانات أشرف أليكس.")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div style="border: 1px solid #666; padding: 20px; border-radius: 15px; text-align: center;">
            <h3 style="color: #C0C0C0;">🥈 الباقة الفضية</h3>
            <p>للمشاريع الناشئة</p>
            <h2 style="color: #D4AF37;">$299</h2>
            <ul style="text-align: right; direction: rtl;">
                <li>تحسين SEO لـ 5 صفحات</li>
                <li>فحص كفاءة الطاقة السنوي</li>
                <li>دعم فني عبر البريد</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    if st.button("اطلب الفضية"):
        st.success("تم تسجيل طلبك، سنتواصل معك فوراً يا قائد.")

with col2:
    st.markdown("""
        <div style="border: 2px solid #D4AF37; padding: 25px; border-radius: 15px; text-align: center; background-color: #111;">
            <h3 style="color: #D4AF37;">🥇 الباقة الذهبية</h3>
            <p><b>الأكثر طلباً</b></p>
            <h2 style="color: #D4AF37;">$599</h2>
            <ul style="text-align: right; direction: rtl;">
                <li>تحسين كامل لمحركات البحث</li>
                <li>تهيئة للظهور في الذكاء الاصطناعي (AEO)</li>
                <li>لوحة بيانات أداء مخصصة</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    if st.button("اطلب الذهبية (الأكثر تميزاً)"):
        st.balloons()
        st.success("اختيار ذكي! الباقة الذهبية هي طريقك للصدارة.")

with col3:
    st.markdown("""
        <div style="border: 1px solid #D4AF37; padding: 20px; border-radius: 15px; text-align: center;">
            <h3 style="color: #FFD700;">👑 الباقة الملكية</h3>
            <p>للمؤسسات الكبرى</p>
            <h2 style="color: #D4AF37;">اتصل بنا</h2>
            <ul style="text-align: right; direction: rtl;">
                <li>إدارة رقمية كاملة 24/7</li>
                <li>حلول Green-Software مخصصة</li>
                <li>استشارات استراتيجية مباشرة</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)
    if st.button("استشارة ملكية خاصة"):
        st.info("سيتم تحويلك لخط التواصل المباشر مع أشرف أليكس.")
        
