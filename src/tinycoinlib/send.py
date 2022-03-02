
from .talk import TinyCoinTalk


class TinyCoinSend(TinyCoinTalk):
    '''
    {Bit,Lite,Doge,...}coin sending (make payments) using the TinyCoinTalk RPC
    client that talks to the {}coind RPC server.
    '''

    def send(self, coin_amount, destination, comment=''):
        '''Perform send-transaction from the default wallet

        Parameters
        ----------
        coin_amount : numerical
            The coin amount (basic units) that is to be transferred.
        destination : string
            Receiving address.

        Returns
        -------
        transaction_id : string
            Hex string for the transaction ID given by the {}coind server.
        '''

        return self.call('sendtoaddress "{}" {} "{}"'.format(
            destination, coin_amount, comment))



    def get_balance(self):
        '''Checks the available balance in the default wallet
        
        Returns
        -------
        coin_amount : numerical
            Balance of the wallet
        '''
        return self.call('getbalance')



    def get_details(self, transaction_id):
        '''Get details of a made transaction.

        Parameters
        ----------
        transaction_id : string
            Transaction id (txid) of a made transaction. This is returned
            by the self.send method.

        Returns
        -------
        transaction_details : dict
            Details about the in-wallet transaction.
        '''
        return self.call('gettransaction {}'.format(transaction_id))



