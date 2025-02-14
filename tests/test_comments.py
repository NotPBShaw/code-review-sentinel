from review_bot.comments import draft_comment


def test_comment_for_high_risk() -> None:
    assert "High-risk" in draft_comment(20)
