# flake8: noqa F401
from .auth import Login, UserResource
from .project import ProjectGet, ProjectCreate, ProjectListGet
from .tracking_sheet import (
    TrackingSheetResource,
    CreateTrackingSheet,
    TrackingSheetStageList,
)
from .qc_report import QCReport, QCReportExport
from .input_data import InputData
from .daily_log import DailyLogResource, DailyLogCreateResource
from .deafult_volumes import DefaultVolumesResource

ENDPOINTS_MAP = {
    Login: "/auth",
    UserResource: "/user",
    ProjectGet: "/project/<project_id>",
    ProjectCreate: "/project",
    ProjectListGet: "/project/list",
    TrackingSheetResource: "/tracking-sheet/<tracking_sheet_id>",
    CreateTrackingSheet: "/tracking-sheet/create/<well_id>",
    TrackingSheetStageList: "/tracking-sheet/stage_list/<well_id>",
    QCReport: "/qc-report/<well_id>",
    QCReportExport: "/qc-report/approve",
    InputData: "/input-data",
    DailyLogResource: "/daily-log/<well_id>",
    DailyLogCreateResource: "/daily-log",
    DefaultVolumesResource: "/default-volumes/<well_id>",
}
