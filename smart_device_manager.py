class SmartDevice:
    def __init__(self, name, device_id):
        # Validation to ensure device ID isn't an empty string
        if not device_id or str(device_id).strip() == "":
            print("Warning: Device ID cannot be empty. Setting fallback ID.")
            self.__device_id = "UNKNOWN-ID"
        else:
            self.__device_id = device_id
        
        self.name = name
        self.__power_status = False  # Devices start powered off by default

    # Getter for device_id using property decorator
    @property
    def device_id(self):
        return self.__device_id

    # Getter for power_status
    @property
    def power_status(self):
        return self.__power_status

    # Setter for power_status to control status updates safely
    @power_status.setter
    def power_status(self, status):
        if isinstance(status, bool):
            self.__power_status = status

    def turn_on(self):
        self.power_status = True
        print(f"{self.name} has been turned ON.")

    def turn_off(self):
        self.power_status = False
        print(f"{self.name} has been turned OFF.")

    def display_info(self):
        current_power = "ON" if self.power_status else "OFF"
        print(f"Device Name: {self.name}")
        print(f"Device ID: {self.device_id}")
        print(f"Power Status: {current_power}")


class TemperatureSensor(SmartDevice):
    def __init__(self, name, device_id, temperature=24.5):
        # Initializing inherited attributes using super()
        super().__init__(name, device_id)
        self.temperature = temperature

    def read_temperature(self):
        if not self.power_status:
            print(f"Operation failed. {self.name} is powered OFF.")
            return
        print(f"{self.name} Temperature Reading: {self.temperature}°C")


class SmartLight(SmartDevice):
    def __init__(self, name, device_id, brightness=50):
        super().__init__(name, device_id)
        # Validation ensuring initial brightness stays between 0 and 100
        if 0 <= brightness <= 100:
            self.brightness = brightness
        else:
            self.brightness = 50

    def increase_brightness(self, amount):
        if not self.power_status:
            print(f"Operation failed. {self.name} is powered OFF.")
            return
        
        new_level = self.brightness + amount
        if new_level > 100:
            self.brightness = 100
        else:
            self.brightness = new_level
        print(f"{self.name} brightness raised to {self.brightness}%")

    def decrease_brightness(self, amount):
        if not self.power_status:
            print(f"Operation failed. {self.name} is powered OFF.")
            return
            
        new_level = self.brightness - amount
        if new_level < 0:
            self.brightness = 0
        else:
            self.brightness = new_level
        print(f"{self.name} brightness dropped to {self.brightness}%")


class SecurityCamera(SmartDevice):
    def __init__(self, name, device_id):
        super().__init__(name, device_id)
        self.recording_status = False

    def start_recording(self):
        if not self.power_status:
            print(f"Operation failed. {self.name} is powered OFF.")
            return
        self.recording_status = True
        print(f"{self.name} is now RECORDING.")

    def stop_recording(self):
        self.recording_status = False
        print(f"{self.name} has STOPPED recording.")

    # Overriding display_info to add unique camera attributes
    def display_info(self):
        super().display_info()
        current_rec = "Recording" if self.recording_status else "Idle"
        print(f"Recording Status: {current_rec}")


# --- Interactive Terminal Menu ---
def main():
    # Creating the required test objects
    living_sensor = TemperatureSensor("Living Room Sensor", "SNSR-404")
    kitchen_light = SmartLight("Kitchen Light", "LGT-101", 75)
    yard_cam = SecurityCamera("Backyard Camera", "CAM-777")

    while True:
        print("\n--- SMART DEVICE MANAGEMENT MENU ---")
        print("1. Display Device Information")
        print("2. Turn Device On")
        print("3. Turn Device Off")
        print("4. Read Temperature")
        print("5. Adjust Brightness")
        print("6. Start Recording")
        print("7. Exit")
        
        user_choice = input("Enter choice (1-7): ").strip()

        if user_choice == "1":
            print("\n--- Current System Status ---")
            living_sensor.display_info()
            print("." * 25)
            kitchen_light.display_info()
            print("." * 25)
            yard_cam.display_info()

        elif user_choice == "2":
            print("\nSelect device to turn ON:")
            print("1. Sensor  2. Light  3. Camera")
            target = input("Choice: ").strip()
            if target == "1": living_sensor.turn_on()
            elif target == "2": kitchen_light.turn_on()
            elif target == "3": yard_cam.turn_on()
            else: print("Invalid device selected.")

        elif user_choice == "3":
            print("\nSelect device to turn OFF:")
            print("1. Sensor  2. Light  3. Camera")
            target = input("Choice: ").strip()
            if target == "1": living_sensor.turn_off()
            elif target == "2": kitchen_light.turn_off()
            elif target == "3": yard_cam.turn_off()
            else: print("Invalid device selected.")

        elif user_choice == "4":
            living_sensor.read_temperature()

        elif user_choice == "5":
            print(f"\nCurrent brightness level is {kitchen_light.brightness}%")
            action = input("Type '+' to increase or '-' to decrease: ").strip()
            change_input = input("Enter adjustment value: ").strip()
            
            if change_input.isdigit():
                val = int(change_input)
                if action == "+":
                    kitchen_light.increase_brightness(val)
                elif action == "-":
                    kitchen_light.decrease_brightness(val)
                else:
                    print("Invalid adjustment action.")
            else:
                print("Error: Please input a valid whole number.")

        elif user_choice == "6":
            print("\n1. Start Recording  2. Stop Recording")
            cam_action = input("Choice: ").strip()
            if cam_action == "1":
                yard_cam.start_recording()
            elif cam_action == "2":
                yard_cam.stop_recording()
            else:
                print("Invalid camera command.")

        elif user_choice == "7":
            print("Shutting down management console. Goodbye.")
            break
            
        else:
            print("Invalid menu option. Try again.")

if __name__ == "__main__":
    main()