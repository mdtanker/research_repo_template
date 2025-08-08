import importlib.metadata

import projectname


def test_version():
    assert importlib.metadata.version("projectname") == projectname.__version__
