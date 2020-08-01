from app.dao import search_data_dao
from app.ml.model_prediction import process_document


def get_all_data():
    all_data = search_data_dao.get_all_data()
    result_list = []
    if all_data:
        for data in all_data:
            data.results['id'] = data.id
            result_list.append(data.results)
    return result_list


def get_result_by_id(id):
    search_result = search_data_dao.get_data_by_id(id)
    if search_result:
        return search_result[0].results
    return search_result


def delete_result_by_id(id):
    delete_result = search_data_dao.delete_data_by_id(id)
    return "Data deleted successfully" if delete_result is True else "Data not deleted"


def process_query(text, task):
    process_results = process_document(text, task)
    insert_results = search_data_dao.insert_data(text, process_results)
    return process_results if insert_results is True else ""
