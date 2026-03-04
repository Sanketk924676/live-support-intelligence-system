from modules.session_state import SessionState
from modules.understanding import extract_issue
from modules.retrieval import retrieve_sop
from modules.decision_engine import suggest_next_step
from modules.mistake_detection import (
    detect_skipped_voltage,
    detect_resolution,
    detect_no_resolution_confirmation,
    detect_root_cause,
    detect_incorrect_step
)
from modules.resolution_tracker import get_progress
from modules.report_generator import generate_report
from modules.escalation import check_escalation


class SupportAgent:
    def __init__(self):
        self.state = SessionState()

    def process_turn(self, speaker, text):

        self.state.increment_turn()

        # -------------------------
        # CUSTOMER TURN PROCESSING
        # -------------------------
        if speaker == "customer":

            extracted = extract_issue(text)

            if extracted.get("product"):
                self.state.product = extracted.get("product")
                self.state.state = "DIAGNOSING"

            if extracted.get("issue") and not self.state.issue:
                self.state.issue = extracted.get("issue")

            # Detect root cause clues
            detect_root_cause(self.state, text)

            # Detect resolution phrases
            detect_resolution(self.state, text)

        # -------------------------
        # AGENT TURN PROCESSING
        # -------------------------
        if speaker == "agent":

            if text not in self.state.steps_completed:
                self.state.steps_completed.append(text)
                self.state.state = "TESTING"

        # -------------------------
        # RETRIEVE SOP
        # -------------------------
        sop = retrieve_sop(self.state.product, self.state.issue)

        next_step = None

        if sop:
            self.state.category = sop["category"]

            # Detect incorrect troubleshooting step (ONLY for agent)
            if speaker == "agent":
                detect_incorrect_step(self.state, text, sop)

            # Suggest next step only if issue not resolved
            if not self.state.resolved:
                next_step = suggest_next_step(self.state, sop)
                detect_skipped_voltage(self.state)
                check_escalation(self.state, sop)

        # -------------------------
        # FINAL STATE TRANSITION
        # -------------------------
        if self.state.resolved:
            self.state.state = "RESOLVED"

        if self.state.escalated:
            self.state.state = "ESCALATED"

        # -------------------------
        # RESPONSE
        # -------------------------
        return {
            "State": self.state.state,
            "Identified Product": self.state.product,
            "Identified Issue": self.state.issue,
            "Suggested Next Step": next_step,
            "Progress": get_progress(self.state, sop) if sop else None,
            "Escalated": self.state.escalated,
            "Mistakes": self.state.agent_mistakes
        }

    # -------------------------
    # FINAL REPORT GENERATION
    # -------------------------
    def final_report(self):

        sop = retrieve_sop(self.state.product, self.state.issue)

        # Check if agent forgot to confirm resolution
        detect_no_resolution_confirmation(self.state)

        return generate_report(self.state, sop)