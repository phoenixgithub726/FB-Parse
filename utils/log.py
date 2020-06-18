from datetime import datetime, date
from utils.setting import setting

_log = None
class log:
    HEADER = '\033[95m'     # <Header>
    BLUE = '\033[94m'       # <Blue>
    GREEN = '\033[92m'      # <Green>
    WARNING = '\033[93m'    # <Warning>
    FAIL = '\033[91m'       # <Fail>
    ENDC = '\033[0m'        # </...>

    @staticmethod
    def getInstance():
        global _log
        if _log == None:
            _log = log()
        return _log

    def private_print(self, message = ''):
        # message will be like as '<B><H>Hello!</H></B> <F>You are failed</F>'.
        # before pront any message, we will convert the html type message to unicode string.
        message = message.replace('<Header>', self.HEADER)
        message = message.replace('<Blue>', self.BLUE)
        message = message.replace('<Green>', self.GREEN)
        message = message.replace('<Warning>', self.WARNING)
        message = message.replace('<Fail>', self.FAIL)
        message = message.replace('</Header>', self.ENDC)
        message = message.replace('</Blue>', self.ENDC)
        message = message.replace('</Green>', self.ENDC)
        message = message.replace('</Warning>', self.ENDC)
        message = message.replace('</Fail>', self.ENDC)
        print(message)
    
    def printLog(self, msg, toFile=True):
        if setting.getInstance().get('LOG') == True:
            self.private_print('\t<Green>LOG ==> %s</Green>' % msg)
        if toFile == True:
            self.printToFile(setting.getInstance().get('LOG_PATH') + '/' + date.today().isoformat() + '.info.log', msg)

    def printError(self, msg, toFile=True):
        if setting.getInstance().get('LOG') == True:
            self.private_print('\t<Fail>LOG ==> %s</Fail>' % msg)
        if toFile == True:
            self.printToFile(setting.getInstance().get('LOG_PATH') + '/' + date.today().isoformat() + '.err.log', msg)

    # ====================== log to file =========================
    def printToFile(self, filepath, log):
        try:
            fp = open(filepath, 'a', encoding='utf8')
            fp.write(datetime.now().isoformat() + '\t' + log + '\n')
            fp.close()
        except Exception as e:
            self.printError('Can not write to log file. Details: %s' % str(e), False)
            return False
        return True
