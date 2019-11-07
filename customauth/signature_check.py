from eth_account.messages import encode_defunct
from eth_account import Account

class Address:
    def fromSignatureAndNonce(self, signature, nonce):
        message = encode_defunct(text=("ethgarden.io " + str(nonce)))
        return(Account.recover_message(message, signature=signature))