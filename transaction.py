class Transaction:
    """This is a transaction class"""

    def __init__(self, transaction_id, set_of_operations, nonce):
        self.transaction_id = ""
        self.set_of_operations = []
        self.nonce = 0

    def create_transaction(self, set_of_operations, nonce):
        self.set_of_operations = set_of_operations
        self.nonce = nonce
        return self

    # This function is created to create a string from transaction objects
    def __repr__(self):
        rep = 'Transaction :' + self.transaction_id + ' ' +' '.join([str(item) for item in self.set_of_operations]) +  str(self.nonce)
        return rep

    # This function is created to print transaction
    def print(self):
        print(repr(self))

