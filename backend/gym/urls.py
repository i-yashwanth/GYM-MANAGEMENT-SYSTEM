from django.urls import path
from . import views

urlpatterns = [
	path('activeMemberships/', views.activeMemberships),
	path('renewMembership/', views.renewMembership, name="renewMembership"),
	path('viewProducts/', views.viewProducts, name='viewProducts'),
	path('groupTrainings/', views.viewGroupTrainings, name='viewGroupTrainings'),
	path('signForTraining/', views.signUpForTraining, name='signForTraining'),
	path('viewAllProducts/', views.viewAllProducts, name='viewAllProducts'),
	path('addProduct/', views.addProduct, name='addProduct'),
	path('test', views.test, name='test'),
]
