from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.contrib import messages
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
from django.urls import reverse

class PostListView(ListView):
  queryset = Post.Published.all()
  context_object_name = 'posts'
  paginate_by = 3
  template_name = 'blog/post/list.html'
  
def post_details(request, post):
  post = get_object_or_404(Post, slug=post, status='published')
  
  #List of active comments
  comments = post.comment.filter(active=True)
  new_comment = None
  if request.method == 'POST':
    #A comment was submitted
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
      #Not saved to database yet
      new_comment = comment_form.save(commit=False)
      new_comment.post = post
      #Saved to database
      new_comment.save()
      messages.success(request, 'Comment added Successfully')
      return redirect(reverse('blog:post_details', args=[post.slug]))
  else:
    comment_form = CommentForm()
  return render(request, 'blog/post/details.html', {'post': post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})
  
def post_share(request, post_id):
  post = get_object_or_404(Post, id=post_id, status='published')
  sent = False
  if request.method == 'POST':
    #Form was submitted
    form = EmailPostForm(request.POST)
    if form.is_valid():
      #Form passed Validation
      cd=form.cleaned_data
      post_url = request.build_absolute_uri(post.get_absolute_url())
      subject = f"{cd['name']} recommends you read" \
                f"{post.title}"
      message = f"Read {post.title} at {post_url}\n\n" \
                f"{cd['name']}\'s comments: {cd['comments']}"
      send_mail(subject, message, 'admin@myblog.com', [cd['receiver']])
      sent = True
      messages.success(request, f"E-mail sent to {cd['receiver']} Successfully")
      return redirect(reverse('blog:post_details', args=[post.slug]))
  else:
    form = EmailPostForm()
  return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})