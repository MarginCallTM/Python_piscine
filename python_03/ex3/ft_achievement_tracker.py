class AchievementHunter:

    def __init__(self):
        self.players = {
            "alice": {
                'first_kill',
                'level_10',
                'treasure_hunter',
                'speed_demon'},
            "bob": {
                'first_kill',
                'level_10',
                'boss_slayer',
                'collector'},
            "charlie": {
                'level_10',
                'treasure_hunter',
                'boss_slayer',
                'speed_demon',
                'perfectionist'}}

    def display_achievements(self):
        for name, achievements in self.players.items():
            print(f"Player {name} achievements: {achievements}")

    def all_unique_achievements(self):
        all_achievements = set()
        for achievement in self.players.values():
            all_achievements = all_achievements | achievement
        print(f"All unique achievements: {all_achievements}")
        print(f"Total unique achievements: {len(all_achievements)}\n")

    def common_to_all(self):
        all_achievements = set.union(*self.players.values())
        for achievement in self.players.values():
            all_achievements = all_achievements & achievement
        print(f"Common to all players: {all_achievements}")

    def rare_achievements(self):
        all_achievements = set.union(*self.players.values())
        rare = set()
        for achievement in all_achievements:
            count = 0
            for player_achievements in self.players.values():
                if achievement in player_achievements:
                    count += 1
            if count == 1:
                rare.add(achievement)

        print(f"Rare achievements (1 player): {rare}\n")

    def compare_two_players(self, player1, player2):
        if player1 not in self.players:
            print(f"Error: '{player1}' is not a valid key")
            return
        if player2 not in self.players:
            print(f"Error: '{player2}' is not a valid key")
            return
        set1 = self.players[player1]
        set2 = self.players[player2]

        common = set1 & set2

        print(f"{player1} vs {player2} common: {common}\n")

    def unique_to_player(self, player1, player2):
        if player1 not in self.players:
            print(f"Error '{player1}' is not a valid key")
            return
        if player2 not in self.players:
            print(f"Error '{player2}' is not a valide key")
            return
        unique = self.players[player1] - self.players[player2]
        print(f"{player1} unique: {unique}")


if __name__ == "__main__":

    print("=== Achievement Tracker System ===\n")
    trophy = AchievementHunter()
    trophy.display_achievements()

    print("\n=== Achievement Analytics ===\n")
    trophy.all_unique_achievements()

    trophy.common_to_all()
    trophy.rare_achievements()

    trophy.compare_two_players("alice", "bob")
    trophy.unique_to_player("alice", "bob")
    trophy.unique_to_player("bob", "alice")
