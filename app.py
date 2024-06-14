from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
JOBS=[
  {
    "id":1,
    "title":'Full Stack Developer',
    "location":'Lahore, Pkaistan',
    "salary":'Rs. 20,00,000'
  },
  {
    "id":2,
    "title":'Software engineer',
    "location":'Islamabad, Pakistan',
    "salary":'Rs. 30,00,000'
  },
  {
    "id":3,
    "title":'Data Scientist',
    "location":'Bengaluru, India',
    "salary":'Rs. 10,00,000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
