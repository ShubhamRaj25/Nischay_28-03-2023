from django.contrib import admin

# from .models import digitized_file_status, upload_file_details,downloaded_file_details,los_did_cid_generation,bureau
from .models import *

admin.site.register(digitized_file_status)
admin.site.register(downloaded_file_details)
admin.site.register(upload_file_details)
admin.site.register(los_did_cid_generation)
admin.site.register(bureau)
admin.site.register(los_lid_generation)
admin.site.register(bank_bank)
admin.site.register(customer_allocation)
admin.site.register(bureau_account_segment_tl)
