from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class MyForm(FlaskForm):
	caption = StringField('Caption', validators=[DataRequired()])
	upload = FileField('Upload', validators=[FileRequired(), FileAllowed(['pdf', 'png', 'jpg', 'jpeg', 'gif', 'ppt'])])















