from app.dao import user_dao


def get_user_information(username):
    users = user_dao.get_all_users_name(username)
    for user in users:
        user_id = user['id']
        # get data from another table
    return users
