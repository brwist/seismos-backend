# flake8: noqa F401
from .auth import Login, UserResource
from .project import ProjectGeneral, ProjectCreate, ProjectListGet, ProjectDownload
from .tracking_sheet import (
    TrackingSheetResource,
    TrackingSheetCreateResource,
    TrackingSheetStageList,
)
from .qc_report import QCReport, QCReportApprove
from .input_data import InputData
from .daily_log import DailyLogResource
from .deafult_values import DefaultValuesResource
from .db_restore import DatabaseRestore
from .sync_cloud import SyncCloud

ENDPOINTS_MAP = {
    Login: "/auth",
    UserResource: "/user",
    ProjectGeneral: "/project/<project_uuid>",
    ProjectCreate: "/project",
    ProjectDownload: "/project/download/<project_uuid>",
    ProjectListGet: "/project/list",
    TrackingSheetResource: "/tracking-sheet/<stage_uuid>",
    TrackingSheetStageList: "/tracking-sheet/stage_list/<well_uuid>",
    TrackingSheetCreateResource: "/tracking-sheet/create/<well_uuid>",
    QCReport: "/qc-report/<well_uuid>",
    QCReportApprove: "/qc-report/approve",
    InputData: "/input-data/<data_area>",
    DailyLogResource: "/daily-log/<well_uuid>",
    DefaultValuesResource: "/default-values/<well_uuid>",
    DatabaseRestore: "/admin/db_restore/<backup_index>",
    SyncCloud: "/sync-cloud/<project_uuid>",
}
