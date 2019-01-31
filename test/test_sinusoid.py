# -*- coding: utf-8 -*-

# FOGLAMP_BEGIN
# See: http://foglamp.readthedocs.io/
# FOGLAMP_END

from unittest.mock import patch
import pytest

from python.foglamp.plugins.south.random import random

__author__ = "Bill Hunt"
__copyright__ = "Copyright (c) 2019 Dianomic Systems"
__license__ = "Apache 2.0"
__version__ = "${VERSION}"

config = random._DEFAULT_CONFIG


def test_plugin_contract():
    # Evaluates if the plugin has all the required methods
    assert callable(getattr(random, 'plugin_info'))
    assert callable(getattr(random, 'plugin_init'))
    assert callable(getattr(random, 'plugin_poll'))
    assert callable(getattr(random, 'plugin_shutdown'))
    assert callable(getattr(random, 'plugin_reconfigure'))


def test_plugin_info():
    assert random.plugin_info() == {
        'name': 'Random Poll plugin',
        'version': '2.0.0',
        'mode': 'poll',
        'type': 'south',
        'interface': '1.0',
        'config': config
    }


def test_plugin_init():
    assert random.plugin_init(config) == config


@pytest.mark.skip(reason="To be implemented")
def test_plugin_poll():
    pass


@pytest.mark.skip(reason="To be implemented")
def test_plugin_reconfigure():
    pass


def test_plugin_shutdown():
    with patch.object(random._LOGGER, 'info') as patch_logger_info:
        random.plugin_shutdown(config)
    patch_logger_info.assert_called_once_with('random plugin shut down.')
