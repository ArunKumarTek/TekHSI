"""Tektronix High Speed Interface.

Provides access to commonly imported items from the `TekHSI` package.
"""

from importlib.metadata import version

from tekhsi.helpers import PACKAGE_NAME
from tekhsi.tek_hsi_connect import TekHSIConnect
from tekhsi.tek_hsi_connect import AcqWaitOn
from tekhsi._tek_highspeed_server_pb2 import WaveformHeader  # pylint: disable= no-name-in-module

# Read version from installed package.
__version__ = version(PACKAGE_NAME)

__all__ = [
    "TekHSIConnect",
    "AcqWaitOn",
    "WaveformHeader",
]