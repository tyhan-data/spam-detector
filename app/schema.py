from pydantic import BaseModel, Field
from typing import Annotated
from enum import Enum

class TargetInfo(str, Enum):
    spam = 'spam'
    ham = 'ham'
    

# Input data
class SpamDetectorInput(BaseModel):
    Text: Annotated[
        str,
        Field(..., min_length=5, title='Text', description='Enter a Description at least 5 character')
    ]
    
    
# Output data
class SpamDetectorOutput(BaseModel):
    Target : TargetInfo
    Probability : float