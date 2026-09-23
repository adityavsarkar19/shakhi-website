import streamlit as st
import streamlit.components.v1 as components
import time
from pathlib import Path
import base64


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="A Very Important Investigation 💌",
    page_icon="💗",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# ============================================================
# IMAGE HELPER
# ============================================================

def image_to_base64(path):

    if not path.exists():
        return None

    mime_types = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".webp": "image/webp",
        ".gif": "image/gif"
    
    }

    mime_type = mime_types.get(path.suffix.lower())

    if mime_type is None:
        return None

    encoded = base64.b64encode(
        path.read_bytes()
    ).decode("utf-8")

    return "data:" + mime_type + ";base64," + encoded


# ============================================================
# FILE PATHS
# ============================================================

BACKGROUND_PATH = Path("assets/background.jpg")
ADI_PATH = Path("assets/adi.jpg")
GRAPH_PATH = Path("assets/graph.gif")
CONGRATULATIONS_PATH = Path("assets/congratulations.jpg")


# ============================================================
# LOAD IMAGES
# ============================================================

background_data = image_to_base64(BACKGROUND_PATH)
adi_data = image_to_base64(ADI_PATH)
graph_data = image_to_base64(GRAPH_PATH)
congratulations_data = image_to_base64(CONGRATULATIONS_PATH)


# ============================================================
# GLOBAL CSS
# ============================================================

