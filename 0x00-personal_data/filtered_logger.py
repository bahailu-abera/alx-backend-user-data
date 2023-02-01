#!/usr/bin/env python3
"""
Module returns log message
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    returns the log message obfuscated
    """
    for field in fields:
        pattern = r"(?<={}=)[\w*\d*\/.@-]+(?={})".format(field, separator)
        message = re.sub(pattern, redaction, message)
    return message
