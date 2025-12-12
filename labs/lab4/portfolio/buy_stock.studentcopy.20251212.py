

import prices as _prices
import time

def _find_position(self, sym):
    for p in self.positions:
        if p.get("sym") == sym:
            return p
    return None

def portfolio_buy_stock(self, sym: str, shares: float, price: float):
    """TODO:    
    - Validate sym in DOW30
         In the lab4 folder is a file prices.py.  Look at the file and find out what DOW30 is
         You can access DOW30 with _prices.DOW30 (see how we import prices above)
    - Validate shares > 0
    - Fetch last-close price via _prices.get_last_close_map([sym]) (use this price to buy shares)
    - Make sure the client has enough cash to make the purchase (price * shares)

    - IMPORTANT: in self.positions there should only be one dictionary per symbol

    - Add the purchase to an existing position or create a new position in self.positions 
    - Be sure to decrease the client cash attribute
    NOTE: UI prompts are handled in main.py: this method only prints for invalid ticker and insufficient funds. The rest are handled in main.py
    """
    def portfolio_buy_stock(self, sym: str, shares: float, price: float):
    

        # Validate ticker symbol
        if sym not in _prices.DOW30:
            print("Invalid ticker symbol.")
            return

        # Validate number of shares
        if shares <= 0:
            print("Shares must be positive.")
            return

        # Get last close price
        price_map = _prices.get_last_close_map([sym])
        if sym not in price_map:
            print("Could not fetch price.")
            return

        last_close_price = price_map[sym]

        #Calculate total cost
        total_cost = last_close_price * shares

        #Check if client has enough cash
        if self.cash < total_cost:
            print("Insufficient funds.")
            return

        #Find exisiting position
        pos = _find_position(self, sym)

        # Create new position or update existing
        if pos is None:
            new_pos = {
                "sym": sym,
                "shares": shares,
                "cost": total_cost
            }
            self.positions.append(new_pos)
        else:
            pos["shares"] += shares
            pos["cost"]  += total_cost

        #Take cash out of account
        self.cash -= total_cost

        return

    
    
    



