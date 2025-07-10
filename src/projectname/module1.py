from __future__ import annotations

from projectname import logger  # pylint: disable=unused-import

# Any functions or classes defined here which you want to be available when to users
# with `import projectname` should be added to the list in `__init__.py`.


def example_function():
    """An example function that can be imported from the project."""
    logger.info("This is an example function.")
    return "Hello from example_function!"
