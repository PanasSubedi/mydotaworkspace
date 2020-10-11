from app import db

heroRoles = db.Table(
    'heroRoles',
    db.Column('hero_id', db.Integer, db.ForeignKey('hero.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(15))

    heroes = db.relationship('Hero', secondary=heroRoles, backref=db.backref('roles', lazy='dynamic'))

class Hero(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    localized_name = db.Column(db.String(50))
    primary_attr = db.Column(db.String(3))
    attack_type = db.Column(db.String(10))
    img = db.Column(db.String(100))
    base_health = db.Column(db.Integer)
    base_health_regen = db.Column(db.Integer)
    base_mana = db.Column(db.Integer)
    base_mana_regen = db.Column(db.Integer)
    base_armor = db.Column(db.Integer)
    base_mr = db.Column(db.Integer)
    base_attack_min = db.Column(db.Integer)
    base_attack_max = db.Column(db.Integer)
    base_str = db.Column(db.Integer)
    base_agi = db.Column(db.Integer)
    base_int = db.Column(db.Integer)
    str_gain = db.Column(db.Integer)
    agi_gain = db.Column(db.Integer)
    int_gain = db.Column(db.Integer)
    attack_range = db.Column(db.Integer)
    projectile_speed = db.Column(db.Integer)
    attack_rate = db.Column(db.Integer)
    move_speed = db.Column(db.Integer)
    turn_rate = db.Column(db.Integer)
    cm_enabled = db.Column(db.Integer)


class PublicMatch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    match_seq_num = db.Column(db.Integer)
    radiant_win = db.Column(db.Boolean)
    start_time = db.Column(db.Integer)
    duration = db.Column(db.Integer)
    avg_mmr = db.Column(db.Integer)
    num_mmr = db.Column(db.Integer)
    lobby_type = db.Column(db.Integer)
    game_mode = db.Column(db.Integer)
    avg_rank_tier = db.Column(db.Integer)
    num_rank_tier = db.Column(db.Integer)
    cluster = db.Column(db.Integer)
    radiant_team = db.Column(db.String(20))
    dire_team = db.Column(db.String(20))

    def __repr__(self):
        return '<PublicMatch {}>'.format(self.id)

class ProMatch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    duration = db.Column(db.Integer)
    start_time = db.Column(db.Integer)
    radiant_win = db.Column(db.Boolean)
    radiant_score = db.Column(db.Integer)
    dire_score = db.Column(db.Integer)
    radiant_team_id = db.Column(db.Integer)
    dire_team_id = db.Column(db.Integer)

    def __repr__(self):
        return '<ProMatch {}>'.format(self.id)

class ProTeam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Float)
    wins = db.Column(db.Integer)
    losses = db.Column(db.Integer)
    name = db.Column(db.String(50), index=True)
    tag = db.Column(db.String(10))
    logo_url = db.Column(db.String(225))

    def matches(self):
        return ProMatch.query.filter((ProMatch.radiant_team_id==self.id) | (ProMatch.dire_team_id == self.id)).all()

    def __repr__(self):
        return '<ProTeam {}>'.format(self.name)
