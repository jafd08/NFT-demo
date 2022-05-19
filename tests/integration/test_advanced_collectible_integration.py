from brownie import AdvancedCollectible, network
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
    get_contract,
)
import time
from scripts.advanced_collectible.deploy_and_create import deploy_and_create
import pytest


def test_can_create_advanced_collectible_integration():
    # deploy contract
    # creact an NFT
    # get a random breed back
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
    # Act
    adv_collectible, creation_tx = deploy_and_create()
    time.sleep(60)
    # Assert
    assert adv_collectible.tokenCounter() == 1
