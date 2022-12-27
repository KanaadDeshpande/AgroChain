docker run --name iroha ^
-d ^
-p 50051:50051 ^
-v "D:\Other computers\My Laptop\DJSCE\BE\SEM7\Classwork\BC\Mini Project\Code\iroha\example:/opt/iroha_data" ^
-v blockstore:/tmp/block_store ^
--network=iroha-network ^
-e KEY=node0 ^
hyperledger/iroha:latest