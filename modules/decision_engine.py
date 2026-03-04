def suggest_next_step(state, sop):
    for step in sop["steps"]:
        if step not in state.steps_completed:
            return step
    return None
