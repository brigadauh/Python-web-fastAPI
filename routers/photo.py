from typing import Optional
from fastapi import APIRouter, Request, Path, Query
import photo_controller as controller
from pydantic import BaseModel

root = '/api/photo'
photo = APIRouter()

class PhotoRequest(BaseModel):
    token: str = None
    body: str = None
    
@photo.post(root)
def photo_folder_scan(photoRequest: PhotoRequest):
    # json_obj = request.get_json()
    # token = json_obj.get('token','')
    # resp=photo.folder_scan(json_obj.get('body',''),token)
    # return resp
    print ('photorequest',photoRequest)
    return controller.folder_scan(photoRequest)

@photo.get(root)
def photo_get_file(
    path: Optional[str] = Query(None, alias="p"),
    token: Optional[str] = Query(None, alias="t")
    ):  
    #path = path.replace('../','')
    print ('photoGetrequest',path, token)
    return controller.get_file(path, token)