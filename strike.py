import requests


# Maximum number of hash for the info query
MAX_HASHES = 50

# End points
INFO_ENDPOINT = 'https://getstrike.net/api/v2/torrents/info/'
COUNT_ENDPOINT = 'https://getstrike.net/api/v2/torrents/count/'
SEARCH_ENDPOINT = 'https://getstrike.net/api/v2/torrents/search/'
DESCRIPTION_ENDPOINT = 'https://getstrike.net/api/v2/torrents/descriptions/'
DOWNLOAD_ENDPOINT = 'https://getstrike.net/api/v2/torrents/download/'

# Valid categories and subcategories
VALID_CATEGORIES = {
    'Anime',
    'Applications',
    'Books',
    'Games',
    'Movies',
    'Music',
    'Other',
    'TV',
    'XXX',
}
VALID_SUBCATEGORIES = {
    'Highres Movies',
    'Hentai',
    'HD Video',
    'Handheld',
    'Games',
    'Fiction',
    'English-translated',
    'Ebooks',
    'Dubbed Movies',
    'Documentary',
    'Concerts',
    'Comics',
    'Books',
    'Bollywood',
    'Audio books',
    'Asian',
    'Anime Music Video',
    'Animation',
    'Android',
    'Academic',
    'AAC',
    '3D Movies',
    'XBOX360',
    'Windows',
    'Wii',
    'Wallpapers',
    'Video',
    'Unsorted',
    'UNIX',
    'UltraHD',
    'Tutorials',
    'Transcode',
    'Trailer',
    'Textbooks',
    'Subtitles',
    'Soundtrack',
    'Sound clips',
    'Radio Shows',
    'PSP',
    'PS3',
    'PS2',
    'Poetry',
    'Pictures',
    'PC',
    'Other XXX',
    'Other TV',
    'Other Music',
    'Other Movies',
    'Other Games',
    'Other Books',
    'Other Applications',
    'Other Anime',
    'Non-fiction',
    'Newspapers',
    'Music videos',
    'Mp3',
    'Movie clips',
    'Magazines',
    'Mac',
    'Lossless',
    'Linux',
    'Karaoke',
    'iOS',
}


class TooManyHashes(Exception):
    """
    Exception raised when there was to many hashes in the query.
    """


class UnknownCategory(Exception):
    """
    Exception raised when an unknown category was given.
    """


class UnkownSubcategory(Exception):
    """
    Exception raised when an unknown subcategory was given.
    """


def info(*hashes):
    """
    Return the informations about some torrents based on their hashes.
    """
    if len(hashes) > MAX_HASHES:
        msg = 'The maximum number of hashes is {}'.format(MAX_HASHES)
        raise TooManyHashes(msg)

    r = requests.get(INFO_ENDPOINT, {'hashes': ','.join(hashes)})
    return r.json()


def count():
    """
    Return the number of indexed torrents.
    """
    return requests.get(COUNT_ENDPOINT).json()


def search(query, category=None, subcategory=None):
    """
    Search for a torrent. You can specify the category and the subcategory.
    """
    if category and category not in VALID_CATEGORIES:
        raise UnknownCategory('Unkown category')

    if subcategory and subcategory not in VALID_SUBCATEGORIES:
        raise UnknownSubcategory('Unkown subcategory')

    payload = {'phrase': query}
    if category:
        payload['category'] = category
    if subcategory:
        payload['subcategory'] = subcategory

    return requests.get(SEARCH_ENDPOINT, payload).json()


def description(hash):
    """
    Get a torrent's description (in base 64) based on its hash.
    """
    return requests.get(DESCRIPTION_ENDPOINT, {'hash': hash}).json()


def download_link(hash):
    """
    Get the download link of a torrent file based on its hash.
    """
    return requests.get(DOWNLOAD_ENDPOINT, {'hash': hash}).json()
