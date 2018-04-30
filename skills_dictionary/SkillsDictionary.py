class SkillDictionary(object):
    def __init__(self, strength=0, attack=0, defence=0, ranged=0, prayer=0, magic=0,
                 runecrafting=0, hitpoints=0, crafting=0, mining=0, smithing=0, fishing=0, cooking=0,
                 firemaking=0, woodcutting=0, agility=0, herblore=0, thieving=0, fletching=0,
                 slayer=0, farming=0, construction=0, hunter=0):
        self.skills = dict()
        self.skills['attack'] = attack
        self.skills['strength'] = strength
        self.skills['defence'] = defence
        self.skills['ranged'] = ranged
        self.skills['prayer'] = prayer
        self.skills['magic'] = magic
        self.skills['runecrafting'] = runecrafting
        self.skills['hitpoints'] = hitpoints
        self.skills['crafting'] = crafting
        self.skills['mining'] = mining
        self.skills['smithing'] = smithing
        self.skills['fishing'] = fishing
        self.skills['cooking'] = cooking
        self.skills['firemaking'] = firemaking
        self.skills['woodcutting'] = woodcutting
        self.skills['agility'] = agility
        self.skills['herblore'] = herblore
        self.skills['thieving'] = thieving
        self.skills['fletching'] = fletching
        self.skills['slayer'] = slayer
        self.skills['farming'] = farming
        self.skills['construction'] = construction
        self.skills['hunter'] = hunter
