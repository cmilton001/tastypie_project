from tastypie.resources import ModelResource
from tastypie.constants import ALL

from talk.models import Talk


class TalkResource(ModelResource):
    class Meta:
        queryset = Talk.objects.all()
        resource_name = 'talk'
        filtering = {'id': ALL}
