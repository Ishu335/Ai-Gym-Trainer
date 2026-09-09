import streamlit as st 
def style_side_bar():
    st.markdown("""
<style>

/* =========================================================
   REPVISION AI — SIDEBAR
   Uses the same global color palette
   ========================================================= */

:root {
    --rv-bg: #0B0F0E;
    --rv-card: #151B19;
    --rv-input: #0F1513;

    --rv-green: #00E676;
    --rv-teal: #00BFA5;

    --rv-text: #F5F7F6;
    --rv-muted: #9AA7A2;
    --rv-border: #29332F;
}


/* =========================================================
   SIDEBAR BACKGROUND
   ========================================================= */

section[data-testid="stSidebar"] {

    background:
        radial-gradient(
            circle at 20% 10%,
            rgba(0, 230, 118, 0.07),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 90%,
            rgba(0, 191, 165, 0.06),
            transparent 35%
        ),
        var(--rv-bg) !important;

    border-right: 1px solid var(--rv-border);

}


/* Sidebar content */

section[data-testid="stSidebar"] > div {

    padding: 1.2rem 1rem;

}


/* =========================================================
   SIDEBAR TITLE
   ========================================================= */

section[data-testid="stSidebar"] h1 {

    color: var(--rv-text) !important;

    font-size: 1.55rem !important;

    font-weight: 800 !important;

    letter-spacing: -0.8px;

    margin-bottom: 1rem !important;

}


/* Green accent */

section[data-testid="stSidebar"] h1::first-letter {

    color: var(--rv-green);

}


/* =========================================================
   SIDEBAR HEADINGS
   ========================================================= */

section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {

    color: var(--rv-text) !important;

    font-weight: 700 !important;

    letter-spacing: -0.3px;

}


/* =========================================================
   DIVIDERS
   ========================================================= */

section[data-testid="stSidebar"] hr {

    border: none !important;

    border-top: 1px solid var(--rv-border) !important;

    margin: 1.2rem 0 !important;

}


/* =========================================================
   LABELS
   ========================================================= */

section[data-testid="stSidebar"]
[data-testid="stWidgetLabel"] p {

    color: var(--rv-muted) !important;

    font-size: 0.85rem !important;

    font-weight: 600 !important;

}


/* =========================================================
   SELECT BOX
   ========================================================= */

section[data-testid="stSidebar"]
div[data-baseweb="select"] > div {

    background-color: var(--rv-input) !important;

    border: 1px solid var(--rv-border) !important;

    border-radius: 10px !important;

    color: var(--rv-text) !important;

    transition:
        border 0.2s ease,
        box-shadow 0.2s ease;

}


/* Select hover */

section[data-testid="stSidebar"]
div[data-baseweb="select"] > div:hover {

    border-color: rgba(0, 230, 118, 0.45) !important;

}


/* =========================================================
   NUMBER INPUT
   ========================================================= */

section[data-testid="stSidebar"]
[data-testid="stNumberInput"] input {

    background-color: var(--rv-input) !important;

    color: var(--rv-text) !important;

    border: 1px solid var(--rv-border) !important;

    border-radius: 10px !important;

}


/* Number input focus */

section[data-testid="stSidebar"]
[data-testid="stNumberInput"] input:focus {

    border-color: var(--rv-green) !important;

    box-shadow:
        0 0 0 2px rgba(0, 230, 118, 0.08) !important;

}


/* =========================================================
   METRIC CARDS
   ========================================================= */

section[data-testid="stSidebar"]
[data-testid="stMetric"] {

    background:
        linear-gradient(
            145deg,
            rgba(21, 27, 25, 0.95),
            rgba(15, 21, 19, 0.95)
        );

    border: 1px solid var(--rv-border);

    border-radius: 12px;

    padding: 12px 14px;

    margin-bottom: 8px;

    box-shadow:
        0 8px 25px rgba(0, 0, 0, 0.18);

}


/* Metric label */

section[data-testid="stSidebar"]
[data-testid="stMetricLabel"] {

    color: var(--rv-muted) !important;

}


/* Metric value */

section[data-testid="stSidebar"]
[data-testid="stMetricValue"] {

    color: var(--rv-green) !important;

    font-weight: 800 !important;

}


/* =========================================================
   PROGRESS BAR
   ========================================================= */

section[data-testid="stSidebar"]
[data-testid="stProgress"] {

    background: var(--rv-card) !important;

    border-radius: 20px !important;

}


section[data-testid="stSidebar"]
[data-testid="stProgress"] > div {

    background:
        linear-gradient(
            90deg,
            var(--rv-green),
            var(--rv-teal)
        ) !important;

    border-radius: 20px !important;

}


/* =========================================================
   START / STOP BUTTON
   ========================================================= */

section[data-testid="stSidebar"]
.stButton > button {

    width: 100%;

    min-height: 46px;

    background:
        linear-gradient(
            135deg,
            var(--rv-green),
            var(--rv-teal)
        ) !important;

    color: #06100C !important;

    border: none !important;

    border-radius: 10px !important;

    font-size: 0.95rem !important;

    font-weight: 800 !important;

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease;

}


/* Button hover */

section[data-testid="stSidebar"]
.stButton > button:hover {

    transform: translateY(-2px);

    box-shadow:
        0 10px 30px rgba(0, 230, 118, 0.20);

}


/* Button active */

section[data-testid="stSidebar"]
.stButton > button:active {

    transform: translateY(0);

}


/* =========================================================
   SUCCESS STATUS
   ========================================================= */

section[data-testid="stSidebar"]
[data-testid="stAlert"] {

    border-radius: 10px !important;

}


/* Success */

section[data-testid="stSidebar"]
[data-testid="stAlert"] {

    background: rgba(0, 230, 118, 0.06) !important;

    border: 1px solid rgba(0, 230, 118, 0.18) !important;

}


/* =========================================================
   STATUS TEXT
   ========================================================= */

.status-good {

    color: var(--rv-green);

    font-weight: 700;

}


.status-warning {

    color: #E8B949;

    font-weight: 700;

}


.status-bad {

    color: #FF5C67;

    font-weight: 700;

}


.status-neutral {

    color: var(--rv-muted);

    font-weight: 600;

}


/* =========================================================
   CUSTOM GYM CARD
   ========================================================= */

.gym-card {

    background:
        linear-gradient(
            145deg,
            rgba(21, 27, 25, 0.96),
            rgba(15, 21, 19, 0.96)
        );

    border: 1px solid var(--rv-border);

    border-radius: 14px;

    padding: 14px;

    margin-bottom: 10px;

    box-shadow:
        0 10px 30px rgba(0, 0, 0, 0.22);

}


/* =========================================================
   ANGLE VALUE
   ========================================================= */

.angle-value {

    color: var(--rv-green);

    font-size: 1.25rem;

    font-weight: 800;

}


/* =========================================================
   WORKOUT COMPLETE
   ========================================================= */

.workout-complete {

    background:
        linear-gradient(
            135deg,
            rgba(0, 230, 118, 0.12),
            rgba(0, 191, 165, 0.08)
        );

    border: 1px solid rgba(0, 230, 118, 0.25);

    border-radius: 14px;

    padding: 15px;

    text-align: center;

    color: var(--rv-green);

    font-weight: 800;

    box-shadow:
        0 0 25px rgba(0, 230, 118, 0.06);

}


/* =========================================================
   SCROLLBAR
   ========================================================= */

section[data-testid="stSidebar"] ::-webkit-scrollbar {

    width: 5px;

}


section[data-testid="stSidebar"] ::-webkit-scrollbar-track {

    background: var(--rv-bg);

}


section[data-testid="stSidebar"] ::-webkit-scrollbar-thumb {

    background: var(--rv-border);

    border-radius: 10px;

}


section[data-testid="stSidebar"] ::-webkit-scrollbar-thumb:hover {

    background: var(--rv-green);

}


/* =========================================================
   MOBILE
   ========================================================= */

@media (max-width: 768px) {

    section[data-testid="stSidebar"] > div {

        padding: 1rem 0.8rem;

    }

}

</style>
""", unsafe_allow_html=True)