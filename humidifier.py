import streamlit as st

st.set_page_config(page_title="Humidity Control Simulation", layout="centered")
st.title("Humidity Control Simulation")

# Повзунок вологості
humidity = st.slider("Humidity (%)", min_value=0, max_value=100, value=50)

# Зберігаємо стан зволожувача (щоб не скидалося на кожен ререндер)
#   Використовуємо st.session_state
if "is_automizer_on" not in st.session_state:
    st.session_state.is_automizer_on = False

# Логіка вмикання/вимикання
if humidity <= 40 and not st.session_state.is_automizer_on:
    st.session_state.is_automizer_on = True
elif humidity >= 53 and st.session_state.is_automizer_on:
    st.session_state.is_automizer_on = False

# Імітація OLED-виводу
if st.session_state.is_automizer_on:
    st.write("**In Operation**")
else:
    st.write("**Ready**")

st.write(f"Humid: {humidity}%")

# Debug-повідомлення (імітація Serial)
if st.session_state.is_automizer_on:
    st.write("Automizer On (Relay: HIGH)")
else:
    st.write("Automizer Off (Relay: LOW)")

# CSS для анімації
circle_css = """
<style>
.rotating {
  animation: rotate 2s linear infinite;
}
@keyframes rotate {
  0%   { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
.svg-container {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}
</style>
"""
st.markdown(circle_css, unsafe_allow_html=True)

# SVG-код
svg_class = "rotating" if st.session_state.is_automizer_on else ""

svg_code = f"""
<div class="svg-container">
<svg width="200" height="200" viewBox="0 0 100 100">
  <g class="{svg_class}" style="transform-origin: 50px 50px;">
    <circle cx="50" cy="50" r="40" fill="#555555"/>
    <line x1="50" y1="50" x2="90" y2="50" stroke="#cccccc" stroke-width="3" />
    <line x1="50" y1="50" x2="50" y2="10" stroke="#cccccc" stroke-width="3" />
    <line x1="50" y1="50" x2="10" y2="50" stroke="#cccccc" stroke-width="3" />
    <line x1="50" y1="50" x2="50" y2="90" stroke="#cccccc" stroke-width="3" />
    <line x1="50" y1="50" x2="78" y2="21" stroke="#cccccc" stroke-width="3" />
    <line x1="50" y1="50" x2="21" y2="21" stroke="#cccccc" stroke-width="3" />
    <line x1="50" y1="50" x2="21" y2="78" stroke="#cccccc" stroke-width="3" />
    <line x1="50" y1="50" x2="78" y2="78" stroke="#cccccc" stroke-width="3" />
  </g>
</svg>
</div>
"""

st.markdown(svg_code, unsafe_allow_html=True)
