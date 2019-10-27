$(function() {
    ZBolt.StateViewModel = function(parameters) {
        var self = this;
        
        self.printerStateViewModel = parameters[0];

        self.printerStateViewModel.stateString.subscribe(function(p){
            var s = $('#state_wrapper');

            if (p == 'Printing') {
                s.addClass('printing')
            } else {
                s.removeClass('printing')
            }
        });

        self.onAfterBinding = function() {
        }

        self.onAfterBinding = function() {
            // new PNotify({
            //     title: gettext("Something went wrong"),
            //     text: gettext("Please consult octoprint.log for details"),
            //     type: "error",
            //     hide: false
            // });
        }

        // Handle Plugin Messages from Server
        self.onDataUpdaterPluginMessage = function (plugin, data) {
            if (plugin !== "zbolt_octoscreen") {
                return;
            }

            console.log("From ZBolt")
            console.log(plugin)
            console.log(data)


            new PNotify({
                title: data.title,
                text: data.text,
                type: "error",
                hide: false
            });

            // switch (data.type) {
            //     case "filament-over":{
            //         //console.log('octolapse.js - render-failed');
            //         self.updateState(data);
            //         var options = {
            //             title: 'Octolapse Rendering Failed',
            //             text: data.msg,
            //             type: 'error',
            //             hide: false,
            //             addclass: "zbolt",
            //             desktop: {
            //                 desktop: true
            //             }
            //         };
            //         // Octolapse.displayPopup(options);
            //         new PNotify(options);
            //         break;
            //     }
            // }
        }
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: ZBolt.StateViewModel,
        dependencies: ["printerStateViewModel"]
    });

    ZBolt.ConnectionViewModel = function(parameters) {
        var self = this;

        self.onAfterBinding = function() {
            var connection = $("#sidebar_plugin_klipper");
            connection.collapse("hide");
         }
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: ZBolt.ConnectionViewModel,
        dependencies: ["connectionViewModel"]
    });

});


