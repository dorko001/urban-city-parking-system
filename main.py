from vehicle import Car
from parking_manager import ParkingManager

def main():
    manager = ParkingManager()

    car = Car("ABC-123")
    entered = manager.enter_vehicle(car, entry_time=10)

    if entered:
        print("Vehicle entered parking")
    else:
        print("Parking full")

    fee = manager.exit_vehicle(car, exit_time=13)
    print("Parking fee:", fee)

if __name__ == "__main__":
    main()
