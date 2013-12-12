# pyrgaw

Python Riot Games API Wrapper

## Usage

Requires a Riot Games API key
    
    from pyrgaw import RGA

    API_KEY = 'Your API Key'

    api = RGA(API_KEY, 'region')

    # Retrieve all champions
    print(api.get_all_champions('free_to_play'))

    # Get recent games by summoner ID
    print(api.get_recent_games(id))

    # Retrieves leagues data for summoner
    print(api.get_leagues(id))

    # Get players stats summaries by summoner ID
    print(api.get_player_stats_summaries(id, 'season'))

    # Get ranked stats by summoner ID
    print(api.get_ranked_stats(id, 'season'))

    # Get mastery pages by summoner ID
    print(api.get_mastery_pages(id))

    # Get rune pages by summoner ID
    print(api.get_rune_pages(id))

    # Get summoner by name
    print(api.get_summoner_by_name('name'))

    # Get summoner by ID
    print(api.get_summoner_by_id(id))

    # Get list of summoner names by summoner IDs
    print(api.get_list_of_summoner_names(id))

    # Retrieves teams for given summoner ID
    print(api.get_teams(id))
