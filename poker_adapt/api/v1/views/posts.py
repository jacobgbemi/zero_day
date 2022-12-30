#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Posts """
from models.post import Post
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/states', methods=['GET'], strict_slashes=False)
@swag_from('documentation/state/get_state.yml', methods=['GET'])
def get_posts():
    """
    Retrieves the list of all Post objects
    """
    all_posts = storage.all(Post).values()
    list_posts = []
    for post in all_posts:
        list_posts.append(post.to_dict())
    return jsonify(list_posts)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/state/get_id_state.yml', methods=['get'])
def get_post(post_id):
    """ Retrieves a specific State """
    post = storage.get(Post, post_id)
    if not post:
        abort(404)

    return jsonify(post.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/state/delete_state.yml', methods=['DELETE'])
def delete_post(post_id):
    """
    Deletes a Post Object
    """

    post = storage.get(Post, post_id)

    if not post:
        abort(404)

    storage.delete(post)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
@swag_from('documentation/state/post_state.yml', methods=['POST'])
def post_post():
    """
    Creates a Post
    """
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'name' not in request.get_json():
        abort(400, description="Missing name")

    data = request.get_json()
    instance = Post(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/state/put_state.yml', methods=['PUT'])
def put_post(post_id):
    """
    Updates a Post
    """
    post = storage.get(Post, post_id)

    if not post:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(post, key, value)
    storage.save()
    return make_response(jsonify(post.to_dict()), 200)