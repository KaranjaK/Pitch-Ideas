from flask import render_template,request,redirect,url_for, abort
from . import main
from flask_login import login_required, current_user
from ..models import Users, Pitches, Upvote, Downvote, Comment
from .forms import UpdateProfile, PitchForm, CommentForm
from .. import db,photos


@main.route('/')
def index():
    pitches = Pitches.query.all()
    pickup = Pitches.query.filter_by(category = 'Pickup').all() 
    interview = Pitches.query.filter_by(category = 'Interview').all()
    products = Pitches.query.filter_by(category = 'Products').all()
    promotion = Pitches.query.filter_by(category = 'Promotion').all()
    return render_template('index.html', pitches = pitches, pickup = pickup,interview = interview, products = products, promotion = promotion)

@main.route('/create_new', methods = ['POST','GET'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data
        category = form.category.data
        user_id = current_user
        new_pitch_object = Pitches(post=post,user_id=current_user._get_current_object().id,category=category,title=title)
        new_pitch_object.pitch_save()
        return redirect(url_for('main.index'))
        
    return render_template('create_pitch.html', form = form)

@main.route('/comment/<int:pitch_id>', methods = ['POST','GET'])
@login_required
def comment(pitch_id):
    form = CommentForm()
    pitch = Pitches.query.get(pitch_id)
    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,pitch_id = pitch_id)
        new_comment.save_c()
        return redirect(url_for('.comment', pitch_id = pitch_id))
    return render_template('comment.html', form =form, pitch = pitch,all_comments=all_comments)

@main.route('/user/<uname>')
def profile(uname):
    user = Users.query.filter_by(username = uname).first()
    user_id = current_user._get_current_object().id
    posts = Pitches.query.filter_by(user_id = user_id).all()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user, posts = posts)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = Users.query.filter_by(username = uname).first()
    form = UpdateProfile()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        user.user_save()

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = Users.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/like/<int:id>',methods = ['POST','GET'])
@login_required
def like(id):
    get_pitches = Upvote.get_upvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for pitch in get_pitches:
        to_str = f'{pitch}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_vote = Upvote(user = current_user, pitch_id=id)
    new_vote.save()
    return redirect(url_for('main.index',id=id))

@main.route('/dislike/<int:id>',methods = ['POST','GET'])
@login_required
def dislike(id):
    pitch = Downvote.get_downvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for p in pitch:
        to_str = f'{p}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_downvote = Downvote(user = current_user, pitch_id=id)
    new_downvote.save()
    return redirect(url_for('main.index',id = id))