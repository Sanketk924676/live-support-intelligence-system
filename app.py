from fastapi import FastAPI
from pydantic import BaseModel
from agent.support_agent import SupportAgent

app = FastAPI()

# Multiple sessions stored here
SESSIONS = {}

class Turn(BaseModel):
    session_id: str
    speaker: str
    text: str

@app.post("/live_turn")
def live_turn(turn: Turn):

    if turn.session_id not in SESSIONS:
        SESSIONS[turn.session_id] = SupportAgent()

    agent = SESSIONS[turn.session_id]

    return agent.process_turn(turn.speaker, turn.text)


@app.get("/final_report/{session_id}")
def final_report(session_id: str):

    if session_id not in SESSIONS:
        return {"error": "Session not found"}

    return SESSIONS[session_id].final_report()