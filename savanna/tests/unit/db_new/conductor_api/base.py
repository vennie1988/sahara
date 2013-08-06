# Copyright (c) 2013 Mirantis Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from savanna import conductor
from savanna.db_new import api as db_api
from savanna.tests.unit import base


class ConductorApiTestCase(base.DbTestCase):
    def setUp(self):
        super(ConductorApiTestCase, self).setUp()
        db_api.setup_db()
        self.api = conductor.Api(use_local=True)

    def tearDown(self):
        db_api.drop_db()
