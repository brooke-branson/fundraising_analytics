from db.models import Organization

from sqlalchemy import select

def add_org(db, name: str) -> bool:
    existing_org = db.scalar(
        select(Organization).where(Organization.name == name)
    )
    if existing_org:
        print("Organizaton already exists!")
        return False
    
    org = Organization(name=name)
    try:
        db.add(org)
        db.commit()
        db.refresh(org)
    except:
        db.rollback()
        raise  

    return org