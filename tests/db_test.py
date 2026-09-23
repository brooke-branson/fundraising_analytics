from app.services.fundraiser_services import fundraiser_summary_org
from app.crud.crud import *
from app.db.session import SessionLocal

db = SessionLocal()

fundraiser_summary_org(db ,"MWR")