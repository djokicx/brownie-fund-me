from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helper import get_account, deploy_mock, LOCAL_CHAIN_ENV


def main():
    deploy_fund_me()


def deploy_fund_me():
    account = get_account()
    # yes, we would like to publish our source code
    # if we are on a persistent network like rinkeby, use the associated address
    # otherwise deploy mocks

    # pulling out the feed address from the config file if not on the local dev network
    if network.show_active() not in LOCAL_CHAIN_ENV:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]

    # othewise mocking
    else:
        deploy_mock()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")

    return fund_me
