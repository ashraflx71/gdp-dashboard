import streamlit as st
import pandas as pd
import math
from pathlib import Path

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='GDP dashboard',
    page_icon=':earth_americas:', # This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------
# Declare some useful functions.

@st.cache_data
def get_gdp_data():
    """Grab GDP data from a CSV file.

    This uses caching to avoid having to read the file every time. If we were
    reading from an HTTP endpoint instead of a file, it's a good idea to set
    a maximum age to the cache with the TTL argument: @st.cache_data(ttl='1d')
    """

    # Instead of a CSV on disk, you could read from an HTTP endpoint here too.
    DATA_FILENAME = Path(__file__).parent/'data/gdp_data.csv'
    raw_gdp_df = pd.read_csv(DATA_FILENAME)

    MIN_YEAR = 1960
    MAX_YEAR = 2022

    # The data above has columns like:
    # - Country Name
    # - Country Code
    # - [Stuff I don't care about]
    # - GDP for 1960
    # - GDP for 1961
    # - GDP for 1962
    # - ...
    # - GDP for 2022
    #
    # ...but I want this instead:
    # - Country Name
    # - Country Code
    # - Year
    # - GDP
    #
    # So let's pivot all those year-columns into two: Year and GDP
    gdp_df = raw_gdp_df.melt(
        ['Country Code'],
        [str(x) for x in range(MIN_YEAR, MAX_YEAR + 1)],
        'Year',
        'GDP',
    )

    # Convert years from string to integers
    gdp_df['Year'] = pd.to_numeric(gdp_df['Year'])

    return gdp_df

gdp_df = get_gdp_data()

# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
'''
# :earth_americas: GDP dashboard

Browse GDP data from the [World Bank Open Data](https://data.worldbank.org/) website. As you'll
notice, the data only goes to 2022 right now, and datapoints for certain years are often missing.
But it's otherwise a great (and did I mention _free_?) source of data.
'''

# Add some spacing
''
''

min_value = gdp_df['Year'].min()
max_value = gdp_df['Year'].max()

from_year, to_year = st.slider(
    'Which years are you interested in?',
    min_value=min_value,
    max_value=max_value,
    value=[min_value, max_value])

countries = gdp_df['Country Code'].unique()

if not len(countries):
    st.warning("Select at least one country")

selected_countries = st.multiselect(
    'Which countries would you like to view?',
    countries,
    ['DEU', 'FRA', 'GBR', 'BRA', 'MEX', 'JPN'])

''
''
''

# Filter the data
filtered_gdp_df = gdp_df[
    (gdp_df['Country Code'].isin(selected_countries))
    & (gdp_df['Year'] <= to_year)
    & (from_year <= gdp_df['Year'])
]

st.header('GDP over time', divider='gray')

''

st.line_chart(
    filtered_gdp_df,
    x='Year',
    y='GDP',
    color='Country Code',
)

''
''


first_year = gdp_df[gdp_df['Year'] == from_year]
last_year = gdp_df[gdp_df['Year'] == to_year]

st.header(f'GDP in {to_year}', divider='gray')

''

cols = st.columns(4)

for i, country in enumerate(selected_countries):
    col = cols[i % len(cols)]

    with col:
        first_gdp = first_year[first_year['Country Code'] == country]['GDP'].iat[0] / 1000000000
        last_gdp = last_year[last_year['Country Code'] == country]['GDP'].iat[0] / 1000000000

        if math.isnan(first_gdp):
            growth = 'n/a'
            delta_color = 'off'
        else:
            growth = f'{last_gdp / first_gdp:,.2f}x'
            delta_color = 'normal'

        st.metric(
            label=f'{country} GDP',
            value=f'{last_gdp:,.0f}B',
            delta=growth,
            delta_color=delta_color
        )
import streamlit as st
import pandas as pd
import altair as alt

# إعدادات الصفحة والجماليات
st.set_page_config(page_title="محلل الناتج المحلي العالمي", page_icon="📈", layout="wide")

# تنسيق العنوان
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌍 لوحة بيانات الناتج المحلي الإجمالي</h1>", unsafe_allow_html=True)
st.write("---")

# وظيفة تحميل البيانات
@st.cache_data
def load_data():
    try:
        # تأكد من وضع الملف في مجلد data
        df = pd.read_csv('data/gdp_data.csv')
        return df
    except:
        return None

df = load_data()

