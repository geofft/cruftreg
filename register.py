#!/usr/bin/env python

from flask import render_template
import hmac

import key

def register(user):
    h = hmac.new(key.key)
    h.update(user)
    return h.hexdigest()

def webregister(user):
    ret = register(user)
    if ret:
        return render_template('success.html', user=user, key=ret)
    else:
        return render_template('failure.html', user=user)

if __name__ == "__main__":
    import os
    if 'REMOTE_USER' in os.environ:
        ret = register(os.environ['REMOTE_USER'])
        if ret:
            print "Successfully registered. Your token is %s" % (ret, )
            print "Save your confirmation code! You will need it to claim an account."
        else:
            print "Failure registering."
    else:
        print "Unauthenticated."
