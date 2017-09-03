import gettext
import os
import sys
from optparse import OptionParser

from binder.application import Application

gettext.bindtextdomain('messages', os.path.join(os.path.dirname(__file__), 'locale'))
gettext.bind_textdomain_codeset('messages', 'utf8')
gettext.textdomain('messages')
gettext.install('messages', localedir=os.path.join(os.path.dirname(__file__), 'locale'), codeset='utf8')

_ = gettext.gettext

usage = _("usage: %prog")


class Command:
    parser = OptionParser(usage=usage, version='%prog 0.1')

    def run(self):
        options, args = self.parser.parse_args()
        app = Application()
        app.run(sys.argv)
