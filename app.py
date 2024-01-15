from flask import Flask, render_template, request, jsonify
from main import prerequest
import datetime

app=Flask(__name__,template_folder='template')

current_start_time = None
current_end_time = None

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/set_detection_time', methods=['POST'])
def set_detection_time():
    global current_start_time, current_end_time
    return render_template('detectionpage.html')

if __name__ == '__main__':
    app.run(debug=True)
