from django.db import models
from django.utils.translation import ugettext_lazy as _
from account.models import Account
from django.forms.models import model_to_dict

class Comment(models.Model):
    text = models.TextField()
    owner = models.ForeignKey(Account)
    comments = models.ManyToManyField('self', null=True, blank=True)
    entry_date = models.DateTimeField(_(u'Comment Date'), auto_now_add=True)


class MainConfiguration(models.Model):
    """
    Configuration model
    """
    ## Mail Settings
    email_use_tls = models.BooleanField(_(u'EMAIL_USE_TLS'),default=True)
    email_host = models.CharField(_(u'EMAIL_HOST'),max_length=1024)
    email_host_user = models.CharField(_(u'EMAIL_HOST_USER'),max_length=255)
    email_host_password = models.CharField(_(u'EMAIL_HOST_PASSWORD'),max_length=255)
    email_port = models.PositiveSmallIntegerField(_(u'EMAIL_PORT'),default=587)

    ## Account Registration/Activation
    allow_registration = models.BooleanField(_(u'Allow Registration'),default=True,help_text=_(u'If disabled, Accounts need to be created internally'))
    active_after_registration = models.BooleanField(_(u'Accounts Active After Registration'),default=True,help_text=_(u'Enable Accounts after registration automatically'))

    ## Notifications
    email_changes_to_reporter = models.BooleanField(_(u'Notify Reporter'),default=True,help_text=_(u'Send Notification to issue reporter for every issue change'))
    email_changes_to_watchers = models.BooleanField(_(u'Notify Watchers'),default=True,help_text=_(u'Send Notification to issue watchers for every issue change'))
    email_changes_to_assignee = models.BooleanField(_(u'Notify Assignee'),default=True,help_text=_(u'Send Notification to issue assignee for every issue change'))
    email_changes_to_people = models.BooleanField(_(u'Notify People'), default=True,help_text=_(u'Send Notification to people assigned to issue for every issue change'))


class History(models.Model):
    account = models.ForeignKey(Account,editable=False)
    message = models.CharField(_(u'Message'), max_length=1024,editable=False)
    entry_date = models.DateTimeField(_(u'Create Date'), auto_now_add=True,editable=False)

