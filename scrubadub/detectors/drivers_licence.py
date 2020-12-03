import re

from .base import RegionLocalisedRegexDetector
from ..filth import DriversLicenceFilth


class DriversLicenceDetector(RegionLocalisedRegexDetector):
    """Use regular expressions to detect UK driving licence numbers,
    Simple pattern matching, no checksum solution.
    """

    name = 'drivers_licence'
    filth_cls = DriversLicenceFilth

    region_regex = {
        # this regex is looking for UK driving licence numbers that follow a pattern, no checksum
        'GB': re.compile(r'''([a-zA-Z9]{5}\s?)((?:\s*\d\s*){6}[a-zA-Z9]{2}\w{3})\s?(\d{2})''', re.IGNORECASE)
    }
