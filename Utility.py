from collections import defaultdict


def get_current_rune_page(rune_pages):
    """Get the current active runepage"""
    for page in rune_pages['pages']:
        if page['current']:
            return page


def get_current_rune_page_runes(page):
    """Get the current active rune names and count"""
    d = defaultdict(int)
    for slot in page['slots']:
        d[slot['rune']['name']] += 1
    return str(dict(d))


def get_current_mastery_page(mastery_pages):
    """Get the current active mastery page"""
    for page in mastery_pages['pages']:
        if page['current']:
            return page


def get_current_mastery_page_points(page):
    """Get the point allocation for the current active mastery page"""
    offense, defense, utility = 0, 0, 0
    for talent in page['talents']:
        if talent['id'] < 4200:
            offense += talent['rank']
        elif 4200 < talent['id'] < 4300:
            defense += talent['rank']
        else:
            utility += talent['rank']
    return ''.join("{0}/{1}/{2}".format(offense, defense, utility))