if df is not None:
    # --- الشريط الجانبي (Sidebar) ---
    st.sidebar.header("🔍 محرك البحث والفلترة")
    
    # محرك بحث الدول (يسمح باختيار دول متعددة)
    all_countries = sorted(df['Country'].unique())
    selected_countries = st.sidebar.multiselect(
        "ابحث عن الدول التي تريد مقارنتها:",
        options=all_countries,
        default=[all_countries[0]] # اختيار أول دولة تلقائياً
    )

    # فلترة السنوات
    min_year = int(df['Year'].min())
    max_year = int(df['Year'].max())
    year_range = st.sidebar.slider("اختر النطاق الزمني:", min_year, max_year, (min_year, max_year))

    # تطبيق الفلترة
    mask = (df['Country'].isin(selected_countries)) & (df['Year'].between(year_range[0], year_range[1]))
    filtered_df = df[mask]

    # --- عرض النتائج ---
    if not filtered_df.empty:
        col1, col2 = st.columns([3, 1])

        with col1:
            st.subheader("📈 الرسم البياني للمقارنة")
            chart = alt.Chart(filtered_df).mark_line(point=True, size=3).encode(
                x=alt.X('Year:O', title='السنة'),
                y=alt.Y('GDP:Q', title='الناتج المحلي (بمليارات الدولارات)'),
                color=alt.Color('Country:N', title='الدولة'),
                tooltip=['Country', 'Year', 'GDP']
            ).properties(height=400).interactive()
            st.altair_chart(chart, use_container_width=True)

        with col2:
            st.subheader("📋 البيانات المختارة")
            st.dataframe(filtered_df.sort_values(by=['Country', 'Year']), use_container_width=True)
            
        # إضافة ميزة "أعلى قيمة" لكل دولة مختارة
        st.write("---")
        st.subheader("💡 ملخص سريع")
        metrics_cols = st.columns(len(selected_countries) if len(selected_countries) <= 4 else 4)
        for i, country in enumerate(selected_countries[:4]): # عرض أول 4 دول فقط كمؤشرات
            country_max = filtered_df[filtered_df['Country'] == country]['GDP'].max()
            metrics_cols[i % 4].metric(label=f"أعلى ناتج لـ {country}", value=f"${country_max}B")
    else:
        st.info("💡 ابدأ بالبحث واختيار الدول من القائمة الجانبية لعرض البيانات.")

else:
    st.error("⚠️ لم نجد ملف البيانات! تأكد من وجود ملف `data/gdp_data.csv`.")
    st.info("يمكنك إنشاء المجلد والملف في GitHub ثم إعادة تحديث الصفحة.")
import streamlit as st
import pandas as pd
import math
from pathlib import Path

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='GDP dashboard',
    page_icon=':earth_americas:', # This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------
# Declare some useful functions.

@st.cache_data
def get_gdp_data():
    """Grab GDP data from a CSV file.

    This uses caching to avoid having to read the file every time. If we were
    reading from an HTTP endpoint instead of a file, it's a good idea to set
    a maximum age to the cache with the TTL argument: @st.cache_data(ttl='1d')
    """

    # Instead of a CSV on disk, you could read from an HTTP endpoint here too.
    DATA_FILENAME = Path(__file__).parent/'data/gdp_data.csv'
    raw_gdp_df = pd.read_csv(DATA_FILENAME)

    MIN_YEAR = 1960
    MAX_YEAR = 2022

    # The data above has columns like:
    # - Country Name
    # - Country Code
    # - [Stuff I don't care about]
    # - GDP for 1960
    # - GDP for 1961
    # - GDP for 1962
    # - ...
    # - GDP for 2022
    #
    # ...but I want this instead:
    # - Country Name
    # - Country Code
    # - Year
    # - GDP
    #
    # So let's pivot all those year-columns into two: Year and GDP
    gdp_df = raw_gdp_df.melt(
        ['Country Code'],
        [str(x) for x in range(MIN_YEAR, MAX_YEAR + 1)],
        'Year',
        'GDP',
    )

    # Convert years from string to integers
    gdp_df['Year'] = pd.to_numeric(gdp_df['Year'])

    return gdp_df

gdp_df = get_gdp_data()

# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
'''
# :earth_americas: GDP dashboard

Browse GDP data from the [World Bank Open Data](https://data.worldbank.org/) website. As you'll
notice, the data only goes to 2022 right now, and datapoints for certain years are often missing.
But it's otherwise a great (and did I mention _free_?) source of data.
'''

# Add some spacing
''
''

min_value = gdp_df['Year'].min()
max_value = gdp_df['Year'].max()

from_year, to_year = st.slider(
    'Which years are you interested in?',
    min_value=min_value,
    max_value=max_value,
    value=[min_value, max_value])

countries = gdp_df['Country Code'].unique()

if not len(countries):
    st.warning("Select at least one country")

