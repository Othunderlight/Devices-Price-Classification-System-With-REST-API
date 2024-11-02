from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import MobilePhone

# Create Resource class for Import/Export functionality
class MobilePhoneResource(resources.ModelResource):
    class Meta:
        model = MobilePhone
        import_id_fields = ['id']  # Now we'll use id for importing
        skip_unchanged = True
        report_skipped = False
        fields = (
            'id', 'battery_power', 'blue', 'clock_speed', 'dual_sim', 'fc', 
            'four_g', 'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc',
            'px_height', 'px_width', 'ram', 'sc_h', 'sc_w', 'talk_time',
            'three_g', 'touch_screen', 'wifi', 'price_range'
        )

    # Add validation for boolean fields
    def before_import_row(self, row, **kwargs):
        """Convert 0/1 values to proper boolean for certain fields"""
        boolean_fields = ['blue', 'dual_sim', 'four_g', 'three_g', 'touch_screen', 'wifi']
        for field in boolean_fields:
            if field in row:
                row[field] = bool(int(row[field]))

@admin.register(MobilePhone)
class MobilePhoneAdmin(ImportExportModelAdmin):  # Changed from admin.ModelAdmin
    resource_class = MobilePhoneResource
    list_display = ['id', 'price_range', 'battery_power', 'ram', 'int_memory']
    list_filter = ['price_range', 'four_g', 'three_g', 'wifi', 'touch_screen']
    search_fields = ['id']
