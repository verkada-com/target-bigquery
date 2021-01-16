from tests import unittestcore
from target_bigquery.state import State

class TestSimpleStream(unittestcore.BaseUnitTest):

    def setUp(self):
        super(TestSimpleStream, self).setUp()

    def test_init(self):
        s = State(**{"a": 1})
        print(s)

    def test_flat_schema(self):
        state = State()
        state.merge(
            {"bookmarks": {"stream_one": {"timestamp": "2020-01-10T00:00:00.000000Z"}}}
        )
        print(state)

        state.merge(
            {"bookmarks": {"stream_one": {"timestamp": "2020-01-11T00:00:00.000000Z"}}}
        )
        print(state)

        state.merge(
            {"bookmarks": {"stream_two": {"timestamp": "2020-01-11T00:00:00.000000Z"}}}
        )
        print(state)

    def test_state_but_no_data(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/partial_load_streams/no_data_stream.json",
            config="../sandbox/target_config_cache.json",
            processhandler="partial-load-job"
        )

        ret = main()
        state = self.get_state()
        self.assertEqual(2, len(state))  # initial emit + end state emit

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        self.assertDictEqual(state[-1], {"bookmarks": {"simple_stream": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

    def test_state_but_no_data_bookmarks_load(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/partial_load_streams/no_data_stream.json",
            config="../sandbox/target_config_cache.json",
            processhandler="bookmarks-partial-load-job"
        )

        ret = main()
        state = self.get_state()
        self.assertEqual(2, len(state))  # initial emit + end state emit

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        self.assertDictEqual(state[-1], {"bookmarks": {"simple_stream": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})
