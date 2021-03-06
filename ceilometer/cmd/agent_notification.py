# -*- encoding: utf-8 -*-
#
# Copyright 2014 OpenStack Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import cotyledon
from cotyledon import oslo_config_glue

from ceilometer import notification
from ceilometer import pipeline
from ceilometer import service

from oslo_config import cfg


def main():
    conf = cfg.ConfigOpts()
    conf.register_cli_opts(pipeline.OPTS)
    service.prepare_service(conf=conf)

    sm = cotyledon.ServiceManager()
    sm.add(notification.NotificationService,
           workers=conf.notification.workers, args=(conf,))
    oslo_config_glue.setup(sm, conf)
    sm.run()
