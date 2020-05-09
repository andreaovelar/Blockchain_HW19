import subprocess
import json
import os
from constants import *
from web3 import Web3
from bit import *
from eth_account import Account
from dotenv import load_dotenv  
from web3.middleware import geth_poa_middleware
from bit.network import NetworkAPI
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1.8545"))
#Set this mnemonic as an environment variable, and include the one you generated as a fallback using:
mnemonic = os.getenv('MNEMONIC', 'govern obscure fiscal ritual crop two gasp canyon lucky author nest body')

def derive_wallets(coin,mnemonic,numderive):
    command ='php derive -g --mnemonic="'+str(mnemonic)+'" --numderive='+str(numderive)+' --coin='+str(coin)+' --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    keys = json.loads(output)
    return(keys)

#output ETH
derive_wallets(ETH,mnemonic,3)


#output BTCTEST
derive_wallets(BTCTEST,mnemonic,3)

coins = {'eth':derive_wallets(ETH,mnemonic,3),'btc-test': derive_wallets(BTCTEST,mnemonic,3)}

eth_privkey = coins['eth'][0]['privkey']
print(eth_privkey)
btc_privkey = coins['btc-test'][0]['privkey']
print(btc_privkey)


def priv_key_to_account(coin,priv_key):
    if coin==ETH:
        return Account.privateKeyToAccount(priv_key)
    else:
        return PrivateKeyTestnet(priv_key)

eth_account=priv_key_to_account(ETH,eth_privkey)
eth_account

btc_account=priv_key_to_account(BTC,btc_privkey)
btc_account


def create_tx(coin,account,to,amount):
    if coin==ETH:
        gasEstimate = w3.eth.estimateGas({"from": account.address, "to": to, "value": amount})
        return {
            "to": to,
            "from": account.address,
            "value": amount,
            "gas": gasEstimate,
            "gasPrice": w3.eth.gasPrice,
            "nonce": w3.eth.getTransactionCount(account.address),
            "chainID": w3.eth.chainId
        }
    else:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])

create_tx(BTC,btc_account,'mmPhfRz2gXLoXMQtzgQ3vxPrwK6GFcugkY',0.00001)
#need to funnd account

create_tx(BTC,btc_account,'mrwjTLQMeqrbU4eg6WGyL7xCf25ewAHsn2',0.00001)

btc_account

def send_tx(coin,account, to, amount):
    tx = create_tx(coin,account,to,amount)
    signed_tx = account.sign_transaction(tx)
    if coin==ETH:
        result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    else: 
        result=NetworkAPI.broadcast_tx_testnet(signed_tx)
    print(result)
    return result

#Send some transactions!
send_tx(BTCTEST,btc_account,'mrwjTLQMeqrbU4eg6WGyL7xCf25ewAHsn2',0.0001)

#Local PoA Ethereum transaction

from web3.middleware import geth_poa_middleware

w3.middleware_onion.inject(geth_poa_middleware, layer=0)

create_tx(ETH,eth_account,'0x30B7C972578985dD504Cd6E1846d55faF25CF37E',1)

send_tx(ETH,eth_account,'0x30B7C972578985dD504Cd6E1846d55faF25CF37E',1)