selected_countries = st.multiselect(
    'Which countries would you like to view?',
    countries,
    ['DEU', 'FRA', 'GBR', 'BRA', 'MEX', 'JPN'])

''
''
''

# Filter the data
filtered_gdp_df = gdp_df[
    (gdp_df['Country Code'].isin(selected_countries))
    & (gdp_df['Year'] <= to_year)
    & (from_year <= gdp_df['Year'])
]

st.header('GDP over time', divider='gray')

''

st.line_chart(
    filtered_gdp_df,
    x='Year',
    y='GDP',
    color='Country Code',
)

''
''


first_year = gdp_df[gdp_df['Year'] == from_year]
last_year = gdp_df[gdp_df['Year'] == to_year]

st.header(f'GDP in {to_year}', divider='gray')

''

cols = st.columns(4)

for i, country in enumerate(selected_countries):
    col = cols[i % len(cols)]

    with col:
        first_gdp = first_year[first_year['Country Code'] == country]['GDP'].iat[0] / 1000000000
        last_gdp = last_year[last_year['Country Code'] == country]['GDP'].iat[0] / 1000000000

        if math.isnan(first_gdp):
            growth = 'n/a'
            delta_color = 'off'
        else:
            growth = f'{last_gdp / first_gdp:,.2f}x'
            delta_color = 'normal'

        st.metric(
            label=f'{country} GDP',
            value=f'{last_gdp:,.0f}B',
            delta=growth,
            delta_color=delta_color
        )
import streamlit as st
import pandas as pd
import altair as alt

# إعدادات الصفحة والجماليات
st.set_page_config(page_title="محلل الناتج المحلي العالمي", page_icon="📈", layout="wide")

# تنسيق العنوان
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🌍 لوحة بيانات الناتج المحلي الإجمالي</h1>", unsafe_allow_html=True)
st.write("---")

# وظيفة تحميل البيانات
@st.cache_data
def load_data():
    try:
        # تأكد من وضع الملف في مجلد data
        df = pd.read_csv('data/gdp_data.csv')
        return df
    except:
        return None

df = load_data()

if df is not None:
    # --- الشريط الجانبي (Sidebar) ---
    st.sidebar.header("🔍 محرك البحث والفلترة")
    
    # محرك بحث الدول (يسمح باختيار دول متعددة)
    all_countries = sorted(df['Country'].unique())
    selected_countries = st.sidebar.multiselect(
        "ابحث عن الدول التي تريد مقارنتها:",
        options=all_countries,
        default=[all_countries[0]] # اختيار أول دولة تلقائياً
    )

    # فلترة السنوات
    min_year = int(df['Year'].min())
    max_year = int(df['Year'].max())
    year_range = st.sidebar.slider("اختر النطاق الزمني:", min_year, max_year, (min_year, max_year))

    # تطبيق الفلترة
    mask = (df['Country'].isin(selected_countries)) & (df['Year'].between(year_range[0], year_range[1]))
    filtered_df = df[mask]

    # --- عرض النتائج ---
    if not filtered_df.empty:
        col1, col2 = st.columns([3, 1])

        with col1:
            st.subheader("📈 الرسم البياني للمقارنة")
            chart = alt.Chart(filtered_df).mark_line(point=True, size=3).encode(
                x=alt.X('Year:O', title='السنة'),
                y=alt.Y('GDP:Q', title='الناتج المحلي (بمليارات الدولارات)'),
                color=alt.Color('Country:N', title='الدولة'),
                tooltip=['Country', 'Year', 'GDP']
            ).properties(height=400).interactive()
            st.altair_chart(chart, use_container_width=True)

        with col2:
            st.subheader("📋 البيانات المختارة")
            st.dataframe(filtered_df.sort_values(by=['Country', 'Year']), use_container_width=True)
            
        # إضافة ميزة "أعلى قيمة" لكل دولة مختارة
        st.write("---")
        st.subheader("💡 ملخص سريع")
        metrics_cols = st.columns(len(selected_countries) if len(selected_countries) <= 4 else 4)
        for i, country in enumerate(selected_countries[:4]): # عرض أول 4 دول فقط كمؤشرات
            country_max = filtered_df[filtered_df['Country'] == country]['GDP'].max()
            metrics_cols[i % 4].metric(label=f"أعلى ناتج لـ {country}", value=f"${country_max}B")
    else:
        st.info("💡 ابدأ بالبحث واختيار الدول من القائمة الجانبية لعرض البيانات.")

else:
    st.error("⚠️ لم نجد ملف البيانات! تأكد من وجود ملف `data/gdp_data.csv`.")
    st.info("يمكنك إنشاء المجلد والملف في GitHub ثم إعادة تحديث الصفحة.")
