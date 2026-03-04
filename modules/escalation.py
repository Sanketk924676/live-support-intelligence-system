def check_escalation(state, sop):

    if not sop:
        return

    total_steps = len(sop["steps"])
    completed = len(state.steps_completed)

    # escalate if all troubleshooting failed
    if completed >= total_steps and not state.resolved:
        state.escalated = True