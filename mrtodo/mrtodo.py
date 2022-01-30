"""This module provides the mrtodo model-controller."""
# mrtodo/mrtodo.py

from typing import Any, Dict, NamedTuple


class CurrentTod(NamedTuple):
    todo: Dict[str, Any]
    error: int
