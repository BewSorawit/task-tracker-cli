from task_tracker.models.task import Task
from task_tracker.utils.filehandle import FileHandle

from typing import List

class TaskService:
    def __init__(self,filename:str):
        self.file_handle = FileHandle(filename)
        
    def add_task(self, task: Task):
        tasks = self.file_handle.read_file()
        
        task_ids = [task["id"] for task in tasks if task["id"] is not None]
        next_id = max(task_ids, default=0) + 1
        task.task_id = next_id
        
        tasks.append(task.to_dict())
        self.file_handle.write_file(tasks)
    
    def list_all_tasks(self) -> List[dict]:
        return self.file_handle.read_file()
    
    def list_tasks_by_status(self, status:str) -> List[dict]:
        tasks = self.file_handle.read_file()
        return [task for task in tasks if task["status"] == status]
    
    def update_status_by_id(self,task_id:int,new_status) -> bool:
        tasks = self.file_handle.read_file()
        for task in tasks:
            if task['id'] == task_id:
                task['status'] = new_status
                self.file_handle.write_file(tasks)
                return True
        return False
    
    def update_description_by_id(self,task_id:int,description:str) -> bool:
        tasks = self.file_handle.read_file()
        for task in tasks:
            if task['id'] == task_id:
                task['description'] = description
                self.file_handle.write_file(tasks)
                return True
        return False
    
    def delete_task_by_id(self,task_id:int)->bool:
        tasks = self.file_handle.read_file()
        for task in tasks:
            if task['id'] == task_id:
                tasks.remove(task)
                self.file_handle.write_file(tasks)
                return True
        print("Not found that id")
        return False
    