from django.urls import path
from .views import *
from . import views


app_name= 'store'

urlpatterns = [
    #path('', views.index, name='post_list'),
    path('', HomeView.as_view(), name='home'),
    path('aboutus/',AboutView.as_view(), name='aboutus'),
    path('contact/',ContactView.as_view(), name='contact'),
    path('allcategories/', CategoryView.as_view(), name='allcategories'),
    path('productdetail/<slug:slug>/', ProductDetailView.as_view(), name='productdetail'),

    path('add-to-cart/<int:pro_id>/', AddToCartView.as_view(),name='addtocart'),
    path('mycart/', MyCartView.as_view(), name='mycart'),
    path('managecart/<int:cp_id>/', ManageCartView.as_view(), name='managecart'),
    path('emptycart/', EmptyCartView.as_view(), name='emptycart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),

    path('khaltipayment/', KhaltiPaymentView.as_view(), name='khaltipayment'),
    path('khaltiverify/', KhaltiVerifyView.as_view(), name='khaltiVerify'),
    path('razorpaysuccess/', RazorpaySucces.as_view(), name='razorpaysuccess'),
    path('success/', views.success, name='success'),

    path('register/', CustomerRegistrationView.as_view(), name='customerregistration'),
    path('logout/', CustomerLogoutView.as_view(), name='customerlogout'),
    path('login/', CustomerLoginView.as_view(), name='customerlogin'),

    path('profile/', CustomerProfileView.as_view(), name='customerprofile'),
    path('profile/order-<int:pk>/', CustomerOrderDetailView.as_view(), name='customerorderdetail'),
    path('search', SearchView.as_view(), name='search'),
    path('forgotpassword/', ForgotPasswordView.as_view(), name='forgotpassword'),
    path('password-reset/<email>/<token>', PasswordResetView.as_view(), name='passwordreset'),


    path('admin-login/', AdminLoginView.as_view(), name='adminlogin'),
    path('admin-home/', AdminHomeView.as_view(),name='adminhome'),
    path('admin-order/<int:pk>/', AdminOrderDetailView.as_view(), name='adminorderdetail'),
    path('admin-all-orders/', AdminOrderListView.as_view(), name='adminorderlist'),

    path('admin-order-<int:pk>-change/', AdminOrderStatusChangeView.as_view(), name='adminorderstatuschange'),
    path('admin-product/list/', AdminProductListView.as_view(), name='adminproductlist'),
    path('admin-product/add/', AdminProductCreateView.as_view(),name='adminproductcreate'),

    #for seperate blog
    path('samplecontactform/',views.contact, name='samplecontactform'),

    path('privacypolicy/',PrivacyPolicyView.as_view(), name='privacypolicy'),
    path('retexc/',RetexcView.as_view(), name='retexc'),
    path('shippingpolicy/',ShippingPolicyView.as_view(), name='shippingpolicy'),
    path('termsandconditions/',TermsandConditionsView.as_view(), name='termsandconditions'),

]