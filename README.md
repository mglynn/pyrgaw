# pyrgaw

Python Riot Games API Wrapper

## Usage

Requires a Riot Games API key
    
    import pyrgaw

    API_KEY = 'Your API Key'
    api = pyrgaw.RGA('region', API_KEY)
    

    ----------CHAMPION----------
    # Retrieve all champions
    print(api.get_all_champions())
    print(api.get_all_champions('true'))

    # Retrieves champion by ID
    print(api.get_champion('1'))
    

    ----------GAME----------
    # Get recent games by summoner ID
    print(api.get_recent_games('summoner_id')))
    

    ----------LEAGUE----------
    # Get leagues mapped by summoner ID for a given list of summoner IDs
    print(api.get_summoner_leagues(summoner_ids))

    # Get league entries mapped by summoner ID for a given list of summoner IDs
    print(api.get_summoner_league_entries(summoner_ids))

    # Get leagues mapped by team ID for a given list of team IDs
    print(api.get_team_leagues(team_ids))

    # Get league entries mapped by team ID for a given list of team IDs
    print(api.get_team_league_entries(team_ids))

    # Get challenger tier leagues
    print(api.get_challenger_leagues('queue_type'))
    
    
    ----------STATIC DATA----------
    # Retrieves champion list
    print(api.get_champion_list('locale', 'version', 'data_by_id', 'champ_data'))

    # Retrieves a champion by its id
    print(api.get_champion_static('id', 'locale', 'version', 'champ_data'))

    # Retrieves item list
    print(api.get_item_list('locale', 'version', 'item_list_data'))

    # Retrieves item by its unique id
    print(api.get_item('id', 'locale', 'version', 'item_data'))

    # Retrieves mastery list
    print(api.get_mastery_list('locale', 'version', 'mastery_list_data'))

    # Retrieves mastery item by its unique id
    print(api.get_mastery('id', 'locale', 'version', 'mastery_data'))

    # Retrieves realm data
    print(api.get_realm_list())

    # Retrieves rune list
    print(api.get_rune_list('locale', 'version', 'rune_list_data'))

    # Retrieves rune by its unique id
    print(api.get_rune('id', 'locale', 'version', 'rune_data'))

    # Retrieves summoner spell list
    print(api.get_summoner_spell_list('locale', 'version', 'data_by_id', 'spell_data'))

    # Retrieves summoner spell by its unique id
    print(api.get_summoner_spell('id', 'locale', 'version', 'spell_data'))

    # Retrieve version data
    print(api.get_versions())

    
    ----------STATS----------
    # Get ranked stats by summoner ID
    print(api.get_ranked_stats('summoner_id', 'season'))

    # Get player stats summaries by summoner ID
    print(api.get_player_stats_summaries('summoner_id', 'season'))


    ----------SUMMONER----------
    # Get summoner objects mapped by standardized summoner name for a given list of summoner names
    print(api.get_summoner_by_name('summoner_names'))

    # Get summoner objects mapped by summoner ID for a given list of summoner IDs
    print(api.get_summoner_objects('summoner_ids'))

    # Get mastery pages mapped by summoner ID for a given list of summoner IDs
    print(api.get_mastery_pages('summoner_ids'))

    # Get summoner names mapped by summoner ID for a given list of summoner IDs
    print(api.get_summoner_by_id('summoner_ids'))

    # Get rune pages mapped by summoner ID for a given list of summoner IDs
    print(api.get_rune_pages('summoner_ids'))


    ----------TEAMS----------
    # Get teams mapped by summoner ID for a given list of summoner IDs
    print(api.get_teams('summoner_ids'))

    # Get teams mapped by team ID for a given list of team IDs
    print(api.get_list_of_teams('team_ids'))


This product is not endorsed, certified or otherwise approved in any way by Riot Games, Inc. or any of its affiliates.
