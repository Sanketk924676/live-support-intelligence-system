def get_progress(state, sop):
    return f"{len(state.steps_completed)}/{len(sop['steps'])}"
