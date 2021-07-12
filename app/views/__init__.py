# flake8: noqa F401
from .auth import Login
from .project import Project, ProjectCreate
from .oc_report import OCReport, OCReportExport

ENDPOINTS_MAP = {
    Login: "/auth",
    Project: "/project/<project_id>",
    ProjectCreate: "/project",
    OCReport: "/oc-report",
    OCReportExport: "/oc-report/export",
}
