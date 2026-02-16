import streamlit as st
import pandas as pd
import altair as alt

# إعدادات الصفحة
st.set_page_config(page_title="لوحة بيانات الناتج المحلي", layout="wide")

# عنوان التطبيق باللغة العربية
st.title("🌍 لوحة بيانات الناتج المحلي الإجمالي (تفاعلية)")
st.write("تصفح بيانات الناتج المحلي الإجمالي من موقع البنك الدولي.")

# وظيفة سحب البيانات
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/datasets/gdp/master/data/gdp.csv"
    data = pd.read_csv(url)
    # هنا نقوم بتغيير أسماء الأعمدة لتناسب الكود وتجنب الخطأ
    data.columns = ['Country', 'Code', 'Year', 'Value']
    return data

try:
    df = load_data()

    # --- محرك البحث في القائمة الجانبية ---
    st.sidebar.header("🔍 محرك البحث والفلترة")
    
    # الحصول على قائمة الدول الفريدة
    available_countries = sorted(df['Country'].unique())
    
    # محرك البحث (Multiselect)
    selected_countries = st.sidebar.multiselect(
        "ما هي الدول التي ترغب في مشاهدتها؟",
        options=available_countries,
        default=["Egypt", "Saudi Arabia"] if "Egypt" in available_countries else [available_countries[0]]
    )

    # اختيار السنوات
    year_range = st.sidebar.slider(
        "ما هي السنوات التي تهمك؟",
        int(df['Year'].min()), int(df['Year'].max()), 
        (1990, 2022)
    )

    # فلترة البيانات
    filtered_df = df[
        (df['Country'].isin(selected_countries)) & 
        (df['Year'].between(year_range[0], year_range[1]))
    ]

    # --- عرض الرسم البياني ---
    if not filtered_df.empty:
        st.subheader("📈 الناتج المحلي الإجمالي بمرور الوقت")
        
        chart = alt.Chart(filtered_df).mark_line(point=True).encode(
            x=alt.X('Year:O', title='السنة'),
            y=alt.Y('Value:Q', title='الناتج المحلي (بالدولار)'),
            color=alt.Color('Country:N', title='الدولة'),
            tooltip=['Country', 'Year', 'Value']
        ).properties(height=400).interactive()
        
        st.altair_chart(chart, use_container_width=True)

        # عرض البطاقات (Metrics) لأحدث سنة مختارة
        st.write("---")
        latest_year = filtered_df['Year'].max()
        st.subheader(f"📊 أرقام ملخصة لعام {latest_year}")
        
        cols = st.columns(len(selected_countries))
        for i, country in enumerate(selected_countries):
            latest_val = filtered_df[(filtered_df['Country'] == country) & (filtered_df['Year'] == latest_year)]['Value'].values
            if len(latest_val) > 0:
                # تحويل الرقم ليكون بمليارات الدولارات لسهولة القراءة
                val_in_billions = latest_val[0] / 1_000_000_000
                cols[i].metric(label=country, value=f"{val_in_billions:,.1f} B$")

    else:
        st.info("الرجاء اختيار دول من القائمة الجانبية لعرض البيانات.")

except Exception as e:
    st.error(f"حدث خطأ: {e}")
import streamlit as st
import pandas as pd
import altair as alt

# إعدادات الصفحة
st.set_page_config(page_title="لوحة بيانات الناتج المحلي", layout="wide")

# عنوان التطبيق باللغة العربية
st.title("🌍 لوحة بيانات الناتج المحلي الإجمالي (تفاعلية)")
st.write("تصفح بيانات الناتج المحلي الإجمالي من موقع البنك الدولي.")

# وظيفة سحب البيانات
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/datasets/gdp/master/data/gdp.csv"
    data = pd.read_csv(url)
    # هنا نقوم بتغيير أسماء الأعمدة لتناسب الكود وتجنب الخطأ
    data.columns = ['Country', 'Code', 'Year', 'Value']
    return data

try:
    df = load_data()

    # --- محرك البحث في القائمة الجانبية ---
    st.sidebar.header("🔍 محرك البحث والفلترة")
    
    # الحصول على قائمة الدول الفريدة
    available_countries = sorted(df['Country'].unique())
    
    # محرك البحث (Multiselect)
    selected_countries = st.sidebar.multiselect(
        "ما هي الدول التي ترغب في مشاهدتها؟",
        options=available_countries,
        default=["Egypt", "Saudi Arabia"] if "Egypt" in available_countries else [available_countries[0]]
    )

    # اختيار السنوات
    year_range = st.sidebar.slider(
        "ما هي السنوات التي تهمك؟",
        int(df['Year'].min()), int(df['Year'].max()), 
        (1990, 2022)
    )

    # فلترة البيانات
    filtered_df = df[
        (df['Country'].isin(selected_countries)) & 
        (df['Year'].between(year_range[0], year_range[1]))
    ]

    # --- عرض الرسم البياني ---
    if not filtered_df.empty:
        st.subheader("📈 الناتج المحلي الإجمالي بمرور الوقت")
        
        chart = alt.Chart(filtered_df).mark_line(point=True).encode(
            x=alt.X('Year:O', title='السنة'),
            y=alt.Y('Value:Q', title='الناتج المحلي (بالدولار)'),
            color=alt.Color('Country:N', title='الدولة'),
            tooltip=['Country', 'Year', 'Value']
        ).properties(height=400).interactive()
        
        st.altair_chart(chart, use_container_width=True)

        # عرض البطاقات (Metrics) لأحدث سنة مختارة
        st.write("---")
        latest_year = filtered_df['Year'].max()
        st.subheader(f"📊 أرقام ملخصة لعام {latest_year}")
        
        cols = st.columns(len(selected_countries))
        for i, country in enumerate(selected_countries):
            latest_val = filtered_df[(filtered_df['Country'] == country) & (filtered_df['Year'] == latest_year)]['Value'].values
            if len(latest_val) > 0:
                # تحويل الرقم ليكون بمليارات الدولارات لسهولة القراءة
                val_in_billions = latest_val[0] / 1_000_000_000
                cols[i].metric(label=country, value=f"{val_in_billions:,.1f} B$")

    else:
        st.info("الرجاء اختيار دول من القائمة الجانبية لعرض البيانات.")

except Exception as e:
    st.error(f"حدث خطأ: {e}")
