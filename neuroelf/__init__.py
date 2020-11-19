# neuroelf (python) package
"""
neuroelf

Provides a collection of functions translated for python from
https://github.com/neuroelf/neuroelf-matlab

:copyright: (c) 2019, Jochen Weber.
:license: BSD, see LICENSE for details.
"""

from . import io

from . import app

_name_ = 'neuroelf'
__version__ = '0.0.1'

__all__ = [
    '__version__',
    '_name_',
    'app',
    'io',
]
