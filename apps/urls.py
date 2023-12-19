from django.urls import path, include

urlpatterns = [
    path('', include("apps.core.urls")),
    path('users/', include("apps.users.urls")),
    path('books/', include("apps.books.urls")),
    path('authors/', include("apps.authors.urls")),
    path('categories/', include("apps.categories.urls"))
]
