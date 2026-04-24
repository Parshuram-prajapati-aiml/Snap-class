import streamlit as st


def style_background_home():
    """
    Redesigned Home Theme — Dark Charcoal + Lime & Blue Accents.
    Column card styles are scoped so they ONLY apply to the two role
    cards and never bleed into logo/tagline helper columns.
    """
    st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">

    <style>
    /* ── Reset & hide Streamlit chrome ── */
    #MainMenu, footer, header { visibility: hidden; }

    /* ── Base background ── */
    .stApp {
        background-color: #07070F !important;
        background-image:
            radial-gradient(ellipse 60% 50% at 80% 10%, rgba(99,55,255,0.18) 0%, transparent 70%),
            radial-gradient(ellipse 40% 40% at 20% 80%, rgba(255,180,0,0.08) 0%, transparent 60%) !important;
    }

    /* Subtle grid overlay */
    .stApp::before {
        content: '';
        position: fixed;
        inset: 0;
        background-image:
            repeating-linear-gradient(0deg, transparent, transparent 59px,
                rgba(255,255,255,0.025) 59px, rgba(255,255,255,0.025) 60px),
            repeating-linear-gradient(90deg, transparent, transparent 59px,
                rgba(255,255,255,0.025) 59px, rgba(255,255,255,0.025) 60px);
        pointer-events: none;
        z-index: 0;
    }

    .block-container {
        padding-top: 2rem !important;
        max-width: 900px !important;
    }

    /* ── Typography overrides ── */
    h1 {
        font-family: 'Bebas Neue', sans-serif !important;
        letter-spacing: 3px !important;
        color: #FFFFFF !important;
    }

    h2 {
        font-family: 'Bebas Neue', sans-serif !important;
        font-size: 2.4rem !important;
        letter-spacing: 1px !important;
        line-height: 1 !important;
        color: #FFFFFF !important;
        text-shadow: none !important;
    }

    p, span, label {
        font-family: 'DM Sans', sans-serif !important;
    }

    /* ── Role card columns ──────────────────────────────────────
       We target the SPECIFIC horizontal block that holds the two
       role cards by using the data-gap attribute Streamlit sets
       on the row wrapper when gap="large".
       This prevents the logo/tagline helper columns from getting
       the dark card treatment.
    ────────────────────────────────────────────────────────── */
    [data-testid="stHorizontalBlock"]:has(> [data-testid="stColumn"]:nth-child(2))
        [data-testid="stColumn"] {
        background: #10101E !important;
        border-radius: 24px !important;
        padding: 2rem 1.75rem !important;
        transition: transform 0.25s ease, box-shadow 0.25s ease !important;
    }

    /* Student column — lime glow */
    [data-testid="stHorizontalBlock"]:has(> [data-testid="stColumn"]:nth-child(2))
        [data-testid="stColumn"]:nth-child(1) {
        border: 1px solid rgba(200,255,0,0.2) !important;
    }
    [data-testid="stHorizontalBlock"]:has(> [data-testid="stColumn"]:nth-child(2))
        [data-testid="stColumn"]:nth-child(1):hover {
        transform: translateY(-5px) !important;
        box-shadow: 0 20px 50px rgba(200,255,0,0.13) !important;
        border-color: rgba(200,255,0,0.45) !important;
    }

    /* Teacher column — blue glow */
    [data-testid="stHorizontalBlock"]:has(> [data-testid="stColumn"]:nth-child(2))
        [data-testid="stColumn"]:nth-child(2) {
        border: 1px solid rgba(100,140,255,0.2) !important;
    }
    [data-testid="stHorizontalBlock"]:has(> [data-testid="stColumn"]:nth-child(2))
        [data-testid="stColumn"]:nth-child(2):hover {
        transform: translateY(-5px) !important;
        box-shadow: 0 20px 50px rgba(100,140,255,0.13) !important;
        border-color: rgba(100,140,255,0.45) !important;
    }

    /* ── Buttons ── */
    div.stButton > button {
        width: 100% !important;
        border-radius: 14px !important;
        height: 52px !important;
        font-family: 'DM Sans', sans-serif !important;
        font-size: 14px !important;
        font-weight: 600 !important;
        border: none !important;
        transition: all 0.2s ease !important;
    }

    div.stButton > button:hover {
        transform: translateY(-2px) !important;
    }

    /* Student button — lime */
    [data-testid="stHorizontalBlock"]:has(> [data-testid="stColumn"]:nth-child(2))
        [data-testid="stColumn"]:nth-child(1) div.stButton > button {
        background: #C8FF00 !important;
        color: #07070F !important;
    }
    [data-testid="stHorizontalBlock"]:has(> [data-testid="stColumn"]:nth-child(2))
        [data-testid="stColumn"]:nth-child(1) div.stButton > button:hover {
        background: #d6ff33 !important;
        box-shadow: 0 8px 24px rgba(200,255,0,0.35) !important;
    }

    /* Teacher button — blue */
    [data-testid="stHorizontalBlock"]:has(> [data-testid="stColumn"]:nth-child(2))
        [data-testid="stColumn"]:nth-child(2) div.stButton > button {
        background: #648CFF !important;
        color: #07070F !important;
    }
    [data-testid="stHorizontalBlock"]:has(> [data-testid="stColumn"]:nth-child(2))
        [data-testid="stColumn"]:nth-child(2) div.stButton > button:hover {
        background: #7a9fff !important;
        box-shadow: 0 8px 24px rgba(100,140,255,0.35) !important;
    }

    /* ── Images ── */
    div[data-testid="stImage"] {
        display: flex !important;
        justify-content: center !important;
    }
    div[data-testid="stImage"] img {
        filter: drop-shadow(0 10px 30px rgba(0,0,0,0.5));
    }
    </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    """Dark Mode Dashboard: Midnight Navy Theme with High-Contrast White Card Fix"""
    st.markdown("""
        <style>
            .stApp {
                background-color: #0F111A !important;
                background-image:
                    radial-gradient(at 0% 0%, rgba(58,32,140,0.15) 0px, transparent 50%),
                    radial-gradient(at 100% 0%, rgba(88,101,242,0.1) 0px, transparent 50%) !important;
            }

            div[style*="background-color: white"],
            div[style*="background-color: rgb(255, 255, 255)"],
            div[style*="background-color: #ffffff"],
            div[style*="background: white"] { color: #000000 !important; }

            div[style*="background-color: white"] [data-testid="stMarkdownContainer"] p,
            div[style*="background-color: rgb(255, 255, 255)"] [data-testid="stMarkdownContainer"] p,
            div[style*="background-color: white"] [data-testid="stMarkdownContainer"] span {
                color: #10121a !important;
                -webkit-text-fill-color: #10121a !important;
                font-weight: 700 !important;
            }

            div[style*="background-color: white"] * { color: #10121a !important; }

            div[style*="background-color: white"] span[style*="background-color: rgb(232, 234, 254)"] {
                color: #5865F2 !important;
                -webkit-text-fill-color: #5865F2 !important;
            }

            div[data-testid="stVerticalBlockBorderWrapper"] {
                background-color: #161925 !important;
                border: 1px solid #2D3748 !important;
                border-radius: 20px !important;
                padding: 1.5rem !important;
                margin-bottom: 1rem !important;
            }

            h1, h2, h3 { color: #FFFFFF !important; text-shadow: none !important; }
            label, .stMarkdown p { color: #A0AEC0; }

            .stTextInput > div > div > input {
                background-color: #1A1D29 !important;
                color: white !important;
                border: 1px solid #2D3748 !important;
                border-radius: 12px !important;
            }

            /* Hide duplicate password visibility icons */
            input[type="password"] ~ button,
            .stTextInput button[aria-label*="show"],
            .stTextInput button[aria-label*="hide"],
            div[class*="stPasswordInput"] button {
                display: none !important;
            }

            /* Show only the native password eye icon */
            input[type="password"]::-webkit-textfield-decoration-container {
                display: flex !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    """Shared Structure and Typography — FIXES OVERLAPPING ICONS"""
    st.markdown("""
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Outfit:wght@800&display=swap');

            #MainMenu, footer, header { visibility: hidden; }
            .block-container { padding-top: 2rem !important; max-width: 1100px !important; }

            h1 { font-family: 'Outfit', sans-serif !important; font-weight: 800 !important; }
            h2, h3 { font-family: 'Plus Jakarta Sans', sans-serif !important; font-weight: 800 !important; }
            p, label, input, span { font-family: 'Plus Jakarta Sans', sans-serif !important; }

            div.stButton > button {
                width: 100% !important;
                border-radius: 14px !important;
                display: flex !important;
                flex-direction: row !important;
                align-items: center !important;
                justify-content: center !important;
                gap: 12px !important;
                height: 3.2rem !important;
                transition: all 0.2s ease !important;
            }

            div.stButton button span[data-testid="stIconMaterial"] {
                font-family: 'Material Symbols Outlined' !important;
                font-size: 24px !important;
                display: flex !important;
                align-items: center !important;
            }

            div.stButton button p {
                font-family: 'Plus Jakarta Sans', sans-serif !important;
                font-weight: 700 !important;
                margin: 0 !important;
                display: flex !important;
                align-items: center !important;
            }

            div.stButton button div[data-testid="stShortcutLabel"] { display: none !important; }

            div.stButton > button:hover {
                transform: translateY(-2px) !important;
                box-shadow: 0 8px 20px rgba(88,101,242,0.4) !important;
            }

            /* Fix overlapping dataframe headers and overflow in Streamlit tables */
            /* Hide AG Grid tooltips and popup menus, but keep Streamlit dialogs visible */
            .ag-tooltip,
            .ag-popup,
            .ag-popup-child,
            .ag-menu,
            [role="tooltip"],
            div[class*="tooltip"],
            div[class*="popup"],
            div[class*="menu"],
            div[class*="dropdown"],
            div[aria-describedby],
            .stToast,
            [class*="Popper"],
            [data-testid*="tooltip"],
            [data-testid*="popup"] {
                display: none !important;
                visibility: hidden !important;
                pointer-events: none !important;
                opacity: 0 !important;
            }

            /* Hide absolute positioned overlays ONLY within dataframes */
            div[data-testid="stDataFrameContainer"] div[style*="position: absolute"],
            div[data-testid="stDataFrameContainer"] div[style*="position:absolute"] {
                display: none !important;
                visibility: hidden !important;
            }

            /* Ensure grid container has proper overflow handling */
            div[role="grid"],
            div[class*="ag-root"],
            div[class*="stDataFrame"] {
                overflow: auto !important;
                position: relative !important;
                z-index: 1 !important;
            }

            /* Fix column headers - proper spacing and no overflow */
            div[role="columnheader"],
            [role="columnheader"] {
                white-space: normal !important;
                word-wrap: break-word !important;
                word-break: break-word !important;
                overflow: hidden !important;
                padding: 12px 8px !important;
                min-height: 50px !important;
                z-index: 2 !important;
            }

            /* Fix grid cells - wrap text and prevent overflow */
            div[role="gridcell"],
            [role="gridcell"] {
                white-space: normal !important;
                word-wrap: break-word !important;
                word-break: break-word !important;
                overflow: hidden !important;
                text-overflow: ellipsis !important;
                padding: 12px 8px !important;
                min-height: 45px !important;
                max-width: 200px !important;
                z-index: 1 !important;
            }

            /* Ensure AG Grid cell content wraps properly */
            .ag-cell-value,
            .ag-header-cell-label {
                white-space: normal !important;
                word-wrap: break-word !important;
                word-break: break-word !important;
                display: block !important;
                line-height: 1.4 !important;
            }

            /* Nuclear suppression of ALL header menu elements */
            .ag-header-cell-menu-button {
                display: none !important;
                width: 0 !important;
                height: 0 !important;
                overflow: hidden !important;
            }

            /* Hide the container that holds the menu button */
            .ag-header-cell-menu-button-container,
            div[class*="menu-button"] {
                display: none !important;
                visibility: hidden !important;
                width: 0 !important;
                height: 0 !important;
                margin: 0 !important;
                padding: 0 !important;
                overflow: hidden !important;
            }

            /* Suppress the menu icon SVG and any graphics */
            .ag-menu-icon,
            .ag-icon-menu,
            svg[class*="menu"],
            svg[class*="ellipsis"],
            [class*="filter-menu-button"],
            [class*="ag-filter"] {
                display: none !important;
                visibility: hidden !important;
                width: 0 !important;
                height: 0 !important;
            }

            /* Hide filter and sort icons completely */
            .ag-icon-filter,
            .ag-icon-sort,
            [aria-label*="Sort"],
            [aria-label*="Filter"] {
                display: none !important;
            }

            /* Make sure no overflow escapes from header cells */
            .ag-header-cell,
            div[role="columnheader"] {
                overflow: hidden !important;
                max-width: 100% !important;
            }

            /* Make dataframe container take full width with proper spacing */
            div[data-testid="stDataFrameContainer"] {
                margin-bottom: 2rem !important;
                overflow-x: auto !important;
                overflow-y: hidden !important;
                z-index: 1 !important;
            }

            /* Remove any floating elements */
            [class*="ag-floating"] {
                display: none !important;
            }

            /* Hide Streamlit column menu specifically */
            button[aria-label*="column"],
            button[aria-label*="sort"],
            button[aria-label*="filter"] {
                display: none !important;
            }
        </style>
    """, unsafe_allow_html=True)