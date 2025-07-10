# ruff: noqa: F401, E402
from __future__ import annotations

import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

logger.addHandler(logging.NullHandler())

from .module1 import (
    # List of functions and classes to be imported when using `import projectname`
    example_function,
)
