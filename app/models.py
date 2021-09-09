from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

class Core(models.Model):
    title = models.CharField(_("title"), max_length=200)
    excerpt = models.TextField(_("excerpt"), null=True)
    author = models.ForeignKey(User, verbose_name=_("Author"),related_name='core', on_delete=models.CASCADE)
    slug = models.SlugField(_("slug"), unique=True)
    updated = models.DateTimeField(_("updated"), auto_now=True)
    published = models.DateTimeField(_("published"), auto_now_add=False)

    def get_absolute_url(self):
        return reverse("app:single", args={ self.slug})
    
    class Meta:
        ordering = ['-published']
    
    def __str__(self):
        return self.title
    