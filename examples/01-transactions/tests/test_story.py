from app.generator import Requirement, generate_story

def test_story_shape():
    story = generate_story(Requirement(
        title="Customer views recent transactions",
        details="..."
    ))
    assert "acceptance_criteria" in story
    assert any("Exactly 10" in s for s in story["acceptance_criteria"])
