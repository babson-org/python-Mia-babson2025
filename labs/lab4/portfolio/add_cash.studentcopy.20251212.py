
import time
def portfolio_add_cash(self, amount: float):
    """TODO:
    - Reject negative amounts
    - Otherwise add to self.cash
    - Print message showing how much cash added and what you new cash balance is
    - return not needed
    """
    if amount < 0:
        print("Cannot add a negative amount of cash.")
        return

    # Add to cash balance
    self.cash += amount

    # Print confirmation message
    print(f"Added ${amount:}. New cash balance is ${self.cash:}.")