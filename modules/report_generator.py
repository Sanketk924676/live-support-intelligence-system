def calculate_score(state, sop):
    score = 10

    # Penalty for escalation
    if state.escalated:
        score -= 3

    # Penalty for mistakes
    score -= len(state.agent_mistakes)

    # Efficiency penalty
    if sop:
        total_steps = len(sop["steps"])
        completed = len(state.steps_completed)

        if total_steps > 0:
            efficiency = completed / total_steps
            if efficiency > 0.8:
                score -= 1

    if score < 0:
        score = 0

    return score


def generate_report(state, sop):

    score = calculate_score(state, sop)

    qa_score = 100 - (len(state.agent_mistakes) * 20)
    if qa_score < 0:
        qa_score = 0

    return {
        "Call Summary": {
            "Product": state.product,
            "Issue": state.issue,
            "Category": state.category,
            "Root Cause": state.root_cause,
            "Final State": state.state,
            "Escalated": state.escalated,
            "Resolution Time (seconds)": state.resolution_time(),
            "Steps Completed": len(state.steps_completed),
            "Total Steps": len(sop["steps"]) if sop else 0,
            "Agent Mistakes": state.agent_mistakes,
            "QA Compliance": f"{qa_score}%",
            "Resolved": state.resolved,
            "Performance Score": f"{score}/10"
        }
    }