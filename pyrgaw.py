import requests


class ResponseException(Exception):
    pass


class RGA():

    def __init__(self, api_key, region):
        self.api_key = api_key
        self.current_season = 'SEASON4'
        self.data_dragon = '4.1.2'
        self.region = region
        self.url_v1 = 'https://prod.api.pvp.net/api/lol/static-data/{0}/v1'.format(self.region)
        self.url_v11 = 'https://prod.api.pvp.net/api/lol/{0}/v1.1'.format(self.region)
        self.url_v12 = 'https://prod.api.pvp.net/api/lol/{0}/v1.2'.format(self.region)
        self.url_v13 = 'https://prod.api.pvp.net/api/lol/{0}/v1.3'.format(self.region)
        self.url_v22 = 'https://prod.api.pvp.net/api/lol/{0}/v2.2'.format(self.region)
        self.url_v23 = 'https://prod.api.pvp.net/api/lol/{0}/v2.3'.format(self.region)

    # Private functions
    def send_request(self, url):
        """Return json object with a response of OK; raise an error otherwise"""
        payload = {'api_key': self.api_key}
        r = requests.get(url, params=payload)
        if r.status_code == 200:
            return r.json()
        else:
            return self.get_response_error(r.status_code)

    @staticmethod
    def get_response_error(status):
        """Raise status code exception"""
        status_codes = {400: 'Bad request', 401: 'Unauthorized',
                        404: 'Summoner not found', 500: 'Internal server error',
                        503: 'Service unavailable'}
        if status in status_codes:
            raise ResponseException(''.join("{0} - {1}".format(status, status_codes[status])))
        else:
            raise ResponseException(status)

    # champion-v1.1 [BR, EUNE, EUW, LAN, LAS, NA, OCE]
    def get_all_champions(self, free_to_play='false'):
        """Retrieve all champions"""
        url = ''.join("{}/champion?freeToPlay={}".format(self.url_v11, free_to_play))
        return self.send_request(url)

    # game-v1.3 [BR, EUNE, EUW, LAN, LAS, NA, OCE]
    def get_recent_games(self, id):
        """Get recent games by summoner ID"""
        url = ''.join("{}/game/by-summoner/{}/recent?".format(self.url_v13, id))
        return self.send_request(url)

    # league-v2.3 [BR, EUNE, EUW, NA, TR]
    def get_challenger_leagues(self, type):
        """Retrieves challenger tier leagues"""
        url = ''.join("{}/league/challenger?type={}".format(self.url_v23, type))
        return self.send_request(url)

    def get_leagues_entry(self, id):
        """Retrieves leagues entry data for summoner, including league entries for all of summoner's teams"""
        url = ''.join("{}/league/by-summoner/{}/entry?".format(self.url_v23, id))
        return self.send_request(url)

    def get_leagues(self, id):
        """Retrieves leagues data for summoner, including leagues for all of the summoner's teams"""
        url = ''.join("{}/league/by-summoner/{}?".format(self.url_v23, id))
        return self.send_request(url)

    # lol-static-data-v1 [BR, EUNE, EUW, KR, LAN, LAS, NA, OCE, RU, TR]
    def get_champion_list(self, locale='', champ_data=''):
        """Retrieves champion list"""
        url = ''.join("{}/champion?locale={}&version={}&champData={}"
            .format(self.url_v1, locale, self.data_dragon, champ_data))
        return self.send_request(url)

    def get_champion(self, id, locale='', champ_data=''):
        """Retrieves a champion by its id"""
        url = ''.join("{}/champion/{}?locale={}&version={}&champData={}"
            .format(self.url_v1, id, locale, self.data_dragon, champ_data))
        return self.send_request(url)

    def get_item(self, id, locale='', item_data=''):
        """Retrieves item by its unique id"""
        url = ''.join("{}/item/{}?locale={}&version={}&itemData{}"
            .format(self.url_v1, id, locale, self.data_dragon, item_data))
        return self.send_request(url)

    def get_item_list(self, locale='', item_list_data=''):
        """Retrieves item list"""
        url = ''.join("{}/item?locale={}&version={}&itemListData={}"
            .format(self.url_v1, locale, self.data_dragon, item_list_data))
        return self.send_request(url)

    def get_mastery(self, id, locale='', mastery_data=''):
        """Retrieves mastery item by its unique id"""
        url = ''.join("{}/mastery/{}?locale={}&version={}&masteryData={}"
            .format(self.url_v1, id, locale, self.data_dragon, mastery_data))
        return self.send_request(url)

    def get_mastery_list(self, locale='', mastery_list_data=''):
        """Retrieves mastery list"""
        url = ''.join("{}/mastery?locale={}&version={}&masteryListData={}"
            .format(self.url_v1, locale, self.data_dragon, mastery_list_data))
        return self.send_request(url)

    def get_realm_list(self):
        """Retrieves realm data"""
        url = ''.join("{}/realm?".format(self.url_v1))
        return self.send_request(url)

    def get_rune(self, id, locale='', rune_data=''):
        """Retrieves rune by its unique id"""
        url = ''.join("{}/rune/{}?locale={}&version={}&runeData={}"
            .format(self.url_v1, id, locale, self.data_dragon, rune_data))
        return self.send_request(url)

    def get_rune_list(self, locale='', rune_list_data=''):
        """Retrieves rune list"""
        url = ''.join("{}/rune?locale={}&version={}&runeListData={}"
            .format(self.url_v1, locale, self.data_dragon, rune_list_data))
        return self.send_request(url)

    def get_summoner_spell(self, id, locale='', spell_data=''):
        """Retrieves summoner spell by its unique id"""
        url = ''.join("{}/summoner-spell/{}?locale={}&version={}&spellData={}"
            .format(self.url_v1, id, locale, self.data_dragon, spell_data))
        return self.send_request(url)

    def get_summoner_spell_list(self, locale='', spell_data=''):
        """Retrieves summoner spell list"""
        url = ''.join("{}/summoner-spell?locale={}&version={}&spellData={}"
            .format(self.url_v1, locale, self.data_dragon, spell_data))
        return self.send_request(url)

    # stats-v1.2 [BR, EUNE, EUW, LAN, LAS, NA, OCE]
    def get_player_stats_summaries(self, id, season=None):
        """Get player stats summaries by summoner ID. One summary is returned per queue type."""
        if season is None:
            season = self.current_season
        url = ''.join("{}/stats/by-summoner/{}/summary?season={}&".format(self.url_v12, id, season))
        return self.send_request(url)

    def get_ranked_stats(self, id, season=None):
        """Get ranked stats by summoner ID. Includes statistics for Twisted Treeline and Summoner's Rift."""
        if season is None:
            season = self.current_season
        url = ''.join("{}/stats/by-summoner/{}/ranked?season={}&".format(self.url_v12, id, season))
        return self.send_request(url)

    # summoner-v1.3 [BR, EUNE, EUW, LAN, LAS, NA, OCE]
    def get_mastery_pages(self, ids):
        """Get mastery pages mapped by summoner ID for a given list of summoner IDs"""
        url = ''.join("{}/summoner/{}/masteries?".format(self.url_v13, ','.join(ids)))
        return self.send_request(url)

    def get_rune_pages(self, ids):
        """Get rune pages mapped by summoner ID for a given list of summoner IDs"""
        url = ''.join("{}/summoner/{}/runes?".format(self.url_v13, ','.join(ids)))
        return self.send_request(url)

    def get_summoner_by_name(self, names):
        """Get summoner objects mapped by standardized summoner name for \
           a given list of summoner names of standardized summoner names"""
        url = ''.join("{}/summoner/by-name/{}?".format(self.url_v13, ','.join(names)))
        return self.send_request(url)

    def get_summoner_by_id(self, ids):
        """Get summoner names mapped by summoner ID for a given list of summoner IDs"""
        url = ''.join("{}/summoner/{}/name?".format(self.url_v13, ','.join(ids)))
        return self.send_request(url)

    def get_summoner_objects(self, ids):
        """Get summoner objects mapped by summoner ID for a given list of summoner IDs"""
        url = ''.join("{}/summoner/{}".format(self.url_v13, ','.join(ids)))
        return self.send_request(url)

    # team-v2.2 [BR, EUNE, EUW, NA, TR]
    def get_teams(self, id):
        """Retrieves teams for given summoner ID"""
        url = ''.join("{}/team/by-summoner/{}?".format(self.url_v22, id))
        return self.send_request(url)

    def get_list_of_teams(self, ids):
        """Get teams mapped by team ID for a given list of team IDs"""
        url = ''.join("{}/team/{}".format(self.url_v22, ids))
        return self.send_request(url)
