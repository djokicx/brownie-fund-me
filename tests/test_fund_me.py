import pytest
from brownie import network, accounts, exceptions
from scripts.helper import LOCAL_CHAIN_ENV, get_account
from scripts.deploy import deploy_fund_me


def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee({"from": account})
    print(entrance_fee)
    print("Funding...")
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    print("Withdrawing...")
    fund_me.withdraw({"from": account})
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_CHAIN_ENV:
        pytest.skip("Only for local testing")
    fund_me = deploy_fund_me()
    bad_actor = accounts[1]
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})
