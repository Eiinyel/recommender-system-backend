from django.contrib import admin
from django.utils.translation import ugettext as _

from recommender.models import *

admin.site.site_header = _('Groupal Touristic Recommender System')
admin.site.index_title = _('Administration')
admin.site.site_title = _('Groupal Touristic Recommender System')


class CustomUserAdmin(admin.ModelAdmin):
    search_fields = ['email', ]

    def save_model(self, request, obj, form, change):
        # Encrypt password from admin if it's not encrypted
        if obj.password and not obj.password[0:20] == 'pbkdf2_sha256$36000$':
            obj.set_password(obj.password)
        super(CustomUserAdmin, self).save_model(request, obj, form, change)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Item)
admin.site.register(ItemAttribute)
admin.site.register(Group)
admin.site.register(Valoration)
admin.site.register(ContextSegment)
admin.site.register(Recommendation)
admin.site.register(City)
admin.site.register(Implication)
admin.site.register(Antecedent)
admin.site.register(Consequent)
admin.site.register(UserContext)
admin.site.register(AttributeCategory)
admin.site.register(PertenanceGrade)
admin.site.register(PreferenceGrade)
