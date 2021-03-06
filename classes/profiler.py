# -*- coding: utf-8 -*-

# Profiler (Timer)
# Author: Rafael Pagliuca <rafael.pagliuca@lnls.br>
# Date created: 2016-03-07

import time

class Profiler:

    def __init__(self, *args, **kwargs):
        self.profiler_stats = { 'start': dict(), 'total': dict(), 'state': dict() }
        self.output_enabled = True

    def disable_output(self):
        self.output_enabled = False

    def enable_output(self):
        self.output_enabled = True

    def start(self, alias):
        self.state = 'running'
        self.profiler_stats['total'][alias] = 0
        self.profiler_stats['state'][alias] = 'running'
        self.profiler_stats['start'][alias] = time.clock()

    def stop(self, alias):
        if self.profiler_stats['state'][alias] == 'running':
            self.profiler_stats['total'][alias] += time.clock() - self.profiler_stats['start'][alias]
            self.profiler_stats['state'][alias] = 'suspended'
        else:
            if self.output_enabled:
                print 'Profiler <' + str(alias) + '> not running, cannot suspend.'

    def resume(self, alias):
        if self.profiler_stats['state'][alias] == 'suspended':
            self.profiler_stats['state'][alias] = 'running'
            self.profiler_stats['start'][alias] = time.clock()
        else:
            if self.output_enabled:
                print 'Profiler <' + str(alias) + '> not suspended, cannot resume.'

    def print_total(self, alias):
        if self.output_enabled:
            print 'profiler_stats[total][' + str(alias) + '] = ' + str(self.profiler_stats['total'][alias])

    def stop_and_print(self, alias):
        self.stop(alias)
        self.print_total(alias)
