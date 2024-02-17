import os
import requests
import datetime
import re

# Integration token obtained from found in Notion settings
notion_api_token = input("Enter your Notion API token (looks like: secret_4L0t0fCh@r4ct3rS): ")

# Last 32 characters from URL of your Notion page
notion_page_id = input("Enter your page_id you would like to take images from (the 32 characters at the end of a page URL): ")

# File Path
custom_filepath = input("Enter the filepath where you want to save the images: ")

# Headers for the HTTP request
headers = {
    'Authorization': f'Bearer {notion_api_token}',
    'Content-Type': 'application/json',
    'Notion-Version': '2021-05-13',  # Notion API version
}

def download_image(url, folder_path, filename):
    
    # Remove illegal characters from the filename
    filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
    filepath = os.path.join(folder_path, filename)

    # Create directory if it doesn't exist
    os.makedirs(folder_path, exist_ok=True)

    response = requests.get(url)
    with open(filepath, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded: {filename} to {custom_filepath}")


def retrieve_block_children(block_id):
    print("Retrieving blocks (async)...")
    blocks = []

    url = f'https://api.notion.com/v1/blocks/{block_id}/children'
    while url:
        response = requests.get(url, headers=headers)
        data = response.json()
        blocks.extend(data['results'])
        url = data.get('next_cursor')

    # Check for more children (images) within toggled blocks
    for block in blocks:
        if block.get('has_children'):
            blocks.extend(retrieve_block_children(block['id']))

    return blocks

def get_preceding_text(blocks, index):
    if index > 0 and blocks[index - 1]['type'] == 'paragraph':
        text = blocks[index - 1]['paragraph']['text'][0]['plain_text']
        return text.replace('\n', '').strip()  # Remove newline characters and leading/trailing whitespaces
    else:
        return "Untitled"


def main():
    # Make API call to retrieve all block children from the page provided
    blocks = retrieve_block_children(notion_page_id)

    # Download images
    image_folder = 'images_with_preceding_text'
    os.makedirs(image_folder, exist_ok=True)
    for index, block in enumerate(blocks):
        if block['type'] == 'image':
            if block.get('image'):
                image_url = block['image']['file']['url']
                preceding_text = get_preceding_text(blocks, index)
                filename = f"{preceding_text}_{index}.png"
                download_image(image_url, custom_filepath, filename)
            else:
                print("Image block does not contain a URL.")

if __name__ == "__main__":
    main()
