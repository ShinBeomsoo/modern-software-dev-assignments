from __future__ import annotations

from typing import List

from fastapi import APIRouter, HTTPException

from .. import db, schemas


router = APIRouter(prefix="/notes", tags=["notes"])


@router.post("", response_model=schemas.Note)
def create_note(payload: schemas.NoteCreate) -> schemas.Note:
    content = payload.content.strip()
    if not content:
        raise HTTPException(status_code=400, detail="Content cannot be empty")
    
    note_id = db.insert_note(content)
    note_row = db.get_note(note_id)
    
    if not note_row:
        raise HTTPException(status_code=500, detail="Failed to retrieve created note")
    
    return schemas.Note.model_validate(dict(note_row))


@router.get("", response_model=List[schemas.Note])
def list_notes() -> List[schemas.Note]:
    rows = db.list_notes()
    return [schemas.Note.model_validate(dict(r)) for r in rows]


@router.get("/{note_id}", response_model=schemas.Note)
def get_single_note(note_id: int) -> schemas.Note:
    row = db.get_note(note_id)
    if row is None:
        raise HTTPException(status_code=404, detail="Note not found")
    
    return schemas.Note.model_validate(dict(row))


