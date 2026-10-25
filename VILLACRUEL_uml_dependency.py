# Dependency
class WiFi:
    def connect(self) -> str: 
        return "Online"

class Phone:
    def check_mail(self, network: WiFi) -> str:
        return network.connect()

# (Test)
device = Phone()
router = WiFi()
print(device.check_mail(router))
