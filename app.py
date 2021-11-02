from flask import Flask, render_template, request, send_file, url_for
import xlrd
import os
import pandas
import codecs
from forms import UploadForm
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'
current_folder = os.getcwd()
excel_file_path = os.path.join(current_folder, 'upload_excel.xlsx')
txt_file_path = os.path.join(current_folder, 'result.txt')
bootstrap = Bootstrap(app)



@app.route('/', methods=['GET', 'POST'])

# функция, которая берет текстовый файл и отправляяет его пользователю. У удаляет исходники

def converter():
# отображаем страницу с формой
    form = UploadForm()
    # если форма валидируется (то есть требования выполняются), то делаем действия с
    # данными. Но сначала она ведь не валидируется.
    #Поэтому код должен убежать вниз и отрть страница с формой
    if form.validate_on_submit():
        global file_name
        # В переменную f загоняем то что получили из формы
        f = form.document_excel.data

        # извлекаем имя файла и его расширение
        file_name, file_extension = os.path.splitext(f.filename)
        # если расширение правильное, то сохраняем файл.
        if file_extension == '.xlsx':
            f.save(excel_file_path)
        else:
            print('файл неправильный')
        excel_data_fr = pandas.read_excel(excel_file_path,header=None)
        print(excel_data_fr)

        # Итерируем по строкам и собираем txt файл
        row = ''
        for i in range(len(excel_data_fr)):
            for j in range(len(excel_data_fr.columns)):
                row = row + str(excel_data_fr.iloc[i,j]) + '\t'
            with codecs.open(txt_file_path, 'a', encoding='utf16') as textfile:
                textfile.write(row + '\n')
                row = ''
        print("Файл должен быть готов")
        try:
            return send_file(txt_file_path, attachment_filename=file_name + '.txt', as_attachment=True)

        finally:
            os.remove(txt_file_path)
            os.remove(excel_file_path)


    return render_template('converter.html', form=form)

def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        file_name, file_extension = os.path.splitext(f.filename)
        if file_extension == '.xlsx':
            f.save(excel_file_path)
            return render_template('converter.html')
        else:
            return render_template('converter.html')

    return render_template('converter.html')

if __name__ == '__main__':
    app.run()
