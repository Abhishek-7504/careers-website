from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
      {
        'id': 1,
        'Title': 'Data Analyst',
        'Location': 'Bengaluru, India',
        'Salary': 'Rs. 10,00,000'
      },
      {
        'id': 2,
        'Title': 'Data Scientist',
        'Location': 'Delhi, India',
        'Salary': 'Rs. 15,00,000'
      },
      {
        'id': 3,
        'Title': 'Frontend Engineer',
        'Location': 'Remote',
        'Salary': '$ 120,000'
      },
      {
        'id': 4,
        'Title': 'Backend Engineer',
        'Location': 'San Francisco, USA',
        'Salary': '$150,000'
      }
    ]

@app.route("/")
def hello_jovian():
    return render_template('home.html', 
                           jobs=JOBS, 
                           company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)