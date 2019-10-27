# coding=utf-8
from __future__ import absolute_import

# import logging
import octoprint.plugin
import flask
import socket

from octoprint.events import Events
from octoprint_zbolt_octoscreen.notifications import Notifications
from octoprint_zbolt_octoscreen.settings import ZBoltSettings


class ZBoltOctoScreenPlugin(octoprint.plugin.SettingsPlugin,
                    octoprint.plugin.EventHandlerPlugin,
                    octoprint.plugin.TemplatePlugin,
                    octoprint.plugin.AssetPlugin,
                    octoprint.plugin.SimpleApiPlugin,
                    octoprint.plugin.StartupPlugin):

    def initialize(self):
        Notifications.initialize(self._plugin_manager)

        self._logger.info("Z-Bolt Toolchanger init")
        self.Settings = ZBoltSettings(self._settings)
        

    def get_assets(self):
        return dict(
            less=['less/theme.less'],
            js=['js/zbolt.js'],
            css=['css/main.css', 'css/theme.css']
        )

    def get_settings_defaults(self):
         return ZBoltSettings.default_settings()

    def get_api_commands(self):
        return dict(
            get_notification=[]
        )

    # def on_event(self, event, payload):
    #     if event is Events.CONNECTED:
    #         self._logger.info("Connecting2:")
            # n = self._plugin_manager.get_plugin('zbolt_octoscreen').Notifications
            # self.send_message({"title": "test221", "text": "asfdsaf23asdfaefsdf"})

    def on_settings_save(self, data):
        octoprint.plugin.SettingsPlugin.on_settings_save(self, data)

    def on_api_command(self, command, data):
        if command == "get_notification":
            return flask.jsonify(message = Notifications.get_message_to_display())

    def on_api_get(self, request):
        return flask.jsonify(printer_name="test2")


    def get_template_configs(self):
        return [
            dict(type="settings", name="Z-Bolt OctoScreen", custom_bindings=False),
        ]


    ##~~ Softwareupdate hook
    def get_update_information(self):
        return dict(
        zbolt=dict(
            displayName = "Z-Bolt OctoScreen",
            displayVersion = self._plugin_version,

            type="github_release",
            user="Z-Bolt",
            repo="OctoPrint-Z-Bolt-OctoScreen",
            current=self._plugin_version,

            pip="https://github.com/Z-Bolt/OctoPrint-Z-Bolt-OctoScreen/archive/{target_version}.zip"
            )
        )


__plugin_name__ = "Z-Bolt OctoScreen"

def __plugin_load__():
    global __plugin_implementation__    
    __plugin_implementation__ = ZBoltOctoScreenPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