st.html(
    """
    <style>

        @import url(
            'https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap'
        );


        /* ====================================================
           GLOBAL
           ==================================================== */

        html,
        body {
            font-family: 'DM Sans', sans-serif !important;
        }


        .stApp {
            background: #fff8f8;
        }


        header {
            visibility: hidden;
        }


        footer {
            visibility: hidden;
        }


        #MainMenu {
            visibility: hidden;
        }


        .block-container {
            max-width: 720px;
            padding-top: 30px;
            padding-bottom: 60px;
        }


        /* ====================================================
           BRIGHT RED
           ==================================================== */

        :root {

            --bright-red: #e00020;

            --bright-red-dark: #c9001d;

            --bright-red-light: #fff1f3;

        }


        /* ====================================================
           STREAMLIT BUTTONS
           ==================================================== */

        .stButton > button {

            width: 100%;

            min-height: 48px;

            border-radius: 14px;

            border: 1px solid #ead5d8;

            background: rgba(255,255,255,0.97);

            color: #3b2529;

            font-family:
                'DM Sans',
                sans-serif;

            font-size: 15px;

            font-weight: 600;

            box-shadow: none;

            transition:
                background 0.2s ease,
                border-color 0.2s ease,
                transform 0.2s ease;

        }


        .stButton > button:hover {

            background: var(--bright-red-light);

            border-color: var(--bright-red);

            color: var(--bright-red-dark);

            transform: translateY(-1px);

        }


        /* ====================================================
           LANDING PAGE
           ==================================================== */

        .landing-wrapper {

            min-height:
                calc(100vh - 50px);

            width: 100%;

            display: flex;

            flex-direction: column;

            align-items: center;

            text-align: center;

            padding:
                45px 20px 30px 20px;

            box-sizing: border-box;

        }


        .landing-title {

            font-family:
                'DM Sans',
                sans-serif;

            font-size: 64px;

            font-weight: 800;

            line-height: 1;

            color: var(--bright-red);

            letter-spacing: -2px;

            margin-bottom: 16px;

        }


        .landing-subtitle {

            font-size: 19px;

            font-weight: 600;

            color: var(--bright-red);

            margin-bottom: 8px;

        }


        .landing-hint {

            font-size: 13px;

            color: var(--bright-red);

            opacity: 0.90;

            margin-bottom: 30px;

        }


        .photo-wrapper {

            position: relative;

            width: min(430px, 86vw);

            height: 480px;

            border-radius: 28px;

            overflow: hidden;

            background:
                rgba(255,255,255,0.65);

            box-shadow:
                0 15px 45px
                rgba(60,20,25,0.18);

        }


        .photo-wrapper img {

            width: 100%;

            height: 100%;

            object-fit: cover;

            object-position: center;

            display: block;

            transition:
                opacity 0.5s ease;

        }


        .photo-message {

            position: absolute;

            inset: 0;

            display: flex;

            align-items: center;

            justify-content: center;

            padding: 45px;

            box-sizing: border-box;

            background:
                rgba(255,255,255,0.90);

            color: #111;

            font-size: 15px;

            line-height: 1.7;

            text-align: center;

            opacity: 0;

            transition:
                opacity 0.5s ease;

            pointer-events: none;

        }


        .photo-wrapper:hover img {
            opacity: 0.08;
        }


        .photo-wrapper:hover
        .photo-message {
            opacity: 1;
        }


        /* ====================================================
           QUIZ
           ==================================================== */

        .quiz-container {

            width: 100%;

            padding-top: 15px;

        }


        .quiz-progress {

            width: 100%;

            height: 6px;

            background: #f0dddd;

            border-radius: 20px;

            overflow: hidden;

            margin-bottom: 32px;

        }


        .quiz-progress-fill {

            height: 100%;

            background: var(--bright-red);

            border-radius: 20px;

        }


        .question-card {

            width: 100%;

            box-sizing: border-box;

            background:
                rgba(255,255,255,0.97);

            border:
                1px solid #eadbdd;

            border-radius: 20px;

            padding:
                30px 28px;

            margin-bottom: 22px;

            text-align: center;

            box-shadow:
                0 8px 25px
                rgba(70,30,35,0.06);

        }


        .question-number {

            font-size: 11px;

            font-weight: 800;

            letter-spacing: 1.5px;

            text-transform: uppercase;

            color: var(--bright-red);

            margin-bottom: 14px;

        }


        .question-text {

            font-family:
                'Playfair Display',
                serif;

            font-size: 27px;

            line-height: 1.35;

            color: #342528;

        }


        /* ====================================================
           RADIO OPTIONS
           ==================================================== */

        div[data-testid="stRadio"] {

            width: 100%;

        }


        div[data-testid="stRadio"] > label {

            display: none !important;

        }


        div[data-testid="stRadio"] > div {

            width: 100%;

            display: flex;

            flex-direction: column;

            gap: 9px;

        }


        div[data-testid="stRadio"]
        div[role="radiogroup"] {

            width: 100%;

            display: flex;

            flex-direction: column;

            gap: 9px;

        }


        div[data-testid="stRadio"] label {

            width: 100%;

            box-sizing: border-box;

            background:
                rgba(255,255,255,0.97);

            border:
                1px solid #e8d7da;

            border-radius: 13px;

            padding:
                13px 16px;

            margin: 0 !important;

            cursor: pointer;

            transition:
                border-color 0.2s ease,
                background 0.2s ease,
                transform 0.2s ease;

        }


        div[data-testid="stRadio"] label:hover {

            border-color: var(--bright-red);

            background: #fff7f7;

            transform: translateY(-1px);

        }


        div[data-testid="stRadio"]
        label p {

            color: #3b2529 !important;

            font-family:
                'DM Sans',
                sans-serif !important;

            font-size: 15px !important;

            font-weight: 500 !important;

            margin: 0 !important;

        }


        /* Hide native radio circles */

        div[data-testid="stRadio"]
        input[type="radio"] {

            display: none !important;

        }


        div[data-testid="stRadio"]
        [data-baseweb="radio"] {

            display: none !important;

        }


        /* ====================================================
           TITLES
           ==================================================== */

        .heart {

            text-align: center;

            font-size: 40px;

            margin-bottom: 5px;

        }


        .main-title {

            font-family:
                'Playfair Display',
                serif;

            font-size: 40px;

            font-weight: 700;

            text-align: center;

            color: var(--bright-red);

            margin-bottom: 8px;

        }


        .subtitle {

            text-align: center;

            color: var(--bright-red);

            font-size: 15px;

            line-height: 1.6;

            margin-bottom: 28px;

        }


        /* ====================================================
           ANALYSIS
           ==================================================== */

        .analysis-message {

            text-align: center;

            color: var(--bright-red);

            font-size: 15px;

            font-weight: 500;

            margin: 22px 0;

        }


        /* ====================================================
           RESULTS
           ==================================================== */

        .results-wrapper {

            width: 100%;

            text-align: center;

            padding-top: 10px;

        }


        .results-title {

            font-family:
                'Playfair Display',
                serif;

            font-size: 42px;

            font-weight: 700;

            color: var(--bright-red);

            line-height: 1.15;

            margin-bottom: 5px;

        }


        .couple-name {

            font-family:
                'Playfair Display',
                serif;

            font-size: 28px;

            font-weight: 700;

            color: var(--bright-red);

            margin-bottom: 32px;

        }


        .result-number {

            font-family:
                'Playfair Display',
                serif;

            font-size: 88px;

            font-weight: 700;

            line-height: 1;

            color: var(--bright-red);

        }


        .result-label {

            font-size: 19px;

            font-weight: 800;

            color: var(--bright-red);

            margin-top: 8px;

            margin-bottom: 32px;

        }


        /* ====================================================
           GRAPH
           ==================================================== */

        .graph-wrapper {

            width: 100%;

            max-width: 640px;

            min-height: 390px;

            margin:
                0 auto 35px auto;

            box-sizing: border-box;

            background:
                rgba(255,255,255,0.97);

            border:
                1px solid #eadbdd;

            border-radius: 22px;

            overflow: hidden;

            display: flex;

            align-items: center;

            justify-content: center;

            box-shadow:
                0 10px 30px
                rgba(70,30,35,0.07);

        }


        .graph-wrapper img {

            width: 100%;

            height: auto;

            max-height: 650px;

            object-fit: contain;

            display: block;

        }


        .graph-placeholder {

            padding:
                60px 30px;

            color: #99777d;

            font-size: 15px;

            line-height: 1.6;

            text-align: center;

        }


        .graph-placeholder-icon {

            font-size: 40px;

            margin-bottom: 15px;

        }


        /* ====================================================
           DECISION
           ==================================================== */

        .decision-label {

            text-align: center;

            color: var(--bright-red);

            font-size: 14px;

            font-weight: 500;

            margin-bottom: 10px;

        }


        /* ====================================================
           FINAL PAGE
           ==================================================== */

        .final-page {

            min-height: 100vh;

            width: 100%;

            display: flex;

            flex-direction: column;

            align-items: center;

            text-align: center;

            background: white;

            padding:
                80px 20px 70px 20px;

            box-sizing: border-box;

        }


        .final-title {

            font-family:
                'DM Sans',
                sans-serif;

            font-size: 68px;

            font-weight: 800;

            color: #b51f32;

            letter-spacing: -2px;

            line-height: 1;

            margin-bottom: 18px;

        }


        .final-subtitle {

            font-family:
                'DM Sans',
                sans-serif;

            font-size: 18px;

            color: #85686d;

            margin-bottom: 45px;

        }


        .final-image {

            width: min(850px, 92vw);

            min-height: 500px;

            display: flex;

            align-items: center;

            justify-content: center;

            background: white;

            border-radius: 20px;

            overflow: hidden;

        }


        .final-image img {

            width: 100%;

            max-height: 800px;

            object-fit: contain;

            display: block;

        }


        .download-button {

            display: inline-block;

            margin-top: 35px;

            padding:
                13px 22px;

            border-radius: 14px;

            border:
                1px solid #ead5d8;

            background: white;

            color: #3b2529;

            font-family:
                'DM Sans',
                sans-serif;

            font-size: 14px;

            font-weight: 600;

            text-decoration: none;

            cursor: pointer;

        }


        .download-button:hover {

            background: #fff3f4;

            border-color: #c95d6e;

            color: #a51e31;

        }


        /* ====================================================
           MOBILE
           ==================================================== */

        @media (max-width: 600px) {

            .block-container {

                padding:
                    20px 14px 45px 14px;

            }


            .landing-wrapper {

                padding-top: 30px;

            }


            .landing-title {

                font-size: 48px;

            }


            .landing-subtitle {

                font-size: 17px;

            }


            .photo-wrapper {

                width: 88vw;

                height: 420px;

            }


            .question-card {

                padding:
                    25px 20px;

            }


            .question-text {

                font-size: 23px;

            }


            .results-title {

                font-size: 35px;

            }


            .couple-name {

                font-size: 25px;

            }


            .result-number {

                font-size: 70px;

            }


            .graph-wrapper {

                min-height: 300px;

            }


            .final-page {

                padding-top: 60px;

            }


            .final-title {

                font-size: 50px;

            }


            .final-subtitle {

                font-size: 16px;

            }


            .final-image {

                min-height: 350px;

            }

        }

    </style>
    """
)


