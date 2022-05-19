from brownie import AdvancedCollectible, network
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
    get_contract,
)
from scripts.advanced_collectible.deploy_and_create import deploy_and_create
import pytest


def test_can_create_advanced_collectible():
    # deploy contract
    # creact an NFT
    # get a random breed back
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for integration testing")
    # Act
    adv_collectible, creation_tx = deploy_and_create()
    requestId = creation_tx.events["requestedCollectible"]["requestId"]
    random_number = 777
    get_contract("vrf_coordinator").callBackWithRandomness(
        requestId, random_number, adv_collectible.address, {"from": get_account()}
    )

    # Assert
    print("adv_collectible.tokenCounter() :", adv_collectible.tokenCounter())
    print("adv_collectible.tokenIdToBreed(0) :", adv_collectible.tokenIdToBreed(0))
    assert adv_collectible.tokenCounter() == 0
    assert adv_collectible.tokenIdToBreed(0) == random_number % 3
