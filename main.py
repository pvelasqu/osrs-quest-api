from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from skills_dictionary.SkillsDictionary import SkillDictionary
import requests
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Quest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quest_name = db.Column(db.String(50), unique=True)
    strength = db.Column(db.Integer)
    crafting = db.Column(db.Integer)
    mining = db.Column(db.Integer)
    smithing = db.Column(db.Integer)
    fishing = db.Column(db.Integer)
    cooking = db.Column(db.Integer)
    firemaking = db.Column(db.Integer)
    woodcutting = db.Column(db.Integer)
    agility = db.Column(db.Integer)
    herblore = db.Column(db.Integer)
    thieving = db.Column(db.Integer)
    fletching = db.Column(db.Integer)
    slayer = db.Column(db.Integer)
    farming = db.Column(db.Integer)
    construction = db.Column(db.Integer)
    hunter = db.Column(db.Integer)
    attack = db.Column(db.Integer)
    defence = db.Column(db.Integer)
    ranged = db.Column(db.Integer)
    prayer = db.Column(db.Integer)
    magic = db.Column(db.Integer)
    runecrafting = db.Column(db.Integer)
    hitpoints = db.Column(db.Integer)

    def __init__(self, quest_name, strength=0, attack=0, defence=0, ranged=0, prayer=0, magic=0,
                 runecrafting=0, hitpoints=0, crafting=0, mining=0, smithing=0, fishing=0, cooking=0,
                 firemaking=0, woodcutting=0, agility=0, herblore=0, thieving=0, fletching=0,
                 slayer=0, farming=0, construction=0, hunter=0):
        self.quest_name = quest_name
        self.strength = strength
        self.crafting = crafting
        self.mining = mining
        self.smithing = smithing
        self.fishing = fishing
        self.cooking = cooking
        self.firemaking = firemaking
        self.woodcutting = woodcutting
        self.agility = agility
        self.herblore = herblore
        self.thieving = thieving
        self.fletching = fletching
        self.slayer = slayer
        self.farming = farming
        self.construction = construction
        self.hunter = hunter
        self.attack = attack
        self.defence = defence
        self.ranged = ranged
        self.prayer = prayer
        self.magic = magic
        self.runecrafting = runecrafting
        self.hitpoints = hitpoints


@app.route("/quest", methods=["POST"])
def add_quest():
    quest_name = request.json['quest_name']
    strength = request.json['strength']
    crafting = request.json['crafting']
    mining = request.json['mining']
    smithing = request.json['smithing']
    fishing = request.json['fishing']
    cooking = request.json['cooking']
    firemaking = request.json['firemaking']
    woodcutting = request.json['woodcutting']
    agility = request.json['agility']
    herblore = request.json['herblore']
    thieving = request.json['thieving']
    fletching = request.json['fletching']
    slayer = request.json['slayer']
    farming = request.json['farming']
    construction = request.json['construction']
    hunter = request.json['hunter']
    attack = request.json['attack']
    defence = request.json['defence']
    ranged = request.json['ranged']
    prayer = request.json['prayer']
    magic = request.json['magic']
    runecrafting = request.json['runecrafting']
    hitpoints = request.json['hitpoints']

    new_quest = Quest(quest_name, strength, attack, defence, ranged, prayer, magic,
                      runecrafting, hitpoints, crafting, mining, smithing, fishing, cooking,
                      firemaking, woodcutting, agility, herblore, thieving, fletching,
                      slayer, farming, construction, hunter)

    db.session.add(new_quest)
    db.session.commit()

    return jsonify({"message": "Quest Added!"})


@app.route("/quest", methods=["GET"])
def get_all_quests():
    all_quests = Quest.query.all()
    quest_output = []

    for quest in all_quests:
        quest_data = dict()
        quest_data['quest_name'] = quest.quest_name
        quest_data['strength'] = quest.strength
        quest_data['attack'] = quest.attack
        quest_data['defence'] = quest.defence
        quest_data['ranged'] = quest.ranged
        quest_data['prayer'] = quest.prayer
        quest_data['magic'] = quest.magic
        quest_data['runecrafting'] = quest.runecrafting
        quest_data['hitpoints'] = quest.hitpoints
        quest_data['crafting'] = quest.crafting
        quest_data['mining'] = quest.mining
        quest_data['smithing'] = quest.smithing
        quest_data['fishing'] = quest.fishing
        quest_data['cooking'] = quest.cooking
        quest_data['firemaking'] = quest.firemaking
        quest_data['woodcutting'] = quest.woodcutting
        quest_data['agility'] = quest.agility
        quest_data['herblore'] = quest.herblore
        quest_data['thieving'] = quest.thieving
        quest_data['fletching'] = quest.fletching
        quest_data['slayer'] = quest.slayer
        quest_data['farming'] = quest.farming
        quest_data['construction'] = quest.construction
        quest_data['hunter'] = quest.hunter
        quest_output.append(quest_data)

    return jsonify({'Quests': quest_output})