# ============================================================
# QUESTIONS
# ============================================================

QUESTIONS = [

    {
        "question":
            "Who is more likely to fall asleep during a video call?",

        "options": [
            "Me",
            "You",
            "Both of us",
            "Neither. We talk forever."
        ]
    },


    {
        "question":
            "What should our ideal lazy Sunday involve?",

        "options": [
            "Food + movies",
            "Going somewhere",
            "Talking for hours",
            "All of the above"
        ]
    },


    {
        "question":
            "Who is more likely to start an unnecessary argument?",

        "options": [
            "Me",
            "You",
            "Both equally",
            "We would never argue"
        ]
    },


    {
        "question":
            "What is the most important ingredient in a good relationship?",

        "options": [
            "Communication",
            "Humour",
            "Food",
            "Putting up with each other's nonsense"
        ]
    },


    {
        "question":
            "If we had an entire day together, what would probably happen?",

        "options": [
            "We would talk all day",
            "We would eat everything",
            "We would go somewhere random",
            "Somehow all three"
        ]
    },


    {
        "question":
            "Final question. Are we suspiciously compatible?",

        "options": [
            "Obviously ❤️",
            "Unfortunately, yes",
            "The evidence is overwhelming",
            "I need legal representation"
        ]
    }

]


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:

    st.session_state.page = "home"


