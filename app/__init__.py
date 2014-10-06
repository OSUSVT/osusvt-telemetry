from flask import Flask
import time

app = Flask(__name__)
app.config.from_object('config')
app.debug = True

#app.jinja_env.globals.update(list=list)

#Credits be to Andreas Jung @ https://www.andreas-jung.com/contents/a-python-decorator-for-measuring-the-execution-time-of-methods
def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print '%2.2f\t| %r \t| (%r, %r)' % \
              (te-ts, method.__name__, args, kw)
        return result

    return timed

from app import views
