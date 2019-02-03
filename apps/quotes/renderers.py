import json
from rest_framework.renderers import JSONRenderer


class QuoteJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        errors = data.get('errors', None)

        if errors is not None:
            return super(QuoteJSONRenderer, self).render(data)

    return json.dumps({
        'quotes': data
    })