if "question_index" not in st.session_state:

    st.session_state.question_index = 0


if "answers" not in st.session_state:

    st.session_state.answers = {}


# ============================================================
# BACKGROUND
# ============================================================

def apply_background():

    if background_data:

        background_css = """
        <style>

            .stApp {

                background-image:
                    linear-gradient(
                        rgba(255,255,255,0.35),
                        rgba(255,255,255,0.35)
                    ),
                    url("BACKGROUND_PLACEHOLDER") !important;

                background-size: cover !important;

                background-position: center !important;

                background-repeat: no-repeat !important;

                background-attachment: fixed !important;

            }

        </style>
        """

        background_css = background_css.replace(
            "BACKGROUND_PLACEHOLDER",
            background_data
        )

        st.html(background_css)


# ============================================================
# HOME PAGE
# ============================================================

def home_page():

    apply_background()


    if adi_data:

        home_html = """
        <style>

            .landing-wrapper {

                min-height:
                    calc(100vh - 50px);

                width: 100%;

                display: flex;

                flex-direction: column;

                align-items: center;

                text-align: center;

                padding:
                    45px 20px 30px 20px;

                box-sizing: border-box;

            }


            .landing-title {

                font-family:
                    'DM Sans',
                    sans-serif;

                font-size: 64px;

                font-weight: 800;

                line-height: 1;

                color: #e00020;

                letter-spacing: -2px;

                margin-bottom: 16px;

            }


            .landing-subtitle {

                font-size: 19px;

                font-weight: 600;

                color: #e00020;

                margin-bottom: 8px;

            }


            .landing-hint {

                font-size: 13px;

                color: #e00020;

                opacity: 0.90;

                margin-bottom: 30px;

            }


            .photo-wrapper {

                position: relative;

                width: min(430px, 86vw);

                height: 480px;

                border-radius: 28px;

                overflow: hidden;

                background:
                    rgba(255,255,255,0.65);

                box-shadow:
                    0 15px 45px
                    rgba(60,20,25,0.18);

            }


            .photo-wrapper img {

                width: 100%;

                height: 100%;

                object-fit: cover;

                object-position: center;

                display: block;

                transition:
                    opacity 0.5s ease;

            }


            .photo-message {

                position: absolute;

                inset: 0;

                display: flex;

                align-items: center;

                justify-content: center;

                padding: 45px;

                box-sizing: border-box;

                background:
                    rgba(255,255,255,0.90);

                color: #111;

                font-size: 15px;

                line-height: 1.7;

                text-align: center;

                opacity: 0;

                transition:
                    opacity 0.5s ease;

                pointer-events: none;

            }


            .photo-wrapper:hover img {
                opacity: 0.08;
            }


            .photo-wrapper:hover
            .photo-message {
                opacity: 1;
            }


            @media (max-width: 600px) {

                .landing-wrapper {
                    padding-top: 30px;
                }

                .landing-title {
                    font-size: 48px;
                }

                .landing-subtitle {
                    font-size: 17px;
                }

                .photo-wrapper {
                    width: 88vw;
                    height: 420px;
                }

            }

        </style>


        <div class="landing-wrapper">

            <div class="landing-title">
                Hi Shakhi!
            </div>


            <div class="landing-subtitle">
                Adi wants to ask you something
            </div>


            <div class="landing-hint">
                hover over the picture
            </div>


            <div class="photo-wrapper">

                <img
                    src="ADI_IMAGE_PLACEHOLDER"
                    alt="Adi"
                >


                <div class="photo-message">

                    <div>

                        Okay, technically this is
                        just a picture of me.

                        <br><br>

                        But apparently I have something
                        very important to ask you.

                        <br><br>

                        So please hover over this picture,
                        read the extremely important message,
                        and then continue.

                    </div>

                </div>

            </div>

        </div>
        """

        home_html = home_html.replace(
            "ADI_IMAGE_PLACEHOLDER",
            adi_data
        )

        st.html(home_html)

    else:

        st.html(
            """
            <div style="
                text-align:center;
                padding:100px 20px;
                color:#777;
            ">

                📷

                <br><br>

                Add your photo here:

                <br><br>

                <strong>
                    assets/adi.jpg
                </strong>

            </div>
            """
        )


    left, center, right = st.columns(
        [1, 2, 1]
    )


    with center:

        if st.button(
            "Let's Go →",
            key="lets_go",
            use_container_width=True
        ):

            st.session_state.page = "quiz"

            st.session_state.question_index = 0

            st.session_state.answers = {}

            st.rerun()


