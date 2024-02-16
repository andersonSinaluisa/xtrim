from dataclasses import dataclass
from datetime import datetime

@dataclass
class Audit:
    id: int
    user_id: int
    action: str
    path: str
    element: str
    os: str
    browser: str
    device: str
    size_screen: str
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime
    
    
def audit_factory(id, user_id, action, path, element, os, browser, device, size_screen, created_at, updated_at, deleted_at):
    return Audit(id, user_id, action, path, element, os, browser, device, size_screen, created_at, updated_at, deleted_at)