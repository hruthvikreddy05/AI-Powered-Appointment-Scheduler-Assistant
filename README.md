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

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/ai-appointment-scheduler-api.git
cd ai-appointment-scheduler-api
