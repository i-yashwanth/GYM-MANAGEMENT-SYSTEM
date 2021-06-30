from django.urls import path
from . import views
import gym.Views.shop as ShopViews
import gym.Views.product as ProductView
import gym.Views.membership as MembershipView
import gym.Views.groupTraining as GroupTrainingView

urlpatterns = [
	path('activeMemberships/', MembershipView.activeMemberships),
	path('renewMembership/', MembershipView.renewMembership, name="renewMembership"),
	path('createMembership/', MembershipView.createMembership, name="createMembership"),
	path('viewMemberships/', MembershipView.viewMemberships, name="viewMemberships"),

	path('product/', ProductView.ProductView.as_view(), name='productView'),
	path('viewProducts/', ProductView.viewProducts, name='viewProducts'),
	path('addProduct/', ProductView.addProduct, name='addProduct'),
	path('deleteProduct/', ProductView.deleteProductFromTheShop, name='deleteProduct'),

	path('groupTrainings/', GroupTrainingView.viewGroupTrainings, name='viewGroupTrainings'),
	path('createGroupTraining/', GroupTrainingView.createGroupTraining, name='createGroupTrainings'),
	path('signForTraining/', GroupTrainingView.signUpForTraining, name='signForTraining'),

	path('shop/', ShopViews.ShopView.as_view(), name="shop"),
	path('viewShops/', ShopViews.viewShops, name='viewShops'),
	path('createShop/', ShopViews.createShop, name='createShop'),
]
