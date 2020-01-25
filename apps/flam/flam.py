import appdaemon.plugins.hass.hassapi as hass

class FlamFireplace(hass.Hass):

    def initialize(self):
        self.fireplace_sensor = self.args['modbus']['sensor']
        self.listen_state(self.decode_status, self.fireplace_sensor)

    def decode_status(self, *kwargs)
        self.log(kwargs)
