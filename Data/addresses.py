class Address:
    def __init__(self):
        self.entered = "Kirchstraße 1"
        self.target = "Kirchstraße 1, Berlin"

    def get_entered_address(self):
        return self.entered

    def get_target_address(self):
        return self.target
