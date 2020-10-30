from tests import unittestcore

"""
Tests:
Load truncate tables with partition fields (should fail)
Load truncate tables without partition (rows should == expected #)
Load append tables with partition field of int or string (should fail)

"""

class TestStreamingInserts(unittestcore.BaseUnitTest):

    def test_simple_stream(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/simple_stream.json",
            config="../sandbox/target_streaming_config.json",
            processhandler="streaming-inserts"
        )
        print("\n")


        ret = main()
        state = self.get_state()
        self.assertEqual(3, len(state))  # 3 states - initial + state + onStreamEnd

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        self.assertDictEqual(state[-1], {"bookmarks": {"simple_stream": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

        table = self.client.get_table("{}.simple_stream".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")
        self.assertIsNone(table.clustering_fields)
        self.assertIsNone(table.partitioning_type)


    def test_simple_stream_with_tables_config(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/simple_stream.json",
            config="../sandbox/target_streaming_config.json",
            tables="./rsc/simple_stream_table_config.json",
            processhandler="streaming-inserts"
        )

        ret = main()
        state = self.get_state()
        self.assertEqual(3, len(state))  # 3 states (no initial emit)

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        self.assertDictEqual(state[-1], {"bookmarks": {"simple_stream": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

        table = self.client.get_table("{}.simple_stream".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")
        self.assertIsNotNone(table.clustering_fields)
        self.assertIsNotNone(table.partitioning_type)

    def test_simple_stream_with_starting_state(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/partial_load_streams/simple_stream.json",
            config="../sandbox/target_streaming_config.json",
            state="./rsc/partial_load_streams/state.json",
            processhandler="streaming-inserts"
        )

        ret = main()
        state = self.get_state()
        self.assertEqual(3, len(state))  # 3 states (no initial emit)

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        self.assertDictEqual(state[-1], {"bookmarks": {"simple_stream": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

        table = self.client.get_table("{}.simple_stream".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")
        self.assertIsNone(table.clustering_fields)
        self.assertIsNone(table.partitioning_type)

    def test_simple_stream_with_table_configs(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/partial_load_streams/simple_stream.json",
            config="../sandbox/target_streaming_config.json",
            tables="./rsc/simple_stream_table_config.json",
            processhandler="streaming-inserts"
        )

        ret = main()
        state = self.get_state()
        self.assertEqual(3, len(state))  # 3 states (no initial emit)

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        self.assertDictEqual(state[-1], {"bookmarks": {"simple_stream": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

        table = self.client.get_table("{}.simple_stream".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")
        self.assertIsNotNone(table.clustering_fields)
        self.assertIsNotNone(table.partitioning_type)

    def test_two_streams(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/partial_load_streams/two_streams.json",
            config="../sandbox/target_streaming_config.json",
            processhandler="streaming-inserts"
        )

        ret = main()
        state = self.get_state()
        self.assertEqual(6, len(state))  # 6 states (no initial emit)

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        self.assertDictEqual(state[-1], {"bookmarks": {"stream_one": {"timestamp": "2020-01-11T00:00:00.000000Z"}, "stream_two": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

        table = self.client.get_table("{}.stream_one".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")

        table = self.client.get_table("{}.stream_two".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")

    def test_two_streams_not_full(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/partial_load_streams/two_streams_not_full_state.json",
            config="../sandbox/target_streaming_config.json",
            processhandler="streaming-inserts"
        )

        ret = main()
        state = self.get_state()
        self.assertEqual(3, len(state))  # 3 states (no initial emit)

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        self.assertDictEqual(state[-1], {"bookmarks": {"stream_one": {"timestamp": "2020-01-11T00:00:00.000000Z"}, "stream_two": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

        table = self.client.get_table("{}.stream_one".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")

        table = self.client.get_table("{}.stream_two".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")

    def test_interlaced_streams(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/partial_load_streams/interlaced_streams.json",
            config="../sandbox/target_streaming_config.json",
            processhandler="streaming-inserts"
        )

        ret = main()
        state = self.get_state()
        self.assertEqual(3, len(state))  # 3 states (no initial emit)

        self.assertEqual(ret, 0, msg="Exit code is not 0!")
        self.assertDictEqual(state[-1], {"bookmarks": {"stream_one": {"timestamp": "2020-01-11T00:00:00.000000Z"}, "stream_two": {"timestamp": "2020-01-11T00:00:00.000000Z"}}})

        table = self.client.get_table("{}.stream_one".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")

        table = self.client.get_table("{}.stream_two".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")

    def test_two_streams_error(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/partial_load_streams/two_streams_error.json",
            config="../sandbox/target_streaming_config.json",
            processhandler="streaming-inserts"
        )

        ret = main()
        state = self.get_state()
        self.assertEqual(5, len(state))  # 5 states (no initial emit)

        self.assertEqual(ret, 2, msg="Exit code is not 0!")
        self.assertDictEqual(state[-1], {"bookmarks": {"stream_one": {"timestamp": "2020-01-11T00:00:00.000000Z"},
                                                       "stream_two": {"timestamp": "2020-01-10T00:00:00.000000Z"}}})

        table = self.client.get_table("{}.stream_one".format(self.dataset_id))
        self.assertEqual(3, table.num_rows, msg="Number of rows mismatch")

        table = self.client.get_table("{}.stream_two".format(self.dataset_id))
        self.assertEqual(2, table.num_rows, msg="Number of rows mismatch")

    def test_two_streams_one_state_error(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/partial_load_streams/two_streams_one_state_error.json",
            config="../sandbox/target_streaming_config.json",
            processhandler="streaming-inserts"
        )

        ret = main()
        state = self.get_state()
        self.assertEqual(1, len(state))  # 1 state only (no initial emit)

        self.assertEqual(ret, 2, msg="Exit code is not 0!")
        self.assertDictEqual(state[-1], {})

        try:
            table = self.client.get_table("{}.stream_one".format(self.dataset_id))
            self.assertEqual(False, True)
        except:
            pass

        try:
            table = self.client.get_table("{}.stream_two".format(self.dataset_id))
            self.assertEqual(False, True)
        except:
            pass


