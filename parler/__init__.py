# following PEP 440
__version__ = '1.1.0.dev0'

__all__ = (
    'is_multilingual_project',
)

from .utils.i18n import is_multilingual_project
