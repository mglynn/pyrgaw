import requests


class ResponseException(Exception):
    pass


class RGA():

    def __init__(self, api_key, region):
        self.api_key = api_key
        self.region = region
        self.url_v11 = 'https://prod.api.pvp.net/api/lol/{0}/v1.1'.format(self.region)
        self.url_v12 = 'https://prod.api.pvp.net/api/lol/{0}/v1.2'.format(self.region)
        self.url_v22 = 'https://prod.api.pvp.net/api/lol/{0}/v2.2'.format(self.region)

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
                        404: 'Summoner not found', 500: 'Internal server error'}
        if status in status_codes:
            raise ResponseException(''.join("{0} - {1}".format(status, status_codes[status])))
        else:
            raise ResponseException(status)

    # champion-v1.1 [NA, EUW, EUNE]
    def get_all_champions(self, free_to_play='false'):
        """Retrieve all champions"""
        url = ''.join("{0}/champion?freeToPlay={1}".format(self.url_v11, free_to_play))
        return self.send_request(url)

    # game-v1.2 [NA, EUW, EUNE]
    def get_recent_games(self, id):
        """Get recent games by summoner ID"""
        url = ''.join("{0}/game/by-summoner/{1}/recent?".format(self.url_v12, id))
        return self.send_request(url)

    # league-v2.2 [EUNE, EUW, NA, TR, BR]
    def get_leagues(self, id):
        """Retrieves leagues data for summoner, including leagues for all of the summoner's teams"""
        url = ''.join("{0}/league/by-summoner/{1}?".format(self.url_v22, id))
        return self.send_request(url)

    # stats-v1.2 [EUNE, NA, EUW]
    def get_player_stats_summaries(self, id, season='SEASON4'):
        """Get player stats summaries by summoner ID. One summary is returned per queue type."""
        url = ''.join("{0}/stats/by-summoner/{1}/summary?season={2}&".format(self.url_v12, id, season))
        return self.send_request(url)

    def get_ranked_stats(self, id, season='SEASON4'):
        """Get ranked stats by summoner ID. Includes statistics for Twisted Treeline and Summoner's Rift."""
        url = ''.join("{0}/stats/by-summoner/{1}/ranked?season={2}&".format(self.url_v12, id, season))
        return self.send_request(url)

    # summoner-v1.2 [NA, EUW, EUNE]
    def get_mastery_pages(self, id):
        """Get mastery pages by summoner ID"""
        url = ''.join("{0}/summoner/{1}/masteries?".format(self.url_v12, id))
        return self.send_request(url)

    def get_rune_pages(self, id):
        """Get rune pages by summoner ID"""
        url = ''.join("{0}/summoner/{1}/runes?".format(self.url_v12, id))
        return self.send_request(url)

    def get_summoner_by_name(self, name):
        """Get summoner by name"""
        url = ''.join("{0}/summoner/by-name/{1}?".format(self.url_v12, name))
        return self.send_request(url)

    def get_summoner_by_id(self, id):
        """Get summoner by ID"""
        url = ''.join("{0}/summoner/{1}?".format(self.url_v12, id))
        return self.send_request(url)

    def get_list_of_summoner_names(self, ids):
        """Get list of summoner names by summoner IDs

        Keyword arguments:
        ids - list of summoner name IDs; length <= 40
        """
        url = ''.join("{0}/summoner/{1}/name?".format(self.url_v12, ','.join(ids)))
        return self.send_request(url)

    # team-v2.2 [EUNE, BR, EUW, TR, NA]
    def get_teams(self, id):
        """Retrieves teams for given summoner ID"""
        url = ''.join("{0}/team/by-summoner/{1}?".format(self.url_v22, id))
        return self.send_request(url)
