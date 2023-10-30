from flask import Blueprint, render_template, request, send_file
from method import extract_table_columns
import tempfile

view = Blueprint("views", __name__)

@view.route("/", methods=["GET", "POST"])
@view.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            print("1")
            return "No file part"

        file = request.files['file']

        if file.filename == '':
            print("2")
            return "No File selected"

        if file and file.filename.endswith('.docx'):
            try:
                # Process the uploaded file
                output_txt_file = tempfile.mktemp(suffix=".txt")
                extract_table_columns(file, output_txt_file)

                # Return the processed text file to the user
                return send_file(output_txt_file, as_attachment=True, download_name="output.txt")
            except Exception as e:
                return str(e)

    return render_template('upload.html')

@view.route("/about")
def about():
    return render_template("about.html")





