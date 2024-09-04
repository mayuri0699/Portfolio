from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(UserAuth)
class UserAuthAdmin(admin.ModelAdmin):
    list_display = UserAuth.DisplayList
    search_fields = UserAuth.searchable_fields
@admin.register(ProfileTable)
class ProfileTableAdmin(admin.ModelAdmin):
    list_display = ProfileTable.DisplayList
    search_fields = ProfileTable.searchable_fields

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = Education.DisplayList
    search_fields = Education.searchable_fields

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = Skill.DisplayList
    search_fields = Skill.searchable_fields

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = Experience.DisplayList
    search_fields = Experience.searchable_fields

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = Projects.DisplayList
    search_fields = Projects.searchable_fields

@admin.register(Interests)
class InterestsAdmin(admin.ModelAdmin):
    list_display = Interests.DisplayList
    search_fields = Interests.searchable_fields

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = Language.DisplayList
    search_fields = Language.searchable_fields

@admin.register(AchievementAwards)
class AchievementAwardsAdmin(admin.ModelAdmin):
    list_display = AchievementAwards.DisplayList
    search_fields = AchievementAwards.searchable_fields

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = Activity.DisplayList
    search_fields = Activity.searchable_fields

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = Contacts.DisplayList
    search_fields = Contacts.searchable_fields



# admin.site.register(Education)
# admin.site.register(Skill)
# admin.site.register(Experience)
# admin.site.register(Projects)
# admin.site.register(Interests)
# admin.site.register(Language)
# admin.site.register(AchievementAwards)
# admin.site.register(Activity)
# admin.site.register(Contacts)