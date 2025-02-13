from .comments import draft_comment
from .models import ChangeSummary
from .risk import risk_score


def run() -> str:
    sample = ChangeSummary(files_changed=6, lines_added=220, lines_deleted=90)
    return draft_comment(risk_score(sample))
