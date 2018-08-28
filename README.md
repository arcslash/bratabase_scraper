# Bratabase Information Scrapper

A simple scrapper to scrape data from the site [bratabase](https://www.bratabase.com/) which is a simple site to solve bra related tasks.Site changes may affect the performance of the script,

The script will generate a folder hierarchy as below,

├── outputs                 
    &nbsp;&nbsp;&nbsp;├── images                    
    &nbsp;&nbsp;&nbsp;├── labels

where label files contains individual entries on the site with a [Json file](https://github.com/isharaux/bratabase_scraper/blob/master/sample.json) in the following format
```
{
    "brand": "Curvy Kate",
    "description": "You may not be able to see it in the photo, but the left cup cuts into breast tissue a little, causing a subtle quad-boob effect.\nIf I look at the end of the wire from the side, I see that the part of the underwire pocket that\"s empty (doesn\"t contain wire) is strained.\nThe back lies horizontally, but there are bulges around the band.\nMy guess is that I need to go up maybe one cup size. Any observations or suggestions?\nThe wires at the center dig into my breast tissue. But I don\"t think this is a sizing issue; my boobs are just very close together.",
    "fit_info": "Fit issues\nCenter gore comfort: Underwires dig into sternum, because they are too high\nStrap separation: Are too far apart\nTop of the cup: Cuts into breast tissue (quad boob effect)\nCups separation: Too separate for my boobs",
    "images": [
        {
            "description": "",
            "location": "outputs/images/n_dhliy/983c2023c2af5d200cb71fbd3489fcb1.jpg"
        },
        {
            "description": "",
            "location": "outputs/images/n_dhliy/c9ab22777725995779d83639d96cb3d6.jpg"
        },
        {
            "description": "",
            "location": "outputs/images/n_dhliy/71e3047aeea9a18389dbb68d8c224187.jpg"
        }
    ],
    "index_size": "28:8",
    "size": "28FF"
}

```

## USEAGE

Install the python dependencies from requirements.txt

```
pip install -r requirements.txt

```


### Running

For development and testing set the variable in scrape.py to

```
type = 'd'
```

And for release,

```
type = 'r'
```
Run scrape.py

```
python scrape.py

```
