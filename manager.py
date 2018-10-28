# encoding: utf-8
from app import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.models.user import User
from app.models.shop import Shop
from app.models.location import Location
from utils import location

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command("db", MigrateCommand)

# 创建用户
@manager.option("-n", "--name", dest="name")
@manager.option("-p", "--password", dest="password")
def save_user(name, password):
    """添加用户"""
    user = User(name=name, password=password)
    db.session.add(user)
    db.session.commit()

# 读取省市区
@manager.command
def save_location():
    """添加省市区"""
    locations = location.get()
    for item in locations:
        local = Location(code=item.get("code"), name=item.get("name"), provinceCode=item.get("provinceCode"), cityCode=item.get("cityCode"))
        db.session.add(local)
    db.session.commit()



if __name__ == "__main__":
    manager.run()