# ============================================================
# QUIZ PAGE
# ============================================================

def quiz_page():

    apply_background()


    index = st.session_state.question_index

    total = len(QUESTIONS)

    question = QUESTIONS[index]


    progress = (
        (index + 1)
        / total
        * 100
    )


    quiz_html = """
    <div class="quiz-container">

        <div class="quiz-progress">

            <div
                class="quiz-progress-fill"
                style="width:PROGRESS_PLACEHOLDER%"
            ></div>

        </div>


        <div class="question-card">

            <div class="question-number">

                Question QUESTION_NUMBER_PLACEHOLDER
                of TOTAL_PLACEHOLDER

            </div>


            <div class="question-text">

                QUESTION_PLACEHOLDER

            </div>

        </div>

    </div>
    """


    quiz_html = quiz_html.replace(
        "PROGRESS_PLACEHOLDER",
        str(progress)
    )


    quiz_html = quiz_html.replace(
        "QUESTION_NUMBER_PLACEHOLDER",
        str(index + 1)
    )


    quiz_html = quiz_html.replace(
        "TOTAL_PLACEHOLDER",
        str(total)
    )


    quiz_html = quiz_html.replace(
        "QUESTION_PLACEHOLDER",
        question["question"]
    )


    st.html(quiz_html)


    previous_answer = (
        st.session_state.answers.get(index)
    )


    if previous_answer in question["options"]:

        default_index = (
            question["options"].index(
                previous_answer
            )
        )

    else:

        default_index = None


    answer = st.radio(
        "Answer",
        question["options"],
        index=default_index,
        key=f"question_{index}",
        label_visibility="collapsed"
    )


    st.write("")


    col1, col2 = st.columns(2)


    with col1:

        if index > 0:

            if st.button(
                "← Previous",
                key=f"previous_{index}",
                use_container_width=True
            ):

                st.session_state.answers[index] = answer

                st.session_state.question_index -= 1

                st.rerun()


    with col2:

        if index < total - 1:

            if st.button(
                "Next →",
                key=f"next_{index}",
                use_container_width=True
            ):

                st.session_state.answers[index] = answer

                st.session_state.question_index += 1

                st.rerun()

        else:

            if st.button(
                "Reveal The Results 💗",
                key="reveal_results",
                use_container_width=True
            ):

                st.session_state.answers[index] = answer

                st.session_state.page = "analysis"

                st.rerun()


