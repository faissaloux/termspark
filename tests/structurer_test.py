from termspark.structurer.structurer import Structurer


class TestStructurer:
    def test_structure_keys(self):
        structurer = Structurer("content").form()

        assert "content" in structurer.keys()
        assert "color" in structurer.keys()
        assert "highlight" in structurer.keys()

    def test_structure_without_both_color_and_highlight(self):
        structurer = Structurer("content").form()

        assert structurer.get("content") == "content"
        assert structurer.get("color") == ""
        assert structurer.get("highlight") == ""

    def test_structure_with_color(self):
        structurer = Structurer("content", "red").form()

        assert structurer.get("content") == "content"
        assert structurer.get("color") == "red"
        assert structurer.get("highlight") == ""

    def test_structure_with_both_color_and_highlight(self):
        structurer = Structurer("content", "red", "yellow").form()

        assert structurer.get("content") == "content"
        assert structurer.get("color") == "red"
        assert structurer.get("highlight") == "yellow"

    def test_structure_with_color_and_highlight_and_style(self):
        structurer = Structurer("content", "red", "yellow", "bold, underline").form()

        assert structurer.get("content") == "content"
        assert structurer.get("color") == "red"
        assert structurer.get("highlight") == "yellow"
        assert structurer.get("style") == ["bold", "underline"]
        assert structurer.get("styled_content") == "content"

    def test_structure_returns_string_content(self):
        structurer = Structurer(24).form()

        assert structurer.get("content") == "24"
