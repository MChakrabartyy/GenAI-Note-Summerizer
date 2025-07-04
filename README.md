﻿![Made with LangChain](https://img.shields.io/badge/Built%20with-LangChain-blueviolet)


# GenAI Note Summarizer 

An AI-powered academic tool that transforms dense PDF notes into clear, structured summaries using OpenAI's GPT-4 via LangChain. Built with Streamlit for a seamless and interactive user experience, this project helps students and researchers revise smarter and faster.

##  Features
- Upload academic PDFs (lecture notes, textbooks, research papers)
- Chunk + summarize content using LangChain and GPT-4
- Context-aware summarization powered by LLMs
- Real-time output in a clean Streamlit UI
- (Upcoming) Export summaries as editable text

## Tech Stack
- **Python**
- **LangChain**
- **OpenAI API**
- **Streamlit**
- **pdfplumber**

##  Project Structure
- `app/` — Core logic for parsing and summarization
- `streamlit_app.py` — Frontend logic (UI)
- `requirements.txt` — Dependencies
- `screenshots/` — Demo visuals (coming soon)

##  Sample Workflow
1. Upload a lecture PDF
2. Text is chunked and cleaned
3. GPT-4 generates key summaries
4. Output shown instantly in browser

---

> Built as part of a self-directed GenAI research project focused on academic productivity.

##  Notes

> This project includes a `simulate=True` flag for offline testing without an OpenAI API key. Great for debugging or showcasing the pipeline flow without using tokens.