# ============================================================
# ANALYSIS PAGE
# ============================================================

def analysis_page():

    apply_background()


    st.html(
        """
        <div style="
            text-align:center;
            padding-top:30px;
        ">

            <div class="heart">
                🔬
            </div>

            <div class="main-title">
                Analysing Responses...
            </div>

            <div class="subtitle">

                Please remain calm while our highly
                qualified relationship scientists
                process the data.

            </div>

        </div>
        """
    )


    progress = st.progress(0)


    messages = [

        "Analysing compatibility...",

        "Cross-referencing answers...",

        "Calculating mutual nonsense tolerance...",

        "Evaluating conversation chemistry...",

        "Consulting highly reputable scientists...",

        "Finalising extremely important results..."

    ]


    placeholder = st.empty()


    for i, message in enumerate(messages):

        placeholder.html(
            """
            <div class="analysis-message">
                MESSAGE_PLACEHOLDER
            </div>
            """.replace(
                "MESSAGE_PLACEHOLDER",
                message
            )
        )


        progress.progress(
            int(
                (i + 1)
                / len(messages)
                * 100
            )
        )


        time.sleep(0.4)


    st.session_state.page = "results"


    time.sleep(0.3)


    st.rerun()


# ============================================================
# RESULTS PAGE
# ============================================================

