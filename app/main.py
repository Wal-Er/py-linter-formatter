def format_linter_error(error: dict) -> dict:
    return {
        key: value
        for key, value in {
            "line": error.get("line_number"),
            "column": error.get("column_number"),
            "message": error.get("text"),
            "name": error.get("code"),
            "source": "flake8"
        }.items()
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        key: value for key, value in {
            "errors": [
                format_linter_error(error) for error in errors
            ],
            "path": file_path,
            "status": "failed"
        }.items()

    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "errors": [],
            "path": tested_file,
            "status": "passed"
        }
        if len(errors_in_file) == 0 else
        format_single_linter_file(tested_file, errors_in_file)
        for tested_file, errors_in_file in linter_report.items()
    ]
