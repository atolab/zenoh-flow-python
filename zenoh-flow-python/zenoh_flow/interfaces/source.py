#
# Copyright (c) 2022 ZettaScale Technology
#
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# http://www.eclipse.org/legal/epl-2.0, or the Apache License, Version 2.0
# which is available at https://www.apache.org/licenses/LICENSE-2.0.
#
# SPDX-License-Identifier: EPL-2.0 OR Apache-2.0
#
# Contributors:
#   ZettaScale Zenoh Team, <zenoh@zettascale.tech>
#


from zenoh_flow import DataSender
from zenoh_flow.types import Context
from typing import Any, Dict


class Source(object):
    """
    The class representing a Zenoh Flow source.

    The `__init__` method is called by the zenoh flow runtime.

    It takes the following parameters:

    :param configuration: Configuration
    :type configuration: dict
    :param outputs: The output streams
    :type outputs: :class:`Dict[str, DataSender]`

    """

    def __init__(
        self,
        context: Context,
        configuration: Dict[str, Any],
        outputs: Dict[str, DataSender],
    ):
        """
        The `__init__` method is called by the zenoh flow runtime.
        This method is expected to initialize the source.
        (E.g. storing relevant configuration and outputs)
        Any source has to implement this method.

        :param context: Zenoh Flow context
        :type configuration: context
        :param configuration: Configuration
        :type configuration: dict`
        :param outputs: The output streams
        :type outputs: :class:`Dict[str, DataSender]`

        :rtype: None
        """
        raise NotImplementedError(
            "Please implement your own method, Source is an interface"
        )

    async def run(self):
        """
        The run method is called by the Zenoh Flow runtime.
        It allows to iterate over inputs interacting with the external world.
        This method is expected to produce data that is then send over the outputs.
        """
        raise NotImplementedError(
            "Please implement your own method, Source is an interface"
        )

    def finalize(self) -> None:
        """
        The finalize method is called by the zenoh flow runtime before destroying the node (e.g., upon stopping the data flow graph).

        It must implement all the required steps to destroy your source state.
        """
        raise NotImplementedError(
            "Please implement your own method, Source is an interface"
        )
