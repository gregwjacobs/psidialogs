from easyprocess import EasyProcess
from nose.tools import with_setup, eq_
from pyvirtualdisplay.smartdisplay import SmartDisplay
import psidialogs

VISIBLE=0
TIMEOUT=30

def check_open(func):
    cmd = '''python -c "import psidialogs;psidialogs.{func}"'''.format(func=func)
    # exception if nothing is displayed
    with SmartDisplay(visible=VISIBLE) as disp:
        with EasyProcess(cmd):
            disp.waitgrab(timeout=TIMEOUT)

def test_message():
    check_open('''message(message='hi')''')
def test_ask_string():
    check_open('''ask_string(message='hi')''')
def test_ask_file():
    check_open('''ask_file(message='hi')''')
def test_ask_folder():
    check_open('''ask_folder(message='hi')''')
def test_choice():
    check_open('''choice(message='hi')''')
def test_multi_choice():
    check_open('''multi_choice(message='hi')''')
def test_text():
    check_open('''text(text='hi')''')
def test_error():
    check_open('''error(message='hi')''')
def test_warning():
    check_open('''warning(message='hi')''')
def test_ask_ok_cancel():
    check_open('''ask_ok_cancel(message='hi')''')
def test_ask_yes_no():
    check_open('''ask_yes_no(message='hi')''')
        