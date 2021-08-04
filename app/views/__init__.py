# flake8: noqa F401
from .auth import Login
from .project import ProjectGet, ProjectCreate
from .tracking_sheet import TrackingSheet, CreateTrackingSheet
from .oc_report import OCReport, OCReportExport
from .input_data import InputData
from .daily_log import DailyLogResource
from .deafult_volumes import DefaultVolumesResource

ENDPOINTS_MAP = {
    Login: "/auth",
    ProjectGet: "/project/<project_id>",
    ProjectCreate: "/project",
    TrackingSheet: "/tracking-sheet/<tracking_sheet_id>",
    CreateTrackingSheet: "/tracking-sheet/create/<well_id>",
    OCReport: "/oc-report",
    OCReportExport: "/oc-report/export",
    InputData: "/input-data",
    DailyLogResource: "/daily-log",
    DefaultVolumesResource: "/default-value/<well_id>",
}
