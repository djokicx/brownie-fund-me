from brownie import MockV3Aggregator, accounts, network, config
from web3 import Web3

DECIMALS = 8
STARTING_PRICE = 200000000000

FORKED_LOCAL_ENV = ["mainnet-fork"]
LOCAL_CHAIN_ENV = ["development", "ganache-local"]


def get_account():
    if (
        network.show_active() in LOCAL_CHAIN_ENV
        or network.show_active() in FORKED_LOCAL_ENV
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mock():
    print(f"Active network is {network.show_active()}")
    print("Deploying mocks...")
    if len(MockV3Aggregator) <= 0:
        mock_agg = MockV3Aggregator.deploy(
            DECIMALS, STARTING_PRICE, {"from": get_account()}
        )
    print("Mocks deployed")
    # using the most recently deployed MockV3Aggregator
