from mycroft.util.log import LOG
from mycroft.messagebus.message import Message
from mycroft.skills.core import MycroftSkill, intent_handler, intent_file_handler

class ScreenshotTool(MycroftSkill):
    
    def __init__(self):
        super(ScreenshotTool, self).__init__(name="ScreenshotTool")
    
    def initialize(self):
        self.add_event("mycroft.display.screenshot.result", self.screenshot_result)
    
    @intent_file_handler("takescreenshot.intent")
    def take_screenshot(self, message):
        self.bus.emit(Message("mycroft.display.screenshot.get"))
        
    def screenshot_result(self, message):
        screenshot_path = message.data.get("result", "")
        LOG.info(screenshot_path)
        
        
def create_skill():
    return ScreenshotTool()
