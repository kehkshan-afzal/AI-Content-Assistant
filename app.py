import os

import streamlit as st
from google import genai
from google.genai import types


MODEL_NAME = "gemini-2.5-flash"

CONTENT_TYPES = [
    "Social media post",
    "Instagram caption",
    "Facebook post",
    "LinkedIn post",
    "X (Twitter) post",
    "Promotional post",
    "Educational post",
    "Product launch post",
]

PLATFORMS = [
    "Instagram",
    "Facebook",
    "LinkedIn",
    "X (Twitter)",
    "TikTok",
    "Pinterest",
    "General",
]

TONES = [
    "Friendly",
    "Professional",
    "Casual",
    "Inspirational",
    "Educational",
    "Persuasive",
    "Fun",
    "Luxury",
]

st.set_page_config(
    page_title="AI Content Assistant",
    page_icon="✍️",
    layout="centered",
)


def get_api_key():
    """Read the Gemini API key from Streamlit secrets or an environment variable."""
    try:
        if "GEMINI_API_KEY" in st.secrets:
            return st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass

    return os.getenv("GEMINI_API_KEY")


def generate_content(content_type, platform, topic, audience, tone):
    """Generate a complete social-media post with caption and hashtags."""
    api_key = get_api_key()

    if not api_key:
        raise ValueError(
            "Gemini API key not found. Add GEMINI_API_KEY to Streamlit Secrets "
            "or set it as an environment variable."
        )

    client = genai.Client(api_key=api_key)

    prompt = f"""
You are an expert social media content writer.

Create ONE complete, ready-to-publish piece of content using these requirements:

Content type: {content_type}
Platform: {platform}
Topic: {topic}
Target audience: {audience}
Tone: {tone}

Return the answer in exactly this structure:

POST:
[The main post copy. Make it engaging, natural, useful, and appropriate for the selected platform.]

CAPTION:
[A polished caption that can be posted with the content. Keep it concise unless the platform normally supports longer captions.]

HASHTAGS:
[8-12 relevant hashtags, each starting with #]

Rules:
- Do not mention that you are an AI.
- Do not use fake statistics, unsupported claims, or invented facts.
- Match the selected tone and audience.
- Avoid unnecessary emojis. Use a few only when they fit the platform and tone.
- Do not add headings other than POST:, CAPTION:, and HASHTAGS:.
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.8,
            max_output_tokens=1000,
        ),
    )

    if not response.text:
        raise ValueError("Gemini returned an empty response.")

    return response.text


st.title("✍️ AI Content Assistant")
st.write("Create ready-to-publish content with Google Gemini.")

st.divider()

content_type = st.selectbox("Content type", CONTENT_TYPES)
platform = st.selectbox("Platform", PLATFORMS)

topic = st.text_input(
    "Topic",
    placeholder="e.g. skincare tips for busy women",
)

audience = st.text_input(
    "Target audience",
    placeholder="e.g. women aged 20-35 interested in skincare",
)

tone = st.selectbox("Tone", TONES)

generate_button = st.button(
    "✨ Generate Content",
    type="primary",
    use_container_width=True,
)

if generate_button:
    if not topic.strip():
        st.warning("Please enter a topic.")
    elif not audience.strip():
        st.warning("Please enter a target audience.")
    else:
        with st.spinner("Generating your content..."):
            try:
                result = generate_content(
                    content_type=content_type,
                    platform=platform,
                    topic=topic.strip(),
                    audience=audience.strip(),
                    tone=tone,
                )

                st.success("Content generated successfully!")
                st.markdown(result)

                st.download_button(
                    label="⬇️ Download Content",
                    data=result,
                    file_name="generated_content.txt",
                    mime="text/plain",
                    use_container_width=True,
                )

            except Exception as error:
                st.error(f"Something went wrong: {error}")

st.divider()
st.caption(f"Powered by Google Gemini ({MODEL_NAME})")
