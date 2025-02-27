# coding: utf-8
"""
.. module:: boardgamegeek
   :platform: Unix, Windows
   :synopsis: interface to boardgamegeek.com

.. moduleauthor:: Cosmin Luță <q4break@gmail.com>
"""

from .api import BGGClient, BGGChoose, BGGRestrictDomainTo, BGGRestrictPlaysTo, BGGRestrictSearchResultsTo
from .api import BGGRestrictCollectionTo
from .legacy_api import BGGClientLegacy
from .exceptions import BGGError, BGGApiRetryError, BGGApiError, BGGApiTimeoutError, BGGValueError, BGGItemNotFoundError
from .cache import CacheBackendNone, CacheBackendMemory, CacheBackendSqlite
from .version import __version__

__all__ = ["BGGClient", "BGGChoose", "BGGRestrictSearchResultsTo", "BGGRestrictPlaysTo", "BGGRestrictDomainTo",
           "BGGRestrictCollectionTo", "BGGError", "BGGValueError", "BGGApiRetryError", "BGGApiError",
           "BGGApiTimeoutError", "BGGItemNotFoundError", "CacheBackendNone", "CacheBackendSqlite", "CacheBackendMemory"]
__all__.extend(["BGGClientLegacy"])

__import__('pkg_resources').declare_namespace(__name__)


