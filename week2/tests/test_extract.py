import os
import pytest

from unittest.mock import patch, MagicMock
from ..app.services.extract import extract_action_items, extract_action_items_llm


def test_extract_bullets_and_checkboxes():
    text = """
    Notes from meeting:
    - [ ] Set up database
    * implement API extract endpoint
    1. Write tests
    Some narrative sentence.
    """.strip()

    items = extract_action_items(text)
    assert "Set up database" in items
    assert "implement API extract endpoint" in items
    assert "Write tests" in items


@patch("week2.app.services.extract.chat")
def test_extract_action_items_llm_basic(mock_chat):
    # Setup mock response
    mock_response = MagicMock()
    mock_response.message.content = '{"items": ["Task 1", "Task 2"]}'
    mock_chat.return_value = mock_response

    text = "Please do Task 1 and Task 2."
    items = extract_action_items_llm(text)

    assert items == ["Task 1", "Task 2"]
    mock_chat.assert_called_once()


def test_extract_action_items_llm_empty_input():
    # Should handle empty input gracefully without calling LLM
    items = extract_action_items_llm("")
    assert items == []

    items = extract_action_items_llm("   ")
    assert items == []


@patch("week2.app.services.extract.chat")
def test_extract_action_items_llm_no_items_found(mock_chat):
    # Setup mock response for text with no action items
    mock_response = MagicMock()
    mock_response.message.content = '{"items": []}'
    mock_chat.return_value = mock_response

    text = "The weather is nice today."
    items = extract_action_items_llm(text)

    assert items == []


@patch("week2.app.services.extract.chat")
def test_extract_action_items_llm_malformed_json(mock_chat):
    # Setup mock response with bad JSON
    mock_response = MagicMock()
    mock_response.message.content = "Invalid JSON string"
    mock_chat.return_value = mock_response

    text = "Something that causes bad JSON."
    # Should handle parsing error and return empty list (as per implementation)
    items = extract_action_items_llm(text)

    assert items == []


@patch("week2.app.services.extract.chat")
def test_extract_action_items_llm_complex_input(mock_chat):
    # Test with bullet lists and keywords to ensure prompt/model handles them
    mock_response = MagicMock()
    mock_response.message.content = '{"items": ["Update database", "Fix bug", "Meeting at 5"]}'
    mock_chat.return_value = mock_response

    text = """
    - [ ] Update database
    todo: Fix bug
    Next: Meeting at 5
    """
    items = extract_action_items_llm(text)

    assert len(items) == 3
    assert "Update database" in items
    assert "Fix bug" in items
    assert "Meeting at 5" in items
