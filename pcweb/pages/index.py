import asyncio
from datetime import datetime

import pynecone as pc
from sqlmodel import Field

from pcweb import styles
from pcweb.base_state import State
from pcweb.templates import webpage


from pcweb.templates.docpage import (
    doclink,
    doccode,
)

background_style = {
    "background_size": "cover",
    "background_repeat": "no-repeat",
    "background_image": "bg.svg",
}

link_style = {
    "color": "black",
    "font_weight": styles.BOLD_WEIGHT,
    "_hover": {"color": styles.ACCENT_COLOR},
}


class Confetti(pc.Component):
    """Confetti component."""

    library = "react-confetti"
    tag = "ReactConfetti"


confetti = Confetti.create


class Waitlist(pc.Model, table=True):
    email: str
    date_created: datetime = Field(default_factory=datetime.utcnow, nullable=False)


class IndexState(State):
    """Hold the state for the home page."""

    # Whether to show the call to action.
    show_c2a: bool = True

    # The waitlist email.
    email: str

    # Whether the user signed up for the waitlist.
    signed_up: bool = False

    # Whether to show the confetti.
    show_confetti: bool = False

    def close_c2a(self):
        """Close the call to action."""
        self.show_c2a = False

    def signup(self):
        """Sign the user up for the waitlist."""
        return self.start_confetti

    def start_confetti(self):
        """Start the confetti."""
        self.show_confetti = True
        return self.stop_confetti

    async def stop_confetti(self):
        """Stop the confetti."""
        await asyncio.sleep(5)
        self.show_confetti = False


def container(*children, **kwargs):
    kwargs = {"max_width": "1440px", "padding_x": ["1em", "2em", "3em"], **kwargs}
    return pc.container(
        *children,
        **kwargs,
    )


def landing():
    return pc.container(
        pc.cond(
            IndexState.show_confetti,
            confetti(),
        ),
        pc.vstack(
            pc.box(
                pc.text(
                    "Edmæte, học",
                    font_size=styles.HERO_FONT_SIZE,
                    font_weight=700,
                    font_family=styles.TEXT_FONT_FAMILY,
                ),
                pc.text(
                    "không lo lạc hướng.",
                    font_size=styles.HERO_FONT_SIZE,
                    font_weight=800,
                    font_family=styles.TEXT_FONT_FAMILY,
                    background_image="linear-gradient(271.68deg, #EE756A 25%, #756AEE 50%)",
                    background_clip="text",
                ),
                text_align="center",
                line_height="1.15",
            ),
            pc.container(
                "Nền tảng học tập dẫn đầu Việt Nam về mảng tâm lý học.",
                color="grey",
                font_size="1.1em",
                font_family=styles.TEXT_FONT_FAMILY,
                text_align="center",
            ),
            pc.cond(
                ~IndexState.signed_up,
                pc.wrap(
                    pc.input(
                        placeholder="Email",
                        on_blur=IndexState.set_email,
                        color="#676767",
                        type="email",
                        size="md",
                        border="2px solid #f4f4f4",
                        box_shadow="rgba(0, 0, 0, 0.08) 0px 4px 12px",
                        bg="rgba(0,0,0,0)",
                        _focus={
                            "border": f"2px solid {styles.ACCENT_COLOR}",
                        },
                    ),
                    pc.button(
                        "Tham gia vào hàng chờ",
                        on_click=IndexState.signup,
                        bg=styles.DOC_TEXT_COLOR,
                        box_shadow=styles.DOC_SHADOW_LIGHT,
                        color="white",
                        margin_top=0,
                        size="md",
                        _hover={
                            "box_shadow": "0 0 .12em .07em #EE756A, 0 0 .25em .11em #756AEE",
                        },
                    ),
                    justify="center",
                    should_wrap_children=True,
                    spacing="1em",
                ),
                pc.text(
                    pc.icon(
                        tag="CheckIcon",
                    ),
                    " Bạn đã tham gia vào hàng chờ.",
                    color=styles.ACCENT_COLOR,
                ),
            ),
            spacing="2em",
        ),
        margin_y="5em",
    )


def list_circle(text):
    return pc.flex(
        pc.text(text),
        width="2em",
        height="2em",
        border_radius="4em",
        bg="#756aee11",
        color="#756aee",
        align_items="center",
        justify_content="center",
        font_weight="800",
    )


