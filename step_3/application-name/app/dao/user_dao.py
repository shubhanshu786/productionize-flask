from app.models.user import Users
from app import db, logger
from sqlalchemy import distinct


def get_all_users():
    try:
        all_users = Users.query.all()
        return all_users if all_users else None
    except Exception:
        logger.exception('Issue which reading all data from user table')
        return None
    finally:
        db.engine.dispose()


def get_all_users_name(name):
    try:
        user_names = db.session.query(distinct(Users.name)).filter(Users.name == name).all()
        return user_names
    except Exception:
        logger.exception('Error occurred while getting all user names')
        return False
    finally:
        db.engine.dispose()


def get_users_by_id(user_id):
    try:
        all_users = Users.query.filter(id=user_id).all()
        return all_users if all_users else None
    except Exception:
        logger.exception('Error occurred while getting all users by id')
        return None
    finally:
        db.engine.dispose()


def insert_new_user(name, password):
    try:
        user = Users(name=name, password=password)
        db.session.add(user)
        write_status = db.session.commit()
        return write_status is None
    except Exception:
        db.session.rollback()
        logger.exception('Error occurred while inserting new user into database')
        return False
    finally:
        db.engine.dispose()


def update_password(name, new_password):
    try:
        user = Users.query.filter(Users.name == name).first()
        user.password = new_password
        update_status = db.session.commit()
        return update_status is None
    except Exception:
        db.session.rollback()
        logger.exception('Error occurred while updating user password')
        return False
    finally:
        db.engine.dispose()
