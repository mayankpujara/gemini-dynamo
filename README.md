# Gemini Dynamo

## Overview
The Gemini Dynamo project combines both frontend and backend technologies to effectively analyze and structure extensive transcripts from YouTube videos, marking a transformative shift in studying methods and improving digital learning experiences.

## Project Scenario
The project addresses the challenging task of analyzing lengthy YouTube transcripts through its Semantic Extraction Algorithm (SEA). Its goal is to simplify the studying process for both students and educators. By quickly pinpointing and categorizing crucial concepts and terms found in university lectures and other lengthy video resources, DynamoCards transforms digital learning, making it easier to develop effective study routines and enhance classroom teaching. It enables users to condense hours of lecture material into concise, easily understandable summaries, representing a significant leap forward in educational technology.

## Features

- **Utilizing Langchain for Script Extraction:** Leveraging Langchain modules, the project excels in extracting scripts from YouTube videos with remarkable precision, ensuring the accurate capture of textual content.
- **Concept Extraction with Generative AI:** Employing cutting-edge technologies like Google Gemini and Vertex AI API, the system meticulously analyzes the text to extract vital concepts crucial for crafting educational flashcards.
- **Secure API Integration with Service Accounts:** Prioritizing data privacy and security, the project establishes secure API connections and processes data through meticulously configured Google service accounts, upholding stringent standards of confidentiality.
- **Interactive Flashcard Generation:** Transforming identified concepts into interactive flashcards enriched with definitions, the system enhances the effectiveness and engagement of studying activities.

## Pre-requisites

- Python 3.8+
- Node.js 14+
- npm or yarn
  
## Project Structure
- Provides a clear overview of the project components
  ```sh
  root/
    │
    ├── backend/                 # Contains the FastAPI application
    │     ├── services/
                ├── main.py              
    │         ├── genai.py             # Core processing scripts for video analysis
    │         └── requirements.txt     # Project Dependencies
    │
    └── frontend/dynamocards               # Houses the React application
              ├── src/                 # Source files for the frontend
              ├── public/              # Public assets and HTML template
              ├── package.json         # NPM dependencies and scripts
              └── README.md            # Frontend documentation


## Setting Up

### Backend

1. Navigate to the backend directory
   ```sh
   cd backend
2. Set up a python virtual environment
   ```sh
   python -m venv env
3. Activate the virtual environemnt
   ```sh
   ./env/Scripts/activate
4. Install the dependencies
   ```sh
   pip install -r requirements.txt
5. Run the FastAPI Server
   ```sh
   uvicorn main:app

### Frontend

1. Navigate to the frontend directory
   ```sh
   cd frontend
   cd dynamocards
2. Install Node Dependencies
   ```sh
   npm install
3. Start the react development environment
   ```sh
   npm run dev

## Workflow

- Backend
  ![Key Concept Refactoring and Output Formatting](https://github.com/mayankpujara/gemini-dynamo/assets/76840933/1351bcbe-9ef3-4606-a54f-9799b854b0e8)

- Frontend
  ![Frontend Integration and Flashcard Handling](https://github.com/mayankpujara/gemini-dynamo/assets/76840933/17a940cc-f624-4b35-9ed4-371a65c74072)
