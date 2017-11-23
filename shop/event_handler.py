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

    #LISTING PRODUCT DETAILS REQUEST
    def product_detail(request, id, slug):
        product = get_object_or_404(Product, id=id, slug=slug, available=True)
        return render(request,
                      'shop/product/detail.html',
                      {'product': product})

    #LISTING THE PRODUCTS REQUEST
    def product_list(request, category_slug=None):
        category = None
        categories = Category.objects.all()
        products = Product.objects.filter(available=True)
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
        return render(request, 'shop/product/list.html', {'category': category,
                                                          'categories': categories,
                                                          'products': products})

    #LISTING ALL OF THE OPTIONS FOR THE CATEGORY ADMIN REQUEST
    def CategoryAdmin(admin.ModelAdmin):
        list_display = ['name', 'slug']
        prepopulated_fields = {'slug': ('name',)}
        return admin.site.register(Category, CategoryAdmin)

    #LISTING ALL OF THE OPTIONS FOR THE PRODUCT ADMIN REQUEST
    def ProductAdmin(admin.ModelAdmin):
        list_display = ['name', 'slug', 'category', 'price', 'stock', 'available', 'created', 'updated']
        list_filter = ['available', 'created', 'updated', 'category']
        list_editable = ['price', 'stock', 'available']
        prepopulated_fields = {'slug': ('name',)}
        return admin.site.register(Product, ProductAdmin)
