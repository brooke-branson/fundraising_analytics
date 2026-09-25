from db.models import Organization
from schemas.organizations import OrganizationResponse

from sqlalchemy import select

def add_org(db, name: str) -> Organization | None:
    existing_org = db.scalar(
        select(Organization).where(Organization.name == name)
    )
    if existing_org:
        return None
    
    org = Organization(name=name)
    try:
        db.add(org)
        db.commit()
        db.refresh(org)
    except:
        db.rollback()
        raise  

    return org

def remove_org(db, id: int) -> OrganizationResponse | None:
    existing_org = db.scalar(
        select(Organization).where(Organization.id == id)
        )
    
    if existing_org:
        deleted_org = OrganizationResponse.model_validate(existing_org)

        db.delete(existing_org)
        db.commit()

        return deleted_org
    
    return None