from dataclasses import dataclass

@dataclass
class Requirement:
    title: str
    details: str
    sla_ms: int = 2000

def generate_story(req: Requirement) -> dict:
    return {
        "title": req.title,
        "description": [
            "Display last 10 transactions (date, description, amount).",
            "Support credits and debits.",
            f"SLA: {req.sla_ms} ms for p95."
        ],
        "acceptance_criteria": [
            "Exactly 10 items when 10+ exist",
            "Most recent first",
            "Graceful when <10 or 0"
        ],
        "validations": [
            "Order verification",
            "Count verification",
            "Latency budget respected"
        ]
    }
