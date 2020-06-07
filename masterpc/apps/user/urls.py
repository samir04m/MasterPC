from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('pc/create/', CreatePc.as_view(), name='create_pc'),
    path('pc/<int:pk>/update', UpdatePc.as_view(), name='update_pc'),
    path('pc/<int:pk>/delete/', DeletePc.as_view(), name='delete_pc'),
    path('pc/<int:pk>/', DetailPc.as_view(), name='detail_pc'),
    
    path('pc/<int:pc_id>/add/<str:name_component>/<int:comp_id>', select_component, name='select_component'),
    path('pc-add-component/<int:pc_id>/<str:name_component>/<int:store_id>', add_component, name='add_component'),
    path('pc-remove-component/<int:pc_id>/<str:name_component>/<int:store_id>', remove_component, name='remove_component'),
    path('pc-change-view/<int:pc_id>/<str:view>/', change_view, name='change_view'),
    
    # path('compare-pc/<int:id_pc1>/vs/<int:id_pc2>/', compare_pc, name='compare_pc'),
    path('compare-pc/', compare_pc, name='compare_pc'),

    path('signup/', UserRegister.as_view(), name='signup'),
    path('register-success/', register_success, name='register_success'),
]
