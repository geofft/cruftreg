#!/usr/bin/env python

def register(user):
    print "XXX attempting to register %s" % (user,)

if __name__ == "__main__":
    import os
    if 'REMOTE_USER' in os.environ:
        register(os.environ['REMOTE_USER'])
