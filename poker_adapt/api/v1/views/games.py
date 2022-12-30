#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Game """
from models.game import Game
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/states', methods=['GET'], strict_slashes=False)
@swag_from('documentation/state/get_state.yml', methods=['GET'])
def get_games():
    """
    Retrieves the list of all Game objects
    """
    all_games = storage.all(Game).values()
    list_games = []
    for game in all_games:
        list_games.append(game.to_dict())
    return jsonify(list_games)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/state/get_id_state.yml', methods=['get'])
def get_game(game_id):
    """ Retrieves a specific Game """
    game = storage.get(Game, game_id)
    if not game:
        abort(404)

    return jsonify(game.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/state/delete_state.yml', methods=['DELETE'])
def delete_game(game_id):
    """
    Deletes a Game Object
    """

    game = storage.get(Game, game_id)

    if not game:
        abort(404)

    storage.delete(game)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
@swag_from('documentation/state/post_state.yml', methods=['POST'])
def post_game():
    """
    Creates a Game
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    instance = Game(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/state/put_state.yml', methods=['PUT'])
def put_game(game_id):
    """
    Updates a Game
    """
    game = storage.get(Game, game_id)

    if not game:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(game, key, value)
    storage.save()
    return make_response(jsonify(game.to_dict()), 200)