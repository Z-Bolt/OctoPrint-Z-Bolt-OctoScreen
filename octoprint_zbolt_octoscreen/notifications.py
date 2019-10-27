from time import time

class NotificationsStorage:
    def initialize(self, plugin_manager):
        self._message = {
            "time": time(),
            "text": "Wake up, Neo...\nThe Matrix has you...\nFollow the white rabbit.\n\n\nKnock, Knock, Neo."
        }
        self._plugin_manager = plugin_manager

    def send_message(self, message):
        self._message = {
            "time": time(),
            "text": message['text'],
            "title": message['title']
        }

        payload = dict()
        payload['title'] = message['title']
        payload['text'] = message['text']
        self._plugin_manager.send_plugin_message("zbolt_octoscreen", payload)


    def get_message_to_display(self):
        if not self._message:
            return None

        m = self._message['text']
        self._message = None
        return m

Notifications = NotificationsStorage()
        



