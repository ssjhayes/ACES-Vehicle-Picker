from django.contrib import admin
from django.urls import include, path
from vehicle_api import views as api_views

# # automatically generate urls for generic endpoints
# router = routers.DefaultRouter()
# router.register(r'users', api_views.UserViewSet)
# router.register(r'groups', api_views.GroupViewSet)

urlpatterns = [
	path('admin/', admin.site.urls),
	# path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
