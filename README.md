# Bratabase Information Scrapper

A simple scrapper to scrape data from the site [bratabase](https://www.bratabase.com/) which is a simple site to solve bra related tasks.Site changes may affect the performance of the script,

The script will generate a folder hierarchy as below,

├── outputs                 
    &nbsp;&nbsp;&nbsp;├── images                    
    &nbsp;&nbsp;&nbsp;├── labels

where label files contains individual entries on the site with a [Json file](https://github.com/isharaux/bratabase_scraper/blob/master/sample.json) in the following format
```
{
  images:[
  {
    location:"images/image1.jpg",
    description:"description"
  },
  {
    location:"images/image2.jpg",
    description:"description"
  },
  {
    location:"images/image3.jpg",
    description:"description"
  }
],
  fit_info:""
  description:"super description",
  brand:"bla bla",
  size:"type of this bra",
  index_size:"type of this bra",

}

```

** USEAGE

Install the python dependencies from requirements.txt

```
pip install -r requirements.txt

```

Run scrape.py

```
python scrape.py

```
