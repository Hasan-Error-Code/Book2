class Device:
    name = ''
    brand = ''
    charge = ''
    battery = ''

    def phone(self):
        Device.name = "Galaxy j2 Pro"
        Device.brand = "Samsung"
        Device.charge = "Type-B"
        Device.battery = "3000 mh"

    def phone(self):
        Device.name = "Galaxy M51"
        Device.brand = "Samsung"
        Device.charge = "Type-C"
        Device.battery = "7000 mh"

out = Device("M51", "Samsung", "Type-C", "7000mh")
print(out)