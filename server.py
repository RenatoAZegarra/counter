from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "super_secret_key"


@app.route('/')
def add_counter():
    session['counter'] = session.get('counter', 0) + 1
    return render_template('index.html', counter = session['counter'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/add_two')
def add_two():
    session['counter'] = session.get('counter', 0) +  1
    return redirect('/')

@app.route('/reset')
def reset():
    session.pop('counter')
    return redirect('/')

@app.route('/increments' , methods=['GET', 'POST'])
def increment():
    if request.method == 'POST':
        increment_value = int(request.form['increment'])
        session['counter'] += increment_value - 1
        return redirect('/')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)