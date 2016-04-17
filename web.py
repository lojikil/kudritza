from bottle import route, request, run
from jinja2 import Template
import lolscript
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)
import login.model
template_cache = {}


@route('/c89.php', method=['post', 'get'])
@route('/backdoor.php', method=['post', 'get'])
def c99():
    if request.method == "POST":
        pass
    return template_cache['backdoor'].render()


@route('/lol')
@route('/lol/')
def lolhome():
    return template_cache['lolhome'].render()


@route('/lol/calc', method=['post', 'get'])
def lolcalc():
    "RCE that should dump a key"
    s0 = """{progn
    {define-variable key "9E43E0E004BD925246655AC0870C7D028586D048A1DE7991A2910799C4D05B72"}
    {"""
    s1 = "{0} {1} {2}"
    if request.method == "POST":
        opt = request.forms.get("operator")
        op0 = request.forms.get("operand0", "")
        op1 = request.forms.get("operand1", "")
        script = s0 + s1.format(opt, op0, op1) + "}}"
        print script
        try:
            ast = lolscript.read(script)
            print ast[0]
            print "died?"
            ret = lolscript.eval(ast[0], {})
            print "died?"
            print ret
            print "died?"
            return str(ret)
        except Exception as e:
            print e
        return "foo"
    return template_cache['lolcalc'].render()


@route('/<name:path>.lol')
def lolloader(name):
    parts = name.split('/')
    root = parts[0:-1]
    filename = parts[-1]
    return lolscript.re_file(filename, root)

for name in ['backdoor', 'lolhome', 'lolcalc']:
    fh = file('./templates/{0}.html'.format(name), 'r')
    template_cache[name] = Template(fh.read())
    fh.close()

if __name__ == "__main__":
    run(host='0.0.0.0', port=8085)
