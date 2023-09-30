from factories import FeatureFactory

class CalculatorApplication:
    """
    A class used to represent a calculator application.

    Attributes
    ----------
    history_manager : InMemoryHistoryManager
        An instance of the InMemoryHistoryManager class.

    Methods
    -------
    run()
        Runs the calculator application.
    perform_calculation()
        Performs a calculation and saves the result to the history.
    view_history()
        Displays the history of calculations.
    """

    def __init__(self):
        """Constructs all the necessary attributes for the CalculatorApplication object."""
        self.history_manager = FeatureFactory.create_factory("history").create_feature()

    def run(self):
        """Runs the calculator application."""
        while True:
            print("\033c", end="")
            print("Enter the operation you want to perform:")
            print("1. Perform calculation")
            print("2. View history")
            print("3. Exit")
            choice = input("Enter your choice: ")

            match choice:
                case "1":
                    self.perform_calculation()
                case "2":
                    self.view_history()
                case "3":
                    print("Exiting...")
                    exit()
                case _:
                    print("Invalid choice")

    def perform_calculation(self):
        """Performs a calculation and saves the result to the history."""
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        available_operations = FeatureFactory.get_available_calculators()
        operation = input(f"Enter the operation to perform ({', '.join(available_operations)}): ")
        
        try:
            feature_factory = FeatureFactory.create_factory(operation)
            calculation = feature_factory.create_feature()
            result = calculation.calculate(x, y)
        except Exception as e:
            print(e)
        else:
            print(f"Result: {result}")
            self.history_manager.append_history(f"{x} {operation} {y} = {result}")
        finally:
            input("Press enter to continue")

    def view_history(self):
        """Displays the history of calculations."""
        print("History:")
        self.history_manager.view_history()
        input("Press enter to continue")

if __name__=="__main__":
    calculator_application = CalculatorApplication()
    calculator_application.run()
