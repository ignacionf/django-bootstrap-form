from django.conf import settings


BOOTSTRAP_COLUMN_COUNT = getattr(settings, 'BOOTSTRAP_COLUMN_COUNT', 12)
BOOTSTRAP_LABEL_COLS = getattr(settings, 'BOOTSTRAP_LABEL_COLS', "col-sm-2 col-lg-2")
