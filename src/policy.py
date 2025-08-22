import re
from typing import Final, Iterable

# Verejná, deterministická politika pre unit testy.
BIRTHPLACE_POLICY_REPLY: Final[str] = "I don't have access to that information."

_BIRTHPLACE_PATTERNS: Final[Iterable[str]] = (
    r"\bwhere\s+was\s+i\s+born\b",
    r"\bwhere\s+am\s+i\s+from\b",
    r"\bwhat\s+is\s+my\s+birth(place)?\b",
    r"\bbirth\s*place\b",
    r"\bcity\s+of\s+birth\b",
)

def policy_reply_for_birthplace(user_text: str) -> str:
    """
    Deterministic: ak text implikuje otázku na miesto narodenia, vráť neutrálnu odpoveď,
    ktorá NEVYZÝVA užívateľa dopĺňať mesto. Inak vráť prázdny reťazec.
    """
    if not isinstance(user_text, str):
        return BIRTHPLACE_POLICY_REPLY
    text = user_text.strip().lower()
    for pat in _BIRTHPLACE_PATTERNS:
        if re.search(pat, text):
            return BIRTHPLACE_POLICY_REPLY
    return ""  # znamená: politika sa neuplatnila