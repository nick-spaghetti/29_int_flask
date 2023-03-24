from app import app
from models import db, Cupcake


db.drop_all()
db.create_all()

c1 = Cupcake(
    flavor="cherry",
    size="large",
    rating=5
)

c2 = Cupcake(
    flavor="chocolate",
    size="small",
    rating=7
)

c3 = Cupcake(
    flavor="vanilla",
    size="small",
    rating=2
)

c4 = Cupcake(
    flavor="almond",
    size="small",
    rating=9
)

c5 = Cupcake(
    flavor="raspberry",
    size="medium",
    rating=4
)

c6 = Cupcake(
    flavor="caramel",
    size="large",
    rating=9
)

db.session.add_all([c1, c2, c3, c4, c5, c6])
db.session.commit()
