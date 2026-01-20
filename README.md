# AI-Powered-Appointment-Scheduler-Assistant
This project builds an AI-powered backend service that converts unstructured appointment requests from text or scanned images into structured scheduling data. It uses OCR for text extraction, NLP for entity detection, and timezone-aware normalization to produce accurate appointment details
# AI Appointment Scheduler API

## Overview
This project is a backend service that parses unstructured appointment requests
(text or OCR-ready input) and converts them into structured scheduling data.
It performs entity extraction, date/time normalization, and includes guardrails
to handle ambiguous inputs.

## Architecture

Input (Text / OCR)
        ↓
Entity Extraction (Date, Time, Department)
        ↓
Normalization (ISO Date, Time, Asia/Kolkata)
        ↓
Guardrails (Ambiguity Handling)
        ↓
Final Appointment JSON Response

## Tech Stack
- Python
- FastAPI
- Rule-based NLP (Regex)
- Timezone-aware normalization (Asia/Kolkata)

## Setup Instructions
 1. Clone the repository
```bash
git clone https://github.com/<hruthvikreddy05>/ai-appointment-scheduler-api.git
cd ai-appointment-scheduler-api

2. Install dependencies
pip install -r requirements.txt

3. Run the server
uvicorn main:app --reload

4. Open Swagger UI
http://127.0.0.1:8000/docs

API Usage
Endpoint
POST /parse-appointment

Request Body
{
  "text": "Book dentist next Friday at 3pm"
}

Successful Response
{
  "appointment": {
    "department": "Dentistry",
    "date": "2025-09-26",
    "time": "15:00",
    "tz": "Asia/Kolkata"
  },
  "status": "ok"
}

Ambiguous Input Response
{
  "status": "needs_clarification",
  "message": "Ambiguous date/time or department"
}

Sample curl Requests
Valid Request
curl -X POST http://127.0.0.1:8000/parse-appointment \
-H "Content-Type: application/json" \
-d '{"text":"Book dentist next Friday at 3pm"}'

Ambiguous Request
curl -X POST http://127.0.0.1:8000/parse-appointment \
-H "Content-Type: application/json" \
-d '{"text":"Book dentist next week"}'

POSTMAN 

Method: POST

URL: http://127.0.0.1:8000/parse-appointment

Body → raw → JSON

{
  "text": "Book dentist next Friday at 3pm"
}
