from django.conf.urls import url
from django.contrib import admin
from rest_framework_mongoengine import routers
from microservice import views
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r"book", views.BookView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='Sorting Service'))
]

urlpatterns += router.urls
