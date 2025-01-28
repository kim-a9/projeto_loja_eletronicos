import base64
import pathlib
from datetime import time
from random import getrandbits
import jinja2
import pdfkit


PLATFORM = pathlib.sys.platform
platform = {
    'win32': 'bins/windows/wkhtmltopdf.exe'
}
CURRENT_PATH = pathlib.Path(__file__).parent
BINARY_PATH = CURRENT_PATH.joinpath(platform[PLATFORM])
TEMPLATE_DIR = CURRENT_PATH.joinpath('templates')
OUTPUT_DIR = CURRENT_PATH.joinpath('output_pdf')

def to_base64(dir, filename):
    with open(dir.joinpath(filename), 'rb') as image_file:
        return str(base64.b64encode(image_file.read()), 'utf-8')
    
def read_file(dir, filename):
    with open(dir.joinpath(filename), 'r') as file:
        return file.read()

def create_pdf(template, vars, css=[]):
    template_path = TEMPLATE_DIR.joinpath(template)
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(TEMPLATE_DIR))

    template = jinja_env.get_template(template)
    html = template.render(vars,
                           static_dir=template_path.parent,
                           to_base64=to_base64,
                           read_file=read_file)

    file_name = f"{getrandbits(101)}{int(time())}.pdf"
    output_dir = OUTPUT_DIR.joinpath(file_name)

    pdf_options = {
        'page-size': 'A4',
        'margin-top': '0.05in',
        'margin-right': '0.05in',
        'margin-bottom': '0.05in',
        'margin-left': '0.05in',
        'encoding': 'utf-8'
    }

    config = pdfkit.configuration(wkhtmltopdf=BINARY_PATH)
    try:
        pdfkit.from_string(
            html,
            output_dir,
            options=pdf_options,
            configuration=config,
            css=css
        )
        return output_dir
    except:
            return False
