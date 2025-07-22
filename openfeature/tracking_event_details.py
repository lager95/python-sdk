from dataclasses import dataclass, field
from typing import Optional, Union

__all__ = [
    "TrackingEventDetails",
]


@dataclass
class TrackingEventDetails:
    value: Optional[float] = None
    _structure: dict[str, Union[bool, str, int, float, dict]] = field(
        default_factory=dict
    )

    def add(
        self, key: str, value: Union[bool, str, int, float, dict]
    ) -> "TrackingEventDetails":
        self._structure[key] = value
        return self

    def get(self, key: str) -> Union[bool, str, int, float, dict]:
        return self._structure[key]
