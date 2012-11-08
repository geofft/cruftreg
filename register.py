#!/usr/bin/env python

from flask import render_template
import hmac

def strip_athena(principal):
    if principal[-15:] == "@ATHENA.MIT.EDU":
        return principal[0:-15]
    else:
        return None

def register(user):
    if not user:
        return None
    h = hmac.new(open('/srv/cruftreg/key').read())
    h.update(user)
    return h.hexdigest()

def webregister(user):
    ret = register(user)
    if ret:
        return render_template('success.html', user=user, token=ret)
    else:
        return render_template('failure.html', user=user)

if __name__ == "__main__":
    import os
    if 'REMOTE_USER' in os.environ:
        user = strip_athena(os.environ['REMOTE_USER'])
        ret = register(user)
        if ret:
            print "Welcome, %s. Your token is %s" % (user, ret)
            print "Save your token, and keep it secure! This token can be used later to"
            print "create an account, once the MITCRUFT.ORG realm is operational. For"
            print "updates on the service, join the mitcruft-announce mailing list at"
            print "http://mailman.mit.edu/mailman/listinfo/mitcruft-announce"
        else:
            print "Failure registering."
    else:
        print "Unauthenticated."
