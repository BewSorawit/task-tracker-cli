import argparse
import sys
from .models.task import Task
from .services.task_service import TaskService

file_name = "tasks.json"
task_service = TaskService(file_name)


def main():
    STATUS_CHOICES = ["done", "To Do", "progress"]
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    parser_add = subparsers.add_parser(name="add", help="Add a new task")
    parser_add.add_argument(
        dest="description", type=str, help="Description of the task"
    )

    # List command
    parser_list = subparsers.add_parser(
        name="list", help="List tasks (optionally by status)"
    )
    parser_list.add_argument(
        dest="status",
        type=str,
        choices=STATUS_CHOICES,
        nargs='?',
        default=None,
        help="Filter tasks by status (done, To Do, progress).",
    )

    # Change mark
    parser_mark = subparsers.add_parser(
        name="mark", help="Update a task's status by task ID"
    )
    parser_mark.add_argument(
        dest="task_id", type=int, help="The ID of the task to update"
    )
    parser_mark.add_argument(
        dest="status",
        type=str,
        choices=STATUS_CHOICES,
        help="The new status of the task ('done', 'To Do', or 'progress')",
    )

    # Change description of the task
    parser_update = subparsers.add_parser(
        name="update", help="Update a task's description by task ID"
    )
    parser_update.add_argument(
        dest="task_id", type=int, help="The ID of the task to update"
    )
    parser_update.add_argument(
        dest="description", type=str, help="The new description of the task"
    )
    
    # Delete command
    parser_delete = subparsers.add_parser(
        name="delete",
        help="Delete a task by task ID"
    )
    parser_delete.add_argument(
        "task_id",
        type=int,
        help="The ID of the task to delete"
)


    args = parser.parse_args()

    if args.command == "add":
        if not args.description.strip():
            print("Error: Task description must be a non-empty string.")
            sys.exit(1)
        task = Task(task_id=None, description=args.description)
        task_service.add_task(task)
        print("Task added successfully.")
    elif args.command == "list":
        if args.status:
            tasks = task_service.list_tasks_by_status(status=args.status)
        else:
            tasks = task_service.list_all_tasks()

        if tasks:
            for task in tasks:
                print(task)
        else:
            print("No tasks found.")
    elif args.command == "mark":
        task_service.update_status_by_id(args.task_id, args.status)
    elif args.command == "update":
        task_service.update_description_by_id(args.task_id, args.description)
    elif args.command == "delete":
        task_service.delete_task_by_id(args.task_id)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
