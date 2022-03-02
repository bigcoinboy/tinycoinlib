
from .talk import TinyCoinTalk


class TinyCoinReceive(TinyCoinTalk):
    '''
    {Bit,Lite,Doge,...}coin payment accepting using the TinyCoinTalk RPC client
    that talks to the {}coind RPC server.

    Based on an arbitrary identifier (transaction_id), it can 
    - create a payment address
    - detect if the payment has been completed
    
    It doesn't save anything on disk by itself, leaving the database managenet
    to the {}coind server.
    '''

    def _check_type(self, transaction_id):
        if not isinstance(transaction_id, str):
            raise ValueError( ('Address label (transaction ID) is not a '
                                'string but its type is {}').format(type(transaction_id)))

   
    def _get_address(self, transaction_id):
        '''
        Returns
        -------
        address : string
            The {}coin address matching the label, if existing.
            If not existing, returns an empty string.
        '''
        try:
            response = self.call('getaddressesbylabel', [transaction_id])
        except Exception as e:
            # This is the case no transaction IDs (RPC server returns code 500)
            return ''
        
        if len(response) > 1:
            raise ValueError(
                    ('More than 1 labels matching id {}: Got {}'
                ).format(transaction_id, response))
        
        return list(response.keys())[0]



    def get_payment_address(self, transaction_id):
        '''Gives the coin address matching the given transaction_id.

        Checks if there is an wallet address with the label "transaction_id",
        creates one if not, and returns the payment address.
        
        Parameters
        ----------
        transaction_id : string
            Identifier of the transaction

        Returns
        -------
        address : string
            The public key address for receiving the user payment.
        '''
        self._check_type(transaction_id)
        
        address = self._get_address(transaction_id)
        if not address:
            address = self.call('getnewaddress', [transaction_id])

        return address


    def payment_completed(self, transaction_id, coin_amount):
        '''Checks if the transaction_id has been completed

        Parameters
        ----------
        transaction_id : string
            Identifier of the transaction
        coin_amount : numerical
            The coin amount (basic units) required for the payment
            to be considered completed.

        Returns
        -------
        completed : bool
            If True, the payment has been completed. Otherwise, False.
        amount : numerical
            Returns the amount paid, in the basic units (DOGE, LTC, BTC, ...)
        '''
        self._check_type(transaction_id)
        
        address = self._get_address(transaction_id)
        if address:
            amount = self.call('getreceivedbyaddress', [address])
            completed = bool(amount and amount > required_amount)
        else:
            raise ValueError('Cannot find the address matching the transaction_id')

        return completed, amount


