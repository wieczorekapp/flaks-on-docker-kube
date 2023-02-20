from flask.cli import FlaskGroup
from project import app, db, Visitor


cli = FlaskGroup(app)

# docker compose -f docker-compose.prod.yml down -v
# docker compose -f docker-compose.prod.yml up -d --build
# docker compose -f docker-compose.prod.yml exec web python manage.py create_db


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(Visitor(ip="192.168.0.1"))
    db.session.commit()


if __name__ == "__main__":
    cli()
