class EventHandler:

    #DEFAULT
    def __init__(self):
        self.value = "http://localhost/8000"

    #RETURNING THE RIGHT HTTP RESPONSE TO LISTENERS REQUEST
    def httpResponse(request):
        urlpatterns = [
            url(r'^admin/', admin.site.urls),
            url(r'^',include('shop.urls', namespace='shop'))
            url(r'^$', views.product_list, name='product_list'),
            url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
            url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
        ]
        return (urlpatterns[])
