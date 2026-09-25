from ast import Or
from fastapi import Depends, FastAPI, HTTPException

from schemas.organizations import *

from db.session import Session, get_db
from db.models import *

from services.fundraiser_services import *

from crud.organizations import *

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

@app.delete(
    "/organizations/{id}",
    response_model=OrganizationResponse
)
def delete_organzation(
    id: int,
    db: Session = Depends(get_db)
    ):
    deleted_org = remove_org(db, id)

    if deleted_org is None:
        raise HTTPException(
            status_code=404,
            detail="Organization not found"
        )

    return deleted_org

@app.get(
    "/summary/{name}",
)
def fundraiser_summary(
    name: str,
    db: Session = Depends(get_db)
):
    summary = fundraiser_summary_org(db, name)

    return summary