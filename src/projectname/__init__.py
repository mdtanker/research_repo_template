# ruff: noqa: F401, E402


import logging

logging.basicConfig(level=logging.INFO)
from ._version import version as __version__

__all__ = ["__version__"]


logger = logging.getLogger(__name__)

from .module1 import (
    # List of functions and classes to be imported when using `import projectname`
    example_function,
)
