from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here.
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect
from django.db import connection
import sqlite3
import django_tables2 as tables
from django_tables2 import RequestConfig
from django import forms
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template


def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):

	

	post = get_object_or_404(Post, pk=pk)
	return render(request,'blog/post_detail.html',{'post':post})
	
def post_new(request):

	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)


	else:

		form = PostForm()

	return render(request, 'blog/post_edit.html', {'form':form})

def post_football(request):
	def dict_gen(curs):
		''' From Python Essential Reference by David Beazley
        '''
		import itertools
		field_names = [d[0].lower() for d in curs.description]
		while True:
			rows = curs.fetchmany()
			if not rows: return
			for row in rows:
				yield dict(itertools.izip(field_names, row))

	conn = sqlite3.connect('TestExample.db')

	c = conn.cursor()

	all_data = [r for r in dict_gen(c.execute('select * from t'))]

	class NameTable(tables.Table):
		status = tables.Column()
		date = tables.Column()
		location = tables.Column()
		starttime = tables.Column()
		endtime = tables.Column()
		hourclock = tables.Column()
		priceper = tables.Column()
		court = tables.Column()
		weekday = tables.Column()




	table = NameTable(all_data)

	RequestConfig(request).configure(table)




	return render(request, 'blog/post_football.html', {'table':table})

def search(request):

	query = request.GET.get('q')
	if query:

		test_text = query
		print(test_text)

		return render(request, 'blog/search_result.html', {'test_text':test_text})
	else:
		posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')


		return render(request, 'blog/post_list.html', {'posts': posts})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def subscribe(request):


	return render(request, 'blog/subscribe.html',{})


def contact(request):


	form_class = ContactForm



	if request.method == 'POST':
		form = form_class(data=request.POST)

		if form.is_valid():
			contact_name = request.POST.get(
				'contact_name'
				, '')
			contact_email = request.POST.get(
				'contact_email'
				, '')
			form_content = request.POST.get('content', '')

			sport_type = request.POST.get('sport_type','')

			weekday = request.POST.get('weekday', '')




			# Email the profile with the
			# contact information
			template = get_template('blog/contact_template.txt')

		context = Context({
			'contact_name': contact_name,
			'contact_email': contact_email,
			'form_content': form_content,
			'sport_type':sport_type,
			'weekday':weekday,

		})
		content = template.render(context)



		email = EmailMessage(
			"New contact form submission",
			content,
			"Your website" + '',
			['youremail@gmail.com'],
			headers={'Reply-To': contact_email}
		)
		email.send()
		print('testtttt')
		print(context)

		wd = context['weekday']
		sport = context['sport_type']
		print('okookok')
		print(wd)
		print(sport)


		conn = sqlite3.connect('subscriberDB.db')

		c = conn.cursor()

		c.execute("CREATE TABLE subscriber (weekday text, sport text);")
		c.execute("INSERT INTO subscriber VALUES (?,?);",(wd, sport))
		conn.commit()
		conn.close()



		return redirect('blog/contact.html')


	return render(request, 'blog/contact.html', {'form': form_class,})



