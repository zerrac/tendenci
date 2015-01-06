from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.conf import settings as d_settings
from django.template import Context, Template

from tendenci import __version__ as version
from tendenci.core.site_settings.models import Setting
from tendenci.core.site_settings.cache import SETTING_PRE_KEY

def settings(request):
    """Context processor for settings
    """
    key = [d_settings.CACHE_PRE_KEY, SETTING_PRE_KEY, 'all']
    key = '.'.join(key)

    settings = cache.get(key)
    if not settings:
        settings = Setting.objects.all()
        is_set = cache.add(key, settings)
        if not is_set:
            cache.set(key, settings)

    contexts = {}
    for setting in settings:
        context_key = [setting.scope, setting.scope_category,
                       setting.name]
        context_key = '_'.join(context_key)

        value = setting.get_value().strip()

        if setting.data_type == 'boolean':
            value = value[0].lower() == 't'
        if setting.data_type == 'int':
            if value.strip(): value = int(value.strip())
            else: value = 0 # default to 0
        # Handle context for the social_media addon's
        # contact_message setting
        if setting.name == 'contact_message':
            page_url = request.build_absolute_uri()
            message_context = {'page_url': page_url}
            message_context = Context(message_context)
            message_template = Template(value)
            value = message_template.render(message_context)

        contexts[context_key.upper()] = value

    contexts['TENDENCI_VERSION'] = version

    contexts['USE_I18N'] = d_settings.USE_I18N

    return contexts


def app_dropdown(request):
    """
    Context processor for getting the template
    needed for a module setting dropdown
    """
    context = {}
    path = request.get_full_path().strip('/')
    path = path.split('/')

    if len(path) < 3:
        context.update({'ADMIN_MENU_APP_TEMPLATE_DROPDOWN': 'site_settings/top_nav.html'})

    else:
        if path[0] == 'settings' and path[1] == 'module':
            context.update({'ADMIN_MENU_APP_TEMPLATE_DROPDOWN': path[2]+'/top_nav.html'})
        else:
            context.update({'ADMIN_MENU_APP_TEMPLATE_DROPDOWN': 'site_settings/top_nav.html'})

    return context