def intro():
    return pc.box(
        container(
            pc.image(src="icon.svg", width="4em", height="4em", margin_bottom="1em"),
            pc.flex(
                pc.box(
                    pc.text(
                        "Một giải pháp hoàn toàn mới.",
                        font_style="normal",
                        font_weight=800,
                        font_size="2em",
                        padding_bottom="0.5em",
                    ),
                    pc.text(
                        "Edmæte giúp cho việc học tập của học sinh hiệu quả hơn rất nhiều, "
                        "qua việc khuyến khích học sinh trải nghiệm ngoài giờ học.",
                        color="#666",
                        margin_bottom="1.5em",
                    ),
                    pc.hstack(
                        list_circle("1"),
                        pc.text("Trải nghiệm được cá nhân hóa.", font_weight="600"),
                        margin_bottom="0.5em",
                    ),
                    pc.text(
                        "Hệ thống AI của Edmæte giúp học sinh nhanh chóng tìm được lộ trình "
                        "học phù hợp, tăng cường hiệu quả học tập của học sinh.",
                        color="#666",
                        margin_bottom=".5em",
                    ),
                    pc.text("Chúng tôi sử dụng công nghệ đầu ngành, như GPT-J của EleutherAI.",
                        color=styles.ACCENT_COLOR_DARK,
                        font_style="normal",
                        margin_bottom="1.5em",
                    ),
                    pc.hstack(
                        list_circle("2"),
                        pc.text("Trải nghiệm học độc đáo", font_weight="600"),
                        margin_bottom="0.5em",
                    ),
                    pc.text(
                        "Học sinh không đơn thuần ngồi trước máy tính để làm",
                        "những bài luyện nhàm chán, mà được tham gia các hoạt động",
                        "trải nghiệm thực tế như Hackathon, Workshop, đi giao lưu, ...",
                        color="#666",
                    ),
                    flex=1,
                    margin_right=[0, 0, "1em"],
                    margin_bottom=["2em", "2em", 0],
                ),
                flex_direction=["column", "column", "column", "row", "row"],
                max_width="30vw"
            ),
        ),
        background="linear-gradient(179.94deg, #FFFFFF 0.05%, #F8F7F8 113.47%)",
        padding_y="60px",
    )


def card(*args, **kwargs):
    kwargs.update(
        {
            "padding": ["1em", "2em"],
            "border": "1px solid #E3E3E3",
            "border_radius": "1em",
            "box_shadow": styles.DOC_SHADOW_LIGHT,
            "align_items": "left",
            "_hover": {"box_shadow": styles.DOC_SHADOW},
        }
    )
    return pc.vstack(*args, **kwargs)


import plotly.graph_objects as go

colors = [
    "#756AEE",
] * 4
colors[2] = "#EE756A"

fig = go.Figure(
    data=[
        go.Bar(
            x=["A", "B", "C", "D"],
            y=[20, 13, 23, 27],
            marker_color=colors,  # marker color can be a single color value or an iterable
        )
    ]
)

components_card = card(
    pc.text(
        "Học tập thông qua cuộc thi.",
        font_size=styles.H3_FONT_SIZE,
        font_weight=styles.BOLD_WEIGHT,
    ),
    pc.text(
        "Thi đấu giúp học sinh tập trung vào bài học, làm cho bài học thêm sinh động, đồng"
        "thời rèn luyện kĩ năng làm việc nhóm và giải quyết vấn đề.",
        color="#676767",
    ),
    doclink(
        "Xem lại những cuộc thi của chúng tôi ->",
        href=""
    ),
    background_image="graphbg.png",
    background_repeat="no-repeat",
    background_position="bottom",
    min_height="35em",
    height="100%",
    width="100%",
    margin_bottom="1em",
)

styling_card = card(
    pc.text(
        "Hệ thống AI hiện đại.",
        font_size=styles.H3_FONT_SIZE,
        font_weight=styles.BOLD_WEIGHT,
    ),
    pc.text(
        "Cá nhân hóa trải nghiệm của từng học sinh sử dụng AI chatbot."
        "Các khuyến khích của AI sẽ được kiểm tra cẩn thận để phù hợp nhất"
        "với học sinh.",
        color="#676767",
        margin_bottom="1em",
    ),
    doclink(
        "Xem cách áp dụng AI đặc biệt của chúng tôi ->",
        href=""
    ),
    pc.center(
        pc.box(
            position="absolute",
            top="calc(50% - 4.5em)",
            left="calc(50% - 4.5em)",
            width="9em",
            height="9em",
            border_radius="50%",
            z_index="20"
        ),
        doccode(
            """edmaete.ai_prompt("Tìm ra khóa học tốt nhất để rèn luyện sự dũng cảm trước đám đông")
{ "name": "Bài 1: Không rụt rè trước đám đông",
   "duration": "120",
   "rating": 4.9
}
""",
            theme="dark",
        ),
        position="relative",
        width="100%",
    ),
    height="100%",
    margin_bottom="1em",
)

react_card = card(
    pc.text(
        "Khi AI không hỗ trợ được bạn, hãy để chuyên gia lo.",
        font_size=styles.H3_FONT_SIZE,
        font_weight=styles.BOLD_WEIGHT,
    ),
    pc.text(
        "Đội ngũ chuyên gia của chúng tôi sẽ giúp bạn về các vấn đề tâm sinh lý mà "
        "AI không thể giúp đỡ được.",
        color="#676767",
    ),
    doclink(
        "Trò chuyện với chuyên gia ->",
        href=""
    ),
    background_image="mentalhealth.jpg",
    background_repeat="no-repeat",
    background_position="center center",
    background_size="10em",
    height="100%",
    margin_bottom="1em",
)


