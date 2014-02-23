from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from django import forms
from issue.models import (Issue, IssueCharValue, IssueTextValue, IssueImageValue,
                          IssueFileValue, IssuePersonValue)
from account.models import Account


class CreateIssueDetailsForm(forms.ModelForm):
    original_fields = {}
    field_value_class = {}
    field_type_instance = {}
    class Meta:
        model = Issue

    def __init__(self, *args, **kwargs):
        super(CreateIssueDetailsForm, self).__init__(*args, **kwargs)
        issue = kwargs.get('instance', None)

        if issue:
            self.fields.pop('effort_calc')
            self.fields.pop('template')
            self.original_fields = self.fields.copy()

            if issue.template:

                char_fields = issue.template.char_fields.all()
                for field in char_fields:
                    self.fields[field.name] = forms.CharField(max_length=255, required=field.required)
                    self.field_value_class[field.name] = IssueCharValue
                    self.field_type_instance[field.name] = field
                    try:
                        item = IssueCharValue.objects.get(issue=issue,field=field)
                        self.fields[field.name].initial = item.value
                    except IssueCharValue.DoesNotExist:
                        pass

                text_fields = issue.template.text_fields.all()
                for field in text_fields:
                    self.fields[field.name] = forms.CharField(widget=forms.Textarea, required=field.required)
                    self.field_value_class[field.name] = IssueTextValue
                    self.field_type_instance[field.name] = field
                    try:
                        item = IssueTextValue.objects.get(issue=issue,field=field)
                        self.fields[field.name].initial = item.value
                    except IssueTextValue.DoesNotExist:
                        pass

                image_fields = issue.template.image_fields.all()
                for field in image_fields:
                    self.fields[field.name] = forms.ImageField(required=field.required)
                    self.field_value_class[field.name] = IssueImageValue
                    self.field_type_instance[field.name] = field
                    try:
                        item = IssueImageValue.objects.get(issue=issue,field=field)
                        self.fields[field.name].initial = item.value
                    except IssueImageValue.DoesNotExist:
                        pass

                file_fields = issue.template.file_fields.all()
                for field in file_fields:
                    self.fields[field.name] = forms.FileField(required=field.required)
                    self.field_value_class[field.name] = IssueFileValue
                    self.field_type_instance[field.name] = field
                    try:
                        item = IssueFileValue.objects.get(issue=issue,field=field)
                        self.fields[field.name].initial = item.value
                    except IssueFileValue.DoesNotExist:
                        pass

                people = issue.template.people.all()
                for field in people:
                    self.fields[field.role] = forms.ModelChoiceField(queryset=Account.objects.all(),required=field.required)
                    self.field_value_class[field.role] = IssuePersonValue
                    self.field_type_instance[field.role] = field
                    try:
                        item = IssuePersonValue.objects.get(issue=issue,field=field)
                        self.fields[field.role].initial = item.value
                    except IssuePersonValue.DoesNotExist:
                        pass

    def save(self, force_insert=False, force_update=False, commit=True):
        m = super(CreateIssueDetailsForm, self).save(commit=False)
        if commit:
            m.save()
        if len(self.field_value_class) > 0:
            for k,v in self.original_fields.iteritems():
                self.cleaned_data.pop(k)
        for k,v in self.cleaned_data.iteritems():
            item,created = self.field_value_class[k].objects.get_or_create(
                issue=m,
                field=self.field_type_instance.get(k))
            item.value = self.cleaned_data.get(k)
            item.save()
        return m


class CreateIssueDetails(UpdateView):
    slug = ''
    context_object_name = 'issue'
    form_class = CreateIssueDetailsForm

    def get(self, request, *args, **kwargs):
        self.slug = kwargs.get('slug')
        return super(CreateIssueDetails, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.slug = kwargs.get('slug')
        return super(CreateIssueDetails, self).post(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Issue, slug=self.slug)


class CreateIssueView(CreateView):

    def get_success_url(self):
        return '/issue/create/details/%s/' % self.object.slug


class CreateIssueFlow(CreateView):
    pass


class CreateIssueField(CreateView):
    page_title = ''
    page_heading = ''
    template_name = 'issue/create/issuefield.html'

    def get_context_data(self, **kwargs):
        context = super(CreateIssueField, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['page_heading'] = self.page_heading
        return context


class ListIssueFieldView(ListView):
    page_title = ''
    page_heading = ''
    template_name = 'issue/view/issuefield.html'

    def get_context_data(self, **kwargs):
        context = super(ListIssueFieldView, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['page_heading'] = self.page_heading
        return context


class ListIssueView(ListView):
    template_name = 'issue/view/issue.html'