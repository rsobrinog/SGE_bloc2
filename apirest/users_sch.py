def user_schema(user):
    return {
        "name":user[0],
        "surname":user[1]
    }

def users_schema(users):
    return [user_schema(user) for user in users]