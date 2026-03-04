import requests

turns = [
    {"speaker": "customer", "text": "My inverter battery is not charging."},
    {"speaker": "agent", "text": "Check terminal connections"},
    {"speaker": "agent", "text": "Inspect charging circuit"},
    {"speaker": "customer", "text": "It is working now"}
]

for turn in turns:
    r = requests.post("http://127.0.0.1:8000/live_turn", json=turn)
    print(r.json())

print("\nFinal Report:")
print(requests.get("http://127.0.0.1:8000/final_report").json())
