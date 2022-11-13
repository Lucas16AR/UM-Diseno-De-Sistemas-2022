from player import Player
from court import Court
from match import Game
from player import Team

def main():
    player1 = Player('Lucas')
    player2 = Player('Gaston')
    player3 = Player('Santiago')
    player4 = Player('Douglas')

    team1 = Team(player1, player2)
    team2 = Team(player3, player4)

    court = Court('Cancha de Padel Numero 10')
    game = Game(court, team1, team2)
    game.play()

if __name__ == "__main__":
    main()