from datetime import datetime
from flask import Flask, render_template, request

# Configure application
app = Flask(__name__)

#Genders and their constants in the formula
GENDERS = [
    {"name": "Male", "r":0.68},
    {"name": "Female", "r":0.55}
]

#Units and their values in grams
WEIGHTS = [
    {"unit": "kg", "coefficient":1000},
    {"unit": "lbs", "coefficient":453.59}
]

#Drinks and their alcohol amount per unit
DRINKS = [
    {"name": "🍺 Beer 330ml (12oz) ABV 5%", "value":16.5},
    {"name": "🍷 Wine 150ml (5oz) ABV 12%", "value":18},
    {"name": "🥃 Spirits 50ml (1.5oz) ABV 40%", "value":20}
]


#Index route
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", drinks=DRINKS, weights=WEIGHTS, genders=GENDERS)
    else:
        #Gender constant
        try:
            r = float(request.form.get("gender"))
        except ValueError:
            return render_template("error.html", message="Gender constant is not valid")
        if not any(gender["r"] == r for gender in GENDERS):
            return render_template("error.html", message="Gender constant is not valid")

        #Converting weight to grams
        try:
            weight = float(request.form.get("weight"))
        except ValueError:
            return render_template("error.html", message="Weight value is not valid")

        try:
            weight_multiplier = float(request.form.get("weight-unit"))
        except ValueError:
            return render_template("error.html", message="Weight unit is not valid")

        weight_in_grams = weight * weight_multiplier


        #Start time
        try:
            start_hour, start_min = map(int, request.form.get("time").split(":"))
        except ValueError:
            return render_template("error.html", message="Not a valid starttime")
        if not 0 <= start_hour < 24 or not 0 <= start_min < 60:
                return render_template("error.html", message="Not a valid time")


        #Current time
        current_hour, current_min = map(int, datetime.now().strftime("%H:%M").split(":"))


        #Difference
        since_hour = (current_hour - start_hour + 24) % 24
        if current_min >= start_min:
            since_min = current_min - start_min
        else:
            since_min = current_min - start_min + 60
            since_hour = (since_hour + 23) % 24

        #Total amount of alcohol taken
        total_alcohol = 0
        # ChatGPT helped with this for loop
        for drink in DRINKS:
            try:
                value = request.form.get(drink["name"], "0")
                quantity = int(value) if value.strip() != "" else 0
            except ValueError:
                return render_template("error.html", message="One or more drink numbers are not valid")
            total_alcohol += quantity * drink['value']


        #Calculating BAC with Widmark Formula
        bac = round((100*total_alcohol/(weight_in_grams*r)) - 0.016*(since_hour + since_min/60), 2)
        if bac < 0:
            bac = 0

        #On average BAC Decreases 0.016 per hour
        wait_min = bac / (0.016 / 60)
        wait_hour = int(wait_min / 60)
        wait_min = round(wait_min % 60)

        return render_template("results.html", bac=bac, h=wait_hour, m=wait_min)