def results_page():

    apply_background()


    st.html(
        """
        <div class="results-wrapper">

            <div class="heart">
                💗
            </div>


            <div class="results-title">

                Compatibility Report

            </div>


            <div class="couple-name">

                Shakhi 🤝 Adi

            </div>


            <div class="result-number">

                100%

            </div>


            <div class="result-label">

                Peak Compatibility

            </div>

        </div>
        """
    )


    if graph_data:

        graph_html = """
        <div class="graph-wrapper">

            <img
                src="GRAPH_IMAGE_PLACEHOLDER"
                alt="Compatibility Graph"
            >

        </div>
        """


        graph_html = graph_html.replace(
            "GRAPH_IMAGE_PLACEHOLDER",
            graph_data
        )


        st.html(graph_html)


    else:

        st.html(
            """
            <div class="graph-wrapper">

                <div class="graph-placeholder">

                    <div class="graph-placeholder-icon">
                        📊
                    </div>

                    <strong>
                        Compatibility Graph
                    </strong>

                    <br><br>

                    Your graph will appear here.

                    <br><br>

                    Add your image as:

                    <br>

                    <strong>
                        assets/graph.jpg
                    </strong>

                </div>

            </div>
            """
        )


    st.html(
        """
        <div class="decision-label">

            Please select your final decision.

        </div>
        """
    )


    # ========================================================
    # REJECT BUTTON
    # ========================================================

    components.html(
        """
        <style>

            * {
                box-sizing: border-box;
            }


            html,
            body {

                margin: 0;

                padding: 0;

                background: transparent;

                overflow: hidden;

            }


            .reject-area {

                position: relative;

                width: 100%;

                height: 260px;

                border-radius: 18px;

            }


            #reject-button {

                position: absolute;

                left: 50%;

                top: 50%;

                transform:
                    translate(-50%, -50%);

                padding:
                    12px 18px;

                border-radius: 14px;

                border:
                    1px solid #ead5d8;

                background: white;

                color: #3b2529;

                font-family:
                    Arial,
                    sans-serif;

                font-size: 14px;

                font-weight: 600;

                cursor: pointer;

                white-space: nowrap;

                box-shadow: none;

                transition:
                    left 0.18s ease,
                    top 0.18s ease;

                z-index: 10;

            }


            #reject-button:hover {

                border-color: #e00020;

                background: #fff1f3;

                color: #c9001d;

            }

        </style>


        <div
            class="reject-area"
            id="reject-area"
        >

            <button
                id="reject-button"
            >

                😭 Reject Boyfriend

            </button>

        </div>


        <script>

            const button =
                document.getElementById(
                    "reject-button"
                );


            const area =
                document.getElementById(
                    "reject-area"
                );


            function moveReject() {

                const areaWidth =
                    area.clientWidth;


                const areaHeight =
                    area.clientHeight;


                const buttonWidth =
                    button.offsetWidth;


                const buttonHeight =
                    button.offsetHeight;


                const padding = 8;


                const maxX =
                    areaWidth
                    - buttonWidth
                    - padding;


                const maxY =
                    areaHeight
                    - buttonHeight
                    - padding;


                if (
                    maxX <= padding ||
                    maxY <= padding
                ) {

                    return;

                }


                const x =
                    padding +
                    Math.random()
                    * (maxX - padding);


                const y =
                    padding +
                    Math.random()
                    * (maxY - padding);


                button.style.left =
                    x + "px";


                button.style.top =
                    y + "px";


                button.style.transform =
                    "none";

            }


            button.addEventListener(
                "mouseenter",
                moveReject
            );


            button.addEventListener(
                "mouseover",
                moveReject
            );


            button.addEventListener(
                "touchstart",
                function(event) {

                    event.preventDefault();

                    moveReject();

                },
                {
                    passive: false
                }
            );


            button.addEventListener(
                "click",
                function(event) {

                    event.preventDefault();

                    moveReject();

                }
            );

        </script>
        """,
        height=270,
        scrolling=False
    )


    # ========================================================
    # ACCEPT BUTTON
    # ========================================================

    st.write("")

    st.write("")

    st.write("")

    if st.button(
        "❤️ Accept Boyfriend",
        key="accept_boyfriend",
        use_container_width=True
    ):

        st.session_state.page = "final"

        st.rerun()


# ============================================================
# FINAL PAGE
# ============================================================

