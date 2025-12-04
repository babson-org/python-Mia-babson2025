
import time
import prices as _prices

def _find_position(self, sym):
    for p in self.positions:
        if p.get("sym") == sym:
            return p
    return None

def portfolio_sell_stock(self, sym: str, shares: float, price: float):
    """TODO:
    - Ensure symbol exists (use _find_position())
    - Ensure shares <= owned
    - Fetch last-close price via _prices.get_last_close_map([sym]) (use this price to sell shares)
    - Reduce position shares; adjust  'cost' proportionally by shares. (assumes average cost accounting)
    - Remove the position if shares drop to 0
    - Increase self.cash by proceeds
    - Hint: the amount you reduce cost is NOT the same as the amount you increase cash
    """
    pos = _find_position(self, sym)
    if pos is None:
        print("Symbol not in portfolio.")
        return
    
    #Validate that shares are positive
    if shares <= 0:
        print("Shares must be positive.")
        return

    if shares > pos["shares"]:
        print("Not enough shares to sell.")
        return

    #Get last close price
    price_map = _prices.get_last_close_map([sym])
    if sym not in price_map:
        print("Could not fetch price.")
        return

    last_close_price = price_map[sym]

    #Calculate proceeds
    sale_value = last_close_price * shares


    #Calculate cost per share
    avg_cost_per_share = pos["cost"] / pos["shares"]

    #Reduce the cost proportionately
    cost_reduction = avg_cost_per_share * shares
    pos["cost"] -= cost_reduction

    #Reduce shares
    pos["shares"] -= shares

    #Remove position if all shares are sold
    if pos["shares"] == 0:
        self.positions.remove(pos)

    #Add cash
    self.cash += sale_value

    return
    

    
       
