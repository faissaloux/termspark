from mock import patch  # type: ignore

from termspark.painter.mode_manager import ModeManager


class TestModeManager:
    @patch("termspark.painter.modes.rgb.RGB.__init__", return_value=None)
    def test_rgb_class_called(self, rgb):
        ModeManager("36,114,200")

        rgb.assert_called_once_with("36,114,200")

    @patch("termspark.painter.modes.rgb.RGB.format")
    def test_rgb_class_format_called(self, rgb):
        ModeManager("36,114,200").format()

        rgb.assert_called_once()

    @patch("termspark.painter.modes.hex.HEX.__init__", return_value=None)
    def test_hex_class_called(self, hex):
        ModeManager("#2472C8")

        hex.assert_called_once_with("#2472C8")

    @patch("termspark.painter.modes.hex.HEX.format")
    def test_hex_class_format_called(self, hex):
        ModeManager("#2472C8").format()

        hex.assert_called_once()

    @patch("termspark.painter.modes.name.Name.__init__", return_value=None)
    def test_name_class_called(self, name):
        ModeManager("blue")

        name.assert_called_once_with("blue")

    @patch("termspark.painter.modes.name.Name.format")
    def test_name_class_format_called(self, name):
        ModeManager("blue").format()

        name.assert_called_once()
