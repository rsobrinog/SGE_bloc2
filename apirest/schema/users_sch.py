def user_schema(user) -> dict:
    response = {"id":user[0],
                "name": user[1],
                "email":user[2]}
    return response

def users_schema(users)-> list[dict]:
    response = [user_schema(user) for user in users]
    return response


