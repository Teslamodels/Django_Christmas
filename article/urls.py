from django.urls import path
from .views import (
    ArticleHome,
    ArticleDetail,
    ArticleUpdate,
    ArticleDelete,
    ArticleCreate,
)

urlpatterns = [
    path('<int:pk>/edit/', ArticleUpdate.as_view(), name='update'),
    path('<int:pk>/', ArticleDetail.as_view(), name='detail'),
    path('<int:pk>/delete/', ArticleDelete.as_view(), name='delete'),
    path('new/', ArticleCreate.as_view(), name='create'),
    path('', ArticleHome.as_view(), name='article'),
]