from Parsing.Site_TezTours import TezTours
from Parsing.Site_AnexTours import AnexTours
from Parsing.Site_ICS import ICS

class Common_Parser:
    def __init__(self):
        self.tez = TezTours()
        #print(self.tez.parse_site())
        #print('================')
        self.anex = AnexTours()
        #print(self.anex.parse_site())
        #print('================')
        self.ics = ICS()
        #print(self.ics.parse_site())

        self.db_common_parser = {}

        self.db_common_parser.update(self.tez.parse_site())
        self.db_common_parser.update(self.anex.parse_site())
        self.db_common_parser.update(self.ics.parse_site())
        self.new_data = self.db_common_parser
        print('new_data :', self.new_data)

    def get_new_data(self):
        return self.new_data
 # def set_tez(self, value):
    #     value = self.tez
    #     self.db_common_parser.append(value)
    #
    # def set_anex(self, value):
    #     self.db_common_parser.append(self.anex)
    #
    # def set_tez(self, value):
    #     self.db_common_parser.append(self.ics)
    #
    # def get_common_parser(self):
    #     return self.db_common_parser

if __name__ == '__main__':
    pars = Common_Parser()
