from scrapper.facebook import FaceBook as fb
from utils.log import log

log.getInstance().printLog('Start the scrapper for instagram.')

fb.getInstance().start()

log.getInstance().printLog('End the scrapper for instagram. See you later.')
