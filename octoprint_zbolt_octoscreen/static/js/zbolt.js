var ZBoltOctoScreen = {}

$(function () {
    ZBoltOctoScreen.StateViewModel = function (parameters) {
        var self = this;

        self.printerStateViewModel = parameters[0];

        self.printerStateViewModel.stateString.subscribe(function (p) {
            var s = $('#state_wrapper');

            if (p === 'Printing') {
                s.addClass('printing')
            } else {
                s.removeClass('printing')
            }
        });

        self.onAfterBinding = function () {
        }

        // Handle Plugin Messages from Server
        self.onDataUpdaterPluginMessage = function (plugin, data) {
            if (plugin !== "zbolt_octoscreen") {
                return;
            }

            new PNotify({
                title: data.title,
                text: data.text,
                type: "error",
                hide: false
            });
        }
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: ZBoltOctoScreen.StateViewModel,
        dependencies: ["printerStateViewModel"]
    });

    ZBoltOctoScreen.ConnectionViewModel = function (parameters) {
        var self = this;

        self.onAfterBinding = function () {
            var connection = $("#sidebar_plugin_klipper");
            connection.collapse("hide");
        }
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: ZBoltOctoScreen.ConnectionViewModel,
        dependencies: ["connectionViewModel"]
    });
});


