#Created CreditCard class
class CreditCard:
    """A customer credit card."""
    def __init__(self, customer, bank, account, limit)
    #The initial balance is zero

    self._balance = 0
    self._customer = customer
    sel._bank = bank
    self._account = account
    self._limit = limit

    def get_customer(self):
        #return name of customer
        return self._customer
    
    def get_bank(self):
        #return bank name
        return self._bank
    
    def get_account(self):
        """Return the Account number 
        (Stored as a string)"""
        return self._account

    def get_limit(self):
        """Returns credit card limit"""
        return self._limit
    
    def get_balance(self):
        """Returns the credit card balance"""
        return self._balance


    #Functions that manipulate constructors

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.
        
        Return True if charge was processed; False if charge was denied"""
        if price + self._balance > self._limit
            return False
        else:
            self.balance += price
            return True
        
    def make_payment(self, amount):
        """Make payment that reduces balance"""
        self.balance -= amount


cc = CreditCard( 'John Doe', '1st Bank' ,'5391 0375 9387 5309' , 1000)