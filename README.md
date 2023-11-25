# ArXiv Paper Scraper

## Overview
This tool streamlines the process of downloading computer vision research papers from arXiv, making it more convenient for researchers, academics, and students.

## Usage

Run the scraper with the desired keywords and the number of papers to download:

`python parseArxiv.py [keywords] --show [number]`

### Example

To download papers related to diffusion in pastweek:

`python parseArxiv.py diffusion --show 100`

This will search 100 recent papers on arxiv, and download the papers related to "diffusion" into the ./papers directory.

### Advanced Usage: Multiple Keywords

You can also search using multiple keywords. Simply include each keyword separated by spaces. For instance, to search for papers related to both "transformer" and "diffusion":

```bash
python parseArxiv.py "transformer" "diffusion" --show 100
```


## Notes
- Ensure you have the necessary permissions and comply with arXiv's terms of service.
- Be mindful of the keywords you set. Typos or overly specific keywords (e.g., misspelling 'diffusion' as 'difffusion') may lead to no results.
- The number of papers specified by `--show` should be within reasonable limits to avoid overloading the server.

## Customizing the Search Topic

The default script configuration searches within the Computer Vision (cs.CV) category on arXiv. To search in a different category, you need to change the `cs.CV` part of the URL in the script.

For example, for searching in the category of Artificial Intelligence, modify the URL as follows:

```python
url = f'https://arxiv.org/list/cs.AI/pastweek?show={args.show}'


