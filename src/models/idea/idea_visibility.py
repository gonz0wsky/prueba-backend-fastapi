""" Idea visibility """
from enum import Enum

class IdeaVisibility(str, Enum):
    """ Idea visibility """
    PUBLIC = "PUBLIC"
    PROTECTED = "PRIVATE"
    PRIVATE = "PROTECTED"
