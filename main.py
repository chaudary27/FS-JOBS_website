
from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Lahore, Pakistan',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Software Developer',
        'location': 'Lahore, Pakistan',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 3,
        'title': 'Front-end developer',
        'location': 'Lahore, Pakistan',
        'salary': 'Rs. 13,00,000'
    },
    {
        'id': 4,
        'title': 'Back-end developer',
        'location': 'Lahore, Pakistan',
    }
]

@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name="FS")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
