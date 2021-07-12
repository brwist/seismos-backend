# flake8: noqa F401
from .auth import Login
from .project import Project, ProjectCreate
from .daily_log import DailyLog

ENDPOINTS_MAP = {
    Login: "/auth",
    Project: "/project/<project_id>",
    ProjectCreate: "/project",
    DailyLog: "/daily-log",
}
