from functools import wraps
from flask import Response, request
auth_data = [{"username": "test1", "password": "testTest"}]
def authfunc(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            filtered_data = [user_data for user_data in auth_data if user_data["username"] == request.authorization["username"]]
            print(filtered_data)
            if filtered_data:
                password = request.authorization['password']
                if password == filtered_data[0]['password']:
                    return func(*args, **kwargs)
        except TypeError:
            return Response('Access denied', status=403)

        return Response('Access denied', status=403)

    return wrapper
