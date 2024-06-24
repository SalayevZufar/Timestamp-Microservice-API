from flask import Flask, jsonify
from email.utils import formatdate
from datetime import datetime
import time
app = Flask(__name__)


@app.route("/api/<date>")
def date_time(date):
    
    if date.isnumeric() == True:

        to_uts = datetime.fromtimestamp(int(date))
        
        
        
        weekday = to_uts.strftime("%a")
        day = to_uts.strftime("%d")
        month = to_uts.strftime("%b")
        year = to_uts.strftime("%Y")
        local_time = to_uts.strftime("%X")
        return jsonify({"unix": date, "utc" : f"{weekday}, {day} {month} {year} {local_time} GMT"})
    else:
        return jsonify({ "error" : "Invalid Date" })
@app.route("/api/")
def current_time():
    current_time = datetime.now()

    
    weekday = current_time.strftime("%a")
    day = current_time.strftime("%d")
    month = current_time.strftime("%b")
    year = current_time.strftime("%Y")
    local_time = current_time.strftime("%X")
        
    return jsonify({"unix": int(time.time()), "utc" : f"{weekday}, {day} {month} {year} {local_time} GMT"})
if __name__ == "__main__":
    app.run(debug=True)
