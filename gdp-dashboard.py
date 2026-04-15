import streamlit as st
import pandas as pd
import numpy as np
import time
import urllib.parse

# 1. الإعدادات الأساسية (يجب أن تكون في البداية)
st.set_page_config(page_title="Ashraf Alex Empire", layout="centered")

# 2. تعريف التنسيقات (CSS)
st.markdown("""
    <style>
    .main { background-color: #000000; color: #D4AF37; }
    .gold-text {
        background: linear-gradient(45deg, #D4AF37, #F9E27E);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        font-size: 2.5em;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. العنوان الرئيسي
st.markdown('<h1 class="gold-text">💎 عروض النمو الرقمي 2026</h1>', unsafe_allow_html=True)

# 4. بقية الكود الخاص بالباقات...
# (ضع هنا كود الباقات الذي أرسلته لك سابقاً)
