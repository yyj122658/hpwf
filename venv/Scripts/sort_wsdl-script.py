#!c:\users\ext.yangyujian\pycharmprojects\hpwf\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'spyne==2.13.16','console_scripts','sort_wsdl'
__requires__ = 'spyne==2.13.16'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('spyne==2.13.16', 'console_scripts', 'sort_wsdl')()
    )
