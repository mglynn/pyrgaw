import requests


class ResponseException(Exception):
    pass


class RGA():
    """A python wrapper class that allows users to access Riot Games API"""

    def __init__(self, region, api_key):
        """Initialize the Riot Games API object"""
        self.region = region
        self.api_key = api_key
        self.endpoints = {'br': 'br.api.pvp.net', 'eune': 'eune.api.pvp.net', 'euw': 'euw.api.pvp.net',
                          'kr': 'kr.api.pvp.net', 'las': 'las.api.pvp.net', 'lan': 'lan.api.pvp.net',
                          'na': 'na.api.pvp.net', 'oce': 'oce.api.pvp.net', 'tr': 'tr.api.pvp.net',
                          'ru': 'ru.api.pvp.net'}
        self.versions = {'champion': '/v1.2/champion', 'game': '/v1.3/game', 'league': '/v2.5/league',
                         'static': '/v1.2', 'match': '/v2.2/match', 'matchhistory': '/v2.2/matchhistory',
                         'stats': '/v1.3/stats', 'summoner': '/v1.4', 'team': '/v2.4/team'}
        self.url = ''.join("https://{}/api/lol/".format(self.endpoints[self.region]))
        self.url_static = 'https://global.api.pvp.net/api/lol/static-data/'
        self.current_season = 'SEASON4'

    # Private functions
    def send_request(self, url):
        """Return json object with a response of OK. Raise an error otherwise"""
        payload = {'api_key': self.api_key}
        r = requests.get(url, params=payload)
        if r.status_code == 200:
            return r.json()
        else:
            return self.get_response_error(r.status_code)

    @staticmethod
    def get_response_error(status):
        """Raise status code exception"""
        status_codes = {400: 'Bad request', 401: 'Unauthorized', 403: 'Forbidden', 404: 'Not found',
                        429: 'Rate limit exceeded', 500: 'Internal server error', 503: 'Service unavailable'}
        if status in status_codes:
            raise ResponseException(''.join("{} - {}".format(status, status_codes[status])))
        else:
            raise ResponseException(status)

    # CHAMPION -- champion-v1.2 [BR, EUNE, EUW, LAN, LAS, NA, OCE]
    def get_all_champions(self, free_to_play='false'):
        """Retrieve all champions"""
        url = ''.join("{}{}{}?freeToPlay={}".format(self.url, self.region, self.versions['champion'], free_to_play))
        return self.send_request(url)

    def get_champion(self, id):
        """Retrieve champion by ID"""
        url = ''.join("{}{}{}/{}?".format(self.url, self.region, self.versions['champion'], id))
        return self.send_request(url)

    # GAME -- game-v1.3 [BR, EUNE, EUW, LAN, LAS, NA, OCE]
    def get_recent_games(self, summoner_id):
        """Get recent games by summoner ID"""
        url = ''.join("{}{}{}/by-summoner/{}/recent?".format(self.url, self.region, self.versions['game'], summoner_id))
        return self.send_request(url)

    # LEAGUE -- league-v2.5 [BR, EUNE, EUW, LAN, LAS, NA, OCE]
    def get_summoner_leagues(self, summoner_ids):
        """Get leagues mapped by summoner ID for a given list of summoner IDs"""
        url = ''.join("{}{}{}/by-summoner/{}?"
                      .format(self.url, self.region, self.versions['league'], ','.join(summoner_ids)))
        return self.send_request(url)

    def get_summoner_league_entries(self, summoner_ids):
        """Get league entries mapped by summoner ID for a given list of summoner IDs"""
        url = ''.join("{}{}{}/by-summoner/{}/entry?"
                      .format(self.url, self.region, self.versions['league'], ','.join(summoner_ids)))
        return self.send_request(url)

    def get_team_leagues(self, team_ids):
        """Get leagues mapped by team ID for a given list of team IDs"""
        url = ''.join("{}{}{}/by-team/{}?".format(self.url, self.region, self.versions['league'], ','.join(team_ids)))
        return self.send_request(url)

    def get_team_league_entries(self, team_ids):
        """Get league entries mapped by team ID for a given list of team IDs"""
        url = ''.join("{}{}{}/by-team/{}/entry?"
                      .format(self.url, self.region, self.versions['league'], ','.join(team_ids)))
        return self.send_request(url)

    def get_challenger_leagues(self, type):
        """Get challenger tier leagues"""
        url = ''.join("{}{}{}/challenger?type={}".format(self.url, self.region, self.versions['league'], type))
        return self.send_request(url)

    # STATIC DATA -- lol-static-data-v1.2 [BR, EUNE, EUW, KR, LAN, LAS, NA, OCE, RU, TR]
    def get_champion_list(self, locale='', version='', data_by_id='', champ_data=''):
        """Retrieves champion list"""
        url = ''.join("{}{}{}/champion?locale={}&version={}&champData={}"
                .format(self.url_static, self.region, self.versions['static'], locale, version, data_by_id, champ_data))
        return self.send_request(url)

    def get_champion_static(self, id, locale='', version='', champ_data=''):
        """Retrieves a champion by its id"""
        url = ''.join("{}{}{}/champion/{}?locale={}&version={}&champData={}"
                .format(self.url_static, self.region, self.versions['static'], id, locale, version, champ_data))
        return self.send_request(url)

    def get_item_list(self, locale='', version='', item_list_data=''):
        """Retrieves item list"""
        url = ''.join("{}{}{}/item?locale={}&version={}&itemListData={}"
                .format(self.url_static, self.region, self.versions['static'], locale, version, item_list_data))
        return self.send_request(url)

    def get_item(self, id, locale='', version='', item_data=''):
        """Retrieves item by its unique id"""
        url = ''.join("{}{}{}/item/{}?locale={}&version={}&itemData{}"
                .format(self.url_static, self.region, self.versions['static'], id, locale, version, item_data))
        return self.send_request(url)

    def get_mastery_list(self, locale='', version='', mastery_list_data=''):
        """Retrieves mastery list"""
        url = ''.join("{}{}{}/mastery?locale={}&version={}&masteryListData={}"
                .format(self.url_static, self.region, self.versions['static'], locale, version, mastery_list_data))
        return self.send_request(url)

    def get_mastery(self, id, locale='', version='', mastery_data=''):
        """Retrieves mastery item by its unique id"""
        url = ''.join("{}{}{}/mastery/{}?locale={}&version={}&masteryData={}"
                .format(self.url_static, self.region, self.versions['static'], id, locale, version, mastery_data))
        return self.send_request(url)

    def get_realm_list(self):
        """Retrieves realm data"""
        url = ''.join("{}{}{}/realm?".format(self.url_static, self.region, self.versions['static']))
        return self.send_request(url)

    def get_rune_list(self, locale='', version='', rune_list_data=''):
        """Retrieves rune list"""
        url = ''.join("{}{}{}/rune?locale={}&version={}&runeListData={}"
                .format(self.url_static, self.region, self.versions['static'], locale, version, rune_list_data))
        return self.send_request(url)

    def get_rune(self, id, locale='', version='', rune_data=''):
        """Retrieves rune by its unique id"""
        url = ''.join("{}{}{}/rune/{}?locale={}&version={}&runeData={}"
                .format(self.url_static, self.region, self.versions['static'], id, locale, version, rune_data))
        return self.send_request(url)

    def get_summoner_spell_list(self, locale='', version='', data_by_id='', spell_data=''):
        """Retrieves summoner spell list"""
        url = ''.join("{}{}{}/summoner-spell?locale={}&version={}&dataById={}&spellData={}"
                .format(self.url_static, self.region, self.versions['static'], locale, version, data_by_id, spell_data))
        return self.send_request(url)

    def get_summoner_spell(self, id, locale='', version='', spell_data=''):
        """Retrieves summoner spell by its unique id"""
        url = ''.join("{}{}{}/summoner-spell/{}?locale={}&version={}&spellData={}"
                .format(self.url_static, self.region, self.versions['static'], id, locale, version, spell_data))
        return self.send_request(url)

    def get_versions(self):
        """Retrieve version data"""
        url = ''.join("{}{}{}/versions?".format(self.url_static, self.region, self.versions['static']))
        return self.send_request(url)

    # STATUS -- lol-status-v1.0 [BR, EUNE, EUW, KR, LAN, LAS, NA, OCE, RU,TR]
    def get_shards(self):
        """Get shard list."""
        url = 'http://status.leagueoflegends.com/shards'
        return self.send_request(url)

    def get_shards_region(self):
        """Get shard status."""
        url = ''.join("{}{}").format('http://status.leagueoflegends.com/shards/', self.region)
        return self.send_request(url)

    # MATCH -- match-v2.2 [BR, EUNE, EUW, KR, LAN, LAS, NA, OCE, PBE, RU, TR]
    def get_match(self, match_id, include_timeline=False):
        """Retrieve match by match ID."""
        url = ''.join("{}{}{}/{}?includeTimeline={}")\
            .format(self.url, self.region, self.versions['match'], match_id, include_timeline)
        return self.send_request(url)

    # MATCH HISTORY -- matchhistory-v2.2 [BR, EUNE, EUW, KR, LAN, LAS, NA, ICE, PBE, RU, TR]
    def get_match_history(self, summoner_id, champion_ids='', ranked_queues='', begin_index='', end_index=''):
        """Retrieve match history by summoner ID."""
        url = ''.join("{}{}{}/{}?championIds={}&rankedQueues={}&beginIndex={}&endIndex={}")\
            .format(self.url, self.region, self.versions['matchhistory'], summoner_id, champion_ids,
                    ranked_queues, begin_index, end_index)
        return self.send_request(url)

    # STATS -- stats-v1.3 [BR, EUNE, EUW, LAN, LAS, NA, OCE]
    def get_ranked_stats(self, summoner_id, season=None):
        """Get ranked stats by summoner ID"""
        if season is None:
            season = self.current_season
        url = ''.join("{}{}{}/by-summoner/{}/ranked?season={}&"
                      .format(self.url, self.region, self.versions['stats'], summoner_id, season))
        return self.send_request(url)

    def get_player_stats_summaries(self, summoner_id, season=None):
        """Get player stats summaries by summoner ID"""
        if season is None:
            season = self.current_season
        url = ''.join("{}{}{}/by-summoner/{}/summary?season={}&"
                      .format(self.url, self.region, self.versions['stats'], summoner_id, season))
        return self.send_request(url)

    # SUMMONER -- summoner-v1.4 [BR, EUNE, EUW, LAN, LAS, NA, OCE]
    def get_summoner_by_name(self, summoner_names):
        """Get summoner objects mapped by standardized summoner name for a given list of summoner names"""
        url = ''.join("{}{}{}/summoner/by-name/{}?"
                      .format(self.url, self.region, self.versions['summoner'], ','.join(summoner_names)))
        return self.send_request(url)

    def get_summoner_objects(self, summoner_ids):
        """Get summoner objects mapped by summoner ID for a given list of summoner IDs"""
        url = ''.join("{}{}{}/summoner/{}"
                      .format(self.url, self.region, self.versions['summoner'], ','.join(summoner_ids)))
        return self.send_request(url)

    def get_mastery_pages(self, summoner_ids):
        """Get mastery pages mapped by summoner ID for a given list of summoner IDs"""
        url = ''.join("{}{}{}/summoner/{}/masteries?"
                      .format(self.url, self.region, self.versions['summoner'], ','.join(summoner_ids)))
        return self.send_request(url)

    def get_summoner_by_id(self, summoner_ids):
        """Get summoner names mapped by summoner ID for a given list of summoner IDs"""
        url = ''.join("{}{}{}/summoner/{}/name?"
                      .format(self.url, self.region, self.versions['summoner'], ','.join(summoner_ids)))
        return self.send_request(url)

    def get_rune_pages(self, summoner_ids):
        """Get rune pages mapped by summoner ID for a given list of summoner IDs"""
        url = ''.join("{}{}{}/summoner/{}/runes?"
                      .format(self.url, self.region, self.versions['summoner'], ','.join(summoner_ids)))
        return self.send_request(url)

    # TEAM -- team-v2.4 [BR, EUNE, EUW, LAN, LAS, NA, OCE]
    def get_teams(self, summoner_ids):
        """Get teams mapped by summoner ID for a given list of summoner IDs"""
        url = ''.join("{}{}{}/by-summoner/{}?"
                      .format(self.url, self.region, self.versions['team'], ','.join(summoner_ids)))
        return self.send_request(url)

    def get_list_of_teams(self, team_ids):
        """Get teams mapped by team ID for a given list of team IDs"""
        url = ''.join("{}{}{}/{}".format(self.url, self.region, self.versions['team'], ','.join(team_ids)))
        return self.send_request(url)
