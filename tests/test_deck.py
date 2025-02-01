#!/usr/bin/env python

"""Tests for `geemap.deck` package."""

import unittest
from unittest.mock import patch

import ee
import geemap.deck as gmd
from tests import fake_ee

try:
    import pydeck as pdk

except ImportError:
    raise ImportError("pydeck needs to be installed to use this module.")


@patch.object(ee, "Image", fake_ee.Image)
@patch.object(ee, "ImageCollection", fake_ee.ImageCollection)
class TestDeck(unittest.TestCase):
    """Tests for `geemap` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.view_state = pdk.ViewState()
        self.image_collection = fake_ee.ImageCollection([])

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_ee_layer_opacity(self):
        """Verify the opacity parameter is processed."""
        m = gmd.Map(ee_initialize=False, initial_view_state=self.view_state)

        with patch.object(fake_ee.Image, "getMapId", autospec=True) as mock_get_map_id:
            m.add_ee_layer(self.image_collection, vis_params={}, opacity=0.5)
            mock_get_map_id.assert_called_once()

            vis_params = mock_get_map_id.call_args[0][1]
            self.assertEquals(vis_params.get("opacity"), 0.5)
