import math

# Constants
SQUARE_FEET_PER_GALLON = 112
HOURS_PER_GALLON = 8
LABOR_COST_PER_HOUR = 35.00


def get_float_input(prompt):
    """Helper function to ensure the user enters a valid positive number."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a value greater than or equal to 0.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numerical value.")


def main():
    print("--- Paint Job Estimator ---")

    # Get user inputs
    wall_space = get_float_input("Enter square feet of wall space to be painted: ")
    paint_price = get_float_input("Enter the price of the paint per gallon: $")

    # Calculations
    # Note: Using math.ceil ensures that if you need a fraction of a gallon,
    # you round up to the next full gallon to purchase.
    gallons_required = math.ceil(wall_space / SQUARE_FEET_PER_GALLON)
    labor_hours = (wall_space / SQUARE_FEET_PER_GALLON) * HOURS_PER_GALLON
    paint_cost = gallons_required * paint_price
    labor_charges = labor_hours * LABOR_COST_PER_HOUR
    total_cost = paint_cost + labor_charges

    # Display the results formatted to 2 decimal places
    print("\n--- Paint Job Estimate ---")
    print(f"Number of gallons of paint required: {gallons_required}")
    print(f"Hours of labor required: {labor_hours:.2f}")
    print(f"Cost of the paint: ${paint_cost:.2f}")
    print(f"Labor charges: ${labor_charges:.2f}")
    print(f"Total cost of the paint job: ${total_cost:.2f}")


if __name__ == "__main__":
    main()
