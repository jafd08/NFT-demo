from brownie import network, AdvancedCollectible
from scripts.helpful_scripts import OPENSEA_URL, get_account, get_breed

dog_metadata_dict = {
    "PUG": "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmdryoExpgEQQQgJPoruwGJyZmz6SqV4FRTX1i73CT3iXn?filename=1-SHIBA_INU.json",
    "ST_BERNARD": "https://ipfs.io/ipfs/QmbBnUjyHHN7Ytq9xDsYF9sucZdDJLRkWz7vnZfrjMXMxs?filename=2-ST_BERNARD.json",
}


def main():
    print(" Working on... ", network.show_active())
    adv_collectible = AdvancedCollectible[-1]
    num_of_collectibles = adv_collectible.tokenCounter()
    print(f" You have {num_of_collectibles} tokenIds")
    for token_id in range(num_of_collectibles):
        breed = get_breed(adv_collectible.tokenIdToBreed(token_id))
        if not adv_collectible.tokenURI(token_id).startswith(
            "https://"
        ):  # tokenuri  hasnt been set
            print(" Setting tokenURI of ", token_id)
            set_tokenURI(token_id, adv_collectible, dog_metadata_dict[breed])


def set_tokenURI(token_id, nft_contract, tokenURI):
    acc = get_account()
    tx = nft_contract.setTokenURI(token_id, tokenURI, {"from": acc})
    tx.wait(1)
    print(
        f" Awesome!! You can view your NFT at {OPENSEA_URL.format(nft_contract, token_id)}"
    )
    print(" Please metadata refresh after 20min ")
