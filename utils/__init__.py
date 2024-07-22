def get_resp(message='', code=0, data=None):
    code = 0 if not message else -1
    message = message or 'success'
    res = {'code': code, 'message': message}
    if data:
        res['data'] = data
    return res