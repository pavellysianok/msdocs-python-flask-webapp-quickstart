import os
import logging
from flask import Flask, redirect, render_template, request, send_from_directory, url_for

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Routes and Handlers
@app.route('/')
def index():
    logger.info('Request for index page received')
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
    name = request.form.get('name')

    if name:
        logger.info('Request for hello page received with name=%s', name)
        return render_template('hello.html', name=name)
    else:
        logger.info('Request for hello page received with no name or blank name -- redirecting')
        return redirect(url_for('index'))

# Error handling
@app.errorhandler(404)
def page_not_found(error):
    logger.error('404 Error: %s', error)
    return render_template('error.html', error_message='Page not found'), 404

@app.errorhandler(Exception)
def handle_error(error):
    logger.exception('Unhandled Exception: %s', error)
    return render_template('error.html', error_message='An unexpected error occurred'), 500

if __name__ == '__main__':
    app.run(debug=True)
