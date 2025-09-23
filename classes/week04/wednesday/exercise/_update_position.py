'''
## Rethinking input_client() and Position Updates

Take a look at input_client() in client.py in the portfolio folder.  
Right now, this is the function that creates a new client.  

### Current Behavior
- Every new client starts with:
  - An empty portfolio (positions = []).
  - An initial **cash contribution**.
- We record that contribution by:
  1. Creating a transaction using create_transaction().
  2. Updating the cash position inside input_client().

This works, but it's not a great design. The logic for updating positions is **scattered**, 
and input_client() is doing too much.

---

### Why This Is a Problem
- Every time a transaction happens, we **must** also update the corresponding position.  
- Right now, there is no single place that enforces this rule.  
- If we forget to update positions after creating a transaction, the system will drift out of sync.

---

### Better Design
We should create a helper function (e.g., _update_position(client, transaction)) that:
- Takes the active client and the new transaction as input.
- Updates the client's positions accordingly.
- Ensures consistency between **transactions** and **positions**.

This helper would be called inside create_transaction(), so that every transaction automatically 
updates the portfolio.

---

### Issues We Need to Handle


1. **Buying a Security**
   - Validate ticker: does it exist in ticker.data?
   - Check available cash: do we have enough to cover the purchase?
   - Update (or create) the position for that symbol.
   - Recalculate the average cost.

2. **Selling a Security**
   - Validate position: do we own that ticker?
   - Check share count: do we have at least that many shares?
   - Reduce (or remove) the position if shares go to zero.
   - Add cash back to the portfolio.

3. **Contributions**
   - no positions exist (first contribution)
   - add to existing cash balance

4. **Withdrawals**
   - Check available cash balance.
   - Reduce the cash position accordingly.

---

### Next Step
Refactor:
- Move position-update logic out of input_client().
- Implement _update_position(client, transaction).
- Call it automatically inside create_transaction() for every transaction type.

For Wednesday, write the function so it handles CONTRIBUTIONS and
WITHDRAWALS.  For now, return None for transaction types BUY or SELL

This way:
- transactions become the **source of truth**.
- positions` always stay consistent with recorded transactions.



'''
def _update_position(client, transaction):

    symbol = transaction["symbol"]
    shares = transaction["shares"]
    trn_type = transaction["type"]

  
    if trn_type == "CONTRIBUTION":
        cash_pos = next((p for p in client["positions"] if p["symbol"] == "$$$$"), None)
        if cash_pos:
            cash_pos["shares"] += shares
        else:
            cash_pos = {
                "id": transaction["id"],
                "shares": shares,
                "symbol": "$$$$",
                "name": "Cash",
                "avg_cost": 1.00
            }
            client["positions"].append(cash_pos)

 
    elif trn_type == "WITHDRAWAL":
        cash_pos = next((p for p in client["positions"] if p["symbol"] == "$$$$"), None)
        if not cash_pos:
            raise ValueError("Withdrawal failed: no cash position found.")
        if cash_pos["shares"] < shares:
            raise ValueError("Withdrawal failed: insufficient cash balance.")
        cash_pos["shares"] -= shares

    elif trn_type in ("BUY", "SELL"):
        return None

    else:
        raise ValueError(f"Unknown transaction type: {trn_type}")
