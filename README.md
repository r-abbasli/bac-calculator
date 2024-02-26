# BAC CALCULATOR
#### Video Demo:  <https://www.youtube.com/watch?v=Tg2UdCoMSzM>
#### Description:

The Application, BAC Calculator, is based on Python web framework Flask. It calculates users’ blood alcohol content, BAC, with inputs from them such as, their gender and weight, when did they start to drink, how many drinks did they consume for each category. It, then, outputs the current BAC, as well as, the time needed for it to be zero.


##### app.py
###### Constants
`app.py` starts with constant lists: `GENDERS`, `WEIGHTS` and `DRINKS`.

`GENDERS` is a list of dictionaries, that contains names of the gender and its 'r' value, which is gender specific constant that affects in resulting BAC figures.

`WEIGHTS` is a list of dictionaries, that contain kilogram and pounds as key called unit, and their respective gram values as a value called coefficient.

`DRINKS` is a list of dictionaries, that contain 3 kind of drinks as key, and the amount of alcohol present in one unit of it as a value.

###### Index route
Index route has two methods, `GET` and `POST`. Previously mentioned lists of dictionies are passed into `index.html` when rendered, as a part of the `GET` method of the route. They will be used as elements for jinja `for loop`s.

On the `POST` method of the index route, the data submitted on the form on `index.html` are retrieved and error handled. Validity of each value is seperately checked with `try` blocks and if there is a `ValueError` or the value is not in accepted range, `error.html` page is rendered with error message as its attribute.

User input for the time, meaning the time they started to drink, is retrieved with `request.form.get` and the current time is retrieved from Python package `datetime`. The difference between them are taken as a couple of varibles, one for hour unit, another for minutes. For that, both of the times' `str` values are splitted with : seperator, and logical calculations are made for individiual characters of the times.

The amount of each of the drink that was listed on the main page is multiplied by the their respective values, alcohol in unit, and summed to see how much pure alcohol user has drunk.

Then current BAC is calculated by using Widmark Formula. According to the formula, BAC decreases 0.016 every hour, on average. BAC and the time required to wait for it to be zero are stored in three variables `bac`, `wait_hour` and `wait_min` to be used as attributes to `results.html`'s renderer.



##### layout.html
`layout.html` is the template file to be used by Flask to render other html files.

##### index.html
`index.html` starts with javascript code that will be convert time field's default value to the current hour and minutes.

Genders are presented alongside with their radio buttons as a jinja loop and the selected option stores 'r' as it's form html tag value.

Underneath, there is a input field that expects user's weight either in kg or lbs and respective radio buttons to choose from kg or lbs.

Below that, the user has to choose the current time, which the app will assume that is within last 24 hours.

Next, a group of drinks and input field for their counts are located at the bottom of the form.

Calculate button submits the form.

Reset button resets all the inputs.

##### error.html
`error.html` file is rendered if any error is successfully handled, showing the error message which is attributed to renderer on the index route's post method.

Return button returns to calculation page.


##### results.html
`results.html` is rendered with values from the index route's post method.
Visually, the page first shows the users current BAC.

Then, expected withdrawal time for alcohol.

Disclaimer notes are also included.

Return button returns to calculation page.
