
import datetime

from flask import Flask, render_template
from multiprocessing import Value

counter = Value('i', 0)
app = Flask(__name__, template_folder="templates", static_folder="static")


@app.route('/')
def root():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.
    dummy_times = [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]

    with counter.get_lock():
        counter.value += 1

    return render_template('home.html', times=dummy_times, counter=counter.value)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='0.0.0.0', port=80, debug=True)
