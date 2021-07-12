# flake8: noqa F401
from .auth import Login
from .project import Project, ProjectCreate
from .tracking_sheet import TrackingSheet, CreateTrackingSheet

ENDPOINTS_MAP = {
    Login: "/auth",
    Project: "/project/<project_id>",
    ProjectCreate: "/project",
    TrackingSheet: "/tracking-sheet/<tracking_sheet_id>",
    CreateTrackingSheet: "/tracking-sheet",
}
