from django import forms
from .models import Post, TaskProposal
from django import forms
from django.contrib.auth import get_user_model
from .models import Department, GroupChat
from django import forms
from .models import Notification, Department, Task, User
from .models import Notification, Department, Task


from django import forms
from .models import Notification, Department, Task, User

User = get_user_model()

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'avatar_url']
        labels = {
            'title': '',
            'avatar_url': 'Hình ảnh đính kèm',
        }
        widgets = {
            'title': forms.Textarea(attrs={
                'placeholder': 'Nhập nội dung bài viết',
                'class': 'form-control',
                'rows': 4
            }),
            'avatar_url': forms.URLInput(attrs={
                'placeholder': 'Nhập URL hình ảnh',
                'class': 'form-control'
            }),
        }


class EmployeeSearchForm(forms.Form):
    query = forms.CharField(
        required=False,
        label='Tìm kiếm',
        widget=forms.TextInput(attrs={'placeholder': 'Tìm theo tên...'})
    )
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        required=False,
        label='Bộ phận',
        empty_label='Tất cả bộ phận'
    )

class CreateGroupForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Chọn thành viên'
    )

    class Meta:
        model = GroupChat
        fields = ['group_name', 'members']


class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['title', 'content', 'recipient_type', 'departments', 'image_url']

    departments = forms.ModelMultipleChoiceField(queryset=Department.objects.all(), required=False)
    recipient_type = forms.ChoiceField(choices=[('all', 'All'), ('department', 'Department')], required=True)
    image_url = forms.ImageField(required=False)  # Trường này để xử lý ảnh đính kèm
#
# class TaskAssignmentForm(forms.ModelForm):
#     users = forms.ModelMultipleChoiceField(
#         queryset=User.objects.none(),  # Khởi tạo rỗng, sẽ fill trong __init__
#         required=True,
#         widget=forms.CheckboxSelectMultiple,
#         label="Giao cho"
#     )
#     deadline = forms.DateField(
#         widget=forms.DateInput(attrs={'type': 'date'}),
#         required=True,
#         label="Thời hạn"
#     )
#
#
#     def __init__(self, *args, **kwargs):
#         user = kwargs.pop('user', None)
#         super().__init__(*args, **kwargs)
#
#         # Lọc danh sách user cùng phòng ban và loại bỏ chính người giao việc
#         if user and user.department:
#             self.fields['users'].queryset = User.objects.filter(department=user.department).exclude(id=user.id)
#         else:
#             self.fields['users'].queryset = User.objects.none()
#
#         # Ẩn trường status nếu có trong form (hoặc loại khỏi Meta.fields cũng được)
#         if 'status' in self.fields:
#             self.fields['status'].widget = forms.HiddenInput()
#
#     class Meta:
#         model = Task
#
#         # KHÔNG đưa 'status' vào fields để tránh hiện trên giao diện
#         fields = ['task_name', 'description','deadline','image', 'document']
#         labels = {
#             'task_name': 'Tiêu đề',
#             'description': 'Mô tả chi tiết',
#             'image': 'Hình ảnh đính kèm',
#             'document': 'Tài liệu liên quan',
#         }
class TaskAssignmentForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.none(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control', 'id': 'users'}),
        required=True,
        label="Giao cho"
    )

    deadline = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'deadline'}),
        required=True,
        label="Thời hạn"
    )

    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'id': 'image'})
    )

    document = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'id': 'document'})
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and user.department:
            self.fields['users'].queryset = User.objects.filter(department=user.department).exclude(id=user.id)

    class Meta:
        model = Task
        fields = ['task_name', 'description', 'users', 'deadline', 'image', 'document']
        widgets = {
            'task_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'task_name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'description'})
        }

class TaskProposalForm(forms.ModelForm):
    class Meta:
        model = TaskProposal
        fields = ['to_department', 'title', 'description', 'image', 'document']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'to_department': 'Gửi đến phòng ban',
            'title': 'Tiêu đề',
            'description': 'Mô tả chi tiết',
            'image': 'Hình ảnh đính kèm',
            'document': 'Tài liệu liên quan',
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Lấy và loại bỏ 'user' khỏi kwargs để tránh lỗi
        super(TaskProposalForm, self).__init__(*args, **kwargs)
        if user and hasattr(user, 'department'):
            self.fields['to_department'].queryset = Department.objects.exclude(id=user.department.id)
        else:
            self.fields['to_department'].queryset = Department.objects.all()

class TaskProposalReviewForm(forms.ModelForm):
    class Meta:
        model = TaskProposal
        fields = ['status', 'feedback']
        widgets = {
            'feedback': forms.Textarea(attrs={'rows': 3}),
        }
