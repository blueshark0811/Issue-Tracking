from django.core.context_processors import csrf
from django.shortcuts import render
from django.views.generic.base import View
from django.forms import ModelForm
from issue.models import (Issue, IssueType, IssueStatus, IssuePriority,IssueCharField,
                          IssueTextField)


class CreateIssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = [
            'title', 'summary', 'effort', 'project_version', 'type',
            'status', 'priority', 'template', 'flow', 'sub_issues','due_date'
        ]


class CreateIssueView(View):
    template_name = 'issue/createissue.html'
    content = {}

    def get(self,request):
        self.content.update(csrf(request))
        self.content['create_issue_form'] = CreateIssueForm()
        return render(request, self.template_name, self.content)

    def post(self,request):
        return render(request, self.template_name)


class CreateIssueTypeForm(ModelForm):
    class Meta:
        model = IssueType
        fields = [
            'name',
        ]


class CreateIssueTypeView(View):
    template_name = 'issue/createissuetype.html'
    content = {}

    def get(self,request):
        self.content.update(csrf(request))
        self.content['create_issue_type_form'] = CreateIssueTypeForm()
        return render(request, self.template_name, self.content)

    def post(self,request):
        return render(request, self.template_name)


class CreateIssueStatusForm(ModelForm):
    class Meta:
        model = IssueStatus
        fields = [
            'status',
        ]


class CreateIssueStatusView(View):
    template_name = 'issue/createissuestatus.html'
    content = {}

    def get(self,request):
        self.content.update(csrf(request))
        self.content['create_issue_status_form'] = CreateIssueStatusForm()
        return render(request, self.template_name, self.content)

    def post(self,request):
        return render(request, self.template_name)


class CreateIssuePriorityForm(ModelForm):
    class Meta:
        model = IssuePriority
        fields = [
            'status',
        ]


class CreateIssuePriorityView(View):
    template_name = 'issue/createissuepriority.html'
    content = {}

    def get(self,request):
        self.content.update(csrf(request))
        self.content['create_issue_priority_form'] = CreateIssuePriorityForm()
        return render(request, self.template_name, self.content)

    def post(self,request):
        return render(request, self.template_name)


class CreateIssueCharForm(ModelForm):
    class Meta:
        model = IssueCharField
        fields = [
            'name',
        ]


class CreateIssueCharView(View):
    template_name = 'issue/createissuechar.html'
    content = {}

    def get(self,request):
        self.content.update(csrf(request))
        self.content['create_issue_char_form'] = CreateIssueCharForm()
        return render(request, self.template_name, self.content)

    def post(self,request):
        return render(request, self.template_name)


class CreateIssueTextForm(ModelForm):
    class Meta:
        model = IssueTextField
        fields = [
            'name',
        ]


class CreateIssueTextView(View):
    template_name = 'issue/createissuetext.html'
    content = {}

    def get(self,request):
        self.content.update(csrf(request))
        self.content['create_issue_text_form'] = CreateIssueTextForm()
        return render(request, self.template_name, self.content)

    def post(self,request):
        return render(request, self.template_name)