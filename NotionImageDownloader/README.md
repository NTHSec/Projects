# Notion to GitHub Image Downloader

This project provides a solution for downloading images from Notion and saving them to a local directory, along with their corresponding captions. It includes two scripts: one without additional naming features and another with enhanced naming functionality based on the preceding text.

## Purpose

The purpose of this project is to simplify the process of downloading images and captions from Notion, particularly for users who want to migrate their content to GitHub or other platforms. By automating the image downloading process, users can save time and effort while preserving the structure and context of their content.

## Scripts

### 1. `NIDwithoutCaptions.py`

This script downloads images from Notion and saves them to a specified directory without any additional naming features. Images are named sequentially, such as "Image_1.png", "Image_2.png", and so on.

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

3. Obtain your Notion API token and database ID. Follow the instructions in the `config.py` file to set up your configuration.

4. Run the desired script:

    ```bash
    python NIDwithoutCaptions.py
    ```

    or

    ```bash
    python NIDwithCaptions.py
    ```

5. Follow the on-screen prompts to authenticate with Notion and specify the directory where you want to save the images.

6. Sit back and relax as the script downloads images from Notion and saves them to the specified directory.
