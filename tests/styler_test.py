from termspark.styler.styler import Styler


class TestStyler:
    def test_pattern(self):
        assert Styler.PATTERN == "[COLOR][HIGHLIGHT][STYLE][CONTENT][RESET]"

    def test_attributes(self):
        element = {
            "content": ["content"],
            "color": ["red"],
            "highlight": [""],
            "style": ["bold"],
        }
        styler = Styler().element(element)

        assert styler.content == ["content"]
        assert styler.content_color == ["red"]
        assert styler.content_highlight == [""]
        assert styler.content_style == ["bold"]

    def test_mixed_styles_attributes(self):
        element = {
            "content": ["content1", "content2"],
            "color": ["red", "white"],
            "highlight": ["white", "blue"],
            "style": [["bold", "underline"], "italic"],
        }
        styler = Styler().element(element)

        assert styler.content == ["content1", "content2"]
        assert styler.content_color == ["red", "white"]
        assert styler.content_highlight == ["white", "blue"]
        assert styler.content_style == [["bold", "underline"], "italic"]

    def test_mixed_styles_missing_attributes(self):
        element = {
            "content": ["content1", "content2"],
            "color": ["white", ""],
            "highlight": ["", "blue"],
            "style": ["", "italic"],
        }
        styler = Styler().element(element)

        assert styler.content == ["content1", "content2"]
        assert styler.content_color == ["white", ""]
        assert styler.content_highlight == ["", "blue"]
        assert styler.content_style == ["", "italic"]

    def test_mixed_styles_multi_word_attributes(self):
        element = {
            "content": ["content1", "content2"],
            "color": ["light red", "white"],
            "highlight": ["white", "light blue"],
            "style": ["double underline", "italic"],
        }
        styler = Styler().element(element)

        assert styler.content == ["content1", "content2"]
        assert styler.content_color == ["light_red", "white"]
        assert styler.content_highlight == ["white", "light_blue"]
        assert styler.content_style == ["double_underline", "italic"]
