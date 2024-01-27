import os
from django.conf import settings
import os

def delete_file(request,url):
    if request.FILES:
            delete_url=os.path.join(settings.BASE_DIR,"media","uploads",os.path.basename(url))
            os.remove(delete_url)