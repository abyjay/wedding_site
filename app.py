from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/events-aby-goa')
def events():
    return render_template('events.html')

@app.route('/invitation')
def invitation():
    return render_template('aby_invitation.html')

@app.route('/when-where')
def location():
    return render_template('when-where.html')

@app.route('/rsvp')
def rsvp():
    return render_template('goa_rsvp.html')

if __name__ == '__main__':
    app.run(debug=True)