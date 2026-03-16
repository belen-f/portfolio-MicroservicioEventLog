# toma un objeto y lo devuelve en formato de diccionario  

def event_schema(event) -> dict:
    return {
        "id":str(event["_id"]),
        "category":str(event["category"]),
        "eventname":str(event["eventname"]),
        "note":str(event["note"])
    }
 
def events_schema(events) -> list:
    return[event_schema(event)for event in events]