from typing import Any

import numpy as np

from .box import Box

def flatdim(space: Space) -> int: ...
def flatten(space: Space, x: Any) -> np.ndarray: ...
def unflatten(space: Space, x: Any) -> Any: ...
def flatten_space(space: Space) -> Box: ...
