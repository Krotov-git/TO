from Parsing.Site_TezTours import TezTours
from Parsing.Site_AnexTours import AnexTours
from Parsing.Site_ICS import ICS
from Parsing.Site_Biblioglobus import Biblioglobus
from Parsing.Site_Pegast import Pegast
from Parsing.Site_TUI import TUI
from Parsing.Site_Inturist import Inturist
from Parsing.Site_Panteon import Panteon

class Common_Parser:
    def __init__(self):
        self.tez = TezTours()
        # print(self.tez.parse_site())
        # print('================')
        self.anex = AnexTours()
        # print(self.anex.parse_site())
        # print('================')
        self.ics = ICS()
        # print(self.ics.parse_site())
        # print('================')
        self.bg = Biblioglobus()
        # print(self.bg.parse_site())
        # print('================')
        self.pg = Pegast()
        # print(self.pg.parse_site())
        # print('================')
        self.tui = TUI()
        # print(self.tui.parse_site())
        # print('================')
        self.intu = Inturist()
        # print(self.tui.parse_site())
        # print('================')
        self.pan = Panteon()
        # print(self.tez.parse_site())
        # print('================')

        self.db_common_parser = {}

        self.db_common_parser.update(self.tez.parse_site())
        self.db_common_parser.update(self.anex.parse_site())
        self.db_common_parser.update(self.ics.parse_site())
        self.db_common_parser.update(self.bg.parse_site())
        self.db_common_parser.update(self.pg.parse_site())
        self.db_common_parser.update(self.tui.parse_site())
        self.db_common_parser.update(self.intu.parse_site())
        self.db_common_parser.update(self.pan.parse_site())
        self.new_data = self.db_common_parser
        #print('new_data :', self.new_data)

    def get_new_data(self):
        return self.new_data


if __name__ == '__main__':
    pars = Common_Parser()
