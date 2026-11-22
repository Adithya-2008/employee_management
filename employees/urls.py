from django.urls import path

from employees.view.employee_view import EmployeeCreateView, EmployeeDetailView,EmployeeByPreviousOrganisationView,EmployeeByCurrentOrganisationView,EmployeeByDesignationView,EmployeeByOrganisationView
from employees.view.organisation_view import OrganisationView
from employees.view.employment_history_view import EmploymentHistoryView
from employees.view.employee_list_view import EmployeeListView


urlpatterns = [
    path('employees/create/',EmployeeCreateView.as_view(),name="create-employees"),
    path('organisations/create/',OrganisationView.as_view(),name="create-organisation"),
    path('employees/<int:emp_id>/employment-history/',EmploymentHistoryView.as_view(),name="employment-history"),
    path('employees/<int:emp_id>/',EmployeeDetailView.as_view(),name="get-employee-details"),
    path('employees/', EmployeeListView.as_view(), name="get-employees-by-ids"),
    path('employees/by-previous-organisation/<int:org_id>/',EmployeeByPreviousOrganisationView.as_view(),name='employees-by-previous-organisation'),
    path('employees/by-current-organisation/<int:org_id>/',EmployeeByCurrentOrganisationView.as_view(),name='employees-by-current-organisation'),
    path('employees/by-current-organisation-designation/<int:org_id>/<str:designation>/',EmployeeByDesignationView.as_view(),name='employees-by-current-organisation-designation'),
    path('employees/by-organisation/<int:org_id>/',EmployeeByOrganisationView.as_view(),name='employees-by-organisation'),
]