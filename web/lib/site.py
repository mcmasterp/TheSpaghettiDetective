from django.contrib.sites.models import Site
from django.conf import settings
import re

def build_full_url(url):
    protocol = 'https://' if settings.SITE_USES_HTTPS else 'http://'
    domain_name = Site.objects.get_current().domain
    normalized_url = re.sub(r'^/', '', url)
    return '{}{}/{}'.format(protocol, domain_name, normalized_url)
