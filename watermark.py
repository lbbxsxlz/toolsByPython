from __future__ import annotations

import argparse
import math
import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


WATERMARK_TEXT = "仅用于贝壳德佑房屋交易，它用无效"


def find_chinese_font(font_path: str | None = None) -> str:
	"""优先查找可用的中文黑体。"""
	candidates = [
		font_path,
		"C:/Windows/Fonts/simhei.ttf",
		"/System/Library/Fonts/STHeiti Medium.ttc",
		"/System/Library/Fonts/STHeiti Light.ttc",
		"/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
		"/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
	]
	for candidate in candidates:
		if candidate and os.path.isfile(candidate):
			return candidate
	raise FileNotFoundError("未找到中文黑体，请通过 --font 指定字体文件")


def add_watermark(
	input_path: str,
	output_path: str,
	font_path: str | None = None,
	opacity: int = 110,
	spacing: float = 1.6,
) -> None:
	"""在整张图片上添加斜向重复的半透明文字水印。"""
	with Image.open(input_path) as source:
		image = ImageOps.exif_transpose(source).convert("RGBA")

	width, height = image.size
	font_size = max(18, min(width, height) // 18)
	font = ImageFont.truetype(find_chinese_font(font_path), font_size)

	# 在足以包围原图的正方形画布上平铺文字，旋转后再裁回原图尺寸。
	# 这样水印会覆盖整张图片，无法通过简单裁剪去掉。
	canvas_size = math.ceil(math.hypot(width, height)) + 2
	watermark_canvas = Image.new(
		"RGBA", (canvas_size, canvas_size), (0, 0, 0, 0)
	)
	draw = ImageDraw.Draw(watermark_canvas)
	bbox = draw.textbbox((0, 0), WATERMARK_TEXT, font=font, stroke_width=1)
	text_width = bbox[2] - bbox[0]
	text_height = bbox[3] - bbox[1]
	opacity = max(0, min(opacity, 255))
	spacing = max(0.5, spacing)
	step_x = text_width + int(max(font_size * 2, 48) * spacing)
	step_y = text_height + int(max(font_size, 24) * spacing)

	for row, y in enumerate(range(-step_y, canvas_size + step_y, step_y)):
		offset_x = step_x // 2 if row % 2 else 0
		for x in range(-step_x + offset_x, canvas_size + step_x, step_x):
			draw.text(
				(x - bbox[0], y - bbox[1]),
				WATERMARK_TEXT,
				font=font,
				fill=(128, 128, 128, opacity),
				stroke_width=1,
				stroke_fill=(80, 80, 80, opacity // 2),
			)

	rotated = watermark_canvas.rotate(
		30,
		resample=getattr(Image, "Resampling", Image).BICUBIC,
		expand=False,
	)
	left = (canvas_size - width) // 2
	top = (canvas_size - height) // 2
	watermark = rotated.crop((left, top, left + width, top + height))

	result = Image.alpha_composite(image, watermark)
	output = Path(output_path)
	output.parent.mkdir(parents=True, exist_ok=True)
	if output.suffix.lower() in {".jpg", ".jpeg"}:
		result.convert("RGB").save(output, quality=95)
	else:
		result.save(output)


def main() -> None:
	parser = argparse.ArgumentParser(description="为图片添加文字水印")
	parser.add_argument("input", help="原图片路径")
	parser.add_argument("output", help="输出图片路径")
	parser.add_argument("--font", help="中文黑体字体文件路径")
	parser.add_argument("--opacity", type=int, default=110, help="不透明度（0-255）")
	parser.add_argument(
		"--spacing",
		type=float,
		default=1.6,
		help="水印间距倍数，数值越大越稀疏（默认：1.6）",
	)
	args = parser.parse_args()

	add_watermark(args.input, args.output, args.font, args.opacity, args.spacing)
	print(f"水印图片已保存至：{args.output}")


if __name__ == "__main__":
	main()
