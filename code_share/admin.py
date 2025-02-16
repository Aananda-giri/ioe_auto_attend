from django.contrib import admin
from .models import Code#, File, Photo     #, Comment

'''
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
'''

class CodeAdmin(admin.ModelAdmin):
    # A handy constant for the name of the alternate database.
    # using = 'fuse_attend'  # using database router
    using = 'default'  # using database router
    #fields = ['created_on', 'title', 'tags', 'author', 'email', 'id']

    ordering = ['-created_on']  # order by created_on

    def save_model(self, request, obj, form, change):
        # Tell Django to save objects to the 'other' database.
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        obj.delete(using=self.using)

    def get_queryset(self, request):
        # Tell Django to look for objects on the 'other' database.
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # Tell Django to populate ForeignKey widgets using a query
        # on the 'other' database.
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        # Tell Django to populate ManyToMany widgets using a query
        # on the 'other' database.
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)


# admin.site.register(Photo, CodeAdmin)

# from django.contrib import admin
# from .models import File
# from .functions import DriveFunctions
# class FileAdmin(admin.ModelAdmin):
#     def delete_queryset(self, request, queryset):
#         # Delete Google Drive files for each instance in the queryset
#         for instance in queryset:
#             print(f'instance: {instance}')
#             # DriveFunctions.delete_files(instance.drive_links)
#             instance.delete()

# admin.site.register(File, FileAdmin)


from django.contrib import admin
from .models import Codes, Files, Container
from .functions import DriveFunctions
class FilesAdmin(admin.ModelAdmin):

    def delete_queryset(self, request, queryset):
        # Delete Google Drive files for each instance in the queryset
        for instance in queryset:
            print(f'instance: {instance}')
            DriveFunctions.delete_files(str(instance.link))
            instance.delete()
    def delete_model(self, request, obj):
        # Tell Django to delete objects from the 'other' database
        print(f'obj: {obj},\n obj.link: {obj.link}')
        DriveFunctions.delete_files(str(obj.link))
        obj.delete()
class ContainerAdmin(admin.ModelAdmin):
    ordering = ['-created_on']  # order by created_on

admin.site.register(Code, CodeAdmin)
admin.site.register(Codes)
admin.site.register(Files, FilesAdmin)
admin.site.register(Container, ContainerAdmin)