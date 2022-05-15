from scripts.helpful_scripts import get_account
from brownie import SimpleCollectible

sample_token_uri = (
    "ipfs://Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
)
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"


def deploy_and_create():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from": account})
    tx = simple_collectible.createCollectible(sample_token_uri, {"from": account})
    tx.wait(1)
    print(
        " Awesome, you can view your NFT at: ",
        OPENSEA_URL.format(
            simple_collectible.address, simple_collectible.tokenCounter() - 1
        ),
    )  # -1 for the recent deployed one
    print(" Please wait up to 20 mins and hit refresh metadata button ")


def main():
    deploy_and_create()