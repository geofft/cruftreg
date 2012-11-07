from flask import render_template, request, g
import PAM

import register

def conv(pam, msgs, resp):
    ret = ""
    if len(msgs) == 1 and msgs[0][1] == PAM.PAM_PROMPT_ECHO_OFF:
        return [(request.form.get('password'), 0)]
    else:
        g.message = "Unknown message from PAM: %s" % (
            ", ".join(msg for msg, msg_style in msgs), )
        return []

def password():
    if request.method == 'POST':
        g.message = ""
        pam = PAM.pam()
        user = request.form.get('user')
        pam.start('cruftreg', user, conv)
        try:
            pam.authenticate()
        except PAM.error as error:
            return render_template('password.html', error=error[0])
        if g.message != "":
            return render_template('password.html', error=error)
        return register.webregister(user)
    else:
        return render_template('password.html')
