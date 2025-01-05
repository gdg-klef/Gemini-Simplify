

# Gemini Text Simplification Tool 🌟

This project is a web application powered by Streamlit and Google Gemini AI. It provides a tool to simplify complex text descriptions based on user preferences for simplicity levels, examples, and key point focus.

---

## Features

- Summarize complex text into simple language.
- Options for different simplicity levels:
  - **Very Simple**: As if explaining to a child.
  - **Simple**: Clear and easy-to-understand language.
  - **Moderate**: General audience-friendly language.
- Additional options to include examples and focus on key points.
- Interactive UI with modern styling.

---

## Directory Structure

```
gdg-klef-Gemini-Simplify/
├── app.py             # Main application file
└── requirements.txt   # Python dependencies
```

---

## Setup Instructions

### Prerequisites

1. **Python 3.8+** is required.
2. A **Google API Key** for the Generative AI model.

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/gdg-klef-Gemini-Simplify.git
   cd gdg-klef-Gemini-Simplify
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Create a `.env` file in the root directory:
     ```
     GOOGLE_API_KEY=your_google_api_key
     ```
   - Replace `your_google_api_key` with your actual API key.

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Access the app**
   - Open the URL shown in the terminal (default: http://localhost:8501).

---

## Usage

1. **Enter a description** in the provided text area.
2. **Select a simplicity level**:
   - Very Simple
   - Simple
   - Moderate
3. **Optional settings**:
   - Check "Include examples" to add clarifying examples.
   - Check "Focus strictly on key points" to avoid unnecessary details.
4. Click **"✨ Summarize ✨"** to generate the summary.
5. View the summary in the output section.

---

## Dependencies

- **Streamlit**: For building the web app.
- **google-generativeai**: To interact with the Google Gemini AI model.
- **python-dotenv**: For managing environment variables.

---

## Troubleshooting

- If the app fails to load:
  - Ensure your Google API key is valid and has access to the required Generative AI services.
  - Double-check your `.env` file for correct formatting.
- If dependencies are missing, re-run:
  ```bash
  pip install -r requirements.txt
  ```

---

## Future Enhancements

- Add support for multiple languages.
- Enhance UI/UX for better interactivity.
- Provide downloadable summaries as a file.

---

## License

This project is licensed under the MIT License.

---

## Contributing

Feel free to fork this repository, create a branch, and submit a pull request for any features or improvements!

---

## Acknowledgments

- [Streamlit](https://streamlit.io)
- [Google Generative AI](https://aistudio.google.com/)
```
