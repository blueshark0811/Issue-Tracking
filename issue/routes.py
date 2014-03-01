from django.conf.urls import patterns, include, url



urlpatterns = patterns('',
    url(r'^create/', include('issue.urls.create', namespace='create')),
    url(r'^view/', include('issue.urls.view', namespace='view')),
    url(r'^delete/', include('issue.urls.delete', namespace='delete')),
    url(r'^edit/', include('issue.urls.edit', namespace='edit')),
    url(r'^search/', include('issue.urls.search', namespace='search')),
)
