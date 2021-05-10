# Generated by Django 2.2.20 on 2021-05-04 15:36

import os
from django.db import migrations


def change_profile_photo_update_url(apps, schema_editor):
    """
    Update two templates, top_menu/_profile_dropdown.html and profiles/index.html, 
    that are pulled down to the site.

    Change the URL for profile photo update from gravatar.com to the upload url on the site
    as users now can upload profile photos. 
    
    In the templates/top_menu/_profile_dropdown.html, update from //gravatar.com/ to
    {% url 'profile.upload_photo' user.id %}
    
    In the templates/profiles/index.html, update from //gravatar.com/ to 
    {% url 'profile.upload_photo' user_this.id %}, and from "Create / update your gravatar" 
    to "Change profile photo"

    """
    from tendenci.apps.theme.utils import get_theme_root
    dir_path = get_theme_root()

    file_path = f'{dir_path}/templates/top_menu/_profile_dropdown.html'
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
            content = content.replace('//gravatar.com/',
                                      "{% url 'profile.upload_photo' user.id %}")

        with open(file_path, 'w') as f:
            f.write(content)

    file_path = f'{dir_path}/templates/profiles/index.html'
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
            content = content.replace('https://en.gravatar.com',
                                      "{% url 'profile.upload_photo' user.id %}")
            content = content.replace('//gravatar.com/',
                                      "{% url 'profile.upload_photo' user_this.id %}")
            content = content.replace('Create / update your gravatar',
                                      "Change profile photo")

        with open(file_path, 'w') as f:
            f.write(content)

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0016_profile_photo'),
    ]

    operations = [
        migrations.RunPython(change_profile_photo_update_url),
    ]