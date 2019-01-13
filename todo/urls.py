from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from todos.views import Index, TodoActions

router = DefaultRouter()
router.register('todos', Index, base_name="all_todos")

urlpatterns = [
    path('admin/', admin.site.urls),

    path('todoactions/<type>/<int:todo_id>/', TodoActions.as_view())

]

urlpatterns += router.urls
