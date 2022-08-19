from random import randint
from enum import Enum, auto


class Match():
    def __init__(self, player_0, player_1):
        self.players = (player_0, player_1)
        self.in_game = False

    def max_speed_of_player(self, monsters):
        max_list = []
        max = None
        for i in range(len(monsters)) :
            if not (monsters[i].isKO == True or monsters[i].charging == True or monster[i].hasAttacked == True):
                if max == None:
                    max = monsters[i].get_stat[Stats.Speed]
                    max_list = [i]
                elif monsters[i].get_stat[Stats.Speed] > monsters[max].get_stats[Stats.Speed]:
                    max = monsters[i].get_stat[Stats.Speed]
                    max_list = [i]
                elif monsters[i].get_stat[Stats.Speed] == monsters[max].get_stats[Stats.Speed]:
                    max_list.append(i)
        if max == None:
            return None
        else :
            return max_list[randint(range(len(max_list)))]

    def max_speed_monster(self):
        max = [None, None]
        if self.players[0].number_of_attacks < 3:
            max[0] = self.max_speed_of_player(self.players[0].monsters_on_ground)
        if self.players[1].number_of_attacks < 3:
            max[1] = self.max_speed_player(self.players[1].monsters_on_ground)
        if max[0] == None:
            if (max[1] == None):
                return None
            else:
                return (1, max[1])
        elif (max[1] == None):
            return (0, max[0])
        elif max[0] > max[1]:
            return (0, max[0])
        elif max[1] > max[0]:
            return (0, max[0])
        else:
            i = randint(range(2))
            return(i, max[i])

class Monster():
    def __init__(self, type, individual_values, level = 1):
        self.type = type
        self.level = level
        self.individual_values = individual_values

    def get_stat(self, stat):
        if stat == Stats.moving
            return self.type.base_stat[stat]
        return self.type.base_stat[stat] + self.individual_values[stat]


class Ingame_Monster():
    def __init__(self, monster):
        self.monster = monster
        self.actual_HP = monster.get_stat[HP]
        self.actual_moving = 0
        self.isKO = False
        self.charging = False
        self.charge_percentage = 0
        self.hasAttacked = False

class Player():
    def __init__(self, monsters_on_ground, monsters_positions, monsters_on_reserve):
        playground = Playground(monsters_positions)

        self.monsters_on_ground = monsters_on_ground
        self.monsters_positions = monsters_positions
        self.monsters_on_reserve = monsters_on_reserve
        self.number_of_attacks = 0

    def exchange_monster(self, monster_on_reserve_number, monster_on_ground_number):
        m = self.monster_on_reserve[monster_on_reserve_number]
        self.monster_on_reserve[monster_on_reserve_number] = self.monster_on_ground[monster_on_ground_number]
        self.monster_on_ground[monster_on_ground_number] = m

    def swap_monster(self, monster_on_reserve_number, monster_on_ground_number):
        m = self.monster_on_reserve[monster_on_reserve_number]
        if m.actual_moving > 0:
            return False
        self.monster_on_ground[monster_on_ground_number].actual_moving = monster.get_stat[Stats.Moving]
        self.monster_on_reserve[monster_on_reserve_number] = self.monster_on_ground[monster_on_ground_number]
        self.monster_on_ground[monster_on_ground_number] = m
        self.playground.apply_effect(self.monster_positions[monster_on_ground_number], Effect_type.Replacing)
        return True

    def reposition_monster(self, pos_from, pos_to, passing = True):
        m = self.playground.get_square(pos_from).monster
        if  m == 0:
            return False
        if not passing and self.playground.get_square(pos_to).monster > 0 :
            m0 = self.playground.get_square(pos_to).monster
            self.playground.put_monster(pos_from, m0)
            self.monsters_positions[m0 - 1] = pos_from
        else:
            self.playground.put_monster(pos_from, 0)
        self.playground.put_monster(pos_to, m)
        self.monsters_positions[m - 1] = pos_to

    def step_monster(self, pos_from, pos_to):
        self.reposition_monster(pos_from, pos_to, True)
        self.playground.apply_orb(pos_to)
        self.playground.apply_effect(pos_to, Effect_type.Passing)

    def move_monster(self, path)
        n = self.playground.get_square(path[0]).monster
        if n == 0:
            return False
        m = self.monster_on_ground[n - 1]
        if self.monster_on_ground[n - 1].actual_moving > 0:
            return False
        for i in range(1, len(path)):
            self.step_monster(path[i-1], path[i])
        self.monsters_positions[n - 1] = path[-1]
        m.actual_moving = m.monster.get_stat[Stats.Moving]
        return True

class Playground():
    def __init__(self, monsters_positions):
        self.ground = [[Square(), Square(), Square()],
                        [Square(), Square(), Square()],
                        [Square(), Square(), Square()]]
        for i in range(3):
            self.put_monster(monsters_positions[i], i  + 1)

    def get_square(self, position):
        col, row = position
        return self.ground[col][row]

    def put_monster(self, position, monster_number):
        self.get_square(position).monster = monster_number

    def apply_effect(self, position, effect_type):
        self.get_square(position).apply_effect(effect_type)

    def apply_orb(self, position):
        self.get_square(position).apply_orb()



class Square():
    def __init__(self):
        self.effect = Square_effect.Null
        self.effectTurn = 0
        self.orb = Square_orb.Null
        self.monster = 0

    def apply_effect(self, effect_type):
        return
        // à completer

    def apply_orb(self)
        return
        // à completer

class Square_effect(Enum):
    Null = 0
    Fire = auto()
    Ice = auto()
    Poison = auto()
    Electric = auto()
    Soap = auto()

class Effect_type(Enum):
    Passing = auto()
    Staying = auto()
    Replacing = auto()

class Square_orb(Enum):
    Null = 0
    HP_orb = auto()
    Soul_orb = auto()

class Stats(Enum):
    HP = auto()
    Strength = auto()
    Spirit = auto()
    Speed = auto()
    Defense = auto()
    Moving = auto()
