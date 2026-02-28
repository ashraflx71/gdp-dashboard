import streamlit as st
import google.generativeai as genai
from PIL import Image

# إعداد المنصة
st.set_page_config(page_title="منصة أشرف حسن", layout="wide")

# استبدل الكلمة بالأسفل بـ المفتاح الخاص بك الذي حصلت عليه من Google AI Studio
API_KEY = "اكتب_هنا_مفتاح_الـ_API_الخاص_بك" 

if API_KEY != "اكتب_هنا_مفتاح_الـ_API_الخاص_بك":
    genai.configure(api_key=API_KEY)

st.sidebar.title("💎 قائمة التحكم")
choice = st.sidebar.radio("انتقل إلى:", ["الرئيسية ولوحة GDP", "محول المعادلات الذكي"])

if choice == "الرئيسية ولوحة GDP":
    st.title("🌱 منصة أشرف حسن للتقنية والاستدامة")
    st.markdown("---")
    st.info("لوحة البيانات تعمل بنجاح وبسرعة عالية.")
    # ملاحظة: يمكنك وضع كود الـ GDP الأصلي هنا ليعمل مع القائمة

else:
    st.title("📝 محول الصور إلى كود LaTeX")
    st.write("ارفع صورة لأي معادلة رياضية وسأحولها لك في ثوانٍ.")
    
    file = st.file_uploader("ارفع الصورة", type=["jpg", "png", "jpeg"])
    if file:
        img = Image.open(file)
        st.image(img, width=300)
        if st.button("تحويل المعادلة 🚀"):
            if API_KEY == "اكتب_هنا_مفتاح_الـ_API_الخاص_بك":
                st.error("من فضلك ضع مفتاح الـ API أولاً في الكود!")
            else:from google import genai

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain how AI works in a few words",
)

print(response.text)
                try:
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    response = model.generate_content(["Convert this math equation to LaTeX code. Give me ONLY the code code starting with $ and ending with $.", img])
                    st.success("تم التحويل!")
                    st.code(response.text, language='latex')
                    st.latex(response.text)
                except Exception as e:
                    st.error(f"حدث خطأ: {e}")
