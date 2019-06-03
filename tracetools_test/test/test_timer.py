import unittest
from tracetools_test.utils import (
    get_trace_event_names,
    run_and_trace,
    cleanup_trace,
)

PKG = 'tracetools_test'

timer_events = [
    'ros2:rcl_timer_init',
    'ros2:rclcpp_timer_callback_added',
    'ros2:rclcpp_timer_callback_start',
    'ros2:rclcpp_timer_callback_end',
]

class TestTimer(unittest.TestCase):

    def test_all(self):
        session_name_prefix = 'session-test-timer-all'
        base_path = '/tmp'
        test_nodes = ['test_timer']

        exit_code, full_path = run_and_trace(base_path, session_name_prefix, timer_events, None, PKG, test_nodes)
        self.assertEqual(exit_code, 0)

        trace_events = get_trace_event_names(full_path)
        print(f'trace_events: {trace_events}')
        self.assertSetEqual(set(timer_events), trace_events)

        cleanup_trace(full_path)


if __name__ == '__main__':
    unittest.main()
