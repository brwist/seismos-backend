# flake8: noqa F401
from .auth import Login
from .project import Project, ProjectCreate
from .deafult_value import DefaultValue

ENDPOINTS_MAP = {
    Login: "/auth",
    Project: "/project/<project_id>",
    ProjectCreate: "/project",
    DefaultValue: "/default-value",
}
