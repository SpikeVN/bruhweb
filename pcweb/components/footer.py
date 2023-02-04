import pynecone as pc

from pcweb import constants, styles
from pcweb.components.logo import logo
from pcweb.pages.index import index

footer_item_style = {
    "font_family": "Inter",
    "font_weight": "500",
    "_hover": {"color": styles.ACCENT_COLOR},
}

footer_style = {
    "box_shadow": "medium-lg",
    "border_top": "0.2em solid #F0F0F0",
    "vertical_align": "bottom",
    "padding_top": "4em",
    "padding_bottom": "2em",
    "padding_x": styles.PADDING_X2,
    "bg": "white",
}


def footer(style=footer_style):
    return pc.box(
        pc.vstack(
            pc.hstack(
                pc.vstack(
                    pc.text(
                        "Edmæte",
                        font_size=styles.H1_FONT_SIZE,
                        color="#000",
                        font_weight=styles.BOLD_WEIGHT
                    ),
                    pc.text(
                        "Nền tảng rèn luyện tâm sinh lý hàng đầu Việt Nam.",
                        font_size="1em",
                        color="#000"
                    ),
                    align_items="start"
                ),
                pc.vstack(
                    pc.text("Trang web", color=styles.SUBHEADING_COLOR),
                    pc.link("Trang chủ", href=index.path, style=footer_item_style),
                    pc.link("Thư viện học liệu", href="", style=footer_item_style),
                    pc.link("Về chúng tôi", href="", style=footer_item_style),
                    align_items="start",
                ),
                pc.vstack(
                    pc.text("Đây là một dự án startup tại", color=styles.SUBHEADING_COLOR),
                    pc.text(
                        "Trường THPT Chuyên Bắc Ninh",
                        color=styles.SUBHEADING_COLOR,
                        font_size=styles.H3_FONT_SIZE,
                        font_weight=styles.BOLD_WEIGHT
                    ),
                    pc.text(
                        "tham gia",
                    ),
                    pc.text(
                        "Cuộc thi Học sinh, sinh viên với ý tưởng khởi nghiệp lần thứ V",
                        color=styles.SUBHEADING_COLOR,
                        font_size=styles.H4_FONT_SIZE,
                        font_weight=styles.BOLD_WEIGHT
                    ),
                    align_items="start",
                ),
                justify="space-between",
                color=styles.LIGHT_TEXT_COLOR,
                align_items="top",
                padding_bottom="3em",
                min_width="100%",
            ),
            pc.hstack(
                pc.text(
                    "Bản quyền © 2023 Edmæte, Inc. Chúng tôi giữ toàn bộ quyền sở hữu trí tuệ về trang web này.",
                    font_weight="500",
                ),
                pc.link(
                    "Liên hệ với chúng tôi",
                    href=constants.CONTACT_URL,
                    font_weight="500",
                    style=footer_item_style,
                ),
                justify="space-between",
                color=styles.LIGHT_TEXT_COLOR,
                padding_bottom="2em",
                min_width="100%",
            ),
        ),
        **style,
    )
