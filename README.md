# pyrgaw

Python Riot Games API Wrapper

## Usage

Requires a Riot Games API key
    
    import pyrgaw

    API_KEY = 'Your API Key'

    rga = pyrgaw.RGA(API_KEY)


    # CHAMPION
    # Retrieve all champions
    print(rga.get_all_champions('region'))
    print(rga.get_all_champions('region', 'true'))

    # Retrieves champion by ID
    print(rga.get_champion('region', '1'))


    # GAME
    # Get recent games by summoner ID
    print(rga.get_recent_games('region', 'summoner_id'))


    # LEAGUE
    # Get leagues mapped by summoner ID for a given list of summoner IDs
    print(rga.get_summoner_leagues('region', summoner_ids))

    # Get league entries mapped by summoner ID for a given list of summoner IDs
    print(rga.get_summoner_league_entries('region', summoner_ids))

    # Get leagues mapped by team ID for a given list of team IDs
    print(rga.get_team_leagues('region', team_ids))

    # Get league entries mapped by team ID for a given list of team IDs
    print(rga.get_team_league_entries('region', team_ids))

    # Get challenger tier leagues
    print(rga.get_challenger_leagues('region', 'queue_type'))
    

    # STATIC DATA
    # Retrieves champion list
    print(rga.get_champion_list('region', 'locale', 'version', 'data_by_id', 'champ_data'))

    # Retrieves a champion by its id
    print(rga.get_champion_static('region', 'id', 'locale', 'version', 'champ_data'))

    # Retrieves item list"
    print(rga.get_item_list('region', 'locale', 'version', 'item_list_data'))

    # Retrieves item by its unique id
    print(rga.get_item('region', 'id', 'locale', 'version', 'item_data'))

    # Retrieves mastery list
    print(rga.get_mastery_list('region', 'locale', 'version', 'mastery_list_data'))

    # Retrieves mastery item by its unique id
    print(rga.get_mastery('region', 'id', 'locale', 'version', 'mastery_data'))

    # Retrieves realm data
    print(rga.get_realm_list('region'))

    # Retrieves rune list
    print(rga.get_rune_list('region', 'locale', 'version', 'rune_list_data'))

    # Retrieves rune by its unique id
    print(rga.get_rune('region', 'id', 'locale', 'version', 'rune_data'))

    # Retrieves summoner spell list
    print(rga.get_summoner_spell_list('region', 'locale', 'version', 'data_by_id', 'spell_data'))

    # Retrieves summoner spell by its unique id
    print(rga.get_summoner_spell('region', 'id', 'locale', 'version', 'spell_data'))

    # Retrieve version data
    print(rga.get_versions('region'))

    
    # STATS
    # Get ranked stats by summoner ID
    print(rga.get_ranked_stats('region', 'summoner_id', 'season'))

    # Get player stats summaries by summoner ID
    print(rga.get_player_stats_summaries('region', 'summoner_id', 'season'))


    # SUMMONER
    # Get summoner objects mapped by standardized summoner name for a given list of summoner names
    print(rga.get_summoner_by_name('region', 'summoner_names'))

    # Get summoner objects mapped by summoner ID for a given list of summoner IDs
    print(rga.get_summoner_objects('region', 'summoner_ids'))

    # Get mastery pages mapped by summoner ID for a given list of summoner IDs
    print(rga.get_mastery_pages('region', 'summoner_ids'))

    # Get summoner names mapped by summoner ID for a given list of summoner IDs
    print(rga.get_summoner_by_id('region', 'summoner_ids'))

    # Get rune pages mapped by summoner ID for a given list of summoner IDs
    print(rga.get_rune_pages('region', 'summoner_ids'))


    # TEAM
    # Get teams mapped by summoner ID for a given list of summoner IDs
    print(rga.get_teams('region' 'summoner_ids'))

    # Get teams mapped by team ID for a given list of team IDs
    print(rga.get_list_of_teams('region', 'team_ids'))


"This product is not endorsed, certified or otherwise approved in any way by Riot Games, Inc. or any of its affiliates."
