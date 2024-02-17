# Timeline

These are just my notes from the project. They are pretty funny to look back on, I hope you get a good laugh out of them too!

2/12/24: Day 1

- mapped out, coded, and tested v1 of the project
- Works functionally with hardcoded API Token and page ID.
- Looking to take away hardcoded token and add user functionality in the future.
    - Maybe I don’t need to use an .env file if I’m promoting the user for token and page URL?

2/13/24: Day 2

- Today was primarily focused on adding cool features - didn’t get a lot of time to work out the bigger problems yet
- Had a problem accessing images that were inside of “toggle” blocks.
    - Fixed by updating the retrieve_block_children function to recursively retrieve all children blocks, including those within toggled blocks.
- Scrapped the **get_media_source_text** function due to being able to perform same functionality inside the main() function.
- Since the images in my CTF notes were all screenshots, they had the default name of ‘Untitled.png’. Because of this, only one image was being downloaded after the script ran because they kept overwriting eachother.
    - Initial fix was naming them based on their timestamp. This worked at first for some documents, but did not for others, as I still had a problem with some duplicate timestamps, which lead to duplicate image names, which lead to images being overwritten.
    - The next fix to address this was to simply add another way of identifying images, which was the position of the image in the document.
        - By prefixing each filename with the image's index or position, followed by a unique identifier like a timestamp. This would ensure that each filename is unique and avoids overwriting.
- While dealing with this overwriting issue, I also considered using the images *caption* as an identifier. Not only would this avoid overwriting, but it would also give me easy file names which I could upload to github accordingly.
    - I don’t think this is entirely *necessary*, but it would be a cool feature if I can implement it smoothly.
- Overall, the script works as intended for personal use. However, my API token and page ID are hardcoded, so I will need to figure out a way to either get the .env file working, or perhaps simply prompt the user for their Token and page ID respectively.
    - I think the final product will have 3 prompts:
    1. Enter your Notion API token (looks like: secret_Al0t0fCh$ract3rS): 
    2. Enter your page_id you would like to take images from (the 32 characters at the end of a page URL): 
    3. Enter the location you want this file to be saved (C:\Users\NTHSec\Desktop\CTFS\): 
    - I think I will try and implement the file save location next, shouldn’t be too difficult, and prompting the user for the first two steps is definitely in my area of expertise (shoutout my college python class!)

2/14/2024: Day 3

- Happy valentines day 💕
- Today I implemented prompting the user for information, instead of hardcoding my own.
    - For testing purposes, this was really annoying 😂!
- Also implemented the custom filepath, so I could save images into my dedicated CTF folder on my local machine.
- I was really excited to implement the caption idea from yesterday, but after many tries it simply didn’t work. Though not all hope was lost. Instead of using captions, I simply used the preceding line (the line before the image) as the “caption” and used it in the naming of the image.
    - This personally worked better for me, as I like to organizing my images by what step of the CTF process I am on. For example knowing that an image is an nmap scan speeds up the writeup process immensely for me.
    - One problem I had with this functionality was the accidental illegal characters I used. I like to do the classic ‘And this was my nmap scan: {image}’, and of course my script did NOT like the colon.
        - Fortunately, this was a pretty easy fix, I just had to strip and sanitize all the illegal characters before naming the file.
- At the point where I’m getting ready to publish. Just need to check if the code can be refined or sped up at all, and if there is anything else I want to build before it goes out.

2/17/2024: Final Day

- Everything is in order to upload!
- Found out today that the header version I was using was outdated, and that was probably a source for many of my errors. However, since the core of this application is done with old documentation, I kept the old version, as it still works.
    - I will probably update the code with the most recent version of Notions documentation at a later time if needed.
- I hope you enjoyed my timeline blog thing haha!
