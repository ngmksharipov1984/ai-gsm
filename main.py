from decimal import Decimal
from pathlib import Path
from typing import Any

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import DateTime, Integer, Numeric, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

DATABASE_URL = "postgresql://postgres:password@192.168.88.59:5443/AzsOnline_RELEASE"


class Base(DeclarativeBase):
    pass


class Card(Base):
    __tablename__ = "Cards"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    card_number: Mapped[str] = mapped_column(String)
    fuel_type: Mapped[str] = mapped_column(String)
    balance: Mapped[Decimal] = mapped_column(Numeric)
    created_at: Mapped[Any] = mapped_column(DateTime)


engine = create_engine(DATABASE_URL)
app = FastAPI(title="Cards Viewer")
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))


@app.get("/", response_class=HTMLResponse)
def read_cards() -> HTMLResponse:
    with Session(engine) as session:
        cards = session.query(Card).all()

    columns = [column.name for column in Card.__table__.columns]
    rows = [{column: getattr(card, column) for column in columns} for card in cards]

    template = templates.get_template("index.html")
    return HTMLResponse(template.render(columns=columns, rows=rows))
