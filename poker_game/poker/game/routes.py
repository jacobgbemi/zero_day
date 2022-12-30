from flask_login import current_user, login_required
from poker import db
from poker.posts.forms import GameForm
from flask import render_template, Blueprint, flash
from poker.models import Game
from poker.game.main import show_hand, show_rank, show_winner

games = Blueprint('games', __name__)

@games.route("/game/new", methods=['GET', 'POST'])
@login_required
def show_cards():
    hands = show_hand()
    ranks = show_rank()
    winner = show_winner()
    # card_image = cards_picture(url_for('static', filename='images/cards/2_of_clubs.png'))
    # # card_image = Image.open('static/images/2_of_clubs.png')
    # # card_image.thumbnail((150, 218))
    form = GameForm()
    if form.validate_on_submit():
        game = Game(winner=form.winner.data, author=current_user)
        db.session.add(game)
        db.session.commit()
        flash(f'{winner} won', 'success')
    return render_template("create_game.html", hands=hands, ranks=ranks,
                            form=form, title="New Poker Game", legend='New Poker Game')