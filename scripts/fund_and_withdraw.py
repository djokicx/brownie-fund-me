from brownie import FundMe, accounts
from scripts.helper import get_account


def main():
    fund()
    withdraw()


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee})
    print(f"{fund_me.addressToAmountFunded(account.address)}")


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print("Funding")
    fund_me.withdraw({"from": account})
