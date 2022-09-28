class Player:

    new_team = []


    def __init__(self, players):
        self.name = players["name"]
        self.age = players["age"]
        self.position = players["position"]
        self.team = players["team"]
        Player.new_team.append(self)

    def print_info(self):
        print(self.name)
        return self

    


players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32,
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33,
        "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32,
        "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    },
    {
        "name": "Kyle Mitchell",
        "age": 31,
        "position": "baller",
        "team": "rocket league"
    },
    {
        "name": "Big Dog",
        "age": "immortal",
        "position": "High Wizard",
        "team": "Winners Circle"
    }

]

new_new_team = []
for i in players:
    new_new_team.append(i)




player_kevin = Player(players[0])

player_kevin.print_info()

