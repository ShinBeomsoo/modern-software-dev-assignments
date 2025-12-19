from __future__ import annotations

from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime


class NoteBase(BaseModel):
    content: str


class NoteCreate(NoteBase):
    pass


class Note(NoteBase):
    id: int
    created_at: str

    class Config:
        from_attributes = True


class ActionItemBase(BaseModel):
    text: str
    done: bool = False


class ActionItemCreate(ActionItemBase):
    note_id: Optional[int] = None


class ActionItem(ActionItemBase):
    id: int
    note_id: Optional[int] = None
    created_at: str

    class Config:
        from_attributes = True


class ExtractRequest(BaseModel):
    text: str
    save_note: bool = False


class ExtractResponse(BaseModel):
    note_id: Optional[int]
    items: List[ActionItemSummary]


class ActionItemSummary(BaseModel):
    id: int
    text: str


class MarkDoneRequest(BaseModel):
    done: bool = True


class MarkDoneResponse(BaseModel):
    id: int
    done: bool
