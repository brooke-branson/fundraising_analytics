from ast import Or
from fastapi import Depends, FastAPI

from schemas.organizations import *

from db.session import Session, get_db
from db.models import *

from crud.organizations import add_org

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Fundraiser Application"}

@app.get("/healthz")
def healthz():
    return {"status": "healthy"} 
       
@app.post(
    "/organizations/add",
    response_model=OrganizationResponse
)
def add_organzation(
    org_data: OrganizationCreate,
    db: Session = Depends(get_db)
    ):

     return add_org(db, org_data.name)