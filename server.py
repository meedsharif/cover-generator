from flask import Flask, render_template, make_response, request, redirect
from flask_weasyprint import HTML, render_pdf

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/cover', methods=['POST', 'GET'])
def my_home():
  if request.method == 'POST':



    html = render_template('cover.html',
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

    # HTML('').write_pdf('/tmp/weasyprint-website.pdf')
    
    # pdf = pdfkit.from_string(rendered, False, configuration=config, options=options)

    # response = make_response(pdf)

    # response.headers['Content-Type'] = 'application/pdf'
    # response.headers['Content-Dispostion'] = 'inline; filename=output.pdf'
    # return response

if __name__ == '__main__':
    app.run(threaded=True, port=5000)