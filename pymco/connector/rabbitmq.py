"""
:py:mod:`pymco.connector.stomp`
"""
from __future__ import absolute_import

import stomp

from . import Connector


class RabbitMQConnector(Connector):
    """RabbitMQ middleware specific connector."""

    def get_target(self, agent, collective):
        """Implement :py:meth:`pymco.connector.Connector.get_target`"""
        return '/exchange/{collective}_broadcast/{agent}'.format(
            agent=agent,
            collective=collective,
        )

    def get_reply_target(self, agent, collective):
        """Implement :py:meth:`pymco.connector.Connector.get_reply_target`"""
        return '/queue/{collective}_reply_{agent}'.format(
            agent=agent,
            collective=collective,
        )

    @classmethod
    def default_connection(cls, config):
        """Creates a :py:class:`stomp.Connection` object with defaults"""
        return stomp.Connection(host_and_ports=config.get_host_and_ports(),
                                vhost=config['plugin.rabbitmq.vhost'])