from flask import Flask, render_template, redirect, url_for
from form import MyForm
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['SECRET_KEY'] = 'erhsry7w456#$%YSsdb'
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_FOLDER'] = 'static/uploads'


@app.route('/', methods=['get', 'post'])
def home():
	form = MyForm()
	if form.validate_on_submit():
		caption = form.caption.data
		filename = secure_filename(form.upload.data.filename)
		form.upload.data.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		print(caption, filename)
		return redirect(url_for('home'))
	return render_template('form.html', form=form)


if __name__ == '__main__':
	app.run()
