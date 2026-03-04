def detect_skipped_voltage(state):
    if "Inspect charging circuit" in state.steps_completed \
       and "Measure battery voltage" not in state.steps_completed:
        if "Skipped voltage verification" not in state.agent_mistakes:
            state.agent_mistakes.append(
                "Skipped voltage verification before inspecting circuit."
            )

def detect_no_resolution_confirmation(state):
    if not state.resolved and len(state.steps_completed) > 0:
        if "Resolution not confirmed" not in state.agent_mistakes:
            state.agent_mistakes.append("Resolution not confirmed with customer.")

def detect_resolution(state, text):
    text_lower = text.lower()

    if (
        "working now" in text_lower
        or "now it is working" in text_lower
        or "it is working" in text_lower
        or "issue resolved" in text_lower
        or "problem solved" in text_lower
    ):
        state.resolved = True

def detect_root_cause(state, text):

    text = text.lower()

    if "loose" in text and "connection" in text:
        state.root_cause = "Loose connection"

    elif "power cable" in text and "loose" in text:
        state.root_cause = "Loose power cable"

    elif "battery terminal" in text and "loose" in text:
        state.root_cause = "Loose battery terminal"

    elif "router restart fixed" in text:
        state.root_cause = "Router software glitch"

    elif "adapter was faulty" in text:
        state.root_cause = "Faulty power adapter"
def detect_incorrect_step(state, agent_text, sop):

    if not sop:
        return

    valid_steps = [step.lower() for step in sop["steps"]]

    if agent_text.lower() not in valid_steps:
        state.agent_mistakes.append(
            "Agent suggested step not in troubleshooting SOP."
        )
