# Blockchain_HW19

# Blockchain_HW

###  Custom testnet blockchain specifications 
#### 1. Puppeth, to generate your genesis block 

Please note the name of the testnet banknet using proof of authority in the below screenshot

![table](https://github.com/andreaovelar/Blockchain_HW18/blob/master/images/Capture.PNG "CLOSE")

Please find below screenshot using address from my crypto wallet and selecting chain ID 333

![table](https://github.com/andreaovelar/Blockchain_HW18/blob/master/images/Capture1.PNG "CLOSE")

Please find below screenshot in which we export the genesis configuration. We can see we created a banknet.json file which contain specifications

![table](https://github.com/andreaovelar/Blockchain_HW18/blob/master/images/Capture2.PNG "CLOSE")

Using the banknet configuration we then proceed to create two nodes with the respective passwords, the screenshot show the public address of the key and the path for the secret key file 

![table](https://github.com/andreaovelar/Blockchain_HW18/blob/master/images/Capture3.PNG "CLOSE")

Please find below initialization of the nodes using the genesis block using testnet.json

![table](https://github.com/andreaovelar/Blockchain_HW18/blob/master/images/Capture4.PNG "CLOSE")

Please find below output of the the first node into mining mode with the following command ./geth --datadir node1 --mine --minerthreads 1

![table](https://github.com/andreaovelar/Blockchain_HW18/blob/master/images/Capture55.PNG "CLOSE")

After Opening a new git bash. Please find below output of the the second node into mining mode with the following command ./geth --datadir node2 --port 30304 --rpc --bootnodes"enode://da89aa7ca0466d909a0fbcf71ff621d6a80be4bb1a8a4d23addf2cb6aa37d4581668555933b279c448afc801119a909ba5fca66b5b363d04a8a0be4de9cc1fa2@127.0.0.1:30303" --ipcdisable 

Please note that the enode address is coming from the node 1 (previous image)

![table](https://github.com/andreaovelar/Blockchain_HW18/blob/master/images/Capture6.PNG "CLOSE")


#### 2. Part 2 - My crypto wallet screenshots

We open the crypto wallet we use to configure the testnet

![table](https://github.com/andreaovelar/Blockchain_HW18/blob/master/images/Capture7.PNG "CLOSE")

Please find below screenshot of the custom network using same parameters that we use on gitbash. http://127.0.0.1:8545 chain id 333 name banknet, we can see that it is prefunded with ETH (significant amount)

![table](https://github.com/andreaovelar/Blockchain_HW18/blob/master/images/Capture8.PNG "CLOSE")

Please find below screenshot that shows that we sent 888 ETH to the account 

![table](https://github.com/andreaovelar/Blockchain_HW18/blob/master/images/Capture9.PNG "CLOSE")

Please find below confirmation of the transaction

![table](https://github.com/andreaovelar/Blockchain_HW18/blob/master/images/Capture10.PNG "CLOSE")

Please find below at the bottom of the image the transaction hash generated 0xf9500f525afb3a898543cd644ed8070ab6170859e68ea74cb1cff6fee33c2bb8  

![table](https://github.com/andreaovelar/Blockchain_HW18/blob/master/images/Capture11.PNG "CLOSE")

Please find below on the gitbash the confirmation of the submitted transaction at the bottom with the same hash we saw on mycrypto 

![table](https://github.com/andreaovelar/Blockchain_HW18/blob/master/images/Capture12.PNG "CLOSE")

Please find below confirmation of the transaction with status pending, after a while it changed to successful  

![table](https://github.com/andreaovelar/Blockchain_HW18/blob/master/images/Capture13.PNG "CLOSE")

## Conclusions 
* We were able to use Puppeth, to generate your genesis block
* We were able to use Geth, command-line tool, to create keys, initialize nodes, and connect the nodes together.
* We use configure our network using The Clique Proof of Authority algorithm
