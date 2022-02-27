import operator as op
from numbers import Number
from typing import List

import numpy as np
import pygame

from config import screen_size


def RectOp(rect, mul, operation=op.mul):
    mul = [*mul, *(([1] if operation in (op.mul, op.truediv) else [0]) * (4 - len(mul)))]
    res = [operation(i, j) for i, j in zip(rect, mul)]
    return pygame.Rect(res)


def clamp(minimum, maximum, val) -> float:
    return max(minimum, min(maximum, val))


def lerp(t, p0: np.ndarray, p1: np.ndarray) -> np.ndarray:
    return (1 - t) * np.asarray(p0) + t * np.asarray(p1)


def rect_clamp(rect: pygame.Rect, minimum, maximum):
    rect.topleft = np.clip(rect.topleft, minimum, maximum)
    rect.bottomright = np.clip(rect.bottomright, minimum, maximum)


def relative_rect(rect: List[List[Number]], abs_size=screen_size) -> pygame.Rect:
    return pygame.Rect([rect[0] * np.asarray(abs_size), rect[1] * np.asarray(abs_size)])
