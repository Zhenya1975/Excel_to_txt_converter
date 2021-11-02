from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField
from werkzeug.utils import secure_filename

class UploadForm(FlaskForm):
    document_excel = FileField('Загрузка файла Excel', validators=[FileRequired(), FileAllowed(['xlsx','xls'], "wrong format!")])
