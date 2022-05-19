from metadata import sample_metadata
from brownie import AdvancedCollectible, network
from scripts.helpful_scripts import get_breed
from metadata.sample_metadata import metadata_template
from pathlib import Path
import requests


def main():
    advanced_collectible = AdvancedCollectible[-1]
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(" You have created  ", number_of_advanced_collectibles, "collectibles!")
    for token_id in range(number_of_advanced_collectibles):
        tok_id_breed = advanced_collectible.tokenIdToBreed(token_id)  # returns int
        breed = get_breed(tok_id_breed)  # returns name of breed
        # check if file exists
        metadata_file_name = (
            f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
        )
        collectible_metadata = metadata_template
        if Path(metadata_file_name).exists():
            print(f" {metadata_file_name}  already exists! Delete it to overwrite")
        else:
            print(" Creating metadata file... ")
            print(metadata_file_name)
            collectible_metadata["name"] = breed
            collectible_metadata["description"] = f" An adorable {breed} pup"
            # collectible_metadata[
            #     "image_uri"
            # ] = "??"  # upload to IPFS to know the image URI, the path on the blockchain
            print("collectible_metadata :", collectible_metadata)

            img_path = "./img/" + breed.lower().replace("_", "-") + ".png"
            image_uri = upload_to_ipfs(img_path)


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:  # open read in binary - fp=filepath
        image_binary = fp.read()
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        # "./img/0-PUG.png" -> "0.PUG.png"
        filename = filepath.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        #    "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
        # the json of the NFT
        print("image_uri :", image_uri)
        return image_uri
        # PINATA (alternative)
        # response = request.post(
        #     PINATA_BASE_URL + endpoint,
        #     files={"file": (filename, image_binary)},
        #     heards=headers,
        # )
        # print("response.json :", response.json)