# Reporting logic that complements the finance module

class ReportGenerator:
    def generate_monthly_sales_report(self, sales_data):
        report = {}
        for pass_type, amount in sales_data.items():
            report[pass_type] = amount
        return report

    def generate_vehicle_report(self, vehicle_count):
        return f"Total vehicles parked this month: {vehicle_count}"

    def generate_financial_summary(self, finance_manager):
        return {
            "Total Revenue": finance_manager.revenue,
            "Total Expenses": finance_manager.expenses,
            "Profit": finance_manager.calculate_profit(),
            "Overdue Debtors": finance_manager.get_overdue_debtors()
        }
