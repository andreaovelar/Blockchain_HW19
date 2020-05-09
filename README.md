# Blockchain_HW

###  Multi-Blockchain Wallet in Python
#### 1. Connecting hd-wallet-derive with python 
After you've integrated this "universal" wallet, you can begin to manage billions of addresses across 300+ coins in this example we are going to use Ethereum and Bitcoin Testnet

## Dependencies  
* PHP must be installed on your operating system (any version, 5 or 7). Don't worry, you will not need to know any PHP.
* You will need to clone the hd-wallet-derive tool.
* bit Python Bitcoin library.
* web3.py Python Ethereum library.

## Steps  
* Project setup files and and programs shold look like the repo with the wallet.py, derive, constants, hd_wallet_derive
* Generate a Mnemonic 
* send transactions using the following commands 
* Please note that for ethereum two nodes for your testnet should be running on the git bash in order for the tx to send 

Please find below screenshot in which we check in git bash that hd wallet derive is working properly. output should look like this after cloning repo and running below command 

![table](https://github.com/andreaovelar/Blockchain_HW19/blob/master/images/Capture3.PNG "CLOSE")

Please find below screenshot for of Bitcoin Testnet transactios recorded for our address 2 received and 6 sent 

![table](https://github.com/andreaovelar/Blockchain_HW19/blob/master/images/Capture1.PNG "CLOSE")

Please find below screenshot for of Bitcoin Testnet transaction using the block explorer, please note the hash of the transaction and the different addresses used.

![table](https://github.com/andreaovelar/Blockchain_HW19/blob/master/images/Capture.PNG "CLOSE")

### Using the banknet configuration we created in Blockchain_HW18 we then proceed to mine two nodes as shown previously. Please remember commands to mine to send ETH 
* First git bash window ./geth --datadir node1 --mine --minerthreads 1
* After Opening a new git bash. Please find below the following command ./geth --datadir node2 --port 30304 --rpc --bootnodes"enode://da89aa7ca0466d909a0fbcf71ff621d6a80be4bb1a8a4d23addf2cb6aa37d4581668555933b279c448afc801119a909ba5fca66b5b363d04a8a0be4de9cc1fa2@127.0.0.1:30303" --ipcdisable 
 The screenshot shows the confirmation of the transaction and respective hash using git bash

![table](https://github.com/andreaovelar/Blockchain_HW19/blob/master/images/Capture5.PNG "CLOSE")

Please find below same hash transaction when we open myCrypto app as well

![table](https://github.com/andreaovelar/Blockchain_HW19/blob/master/images/Capture8.PNG "CLOSE")

## Useful commands to send ETH and Bitcoin testnet 
* send_tx(BTCTEST,btc_account,'mrwjTLQMeqrbU4eg6WGyL7xCf25ewAHsn2',0.0001)
* send_tx(ETH,eth_account,'0x30B7C972578985dD504Cd6E1846d55faF25CF37E',1)

## Conclusions 
* We were able to use hd wallet derive and python to send ETH and bitcoin testnet 
* We use our network using The Clique Proof of Authority algorithm from previous assignment to send the ETH 
