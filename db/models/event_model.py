# BaseModel permite validar y documentar la estructura de los datos que se manejan en la API. 
 
from pydantic import BaseModel
from typing import Optional

class Event(BaseModel):
    id: Optional[str] = None 
    category: str
    eventname: str
    note: str