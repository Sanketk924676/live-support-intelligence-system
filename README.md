# Live Technical Support Intelligence System

An AI-powered system that analyzes live conversations between customers and support agents to assist troubleshooting, detect mistakes, track resolution progress, and generate post-call analysis reports.

This system processes conversation transcripts in real-time and provides intelligent recommendations to improve technical support efficiency.

---

# Project Overview

The Live Technical Support Intelligence System processes real-time support conversations and provides intelligent assistance to support agents.

The system performs the following tasks:

- Accepts live conversation transcripts
- Understands the conversation context
- Identifies the product and issue
- Retrieves troubleshooting steps from technical documentation
- Suggests next troubleshooting steps
- Detects mistakes made by the support agent
- Tracks issue resolution progress
- Generates a structured post-call report

---

# Key Features

• Real-time conversation analysis  
• Product and issue identification  
• Technical documentation retrieval  
• Troubleshooting step recommendation  
• Agent mistake detection  
• Resolution tracking  
• Escalation detection  
• Post-call performance analysis  
• Multi-session support  

---

# System Architecture

Customer Conversation  
↓  
Conversation Understanding (LLM)  
↓  
Issue Identification  
↓  
Technical Documentation Retrieval  
↓  
Decision Engine  
↓  
Agent Assist (Next Step Suggestion)  
↓  
Mistake Detection  
↓  
Resolution Tracking  
↓  
Post Call Report Generation  

---

# Tech Stack

Programming Language  
Python

Framework  
FastAPI

LLM Provider  
Groq API

LLM Model  
LLaMA 3 (llama3-8b-8192)

Data Storage  
JSON based technical documentation

Environment Management  
Python Virtual Environment

---

# Project Structure

live_support_intelligence_agent

agent/  
 support_agent.py  

modules/  
 understanding.py  
 retrieval.py  
 decision_engine.py  
 mistake_detection.py  
 escalation.py  
 resolution_tracker.py  
 report_generator.py  
 session_state.py  

data/  
 technical_docs.json  

simulation/  
 simulate_call.py  

app.py  
config.py  
requirements.txt  
README.md  

---

# Setup Instructions

## 1 Clone Repository

git clone https://github.com/Sanketk924676/live-support-intelligence-system.git  
cd live-support-intelligence-system  

---

## 2 Create Virtual Environment

python -m venv venv

Activate environment

Windows

venv\Scripts\activate

Linux / Mac

source venv/bin/activate

---

## 3 Install Dependencies

pip install -r requirements.txt

---

## 4 Add Groq API Key

Create a `.env` file in the root directory

GROQ_API_KEY=your_api_key_here

---

## 5 Run the Application

uvicorn app:app --reload

Server will start at

http://127.0.0.1:8000

---

## 6 Open API Interface

http://127.0.0.1:8000/docs

Swagger UI allows testing the API endpoints.

---

# API Usage

## Live Conversation Processing

Endpoint

POST /live_turn

Example Request

{
  "session_id": "call_001",
  "speaker": "customer",
  "text": "My system speaker is not working."
}

Example Response

{
  "State": "DIAGNOSING",
  "Identified Product": "system speaker",
  "Identified Issue": "not working",
  "Suggested Next Step": "Check power connection",
  "Progress": "0/5",
  "Escalated": false,
  "Mistakes": []
}

---

# Example Conversation Simulation

Step 1

{
  "session_id": "call_001",
  "speaker": "customer",
  "text": "My system speaker is not working."
}

Step 2

{
  "session_id": "call_001",
  "speaker": "agent",
  "text": "Check power connection"
}

Step 3

{
  "session_id": "call_001",
  "speaker": "customer",
  "text": "The power cable was loose but now it is working."
}

---

# Final Report Generation

Endpoint

GET /final_report/{session_id}

Example

GET /final_report/call_001

Example Output

{
  "Call Summary": {
    "Product": "system speaker",
    "Issue": "not working",
    "Category": "Audio System",
    "Root Cause": "Loose power cable",
    "Final State": "RESOLVED",
    "Escalated": false,
    "Resolution Time (seconds)": 120,
    "Steps Completed": 1,
    "Total Steps": 5,
    "Agent Mistakes": [],
    "QA Compliance": "100%",
    "Resolved": true,
    "Performance Score": "10/10"
  }
}

---

# Functional Capabilities

Conversation Understanding

• Speaker role tracking  
• Intent classification  
• Issue extraction  
• Symptom mapping  

Troubleshooting Logic

• Match symptoms with SOP  
• Track completed troubleshooting steps  
• Suggest next troubleshooting action  

Mistake Detection

• Detect skipped troubleshooting steps  
• Detect incorrect agent advice  
• Detect missing resolution confirmation  

Resolution Tracking

• Detect issue resolution  
• Measure resolution time  
• Count troubleshooting steps attempted  
• Escalation detection  

---

# Non Functional Requirements

• Each conversation turn processed in under 5 seconds  
• Maintain session context across turns  
• Modular architecture  
• Reduced hallucination by rule-based decision layer  

---

# Future Improvements

• Vector database for technical document retrieval  
• Speech-to-text integration for live call audio  
• Web dashboard for monitoring support agents  
• Integration with CRM systems  
• Machine learning based intent detection  

---

# Author

Sanket Kerannavar

---

# License

This project is intended for educational and demonstration purposes.

