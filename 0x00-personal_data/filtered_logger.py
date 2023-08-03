#!/usr/bin/env python3
""" a function that returns the log message obfuscated """
from typing import List
import logging
import re
import os


patterns = {
        'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
        'replace': lambda x: r'\g<field>={}'.format(x),
}

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str,
        ) -> str:
    """Filters a log line."""
    extract, replace = (patterns['extract'], patterns['replace'])
    return re.sub(extract(fields, separator), replace(redaction), message)
