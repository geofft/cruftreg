from flask import request, make_response

import register

def spnego():
    if 'REMOTE_USER' in request.environ:
        return register.webregister(register.strip_athena(request.environ['REMOTE_USER']))
    else:
        return make_response(("no", 401, {}))
