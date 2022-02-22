from flask import render_template, url_for, request, redirect, Blueprint, flash, abort
from flask_login import current_user, login_required
from puppycompanyblog import db
from puppycompanyblog.models import BlogPost
from puppycompanyblog.blogposts.forms import BlogPostForm

blog_post = Blueprint('blogposts', __name__)


# Create
@blog_post.route('/create', methods=['GET','POST'])
@login_required
def create_post():
    form = BlogPostForm()

    if form.validate_on_submit():

        blog_post = BlogPost(title=form.title.data,
                             text=form.text.data,
                             user_id=current_user.id)

        db.session.add(blog_post)
        db.session.commit()

        flash('Blog post created')

        return redirect(url_for('core.index'))

    return render_template('create_post.html', form=form)


# Read Posts
@blog_post.route('/<int:blog_post_id>')
def blog_post(blog_post_id):

    blog_post = BlogPost.query.get_or_404(blog_post_id)

    return render_template('blog_post.html',
                           title=blog_post.title,
                           date=blog_post.date,
                           post=blog_post)


# Update post
@blog_post.route('/<int:blog_post_id>/update', methods=['GET','POST'])
@login_required
def update_post(blog_post_id):

    # make sure you only can edit your own posts
    blog_post = BlogPost.query.get_or_404(blog_post_id)

    if blog_post.author != current_user:
        abort(403)

    # if it's the Author
    form = BlogPostForm()

    # When submits just save the post
    if form.validate_on_submit():

        blog_post.title = form.title.data,
        blog_post.text = form.text.data,

        db.session.commit()

        flash('Blog post updated')

        return redirect(url_for('blogposts.blog_post'), blog_post_id=blog_post.id)

    # Prefill with old data
    elif request.method == 'GET':
        form.title.data = blog_post.title
        form.text.data = blog_post.text

    return render_template('create_post.html', title='Updating', form=form)


# Delete post
@blog_post.route('/<int:blog_post_id>/delete', methods=['GET','POST'])
@login_required
def delete_post(blog_post_id):

    # make sure you only can delete your own posts
    blog_post = BlogPost.query.get_or_404(blog_post_id)

    if blog_post.author != current_user:
        abort(403)

    # if it's the Author
    form = BlogPostForm()

    db.session.delete(blog_post)
    db.session.commit()

    flash('Blog post deleted')

    return redirect(url_for('core.index'))


