# This empty file marks api as a Python package
from .config import MODE

if MODE == "mock":
    from . import robinhood_mock as robinhood
else:
    from . import robinhood