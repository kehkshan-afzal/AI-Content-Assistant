# ✍️ AI Content Assistant

A simple AI-powered content generation app built with **Python**, **Streamlit**, and the **Google Gemini API**.

The app allows users to select a content type, platform, topic, target audience, and tone. It then generates a complete, ready-to-publish post with a caption and relevant hashtags.

## Features

- Select content type
- Select social media platform
- Enter a topic
- Define the target audience
- Select a writing tone
- Generate a complete social media post
- Generate a caption
- Generate relevant hashtags
- Download generated content as a `.txt` file
- Simple and clean Streamlit interface
- Uses Google's Gemini Interactions API

## Tech Stack

- **Python**
- **Streamlit**
- **Google Gemini API**
- **Google GenAI Python SDK**

## Project Structure

```text
ai-content-assistant/
├── app.py
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.10 or newer
- A Google Gemini API key
- A GitHub account for deployment
- A Streamlit Community Cloud account for deployment

## 1. Get a Gemini API Key

Create a Gemini API key through Google AI Studio.

Keep your API key private.

**Never put your API key directly inside `app.py` or commit it to GitHub.**

## 2. Install the Project Locally

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/ai-content-assistant.git
```

Go into the project directory:

```bash
cd ai-content-assistant
```

Create a virtual environment:

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure the Gemini API Key

The application reads the API key from `GEMINI_API_KEY`.

### Windows Command Prompt

```bash
set GEMINI_API_KEY=YOUR_API_KEY
```

### macOS / Linux

```bash
export GEMINI_API_KEY="YOUR_API_KEY"
```

For Streamlit Community Cloud, use Streamlit Secrets instead of putting the key in your code.

## 5. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 6. Using the App

Choose a **Content Type**, **Platform**, and **Tone**, then enter the **Topic** and **Target Audience**.

Example:

```text
Content Type: Instagram caption
Platform: Instagram
Topic: Skincare tips for busy women
Target Audience: Women aged 20-35 interested in skincare
Tone: Friendly
```

Click **✨ Generate Content**.

The app generates:

```text
POST:
...

CAPTION:
...

HASHTAGS:
#...
#...
```

You can download the generated content as a `.txt` file.

## 7. Deploy on Streamlit Community Cloud

### Step 1: Push the Project to GitHub

Your repository should contain:

```text
app.py
requirements.txt
README.md
```

Commit and push the files to GitHub.

### Step 2: Create a Streamlit App

Open Streamlit Community Cloud and sign in with GitHub.

Create a new app and select:

- Repository: `YOUR-USERNAME/ai-content-assistant`
- Branch: `main`
- Main file: `app.py`

### Step 3: Add the API Key

In the Streamlit deployment settings, open **Secrets** and add:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

Do not add the API key to GitHub.

### Step 4: Deploy

Click **Deploy**.

Streamlit will install the packages listed in `requirements.txt` and launch the application.

## Gemini API

This project uses Google's `google-genai` Python SDK and the Gemini **Interactions API**.

The application sends the user's content requirements to Gemini and receives generated content.

```text
User Input
    ↓
Streamlit UI
    ↓
Prompt
    ↓
Google Gemini
    ↓
Post + Caption + Hashtags
```

## Security

Never commit API keys or other secrets to GitHub.

Use:

- Environment variables for local development
- Streamlit Secrets for Streamlit Community Cloud

If an API key is accidentally exposed, revoke it and create a new one.

## Future Improvements

Possible improvements include:

- Multiple content variations
- Content length selector
- Language selector
- Call-to-action selector
- Brand voice settings
- Emoji control
- Copy-to-clipboard button
- Content history
- Generate multiple posts at once
- Image generation
- PDF/DOCX export
- Custom hashtag count
- Saved brand profiles

## License

This project is provided for educational and personal use. Add an appropriate open-source license if you plan to distribute the project publicly.
