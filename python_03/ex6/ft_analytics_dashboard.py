from typing import Dict, List, Any

players: Dict[str, Dict[str, Any]] = {
    'alice': {
        'level': 41,
        'total_score': 2824,
        'sessions_played': 13,
        'favorite_mode': 'ranked',
        'achievements_count': 5,
    },
    'bob': {
        'level': 16,
        'total_score': 4657,
        'sessions_played': 27,
        'favorite_mode': 'ranked',
        'achievements_count': 2,
    },
    'charlie': {
        'level': 44,
        'total_score': 9935,
        'sessions_played': 21,
        'favorite_mode': 'ranked',
        'achievements_count': 7,
    },
    'diana': {
        'level': 3,
        'total_score': 1488,
        'sessions_played': 21,
        'favorite_mode': 'casual',
        'achievements_count': 4,
    },
    'eve': {
        'level': 33,
        'total_score': 1434,
        'sessions_played': 81,
        'favorite_mode': 'casual',
        'achievements_count': 7,
    },
    'frank': {
        'level': 15,
        'total_score': 8359,
        'sessions_played': 85,
        'favorite_mode': 'competitive',
        'achievements_count': 1,
    },
}

sessions: List[Dict[str, Any]] = [
    {'player': 'bob',     'score': 1831, 'mode': 'competitive',
     'completed': False, 'country': 'France'},
    {'player': 'bob',     'score': 1478, 'mode': 'casual',
     'completed': True,  'country': 'Germany'},
    {'player': 'diana',   'score': 1570, 'mode': 'competitive',
     'completed': False, 'country': 'Brazil'},
    {'player': 'alice',   'score': 1981, 'mode': 'ranked',
     'completed': True,  'country': 'France'},
    {'player': 'diana',   'score': 2361, 'mode': 'competitive',
     'completed': False, 'country': 'Japan'},
    {'player': 'eve',     'score': 2985, 'mode': 'casual',
     'completed': True,  'country': 'Germany'},
    {'player': 'frank',   'score': 1285, 'mode': 'casual',
     'completed': True,  'country': 'Brazil'},
    {'player': 'alice',   'score': 1238, 'mode': 'competitive',
     'completed': False, 'country': 'Japan'},
    {'player': 'frank',   'score': 2754, 'mode': 'casual',
     'completed': True,  'country': 'France'},
    {'player': 'charlie', 'score': 1196, 'mode': 'casual',
     'completed': True,  'country': 'Germany'},
]

achievements: List[str] = [
    'first_blood', 'level_master', 'speed_runner', 'treasure_seeker',
    'boss_hunter', 'pixel_perfect', 'combo_king', 'explorer',
]


def categorize(score: int) -> str:
    if score > 2000:
        return 'high'
    elif score >= 1500:
        return 'medium'
    else:
        return 'low'


def list_comprehension_examples() -> None:
    print("=== List Comprehension Examples ===")
    high_scores = [
        player for player in players
        if players[player]['total_score'] > 2000
    ]
    scores_doubled = [
        data['total_score'] * 2
        for _, data in players.items()
    ]
    active_players = [
        session['player']
        for session in sessions
        if session['completed']
    ]
    print(f"High scorers (>2000): {high_scores}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_players}")


def dict_comprehension_examples() -> None:
    print("=== Dict Comprehension Examples ===")
    player_scores = {
        name: data['total_score']
        for name, data in players.items()
    }
    score_categories = {
        category: sum(
            1 for s in sessions if categorize(s['score']) == category
        )
        for category in ['high', 'medium', 'low']
    }
    achievement_counts = {
        name: data['achievements_count']
        for name, data in players.items()
    }
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievement_counts}")


def set_comprehension_examples() -> None:
    print("=== Set Comprehension Examples ===")
    unique_players = {session['player'] for session in sessions}
    unique_achievements = {achievement for achievement in achievements}
    active_countries = {session['country'] for session in sessions}
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active countries: {active_countries}")


def combined_analysis() -> None:
    print("=== Combined Analysis ===")
    total_players = len(players)
    total_unique_achievements = len({a for a in achievements})
    average_score = (
        sum(data['total_score'] for _, data in players.items()) / len(players)
    )
    top_performer = max(players, key=lambda name: players[name]['total_score'])
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {average_score:.2f}")
    print(
        f"Top performer: {top_performer} "
        f"({players[top_performer]['total_score']} points, "
        f"{players[top_performer]['achievements_count']} achievements)"
    )


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")
    list_comprehension_examples()
    dict_comprehension_examples()
    set_comprehension_examples()
    combined_analysis()
