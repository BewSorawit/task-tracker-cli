import datetime


class Task:
    def __init__(
        self,
        task_id: int,
        description: str,
        status: str = "To Do",
        created_at=None,
        updated_at=None,
    ):
        self.task_id = task_id
        self.description = description
        self.status = status
        self.created_at = created_at or datetime.datetime.now()
        self.updated_at = updated_at or datetime.datetime.now()

    def to_dict(self):
        return {
            "id": self.task_id,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    def __repr__(self):
        return (
            f"Task(task_id={self.task_id}, description='{self.description}', "
            f"created_at={self.created_at!r}, updated_at={self.updated_at!r})"
        )
