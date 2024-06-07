from __future__ import annotations

from uuid import UUID

from pydantic import BaseModel


class RunInfo(BaseModel):
    """Class that contains metadata for a single execution of a Chain or model."""

    run_id: UUID
    """A unique identifier for the model or chain run."""