def intro_grid():
    return pc.flex(
        container(
            pc.grid(
                pc.grid_item(
                    components_card,
                    col_span=2,
                ),
                pc.grid_item(
                    styling_card,
                    col_span=2,
                ),
                pc.grid_item(
                    react_card,
                    col_span=1,
                ),
                h="30em",
                template_rows="repeat(2, 1fr)",
                template_columns="repeat(5, 1fr)",
                width="100%",
                gap=4,
            ),
            min_height="30em",
            template_rows="repeat(2, 1fr)",
            template_columns="repeat(5, 1fr)",
            width="100%",
            gap=4,
        ),
        margin_y="60px",
    )


def intro_gridmobile():
    return pc.box(
        container(
            components_card,
            styling_card,
            width="100%",
            padding_y="1em",
        ),
    )


def gallery_card(gif, website):
    return pc.link(
        pc.box(
            pc.image(
                src=gif,
                height="18em",
            ),
            border_radius="1em",
            box_shadow=styles.DOC_SHADOW_DARK,
            overflow="hidden",
            _hover={
                "box_shadow": "0 0 .25em .11em #756AEE",
            },
        ),
        href=website,
    )


def gallery():
    return container(
        pc.vstack(
            pc.text(
                "Thư viện học liệu", font_size=styles.H2_FONT_SIZE, font_weight=styles.BOLD_WEIGHT
            ),
            pc.text(
                "Thư viện rộng lớn của chúng tôi có rất nhiều các dạng bài tập, phù hợp với nhiều"
                " đối tượng học sinh.",
                doclink("Xem thêm →", href=""),
                color="#676767",
            ),
            pc.center(
                pc.hstack(
                    pc.text(
                        "Hiện chưa có bài học nào cả.",
                        color="#676767",
                    ),
                    spacing="1em",
                    margin_top="1em",
                ),
                width="100%",
            ),
            align_items="left",
            border="1px solid #E3E3E3",
            box_shadow=styles.DOC_SHADOW_LIGHT,
            border_radius="12px",
            width="100%",
            padding=["1em", "2em"],
        ),
        margin_top=["3em", "3em", "5em", "12em", "12em"],
        margin_bottom="2em",
    )


def prompt_sign():
    return pc.text(
        "$",
        color=styles.ACCENT_COLOR,
        font_size=styles.H3_FONT_SIZE,
        font_family=styles.TEXT_FONT_FAMILY,
        style={"userSelect": "none"},
    )


def view_docs_button():
    return pc.link(
        pc.button(
            "View Docs",
            font_weight="700",
            font_family=styles.TEXT_FONT_FAMILY,
            bg=styles.ACCENT_COLOR,
            color="white",
            padding="1.5em",
            style={
                "_hover": {
                    "background": "white",
                    "color": styles.ACCENT_COLOR,
                    "transform": "scale3d(1.1, 1.1, 1.1)",
                    "transition_duration": ".5s",
                },
            },
        ),
        style={
            "_hover": {},
        },
        href="",
    )


def installation():
    return pc.box(
        pc.vstack(
            pc.heading(
                "Đăng kí ngay hôm nay!",
                font_weight=styles.BOLD_WEIGHT,
                font_size=styles.H2_FONT_SIZE,
            ),
            pc.box(
                pc.text(
                    "Đăng kí thật đơn giản và dễ dàng. Bạn chỉ cần cung cấp email và đặt "
                    "mật khẩu cho tài khoản của mình thôi.",
                    font_size=styles.H4_FONT_SIZE,
                ),
                pc.text(
                    "(Yên tâm, chúng tôi không bán thông tin cá nhân của bạn hay spam hộp thư của bạn đâu.)",
                    font_size=styles.H4_FONT_SIZE,
                ),
                color="rgba(255,255,255,.7)",
                font_family=styles.TEXT_FONT_FAMILY,
                padding_y="1em",
                margin_bottom=".5em"
            ),
            pc.text(
                "Khi đăng kí, bạn đồng ý với ",
                pc.span(
                    pc.link("Điều khoản dịch vụ"),
                    color="#4287f5"
                ),
                " và ",
                pc.span(
                    pc.link("Chính sách bảo mật"),
                    color="#4287f5"
                ),
                " của chúng tôi.",
                font_size=styles.H4_FONT_SIZE,
                color="rgba(255,255,255,.7)",
                font_family=styles.TEXT_FONT_FAMILY,
            ),
            pc.button(
                "Đăng kí",
                color_scheme="blue", size="lg"
            ),
            align_items="start",
            max_width="38em",
            margin_x="auto",
        ),
        padding_x=styles.PADDING_X2,
        font_family=styles.TEXT_FONT_FAMILY,
        font_size="1.2em",
        padding_y="8em",
        color="white",
        bg="black",
    )


def c2a():
    return pc.box()


@webpage(path="/")
def index() -> pc.Component:
    """Get the main Pynecone landing page."""
    return pc.box(
        landing(),
        intro(),
        pc.desktop_only(
            intro_grid(),
        ),
        pc.mobile_and_tablet(
            intro_gridmobile(),
        ),
        gallery(),
        installation(),
        pc.cond(
            IndexState.show_c2a,
            c2a(),
        ),
    )
