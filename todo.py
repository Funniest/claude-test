import json
from dataclasses import asdict, dataclass, field
from datetime import datetime


@dataclass
class Task:
    name: str
    done: bool = False
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def add_task(tasks, task_name):
    task = Task(name=task_name)
    tasks.append(task)
    return tasks


def format_task(index, task):
    status = "x" if task.done else " "
    return f"{index}. [{status}] {task.name} (생성: {task.created_at})"


def save_tasks(tasks: list[Task], filename: str = "tasks.json") -> None:
    """할일 목록을 JSON 파일로 저장한다."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump([asdict(task) for task in tasks], f, ensure_ascii=False, indent=2)


def load_tasks(filename: str = "tasks.json") -> list[Task]:
    """JSON 파일에서 할일 목록을 불러온다."""
    with open(filename, "r", encoding="utf-8") as f:
        return [Task(**data) for data in json.load(f)]


def main():
    tasks = []
    for task_name in ['장보기', '운동하기', '독서하기']:
        add_task(tasks, task_name)

    for i, task in enumerate(tasks, 1):
        print(format_task(i, task))

    save_tasks(tasks)
    print("\ntasks.json 저장 완료")

    loaded = load_tasks()
    print("\ntasks.json 불러오기:")
    for i, task in enumerate(loaded, 1):
        print(format_task(i, task))


if __name__ == '__main__':
    main()
