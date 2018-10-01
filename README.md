Introduction to Django ORM
=========================

To create new application to your django project use the following  command

```
    $ python manage.py startapp orm_intro
```

Let's create a sample model of Post to see how django's built in ORM works. In orm_intro/models.py
```
    from django.db import models
    from datetime import datetime
    class Post(models.Model):
        title = models.CharField(max_length=200)
        description = models.TextField()
        createddate = models.DateTimeField(default=datetime.now())

```

To convert the above model as a database table we need to apply database migrations to the model. Create migration files with the following command
```
    $ python manage.py makemigrations
```

To apply the created migrations use the following command
```
    $ python manage.py migrate
```

The above command create a table in the database. By default django comes with a shell where we can perform ORM queries on the models.

Following are steps to go to django shell and perform database querying on the models.
```
    $ python manage.py shell
    >>> from orm_intro.models import Post
    >>> p = Post()
    >>> p.title = "learn some math"
    >>> p.description = "1+2 = 3"
    >>> p.save()

    >>> Post.objects.create(title="Learn some science", description="E = mc2")
    <Post: Post object>
    >>> p = Post.objects.get(title="learn some math")
    >>> p.title = "Math is Interesting"
    >>> p.description = "a2+2ab+b2"
    >>> p.save()
    >>> p = Post.objects.get(title="Learn some science")
    >>> p.delete()
    >>> Post.objects.count()


```
