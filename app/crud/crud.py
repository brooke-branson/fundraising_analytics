from sqlalchemy.engine.reflection import ObjectScope
from app.db.models import *
from app.db.session import SessionLocal
from decimal import Decimal
from datetime import date

from sqlalchemy import select

db = SessionLocal()

def add_item(db, model) -> bool:
    try:
        db.add(model)
        db.commit()
        db.refresh(model)
    except:
        db.rollback()
        raise  
    return True

def remove_item(db, model) -> bool:
    return False

def edit_item(db, model) -> bool:
    return False

new_product = Product(
    organization_id = 1,
    name = "Polish Sausage",
    category = "Food Item"
)
new_fund_product = FundraiserProduct(
    fundraiser_id = 8,
    product_id = 2,
    sale_price = Decimal(4.55),
    starting_quantity = 56,
    ending_quantity = 4
)

new_expense = Expenses(
    fundraiser_id = 8,
    description = "Costco Polish Sausages",
    amount = Decimal(70.82),
    category = "Food"
)
add_item(db, new_expense)