"""This module provides the RP To-Do model-controller."""
# mrtodo/mrtodo.py

from typing import Any, Dict, NamedTuple


class CurrentTod(NamedTuple):
    todo: Dict[str, Any]
    error: int
