# AgroChain: Blockchain-Based IoT Agricultural Governance

by Jazib Dawre, Junaid Girkar, Kanaad Deshpande and Ramchandra Mangrulkar


## Abstract


>Current IoT networks have been the scrutiny of cyber security analysis due to their abhorrent lack of security and privacy in the network. They have been the primary targets for numerous botnet attacks and reconnaissance targets. On the other hand, blockchains have proved vital in data confidentiality and security on an event-based transaction system. This paper presents a novel approach towards integrating IoT and Blockchain using Hyperledger Iroha to create a permissioned, private blockchain that focuses on privacy and security while maintaining near-real-time performances in IoT applications. We propose a multilevel architecture that stays true to the grounded concepts of zoning in an IoT network while improving data privacy and access control within the system. The addition of role-based authentication allows entities for cross-ownership of permissioned entities and data in the network, thus allowing for truly decentralized operation.


### Keywords

IoT, Blockchain, Ethereum, Raspberry Pi, Arduino, Hyperledger Iroha, Chaincode, Smart Contract, Automation

## How to run

You need to setup the arduino and raspberry pi along with their respective sensors first!

1. Clone the [iroha](https://github.com/hyperledger/iroha) repository at the root
2. Follow [instructions](https://iroha.readthedocs.io/en/develop) to setup the iroha docker containers
3. Run the `IrohaSetup.py` followed by `IrohaMain.py`

## License
[MIT License](./license.md)
## Citation
