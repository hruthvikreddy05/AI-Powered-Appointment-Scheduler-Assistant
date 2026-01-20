from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pytz
import re

app = FastAPI(title="AI Appointment Scheduler API")

TIMEZONE = pytz.timezone("Asia/Kolkata")

DEPARTMENT_MAP = {
    "dentist": "Dentistry",
    "doctor": "General Medicine",
    "cardiology": "Cardiology"
}

class AppointmentRequest(BaseModel):
    text: str

def extract_entities(text: str):
    text = text.lower()
    date_match = re.search(r'next\s+\w+', text)
    time_match = re.search(r'\d+\s*(am|pm)', text)

    department = None
    for key in DEPARTMENT_MAP:
        if key in text:
            department = key

    if not date_match or not time_match or not department:
        return None

    return {
        "date_phrase": date_match.group(),
        "time_phrase": time_match.group(),
        "department": department
    }

def normalize(date_phrase, time_phrase):
    now = datetime(2025, 9, 20, tzinfo=TIMEZONE)

    if "next friday" in date_phrase:
        date = now + relativedelta(weekday=4)
    else:
        return None

    hour = int(re.search(r'\d+', time_phrase).group())
    if "pm" in time_phrase and hour != 12:
        hour += 12

    return {
        "date": date.strftime("%Y-%m-%d"),
        "time": f"{hour:02d}:00",
        "tz": "Asia/Kolkata"
    }

@app.post("/parse-appointment")
def parse_appointment(request: AppointmentRequest):

    raw_text = request.text.strip()
    entities = extract_entities(raw_text)

    if not entities:
        return {
            "status": "needs_clarification",
            "message": "Ambiguous date/time or department"
        }

    normalized = normalize(
        entities["date_phrase"],
        entities["time_phrase"]
    )

    if not normalized:
        return {
            "status": "needs_clarification",
            "message": "Unable to normalize date/time"
        }

    return {
        "appointment": {
            "department": DEPARTMENT_MAP[entities["department"]],
            "date": normalized["date"],
            "time": normalized["time"],
            "tz": normalized["tz"]
        },
        "status": "ok"
    }

