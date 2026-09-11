from app.db.session import SessionLocal
from app.db.models import *
from datetime import date

from sqlalchemy import select

db = SessionLocal()

def fundraiser_summary_org(org_name: str) -> dict:

    res = {}

    org = db.scalar(
        select(Organization).where(Organization.name == org_name)
    )

    fundraisers = db.scalars(
        select(Fundraiser).join(
            Organization,
            Fundraiser.organization_id == Organization.id
        ).where(Organization.id == org.id)
    ).all()

    if org:
        res["organization"] = org.name
        res["fundraisers"] = []

    for x in fundraisers:
        total_sold = 0
        revenue = 0
        total_expenses = 0
        expenses = db.scalars(
            select(Expenses).where(
                Expenses.fundraiser_id == x.id
            )
        )
        products = db.execute(
            select(FundraiserProduct, Product).join(
                Product,
                FundraiserProduct.product_id == Product.id
            ).where(
                FundraiserProduct.fundraiser_id == x.id
            )
        ).all()

        fundraiser = {
            "name": x.name,
            "id": x.id,
            "type": x.event_type,
            "event_date": x.event_date,
            "expected_attend": x.expected_attendance,
            "products": [],
            "expenses": [],
            "profits": 0.00
        }

        for f_prod, prod in products:
            product = {
                "name": prod.name,
                "id": prod.id,
                "sale_price": f_prod.sale_price,
                "starting_quantity": f_prod.starting_quantity,
                "sold": None,
                "revenue": None
            }
    
            if x.status == "completed":
                sold = f_prod.starting_quantity - f_prod.ending_quantity
                product_rev = sold * f_prod.sale_price

                total_sold += sold
                revenue += product_rev

                product["sold"] = sold
                product["revenue"] = product_rev

            fundraiser["products"].append(product)

        for y in expenses:
            expense = {
                "description": y.description,
                "amount": y.amount
            }
            total_expenses += y.amount
            fundraiser["expenses"].append(expense)
        
        fundraiser["profits"] = revenue - total_expenses
        res["fundraisers"].append(fundraiser)

    print(res)
    
fundraiser_summary_org("MWR")