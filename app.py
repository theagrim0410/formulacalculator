from flask import Flask, render_template, request
from sympy import symbols, integrate, exp, pi

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    ch = int(request.form['choice'])
    result = None
    subresult = None

    if ch == 0:
        x = symbols('x')
        T = float(request.form['T'])
        var = 16115 / T
        inte = exp(43.2 - var)
        result = float(integrate(inte, (x, 0, 1)))

    elif ch == 1:
        d = float(request.form['d'])
        p = float(request.form['p'])
        c = float(request.form['c'])
        a = d * p * c
        b = p * (100 - c)
        result = float((a + b) / c)

    elif ch == 2:
        c1 = float(request.form['c1'])
        c2 = float(request.form['c2'])
        r = float(request.form['r'])
        result = float(((100 / c1) - (100 / c2)) * r)

    elif ch == 3:
        r = float(request.form['r'])
        l = float(request.form['l'])
        surface = 2 * pi * r * l
        ch2 = int(request.form['ch2'])

        if ch2 == 0:
            pulp = float(request.form.get('pulp', 0))  # default 0 if not provided
            result = float(pulp / surface)

        elif ch2 == 1:
            lf = float(request.form.get('lf', 0))      # default 0 if not provided
            pulp = lf * surface
            result = float(pulp)


    elif ch == 4:
        adwt = float(request.form['adwt'])
        moisture = float(request.form['moisture'])
        bdwt = adwt * (1 - (moisture / 100))
        charge = float(request.form['charge'])
        wl_strength = float(request.form['wl_strength'])
        wl_required = (bdwt * charge) * 10 / wl_strength
        moisture_content = adwt - bdwt
        wood = 1
        liquid = 3
        total_liquid = moisture_content * liquid / wood
        bl_required = total_liquid - wl_required - moisture_content
        subresult = wl_required
        result = bl_required

    return render_template('index.html', result=result, subresult=subresult, choice=ch)

if __name__ == '__main__':
    app.run(debug=True)