def final_page():

    # --------------------------------------------------------
    # PURE WHITE BACKGROUND
    # --------------------------------------------------------

    st.html(
        """
        <style>

            .stApp {

                background:
                    #ffffff !important;

            }


            .block-container {

                max-width:
                    1000px !important;

                padding-top:
                    0 !important;

                padding-bottom:
                    0 !important;

            }

        </style>
        """
    )


    # --------------------------------------------------------
    # IMAGE EXISTS
    # --------------------------------------------------------

    if congratulations_data:

        final_html = """
        <style>

            .final-page {

                min-height: 100vh;

                width: 100%;

                display: flex;

                flex-direction: column;

                align-items: center;

                text-align: center;

                background: white;

                padding:
                    80px 20px 70px 20px;

                box-sizing: border-box;

            }


            .final-title {

                font-family:
                    'DM Sans',
                    sans-serif;

                font-size: 68px;

                font-weight: 800;

                color: #b51f32;

                letter-spacing: -2px;

                line-height: 1;

                margin-bottom: 18px;

            }


            .final-subtitle {

                font-family:
                    'DM Sans',
                    sans-serif;

                font-size: 18px;

                color: #85686d;

                margin-bottom: 45px;

            }


            .final-image {

                width: min(850px, 92vw);

                min-height: 500px;

                display: flex;

                align-items: center;

                justify-content: center;

                background: white;

                border-radius: 20px;

                overflow: hidden;

            }


            .final-image img {

                width: 100%;

                max-height: 800px;

                object-fit: contain;

                display: block;

            }


            .download-button {

                display: inline-block;

                margin-top: 35px;

                padding:
                    13px 22px;

                border-radius: 14px;

                border:
                    1px solid #ead5d8;

                background: white;

                color: #3b2529;

                font-family:
                    'DM Sans',
                    sans-serif;

                font-size: 14px;

                font-weight: 600;

                text-decoration: none;

                cursor: pointer;

            }


            .download-button:hover {

                background: #fff3f4;

                border-color: #c95d6e;

                color: #a51e31;

            }


            @media (max-width: 600px) {

                .final-page {

                    padding-top: 60px;

                }


                .final-title {

                    font-size: 50px;

                }


                .final-subtitle {

                    font-size: 16px;

                }


                .final-image {

                    min-height: 350px;

                }

            }

        </style>


        <div class="final-page">

            <div class="final-title">

                Congratulations

            </div>


            <div class="final-subtitle">

                The investigation has reached its
                scientifically inevitable conclusion. ❤️

            </div>


            <div class="final-image">

                <img
                    id="congratulations-image"
                    src="CONGRATULATIONS_IMAGE_PLACEHOLDER"
                    alt="Congratulations"
                >

            </div>


            <a
                id="download-link"
                class="download-button"
                href="CONGRATULATIONS_IMAGE_PLACEHOLDER"
                download="congratulations.jpg"
            >

                💾 Save Your Congratulations

            </a>

        </div>


        <script>

            window.addEventListener(
                "load",
                function() {

                    const link =
                        document.getElementById(
                            "download-link"
                        );


                    if (link) {

                        setTimeout(
                            function() {

                                link.click();

                            },
                            300
                        );

                    }

                }
            );

        </script>
        """


        final_html = final_html.replace(
            "CONGRATULATIONS_IMAGE_PLACEHOLDER",
            congratulations_data
        )


        st.html(final_html)


    else:

        st.html(
            """
            <style>

                .final-page {

                    min-height: 100vh;

                    width: 100%;

                    display: flex;

                    flex-direction: column;

                    align-items: center;

                    text-align: center;

                    background: white;

                    padding:
                        80px 20px;

                    box-sizing: border-box;

                }


                .final-title {

                    font-family:
                        'DM Sans',
                        sans-serif;

                    font-size: 68px;

                    font-weight: 800;

                    color: #b51f32;

                    letter-spacing: -2px;

                    line-height: 1;

                    margin-bottom: 45px;

                }


                .final-placeholder {

                    width: min(850px, 92vw);

                    min-height: 500px;

                    border:
                        1px solid #eeeeee;

                    border-radius: 20px;

                    display: flex;

                    align-items: center;

                    justify-content: center;

                    color: #999;

                    text-align: center;

                }

            </style>


            <div class="final-page">

                <div class="final-title">

                    Congratulations

                </div>


                <div class="final-placeholder">

                    <div>

                        📷

                        <br><br>

                        Add your final image here:

                        <br><br>

                        <strong>
                            assets/congratulations.jpg
                        </strong>

                    </div>

                </div>

            </div>
            """
        )


# ============================================================
# PAGE ROUTER
# ============================================================

if st.session_state.page == "home":

    home_page()


elif st.session_state.page == "quiz":

    quiz_page()


elif st.session_state.page == "analysis":

    analysis_page()


elif st.session_state.page == "results":

    results_page()


elif st.session_state.page == "final":

    final_page()