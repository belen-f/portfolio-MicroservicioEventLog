from fastapi import APIRouter, HTTPException, status
from db.models.event_model import Event
from db.schemas.event_schema import event_schema, events_schema
from db.database import db_events
from bson import ObjectId

router = APIRouter(
    prefix="/event",
    tags=["event"],
    responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

@router.get("/all_events",
         status_code=status.HTTP_200_OK,
         response_model=list[Event],
         summary="Este endpoint trae todos los eventos registrados")
async def get_all_events():
    list_event = events_schema(db_events.events.find())
    if not list_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay eventos en la lista"
        )
    return list_event

# Path
@router.get("/{id}",
            status_code=status.HTTP_200_OK,
            summary="Este endpoint devuelve un evento según su ID (por path)")  
async def event(id: str):

      try:
        result = db_events.events.find_one({"_id": ObjectId(id)}) # En MongoDB, el ID se modela como un "objeto ID". ObjectId es la clase que representa ese objeto (ODM)
      except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El formato del ID no es válido"
        )

      if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Evento no encontrado"
        )
      
      return event_schema(result)

# Query
@router.get("/",
            status_code=status.HTTP_200_OK,
            response_model= Event,
            summary="Este endpoint devuelve un evento según su ID (por query)") 
async def event(id: str):
      try:
        result = db_events.events.find_one({"_id": ObjectId(id)}) # En MongoDB, el ID se modela como un "objeto ID". ObjectId es la clase que representa ese objeto (ODM)
      except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El formato del ID no es válido"
        )

      if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Evento no encontrado"
        )
      
      return event_schema(result)
    
@router.post("/", 
             response_model=Event,
             status_code=status.HTTP_201_CREATED,
             summary="Este endpoint crea un nuevo evento")
async def new_event(event: Event):
    if type(search_event("eventname", event.eventname)) == Event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="El evento ya existe")

    event_dict = dict(event) # inserta un diccionario pero con id null.
    del event_dict["id"] # por eso se elimina el ID del diccionario, para que la DB lo genere automaticamente.

    id = db_events.events.insert_one(event_dict).inserted_id # con insert_one se inserta el evento en la DB y con inserted_id se obtiene el id generado por la DB para ese evento.

    new_event = event_schema(db_events.events.find_one({"_id": id})) # con find_one se busca el evento recién creado por su ID y al resultado event_schema le da formato de diccionario.

    return Event(**new_event) # finalmente, retorna el evento del tipo Event. El ** se utiliza para desempaquetar el diccionario new_event y pasar todos sus elementos como argumentos separados a la clase Event.

@router.put("/", 
            status_code=status.HTTP_200_OK,
            response_model=Event,
            summary="Este endpoint actualiza un evento"
            )
async def event(event: Event):

    event_dict = dict(event)
    del event_dict["id"]

    try:
        db_events.events.find_one_and_replace( 
            filter={"_id": ObjectId(event.id)}, # Busca el evento por id.
            replacement= event_dict, # Lo reemplaza(menos el id)
            upsert= False # si no existe, NO lo crea.
            ) 
    except:
        return {"error": "No se ha actualizado el evento"}

    return search_event("_id", ObjectId(event.id))

@router.delete("/{id}", 
               status_code=status.HTTP_204_NO_CONTENT,
               summary="Este endpoint borra un evento por su ID")
async def event(id: str):
      try:
        obj_id = ObjectId(id)
      except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El formato del ID no es válido"
        )

      result = db_events.events.delete_one({"_id": obj_id})

      if result.deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Evento no encontrado, nada para eliminar"
        )
      
      return

def search_event(field: str, key):

    try:
        event = db_events.events.find_one({field: key})
        return Event(**event_schema(event))
    except:
        return {"error": "No se ha encontrado el evento"}