from flask import Flask, render_template, make_response, request, redirect
from flask_weasyprint import HTML, render_pdf

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/labreport')
def labreport():
  return render_template('coverform-lab.html')

@app.route('/assignment')
def assignment():
  return render_template('coverform-assignment.html')

@app.route('/cover-assignment', methods=['POST', 'GET'])
def cover_assigment():
  if request.method == 'POST':

    html = render_template('cover-assignment.html',
    subject = str.upper(request.form.get('subject')), 
    name= request.form.get('name'),
    id = request.form.get('id'),
    semester = request.form.get('semester'),
    section = request.form.get('section'),
    session = request.form.get('session'),
    date_of_sub = request.form.get('date_of_sub'),
    teachers_name = request.form.get('teachers_name'),
    teachers_title = request.form.get('teachers_title'),
    teachers_dept = request.form.get('teachers_dept'),
    course_code = request.form.get('course_code'),
    course_name = request.form.get('course_name')
    )

    return render_pdf(HTML(string=html))

@app.route('/cover-lab', methods=['POST', 'GET'])
def cover_lab():
  if request.method == 'POST':

    html = render_template('cover-lab.html',
    subject = str.upper(request.form.get('subject')), 
    name= request.form.get('name'),
    id = request.form.get('id'),
    semester = request.form.get('semester'),
    section = request.form.get('section'),
    exp_no = request.form.get('exp_no'),
    exp_name = request.form.get('exp_name'),
    course_code = request.form.get('course_code'),
    course_name = request.form.get('course_name'),
    date_of_exp = request.form.get('date_of_exp'),
    date_of_sub = request.form.get('date_of_sub'),
    teachers_name = request.form.get('teachers_name')
    )

    return render_pdf(HTML(string=html))


if __name__ == '__main__':
    app.run(threaded=True, port=5000)