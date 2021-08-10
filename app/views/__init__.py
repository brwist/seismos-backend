# flake8: noqa F401
from .auth import Login
from .project import ProjectGet, ProjectCreate, ProjectListGet
from .tracking_sheet import (
    TrackingSheetResource,
    CreateTrackingSheet,
    TrackingSheetStageList,
)
from .oc_report import QCReport, QCReportExport
from .input_data import InputData
from .daily_log import DailyLogResource, DailyLogCreateResource
from .deafult_volumes import DefaultVolumesResource

ENDPOINTS_MAP = {
    Login: "/auth",
    ProjectGet: "/project/<project_id>",
    ProjectCreate: "/project",
    ProjectListGet: "/project/list",
    TrackingSheetResource: "/tracking-sheet/<tracking_sheet_id>",
    CreateTrackingSheet: "/tracking-sheet/create/<well_id>",
    TrackingSheetStageList: "/tracking-sheet/stage_list/<well_id>",
    QCReport: "/oc-report",
    QCReportExport: "/oc-report/export",
    InputData: "/input-data",
    DailyLogResource: "/daily-log/<well_id>",
    DailyLogCreateResource: "/daily-log",
    DefaultVolumesResource: "/default-volumes/<well_id>",
}
