# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Python todo list utility using `dataclass` for task modeling. No external dependencies — standard library only.

## Commands

```bash
python3 todo.py                        # Run the app
python3 -m unittest test_todo -v       # Run all tests
python3 -m unittest test_todo.TestAddTask.test_add_to_empty_list  # Run a single test
```

## Architecture

- `todo.py` — `Task` dataclass (`name`, `done`, `created_at`) and helper functions (`add_task`, `format_task`)
- `test_todo.py` — unittest tests covering `Task`, `add_task`, `format_task`

## Coding Rules

- 모든 함수에 타입 힌트 필수
- 모든 함수에 docstring 작성

## Commit Convention

`동사: 내용` 형식 (예: `add: 할일 완료 기능 추가`, `fix: 날짜 포맷 오류 수정`)

## Caution

- `tasks.json`은 사용자 데이터 파일이므로 코드 변경 시 삭제하지 말 것
