# Auto join cs2 giveaway

Auto join items giveaways on Steam. Currently available for sites: [Skinsmonkey](https://skinsmonkey.com/free-csgo-skins), [MannCo](https://mannco.store/)

## Requisites

Makefile

Python 3.8 or later versions

Run command to install required Python libraries

`pip install -r requirements.txt`

## Usage

### Console

Login to your giveaway sites. Use Inspector->Network to get your cookies. Create a **.env** file in the same folder, fill in as the image below, Twitter token is to join with your twitter url.

![.env](img/Capture.PNG)

`
    make
`

or

`make + [giveaways command]` in **Makefile** to run one by one website

### Website

`make web` to build a website UI and update tokens in your own machine at localhost:5000

## Notes

`timezone` in **Makefile** is to sync your system time settings for Windows, run with admin privilege for this command.
