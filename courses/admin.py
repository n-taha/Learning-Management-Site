from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from courses.models import (
    Course, Payment, UserCourse,
    Tag, Prerequisite, Learning,
    Video, ManualPayment,AdditionalInfo
)

# ---------- Base Admin for custom CSS/JS ----------
class BaseAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('courses/css/custom_admin.css',)
        }
        js = ('courses/js/custom_admin.js',)


# ---------- Inline Admin ----------
class TagInline(admin.TabularInline):
    model = Tag
    extra = 1
    classes = ["collapse"]

class VideoInline(admin.TabularInline):
    model = Video
    extra = 1
    show_change_link = True

class LearningInline(admin.TabularInline):
    model = Learning
    extra = 1
    classes = ["collapse"]

class PrerequisiteInline(admin.TabularInline):
    model = Prerequisite
    extra = 1
    classes = ["collapse"]


# ---------- Course Admin ----------
@admin.register(Course)
class CourseAdmin(BaseAdmin):
    inlines = [TagInline, LearningInline, PrerequisiteInline, VideoInline]

    list_display = (
        "name",
        "colored_price",
        "colored_discount",
        "active_badge",
    )
    list_filter = ("active", "discount")
    search_fields = ("name",)
    list_per_page = 10

    def colored_price(self, course):
        return format_html("<b style='color:#0dcaf0;'>৳ {}</b>", course.price)

    def colored_discount(self, course):
        color = "#198754" if course.discount and course.discount > 0 else "#6c757d"
        return format_html("<span style='color:{};'>{}%</span>", color, course.discount)

    def active_badge(self, course):
        if getattr(course, "active", False):
            return format_html('<span class="course-badge-active">Active</span>')
        return format_html('<span class="course-badge-inactive">Inactive</span>')

    colored_price.short_description = "Price"
    colored_discount.short_description = "Discount"
    active_badge.short_description = "Status"


# ---------- Payment Admin ----------
@admin.register(Payment)
class PaymentAdmin(BaseAdmin):
    list_display = ("order_id", "user_link", "course_link")
    list_filter = ("course",)
    search_fields = ("order_id", "user__username")
    list_per_page = 15

    def user_link(self, obj):
        url = reverse("admin:auth_user_change", args=(obj.user.id,))
        return format_html("<a href='{}' target='_blank'>{}</a>", url, obj.user)

    def course_link(self, obj):
        url = reverse("admin:courses_course_change", args=(obj.course.id,))
        return format_html("<a href='{}' target='_blank'>{}</a>", url, obj.course)

    user_link.short_description = "User"
    course_link.short_description = "Course"


# ---------- UserCourse Admin ----------
@admin.register(UserCourse)
class UserCourseAdmin(BaseAdmin):
    list_display = ("id", "user_link", "course_link")
    list_filter = ("course",)
    search_fields = ("user__username", "course__name")
    list_per_page = 20

    def user_link(self, obj):
        url = reverse("admin:auth_user_change", args=(obj.user.id,))
        return format_html("<a href='{}' target='_blank'>{}</a>", url, obj.user)

    def course_link(self, obj):
        url = reverse("admin:courses_course_change", args=(obj.course.id,))
        return format_html("<a href='{}' target='_blank'>{}</a>", url, obj.course)

    user_link.short_description = "User"
    course_link.short_description = "Course"


# ---------- ManualPayment Admin (minimal fields only) ----------
@admin.register(ManualPayment)
class ManualPaymentAdmin(BaseAdmin):
    list_display = ("transaction_id", "user", "course")
    search_fields = ("transaction_id", "user__username")
    list_per_page = 20


# ---------- Video Admin ----------
@admin.register(Video)
class VideoAdmin(BaseAdmin):
    list_display = ("title", "course", "serial_number")
    list_filter = ("course",)
    search_fields = ("title",)
    list_per_page = 30


admin.site.register(AdditionalInfo)

# ---------- Global Admin Customization ----------
admin.site.site_header = "🌤 SkyCourse Admin"
admin.site.site_title = "SkyCourse Control"
admin.site.index_title = "SkyCourse Control Center"
