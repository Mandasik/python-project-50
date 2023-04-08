INTERNAL_REPRESENTACION = [
    {
        "name": "common",
        "status": "nested",
        "chieldren": [
            {
                "name": "follow",
                "node_type": "leaf",
                "status": "only_2",
                "value": {"second": False},
            },
            {
                "name": "setting1",
                "node_type": "leaf",
                "status": "equal",
                "value": {"first": "Value 1"},
            },
            {
                "name": "setting2",
                "node_type": "leaf",
                "status": "only_1",
                "value": {"first": 200},
            },
            {
                "name": "setting3",
                "node_type": "leaf",
                "status": "not_equal",
                "value": {"first": True, "second": None},
            },
            {
                "name": "setting4",
                "node_type": "leaf",
                "status": "only_2",
                "value": {"second": "blah blah"},
            },
            {
                "name": "setting5",
                "node_type": "dir",
                "status": "only_2",
                "value": {"second": {"key5": "value5"}},
            },
            {
                "name": "setting6",
                "status": "nested",
                "chieldren": [
                    {
                        "name": "doge",
                        "status": "nested",
                        "chieldren": [
                            {
                                "name": "wow",
                                "node_type": "leaf",
                                "status": "not_equal",
                                "value": {"first": "", "second": "so much"},
                            }
                        ],
                    },
                    {
                        "name": "key",
                        "node_type": "leaf",
                        "status": "equal",
                        "value": {"first": "value"},
                    },
                    {
                        "name": "ops",
                        "node_type": "leaf",
                        "status": "only_2",
                        "value": {"second": "vops"},
                    },
                ],
            },
        ],
    },
    {
        "name": "group1",
        "status": "nested",
        "chieldren": [
            {
                "name": "baz",
                "node_type": "leaf",
                "status": "not_equal",
                "value": {"first": "bas", "second": "bars"},
            },
            {
                "name": "foo",
                "node_type": "leaf",
                "status": "equal",
                "value": {"first": "bar"},
            },
            {
                "name": "nest",
                "node_type": "dir",
                "status": "not_equal",
                "value": {"first": {"key": "value"}, "second": "str"},
            },
        ],
    },
    {
        "name": "group2",
        "node_type": "dir",
        "status": "only_1",
        "value": {"first": {"abc": 12345, "deep": {"id": 45}}},
    },
    {
        "name": "group3",
        "node_type": "dir",
        "status": "only_2",
        "value": {"second": {"deep": {"id": {"number": 45}}, "fee": 100500}},
    },
]