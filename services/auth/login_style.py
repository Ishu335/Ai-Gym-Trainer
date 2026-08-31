# styles.py

import streamlit as st


def load_login_css():

    st.markdown("""
    <style>

    /* =========================================================
       REPVISION AI — COLOR PALETTE
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
       APP BACKGROUND
       ========================================================= */

    .stApp {
        background:
            radial-gradient(
                circle at 15% 20%,
                rgba(0, 230, 118, 0.08),
                transparent 30%
            ),
            radial-gradient(
                circle at 85% 80%,
                rgba(0, 191, 165, 0.07),
                transparent 30%
            ),
            var(--rv-bg);

        color: var(--rv-text);
    }


    /* =========================================================
       HIDE STREAMLIT HEADER
       ========================================================= */

    header {
        visibility: hidden;
    }


    /* =========================================================
       MAIN CONTAINER
       ========================================================= */

    .block-container {
        max-width: 1000px;

        padding-top: 3rem;
        padding-bottom: 3rem;
    }


    /* =========================================================
       TITLE
       ========================================================= */

    h1 {
        text-align: center !important;

        font-size: 3.2rem !important;
        font-weight: 800 !important;

        letter-spacing: -2px;

        color: var(--rv-text) !important;

        margin-bottom: 0.4rem !important;
    }


    /* Green accent on emoji/title area */

    h1::first-letter {
        color: var(--rv-green);
    }


    /* =========================================================
       SUBTITLE
       ========================================================= */

    .stMarkdown h3 {
        text-align: center !important;

        color: var(--rv-green) !important;

        font-size: 1.25rem !important;
        font-weight: 600 !important;

        margin-top: 0.5rem !important;
        margin-bottom: 0.8rem !important;
    }


    /* =========================================================
       DESCRIPTION
       ========================================================= */

    .stMarkdown p {
        text-align: center;

        color: var(--rv-muted);

        font-size: 1rem;

        line-height: 1.7;
    }


    .stMarkdown strong {
        color: var(--rv-text);
    }


    /* =========================================================
       STREAMLIT IMAGE
       ========================================================= */

    div[data-testid="stImage"] {

        display: flex;

        justify-content: center;
        align-items: center;

        width: 100%;

        margin: 1rem auto 0 auto;

        position: relative;
    }


    /* Actual image */

    div[data-testid="stImage"] img {

        width: auto !important;

        max-width: 100% !important;

        max-height: 520px !important;

        object-fit: contain;

        display: block;

        /* DO NOT add background */

        background: transparent !important;

        /* Smooth edges */

        border: none !important;

        outline: none !important;

        border-radius: 0 !important;

        /* Subtle green glow */

        filter:
            drop-shadow(0 0 10px rgba(0, 230, 118, 0.08))
            drop-shadow(0 20px 35px rgba(0, 0, 0, 0.45));

        transition:
            transform 0.3s ease,
            filter 0.3s ease;
    }


    /* Image hover */

    div[data-testid="stImage"] img:hover {

        transform: scale(1.015);

        filter:
            drop-shadow(0 0 18px rgba(0, 230, 118, 0.14))
            drop-shadow(0 25px 45px rgba(0, 0, 0, 0.55));
    }


    /* =========================================================
       IMAGE GLOW
       ========================================================= */

    div[data-testid="stImage"]::before {

        content: "";

        position: absolute;

        width: 45%;
        height: 45%;

        top: 35%;
        left: 50%;

        transform: translate(-50%, -50%);

        background: var(--rv-green);

        opacity: 0.045;

        filter: blur(90px);

        pointer-events: none;

        z-index: 0;
    }


    /* =========================================================
       LOGIN FORM
       ========================================================= */

    div[data-testid="stForm"] {

        background:
            linear-gradient(
                145deg,
                rgba(21, 27, 25, 0.96),
                rgba(15, 21, 19, 0.96)
            );

        border: 1px solid rgba(0, 230, 118, 0.16);

        border-radius: 20px;

        padding: 2rem;

        margin: 2rem auto 0 auto;

        max-width: 520px;

        box-shadow:
            0 20px 60px rgba(0, 0, 0, 0.45),
            0 0 35px rgba(0, 230, 118, 0.035);

        backdrop-filter: blur(15px);
    }


    /* =========================================================
       INPUT LABEL
       ========================================================= */

    [data-testid="stWidgetLabel"] p {

        color: #D7E0DC !important;

        font-weight: 600 !important;

        text-align: left !important;

        font-size: 0.9rem !important;
    }


    /* =========================================================
       INPUT
       ========================================================= */

    [data-testid="stTextInput"] input {

        background-color: var(--rv-input) !important;

        color: var(--rv-text) !important;

        border: 1px solid var(--rv-border) !important;

        border-radius: 10px !important;

        padding: 0.75rem 1rem !important;

        transition:
            border 0.2s ease,
            box-shadow 0.2s ease;
    }


    /* Input focus */

    [data-testid="stTextInput"] input:focus {

        border-color: var(--rv-green) !important;

        box-shadow:
            0 0 0 2px rgba(0, 230, 118, 0.10) !important;
    }


    /* Placeholder */

    [data-testid="stTextInput"] input::placeholder {

        color: #68756F !important;
    }


    /* =========================================================
       START SESSION BUTTON
       ========================================================= */

    [data-testid="stFormSubmitButton"] button {

        width: 100%;

        min-height: 48px;

        background:
            linear-gradient(
                135deg,
                var(--rv-green),
                var(--rv-teal)
            ) !important;

        color: #06100C !important;

        border: none !important;

        border-radius: 10px !important;

        font-size: 1rem !important;

        font-weight: 800 !important;

        margin-top: 0.6rem;

        transition:
            transform 0.2s ease,
            box-shadow 0.2s ease;
    }


    /* Button hover */

    [data-testid="stFormSubmitButton"] button:hover {

        transform: translateY(-2px);

        box-shadow:
            0 10px 30px rgba(0, 230, 118, 0.25);
    }


    /* Button click */

    [data-testid="stFormSubmitButton"] button:active {

        transform: translateY(0);
    }


    /* =========================================================
       ERROR MESSAGE
       ========================================================= */

    [data-testid="stAlert"] {

        border-radius: 10px !important;
    }


    /* =========================================================
       MOBILE
       ========================================================= */

    @media (max-width: 768px) {

        .block-container {

            padding-top: 2rem;

            padding-left: 1rem;

            padding-right: 1rem;
        }


        h1 {

            font-size: 2.3rem !important;

        }


        div[data-testid="stImage"] img {

            max-height: 400px !important;

        }


        div[data-testid="stForm"] {

            padding: 1.4rem;

        }

    }

    </style>
    """, unsafe_allow_html=True)