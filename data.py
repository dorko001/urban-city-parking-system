# Sample data to initialize the system

monthly_sales = {
    "Weekly Pass": 1200,
    "Monthly Pass": 3000,
    "Single Entry": 500
}

# Example initialization
def initialize_system():
    parking_manager = ParkingManager()
    finance_manager = FinanceManager()
    report_generator = ReportGenerator()

    # Add vehicles and financial data as needed
    # This is where you can integrate previous assessment data

    return parking_manager, finance_manager, report_generator
