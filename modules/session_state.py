import time

class SessionState:
    def __init__(self):
        self.product = None
        self.issue = None
        self.category = None
        self.symptoms = []
        self.steps_completed = []
        self.agent_mistakes = []
        self.resolved = False
        self.escalated = False
        self.root_cause = None
        self.state = "INIT"  # INIT → DIAGNOSING → TESTING → RESOLVED → ESCALATED
        self.start_time = time.time()
        self.turns = 0

    def increment_turn(self):
        self.turns += 1

    def resolution_time(self):
        return round(time.time() - self.start_time, 2)