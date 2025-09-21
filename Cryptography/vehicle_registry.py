class VehicleRegistry:
    def __init__(self):
        self.vehicles = {}  

    def register_vehicle(self, plate: str, owner: str, model: str) -> bool:
        """Register a new vehicle if plate not already used."""
        if plate in self.vehicles:
            return False
        self.vehicles[plate] = {"owner": owner, "model": model}
        return True

    def get_vehicle(self, plate: str):
        """Retrieve vehicle details by plate number."""
        return self.vehicles.get(plate, None)
