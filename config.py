DATASET_TEMPLATES = {
    "school": {
        "table_name": "students",
        "columns": [
            ("id", "INTEGER PRIMARY KEY"),
            ("name", "TEXT"),
            ("age", "INTEGER"),
            ("grade", "TEXT"),
            ("marks", "INTEGER")
        ]
    },
    "bank": {
        "table_name": "customers",
        "columns": [
            ("id", "INTEGER PRIMARY KEY"),
            ("name", "TEXT"),
            ("account_number", "TEXT"),
            ("balance", "REAL"),
            ("income", "REAL")
        ]
    },
    "business": {
        "table_name": "employees",
        "columns": [
            ("id", "INTEGER PRIMARY KEY"),
            ("name", "TEXT"),
            ("position", "TEXT"),
            ("salary", "REAL"),
            ("department", "TEXT")
        ]
    }
}
