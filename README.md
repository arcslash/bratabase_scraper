# Bratabase Information Scrapper

A simple scrapper to scrape data from the site [bratabase](https://www.bratabase.com/) which is a simple site to solve bra related tasks.Site changes may affect the performance of the script,

The script will generate a folder hierarchy as below,

├── outputs                 
    &nbsp;&nbsp;&nbsp;├── images                    
    &nbsp;&nbsp;&nbsp;├── labels

where label files contain individual entries on the site with a [Json file](https://github.com/isharaux/bratabase_scraper/blob/master/sample.json) in the following format
```
{
    "brand": "Panache",
    "description": "There is wrinkling along the bottom and outer edges of the cups, the gore does not fully tack (it may be resting on my breast tissue?), and there is the slightest of quadding in the upper lace part of the cups. Other than these issues, this bra is comfortable.\nI have tried the 32G, but the wrinkling along the bottom and edges were even more apparent; however, the gore did tack. I do not have any other bras to use as a reference, unfortunately.\nI am an even 2/5 when properly supported and believe I\"m projected. I also have prominent \"puffy\" nipples that get squished when I\"m wearing bras, so when I measured, I gently squished them down with the cloth measuring tape.\nWhat does this fit say about my breast shape? Did I just pick the wrong size? I would love advice and suggestions!",
    "fit_info": "Fit issues\nCenter gore placement: Doesn\"t lie flat against sternum\nTop of the cup: Cuts into breast tissue (quad boob effect)\nCup\"s width: There is empty fabric on the sides (Cup too wide)",
    "images": [
        {
            "description": "",
            "location": "outputs/images/n_dizo7/ab58210404dccbaafc5dd1bc37b28bcb.jpg"
        },
        {
            "description": "",
            "location": "outputs/images/n_dizo7/0df6aee644d6b57f57b3a3eae82aad63.jpg"
        },
        {
            "description": "Slight wrinkling along the outer edges.",
            "location": "outputs/images/n_dizo7/e72f6cd474232e197e845aa6eab14f3b.jpg"
        },
        {
            "description": "Notice the wrinkling above the wire.",
            "location": "outputs/images/n_dizo7/00e05043048336b69a43224b0814eb90.jpg"
        },
        {
            "description": "Gore does not completely tack.",
            "location": "outputs/images/n_dizo7/329cc9e3a608d26bed52d8a7945f8606.jpg"
        },
        {
            "description": "",
            "location": "outputs/images/n_dizo7/a89333f558124b418b5cf5c6cf9bc119.jpg"
        }
    ],
    "index_size": "32:8",
    "model": "Envy Balconnet Bra (7285)",
    "size": "32FF"
}

```

## USEAGE

Install python dependencies from requirements.txt

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
