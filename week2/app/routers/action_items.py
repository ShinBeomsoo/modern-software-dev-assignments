from __future__ import annotations

from typing import List, Optional

from fastapi import APIRouter, HTTPException

from .. import db, schemas
from ..services.extract import extract_action_items, extract_action_items_llm


router = APIRouter(prefix="/action-items", tags=["action-items"])


@router.post("/extract", response_model=schemas.ExtractResponse)
def extract(payload: schemas.ExtractRequest) -> schemas.ExtractResponse:
    text = payload.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Text is required for extraction")

    note_id: Optional[int] = None
    if payload.save_note:
        note_id = db.insert_note(text)

    # Use LLM extractor if available or fallback to classic one
    # Note: For now keeping it simple, but this is where strategy could go
    items = extract_action_items_llm(text)
    if not items: # Fallback if LLM fails or returns nothing
        items = extract_action_items(text)
        
    ids = db.insert_action_items(items, note_id=note_id)
    
    summaries = [
        schemas.ActionItemSummary(id=i, text=t) 
        for i, t in zip(ids, items)
    ]
    
    return schemas.ExtractResponse(note_id=note_id, items=summaries)


@router.get("", response_model=List[schemas.ActionItem])
def list_all(note_id: Optional[int] = None) -> List[schemas.ActionItem]:
    rows = db.list_action_items(note_id=note_id)
    return [schemas.ActionItem.model_validate(dict(r)) for r in rows]


@router.post("/{action_item_id}/done", response_model=schemas.MarkDoneResponse)
def mark_done(action_item_id: int, payload: schemas.MarkDoneRequest) -> schemas.MarkDoneResponse:
    success = db.mark_action_item_done(action_item_id, payload.done)
    if not success:
        # Note: In a real app, you might want to check if it exists first
        # but for simplicity we'll just return what was requested
        pass
    return schemas.MarkDoneResponse(id=action_item_id, done=payload.done)


