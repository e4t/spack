# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

"""Schema for system.yaml configuration file.

.. literalinclude:: ../spack/schema/system.py
   :lines: 13-
"""


#: Properties for inclusion in other schemas
properties = {
    'system': {
        'oneOf': [
            {
                'type': 'object',
                'additionalProperties': False,
                'properties': {
                    'include': {
                        'type': 'array',
                        'default': [],
                        'items': { 'type': 'string' }
                    }
                }
            },
            {
                'type': 'object',
                'additionalProperties': False,
                'properties': {
                    'exclude': {
                        'type': 'array',
                        'default': [],
                        'items': { 'type': 'string' }
                    }
                }
            }
        ]
    }
}

#: Full schema with metadata
schema = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'title': 'Spack system configuration file schema',
    'type': 'object',
    'additionalProperties': False,
    'properties': properties,
}
