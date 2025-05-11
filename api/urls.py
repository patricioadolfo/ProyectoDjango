from rest_framework import routers
from api.viewset import EnvioViewset

router = routers.SimpleRouter()

router.register('envio', EnvioViewset)

urlpatterns = router.urls
