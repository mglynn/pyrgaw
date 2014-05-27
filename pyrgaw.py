import requests


class ResponseException(Exception):
    pass


class RGA():

    def __init__(self, api_key):
        self.api_key = api_key
        self.current_season = 'SEASON4'
        self.url = 'https://prod.api.pvp.net/api/lol/'
        self.url_static = 'https://prod.api.pvp.net/api/lol/static-data/'
        self.versions = {'champion': '/v1.2/champion', 'game': '/v1.3/game', 'league': '/v2.4/league',
                         'static': '/v1.2', 'stats': '/v1.3/stats', 'summoner': '/v1.4', 'team': '/v2.3/team'}

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
        status_codes = {400: 'Bad request', 401: 'Unauthorized', 404: 'Not found',
                        429: 'Rate limit exceeded', 500: 'Internal server error', 503: 'Service unavailable'}
        if status in status_codes:
            raise ResponseException(''.join("{} - {}".format(status, status_codes[status])))
        else:
            raise ResponseException(status)

    # CHAMPION -- champion-v1.2 [BR, EUNE, EUW, LAN, LAS, NA, OCE]
    def get_all_champions(self, region, free_to_play='false'):
        """Retrieve all champions"""
        url = ''.join("{}{}{}?freeToPlay={}".format(self.url, region, self.versions['champion'], free_to_play))
        return self.send_request(url)

    def get_champion(self, region, id):
        """Retrieve champion by ID"""
        url = ''.join("{}{}{}/{}?".format(self.url, region, self.versions['champion'], id))
        return self.send_request(url)

    # GAME -- game-v1.3 [BR, EUNE, EUW, LAN, LAS, NA, OCE]
    def get_recent_games(self, region, summoner_id):
        """Get recent games by summoner ID"""
        url = ''.join("{}{}{}/by-summoner/{}/recent?".format(self.url, region, self.versions['game'], summoner_id))
        return self.send_request(url)

    # LEAGUE -- league-v2.4 [BR, EUNE, EUW, LAN, LAS, NA, OCE]
    def get_summoner_leagues(self, region, summoner_ids):
        """Get leagues mapped by summoner ID for a given list of summoner IDs"""
        url = ''.join("{}{}{}/by-summoner/{}?"
                      .format(self.url, region, self.versions['league'], ','.join(summoner_ids)))
        return self.send_request(url)

    def get_summoner_league_entries(self, region, summoner_ids):
        """Get league entries mapped by summoner ID for a given list of summoner IDs"""
        url = ''.join("{}{}{}/by-summoner/{}/entry?"
                      .format(self.url, region, self.versions['league'], ','.join(summoner_ids)))
        return self.send_request(url)

    def get_team_leagues(self, region, team_ids):
        """Get leagues mapped by team ID for a given list of team IDs"""
        url = ''.join("{}{}{}/by-team/{}?".format(self.url, region, self.versions['league'], ','.join(team_ids)))
        return self.send_request(url)

    def get_team_league_entries(self, region, team_ids):
        """Get league entries mapped by team ID for a given list of team IDs"""
        url = ''.join("{}{}{}/by-team/{}/entry?".format(self.url, region, self.versions['league'], ','.join(team_ids)))
        return self.send_request(url)

    def get_challenger_leagues(self, region, type):
        """Get challenger tier leagues"""
        url = ''.join("{}{}{}/challenger?type={}".format(self.url, region, self.versions['league'], type))
        return self.send_request(url)

    # STATIC DATA -- lol-static-data-v1.2 [BR, EUNE, EUW, KR, LAN, LAS, NA, OCE, RU, TR]
    def get_champion_list(self, region, locale='', version='', data_by_id='', champ_data=''):
        """Retrieves champion list"""
        url = ''.join("{}{}{}/champion?locale={}&version={}&champData={}"
                .format(self.url_static, region, self.versions['static'], locale, version, data_by_id, champ_data))
        return self.send_request(url)

    def get_champion_static(self, region, id, locale='', version='', champ_data=''):
        """Retrieves a champion by its id"""
        url = ''.join("{}{}{}/champion/{}?locale={}&version={}&champData={}"
                .format(self.url_static, region, self.versions['static'], id, locale, version, champ_data))
        return self.send_request(url)

    def get_item_list(self, region, locale='', version='', item_list_data=''):
        """Retrieves item list"""
        url = ''.join("{}{}{}/item?locale={}&version={}&itemListData={}"
                .format(self.url_static, region, self.versions['static'], locale, version, item_list_data))
        return self.send_request(url)

    def get_item(self, region, id, locale='', version='', item_data=''):
        """Retrieves item by its unique id"""
        url = ''.join("{}{}{}/item/{}?locale={}&version={}&itemData{}"
                .format(self.url_static, region, self.versions['static'], id, locale, version, item_data))
        return self.send_request(url)

    def get_mastery_list(self, region, locale='', version='', mastery_list_data=''):
        """Retrieves mastery list"""
        url = ''.join("{}{}{}/mastery?locale={}&version={}&masteryListData={}"
                .format(self.url_static, region, self.versions['static'], locale, version, mastery_list_data))
        return self.send_request(url)

    def get_mastery(self, region, id, locale='', version='', mastery_data=''):
        """Retrieves mastery item by its unique id"""
        url = ''.join("{}{}{}/mastery/{}?locale={}&version={}&masteryData={}"
                .format(self.url_static, region, self.versions['static'], id, locale, version, mastery_data))
        return self.send_request(url)

    def get_realm_list(self, region):
        """Retrieves realm data"""
        url = ''.join("{}{}{}/realm?".format(self.url_static, region, self.versions['static']))
        return self.send_request(url)

    def get_rune_list(self, region, locale='', version='', rune_list_data=''):
        """Retrieves rune list"""
        url = ''.join("{}{}{}/rune?locale={}&version={}&runeListData={}"
                .format(self.url_static, region, self.versions['static'], locale, version, rune_list_data))
        return self.send_request(url)

    def get_rune(self, region, id, locale='', version='', rune_data=''):
        """Retrieves rune by its unique id"""
        url = ''.join("{}{}{}/rune/{}?locale={}&version={}&runeData={}"
                .format(self.url_static, region, self.versions['static'], id, locale, version, rune_data))
        return self.send_request(url)

    def get_summoner_spell_list(self, region, locale='', version='', data_by_id='', spell_data=''):
        """Retrieves summoner spell list"""
        url = ''.join("{}{}{}/summoner-spell?locale={}&version={}&dataById={}&spellData={}"
                .format(self.url_static, region, self.versions['static'], locale, version, data_by_id, spell_data))
        return self.send_request(url)

    def get_summoner_spell(self, region, id, locale='', version='', spell_data=''):
        """Retrieves summoner spell by its unique id"""
        url = ''.join("{}{}{}/summoner-spell/{}?locale={}&version={}&spellData={}"
                .format(self.url_static, region, self.versions['static'], id, locale, version, spell_data))
        return self.send_request(url)

    def get_versions(self, region):
        """Retrieve version data"""
        url = ''.join("{}{}{}/versions?".format(self.url_static, region, self.versions['static']))
        return self.send_request(url)

    # STATS -- stats-v1.3 [BR, EUNE, EUW, LAN, LAS, NA, OCE]
    def get_ranked_stats(self, region, summoner_id, season=None):
        """Get ranked stats by summoner ID"""
        if season is None:
            season = self.current_season
        url = ''.join("{}{}{}/by-summoner/{}/ranked?season={}&"
                      .format(self.url, region, self.versions['stats'], summoner_id, season))
        return self.send_request(url)

    def get_player_stats_summaries(self, region, summoner_id, season=None):
        """Get player stats summaries by summoner ID"""
        if season is None:
            season = self.current_season
        url = ''.join("{}{}{}/by-summoner/{}/summary?season={}&"
                      .format(self.url, region, self.versions['stats'], summoner_id, season))
        return self.send_request(url)

    # SUMMONER -- summoner-v1.4 [BR, EUNE, EUW, LAN, LAS, NA, OCE]
    def get_summoner_by_name(self, region, summoner_names):
        """Get summoner objects mapped by standardized summoner name for a given list of summoner names"""
        url = ''.join("{}{}{}/summoner/by-name/{}?"
                      .format(self.url, region, self.versions['summoner'], ','.join(summoner_names)))
        return self.send_request(url)

    def get_summoner_objects(self, region, summoner_ids):
        """Get summoner objects mapped by summoner ID for a given list of summoner IDs"""
        url = ''.join("{}{}{}/summoner/{}".format(self.url, region, self.versions['summoner'], ','.join(summoner_ids)))
        return self.send_request(url)

    def get_mastery_pages(self, region, summoner_ids):
        """Get mastery pages mapped by summoner ID for a given list of summoner IDs"""
        url = ''.join("{}{}{}/summoner/{}/masteries?"
                      .format(self.url, region, self.versions['summoner'], ','.join(summoner_ids)))
        return self.send_request(url)

    def get_summoner_by_id(self, region, summoner_ids):
        """Get summoner names mapped by summoner ID for a given list of summoner IDs"""
        url = ''.join("{}{}{}/summoner/{}/name?"
                      .format(self.url, region, self.versions['summoner'], ','.join(summoner_ids)))
        return self.send_request(url)

    def get_rune_pages(self, region, summoner_ids):
        """Get rune pages mapped by summoner ID for a given list of summoner IDs"""
        url = ''.join("{}{}{}/summoner/{}/runes?"
                      .format(self.url, region, self.versions['summoner'], ','.join(summoner_ids)))
        return self.send_request(url)

    # TEAM -- team-v2.3 [BR, EUNE, EUW, LAN, LAS, NA, OCE]
    def get_teams(self, region, summoner_ids):
        """Get teams mapped by summoner ID for a given list of summoner IDs"""
        url = ''.join("{}{}{}/by-summoner/{}?".format(self.url, region, self.versions['team'], ','.join(summoner_ids)))
        return self.send_request(url)

    def get_list_of_teams(self, region, team_ids):
        """Get teams mapped by team ID for a given list of team IDs"""
        url = ''.join("{}{}{}/{}".format(self.url, region, self.versions['team'], ','.join(team_ids)))
        return self.send_request(url)
