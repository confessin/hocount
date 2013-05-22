from google.appengine.ext.db import djangoforms

import models


class DawgForm(djangoforms.ModelForm):
    class Meta:
        model = models.Dawg
        exclude = ['added_by', 'hoes', 'ytmnds']
