from app.models.search_data import OldData
from app import db, logger


def get_all_data():
    try:
        all_data = OldData.query.all()
        return all_data
    except Exception:
        logger.exception('Issue which reading all data from user table')
        return ""
    finally:
        db.engine.dispose()


def get_data_by_id(data_id):
    try:
        data = OldData.query.filter(OldData.id == data_id).all()
        return data
    except Exception:
        logger.exception('Error occurred while getting data by id')
        return ""
    finally:
        db.engine.dispose()


def insert_data(text, results):
    try:
        data = OldData(text=text, results=results)
        db.session.add(data)
        write_status = db.session.commit()
        return write_status is None
    except Exception:
        db.session.rollback()
        logger.exception('Error occurred while inserting new data into database')
        return False
    finally:
        db.engine.dispose()


def delete_data_by_id(data_id):
    try:
        OldData.query.filter(OldData.id == data_id).delete()
        delete_status = db.session.commit()
        return delete_status is None
    except Exception:
        db.session.rollback()
        logger.exception('Error occurred while deleting data from database')
        return False
    finally:
        db.engine.dispose()