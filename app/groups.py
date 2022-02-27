from fastapi import APIRouter, HTTPException
from db import db_collection


routers = APIRouter(
    prefix='/api/v1',
    responses={404: {"description": "Not found"}},)


def schema_helper(data) -> dict:
    
    return {
        "group": {
            "id": str(data["_id"]),
            "name": data["name"],
            "vendor_des": data["vendor_des"],
            "target_sector": data["target_sector"],
            "target_locale": data["target_locale"],
            "attrib_country": data["attrib_country"],
            "first_seen": data["first_seen"],
            "malware": data["malware"],

            }
        }


@routers.get('/status')
async def get_status():
    return {'status': 'running'}


@routers.get('/all')
async def all_groups():
    grp_info = [] 
    if grp_info.extend(
        schema_helper(group)
        for group in db_collection.find()
    ) is None:
    #for groups in db_collection.find() :
        #grp_info.extend(schema_helper(groups))
        return grp_info
    
    raise HTTPException(status_code=404, detail='Error in lookup')
    
  

@routers.get('/group/{groupname}')
async def specific_groups(groupname: str):
    
    groups = []
    
    groups.extend(
        schema_helper(group)
        for group in db_collection.find({"$text": {"$search": groupname}}))

    return groups