@app.route("/quest/<quest_name>", methods=["GET"])
def get_one_quest(quest_name):
    quest = Quest.query.filter_by(quest_name=quest_name).first()
    if not quest:
        return jsonify({'Message': 'No Quest Found!'})

    quest_data = dict()
    quest_data['quest_name'] = quest.quest_name
    quest_data['strength'] = quest.strength
    quest_data['attack'] = quest.attack
    quest_data['defence'] = quest.defence
    quest_data['ranged'] = quest.ranged
    quest_data['prayer'] = quest.prayer
    quest_data['magic'] = quest.magic
    quest_data['runecrafting'] = quest.runecrafting
    quest_data['hitpoints'] = quest.hitpoints
    quest_data['crafting'] = quest.crafting
    quest_data['mining'] = quest.mining
    quest_data['smithing'] = quest.smithing
    quest_data['fishing'] = quest.fishing
    quest_data['cooking'] = quest.cooking
    quest_data['firemaking'] = quest.firemaking
    quest_data['woodcutting'] = quest.woodcutting
    quest_data['agility'] = quest.agility
    quest_data['herblore'] = quest.herblore
    quest_data['thieving'] = quest.thieving
    quest_data['fletching'] = quest.fletching
    quest_data['slayer'] = quest.slayer
    quest_data['farming'] = quest.farming
    quest_data['construction'] = quest.construction
    quest_data['hunter'] = quest.hunter

    return jsonify({'Quests': quest_data})


@app.route("/user/<username>", methods=["GET"])
def get_doable_quests(username):
    jagex_api_url = "http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player=" + username
    player_request = requests.get(jagex_api_url).text.split(',')

    skills = SkillDictionary(attack=player_request[3], defence=player_request[5], strength=player_request[7],
                             hitpoints=player_request[9], ranged=player_request[11], prayer=player_request[13],
                             magic=player_request[15], cooking=player_request[17], woodcutting=player_request[19],
                             fletching=player_request[21], fishing=player_request[23],
                             firemaking=player_request[25], crafting=player_request[27],
                             smithing=player_request[29], mining=player_request[31], herblore=player_request[33],
                             agility=player_request[35], thieving=player_request[37], slayer=player_request[39],
                             farming=player_request[41], runecrafting=player_request[43],
                             hunter=player_request[45], construction=player_request[47]
                             )
    skills_dict = skills.skills
    all_quests = Quest.query.filter(skills_dict['attack'] >= Quest.attack, skills_dict['defence'] >= Quest.defence,
                                    skills_dict['strength'] >= Quest.strength, skills_dict['prayer'] >= Quest.prayer,
                                    skills_dict['hitpoints'] >= Quest.hitpoints, skills_dict['ranged'] >= Quest.ranged,
                                    skills_dict['magic'] >= Quest.magic, skills_dict['cooking'] >= Quest.cooking,
                                    skills_dict['woodcutting'] >= Quest.woodcutting,
                                    skills_dict['fletching'] >= Quest.fletching,
                                    skills_dict['fishing'] >= Quest.fishing, skills_dict['smithing'] >= Quest.smithing,
                                    skills_dict['firemaking'] >= Quest.firemaking,
                                    skills_dict['crafting'] >= Quest.crafting, skills_dict['hunter'] >= Quest.hunter,
                                    skills_dict['mining'] >= Quest.mining, skills_dict['herblore'] >= Quest.herblore,
                                    skills_dict['agility'] >= Quest.agility, skills_dict['thieving'] >= Quest.thieving,
                                    skills_dict['slayer'] >= Quest.slayer, skills_dict['farming'] >= Quest.farming,
                                    skills_dict['runecrafting'] >= Quest.runecrafting,
                                    skills_dict['construction'] >= Quest.construction
                                    ).all()

    quest_output = []

    for quest in all_quests:
        quest_output.append(quest.quest_name)

    return jsonify({'Stats': skills.skills, 'Name': username, 'Quest': quest_output})


@app.route("/", methods=["GET"])
def index():
    return "Welcome to the Oldschool-Runescape Quest API"


if __name__ == '__main__':
    app.run(debug=True)
