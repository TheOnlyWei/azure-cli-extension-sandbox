# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

import os.path

def load_arguments(self, _):
    with self.argument_context('do stuff') as c:
        c.argument('foo', help='Optional foo.')