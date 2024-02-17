# Notion to GitHub Image Downloader

This project provides a solution for downloading images from Notion and saving them to a local directory, along with their corresponding captions. It includes two scripts: one without additional naming features and another with enhanced naming functionality based on the preceding text.

## Purpose

The purpose of this project is to simplify the process of downloading images and captions from Notion, particularly for users who want to migrate their content to GitHub or other platforms. By automating the image downloading process, users can save time and effort while preserving the structure and context of their content.

## Scripts

### 1. `NIDwithoutCaptions.py`

This script downloads images from Notion and saves them to a specified directory without any additional naming features. Images are named sequentially based on the index (or position) of the image on the page. The filenames will look like "Image_1.png", "Image_2.png", and so on.

### 2. `NIDwithCaptions.py`

This script extends the functionality of the previous script by including enhanced naming features. It retrieves the text preceding each image block in Notion and uses it to name the corresponding image file. This allows for more descriptive filenames based on the context provided by the preceding text.

## Quick Start Guide

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/notion-to-github.git
    ```

2. Install any necessary dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Obtain your Notion API token:
   - You can get your API Token by navigating to your [Notion integrations page](https://www.notion.so/my-integrations).
   - Click "New Integration"
   - Copy your API token (looks like `secret_BlAhBlahblah123`)
   - If you get stuck refer to this [article](https://developers.notion.com/docs/authorization#:~:text=Click%20the%20New%20integration%20button,to%20authenticate%20REST%20API%20requests.)

4. Obtain your desired Notion page ID (from the page that you're downloading images from):
   - This is the 32 characters at the end of the page URL

    ![2024-02-17 17_58_02-SamplePage](https://github.com/NTHSec/Projects/assets/150489159/41231696-302a-4512-8c18-8adf38bcc976)

5. Connect your integration to the desired page:
    - On the top right of your Notion document, select the three dots ••• 
    - Scroll down to `Add connections`, and use the search bar to find and select the integration from the dropdown list.
      
    ![Connection](https://github.com/NTHSec/Projects/assets/150489159/5fb9abde-f0bc-4031-b35e-5e121fed0e69)

    - If you get stuck, look [here!](https://developers.notion.com/docs/authorization#integration-permissions)

6. Run the desired script and follow the prompts.:

    ```bash
    python NIDwithoutCaptions.py
    ```

    The ouput should look like:

    ![NIDwithoutcaption](https://github.com/NTHSec/Projects/assets/150489159/7e9438e5-537b-4d59-9224-7059023c75f1)


    or

    ```bash
    python NIDwithCaptions.py
    ```

    The output should look like:

    ![NIDwithcaption](https://github.com/NTHSec/Projects/assets/150489159/5349fac0-f0d0-4365-b290-39224f14b48c)


7. Make sure to copy paste for the prompts! This will allow Notion to authenticate properly and specify the directory where you want to save the images.

8. Sit back and relax as the script downloads images from Notion and saves them to the specified directory.


*Note: This code was made using an older version of Notion's API version due to many errors I faced. The script still works as intended, but it is good to keep in mind that if you want to adjust the code you will have to refer to older Notion documentation.*  
