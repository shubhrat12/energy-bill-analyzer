import streamlit as st
import time

# --- Page Config ---
st.set_page_config(
    page_title="Energy Bill Analyzer",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- Custom CSS ---
st.markdown("""
<style>
    /* Base theme overrides */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 760px;
    }

    /* Header */
    .app-header {
        text-align: center;
        margin-bottom: 2rem;
    }
    .app-header h1 {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1a1a2e;
        letter-spacing: -0.5px;
    }
    .app-header p {
        color: #555;
        font-size: 1rem;
        margin-top: 0.25rem;
    }

    /* Upload area styling */
    .upload-label {
        font-weight: 600;
        font-size: 0.95rem;
        color: #1a1a2e;
        margin-bottom: 0.5rem;
    }

    /* Results card */
    .result-card {
        background: #f0f7ff;
        border-left: 4px solid #2563eb;
        border-radius: 6px;
        padding: 1rem 1.25rem;
        margin-bottom: 0.75rem;
    }
    .result-card .label {
        font-size: 0.78rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        color: #2563eb;
        margin-bottom: 0.2rem;
    }
    .result-card .value {
        font-size: 1.4rem;
        font-weight: 700;
        color: #1a1a2e;
    }

    /* Suggestion items */
    .suggestion-item {
        display: flex;
        align-items: flex-start;
        gap: 0.75rem;
        background: #fff;
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        padding: 0.85rem 1rem;
        margin-bottom: 0.6rem;
    }
    .suggestion-icon {
        font-size: 1.3rem;
        line-height: 1;
        flex-shrink: 0;
    }
    .suggestion-text {
        font-size: 0.95rem;
        color: #1a1a2e;
        line-height: 1.45;
    }
    .suggestion-text strong {
        display: block;
        margin-bottom: 0.15rem;
    }
    .suggestion-text span {
        color: #555;
        font-size: 0.88rem;
    }

    /* Section heading */
    .section-heading {
        font-size: 1.05rem;
        font-weight: 700;
        color: #1a1a2e;
        margin: 1.5rem 0 0.75rem;
        padding-bottom: 0.4rem;
        border-bottom: 2px solid #e5e7eb;
    }

    /* Divider */
    hr { border-color: #e5e7eb; }

    /* Analyze button override */
    div.stButton > button {
        background-color: #2563eb;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 0.55rem 1.5rem;
        font-size: 1rem;
        font-weight: 600;
        width: 100%;
        transition: background 0.2s;
    }
    div.stButton > button:hover {
        background-color: #1d4ed8;
        color: white;
    }
</style>
""", unsafe_allow_html=True)


# --- Header ---
st.markdown("""
<div class="app-header">
    <h1>⚡ Energy Bill Analyzer</h1>
    <p>Upload your energy bill and get instant insights and savings tips.</p>
</div>
""", unsafe_allow_html=True)


# --- File Upload ---
st.markdown('<div class="upload-label">Upload your energy bill</div>', unsafe_allow_html=True)
uploaded_file = st.file_uploader(
    label="Upload your energy bill",
    type=["pdf", "png", "jpg", "jpeg"],
    label_visibility="collapsed",
    help="Supported formats: PDF, PNG, JPG"
)

if uploaded_file:
    st.success(f"✅ **{uploaded_file.name}** uploaded successfully ({uploaded_file.size / 1024:.1f} KB)")

st.markdown("<br>", unsafe_allow_html=True)

# --- Analyze Button ---
analyze_clicked = st.button("🔍 Analyze Bill", disabled=(uploaded_file is None))

if uploaded_file is None:
    st.caption("Upload a bill file above to enable analysis.")


# --- Results (shown after clicking Analyze) ---
if analyze_clicked and uploaded_file is not None:

    with st.spinner("Analyzing your bill…"):
        time.sleep(1.8)  # Simulate processing time

    st.markdown("---")

    # -- Extracted Data --
    st.markdown('<div class="section-heading">📊 Extracted Bill Data</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="result-card">
            <div class="label">Total Amount Due</div>
            <div class="value">$150.00</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="result-card">
            <div class="label">Energy Usage</div>
            <div class="value">500 kWh</div>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="result-card">
            <div class="label">Billing Period</div>
            <div class="value">May 2025</div>
        </div>""", unsafe_allow_html=True)

    col4, col5 = st.columns(2)
    with col4:
        st.markdown("""
        <div class="result-card">
            <div class="label">Rate per kWh</div>
            <div class="value">$0.30</div>
        </div>""", unsafe_allow_html=True)
    with col5:
        st.markdown("""
        <div class="result-card">
            <div class="label">Peak Usage Time</div>
            <div class="value">6 – 9 PM</div>
        </div>""", unsafe_allow_html=True)

    # -- Suggestions --
    st.markdown('<div class="section-heading">💡 Energy-Saving Suggestions</div>', unsafe_allow_html=True)

    suggestions = [
        {
            "icon": "🌡️",
            "title": "Install a smart thermostat",
            "detail": "Automatically adjusts temperature when you're away. Can reduce heating and cooling costs by up to 15%.",
        },
        {
            "icon": "🪟",
            "title": "Seal drafts around windows and doors",
            "detail": "Weatherstripping and caulk are low-cost fixes that prevent warm or cool air from escaping.",
        },
        {
            "icon": "🕗",
            "title": "Shift usage away from peak hours (6–9 PM)",
            "detail": "Run dishwashers, laundry, and EV charging overnight to take advantage of off-peak rates.",
        },
        {
            "icon": "💡",
            "title": "Replace remaining incandescent bulbs with LED",
            "detail": "LEDs use up to 80% less energy and last significantly longer than traditional bulbs.",
        },
        {
            "icon": "🔌",
            "title": "Unplug devices on standby",
            "detail": "'Phantom load' from idle electronics can account for up to 10% of your monthly bill.",
        },
    ]

    for s in suggestions:
        st.markdown(f"""
        <div class="suggestion-item">
            <div class="suggestion-icon">{s['icon']}</div>
            <div class="suggestion-text">
                <strong>{s['title']}</strong>
                <span>{s['detail']}</span>
            </div>
        </div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.caption("ℹ️ Results shown are based on mock data for demonstration purposes. Connect a live OCR/AI backend to analyze real bills.")
