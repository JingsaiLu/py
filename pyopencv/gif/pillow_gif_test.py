#! usr/bin/python
#coding=utf-8


from PIL import Image, ImageSequence

with Image.open('./positive sequence.gif') as im:
    if im.is_animated:
        frames = [f.copy() for f in ImageSequence.Iterator(im)]
        # frames.reverse() # 内置列表倒序方法
        # 将倒序后的所有帧图像保存下来
        frames[0].save('out.gif', save_all=True, append_images=frames[1:])