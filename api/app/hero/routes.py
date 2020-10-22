from app.hero import bp
from flask import request

from app.models.main_models import Hero

@bp.route('/hero/<int:id>', methods=['GET'])
def get_hero(id):
    """
    Returns details for a single hero

    Endpoint: /hero/{hero_id}
    Method: GET

    Request params:
        id: ID of a hero

    Response params:
    {
        _links: {
            self
        },
        agi_gain, attack_range, attack_rate, attack_type, base_agi,
        base_armor, base_attack_max, base_attack_min, base_health,
        base_health_regen, base_int, base_mana, base_mana_regen,
        base_mr, base_str, cm_enabled, icon_url, id, image_url,
        int_gain, move_speed, name, primary_attr, projectile_speed,
        roles, str_gain, turn_rate
    }
    """
    return Hero.query.get_or_404(id).to_detailed_dict()

@bp.route('/hero', methods=['GET'])
def get_heroes():
    """
    Returns a paginated list of all the heroes

    Endpoint: /hero
    Method: GET

    Request params:
        id: ID of the required player

    Response params:
    {
        _links: {
            self
        },
        icon_url, id, image_url, name
    }
    """

    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), Hero.query.count())
    data = Hero.to_collection_dict(Hero.query, page, per_page, 'hero.get_heroes')
    return data
